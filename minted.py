#!/usr/bin/env python
''' A pandoc filter that has the LaTeX writer use minted for typesetting code.

Usage:
    pandoc --filter ./minted.py -o myfile.tex myfile.md
'''

from pandocfilters import toJSONFilter, RawBlock, RawInline

def unpack(value, meta):
    ''' Unpack the body and language of a pandoc code element.

    Args:
        value   contents of pandoc object
        meta    document metadata
    '''
    [attrib, body] = value
    try:
        [_, [language, *_], _] = attrib
    except ValueError:
        # Use default language, or don't highlight.
        language = meta.get('minted-language')
        if language is not None:
            language = language['c'][0]['c']

    return body, language

def minted(key, value, format, meta):
    ''' Use minted for code in LaTeX.

    Args:
        key     type of pandoc object
        value   contents of pandoc object
        format  target output format
        meta    document metadata
    '''
    if format == 'latex':
        if key == 'CodeBlock':
            body, language = unpack(value, meta)
            if language is None:
                return

            begin = r'\begin{minted}{' + language + '}\n'
            end = '\n' + r'\end{minted}'

            return [RawBlock(format, begin + body + end)]

        elif key == 'Code':
            body, language = unpack(value, meta)
            if language is None:
                return
            
            begin = r'\mintinline{' + language + '}{'
            end = '}'

            return [RawInline(format, begin + body + end)]

if __name__ == '__main__':
    toJSONFilter(minted)

