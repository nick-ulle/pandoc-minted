#!/usr/bin/env python
''' A Pandoc filter that makes the LaTeX writer default to minted for code.

Usage:
    pandoc --filter ./minted.py -o myfile.tex myfile.md
'''

from pandocfilters import toJSONFilter, RawBlock, RawInline

def minted(key, value, format, meta):
    ''' Use minted environments for code blocks in LaTeX.

    Args:
        key     type of pandoc object
        value   contents of pandoc object
        format  target output format
        meta    document metadata
    '''
    if format == 'latex':
        if key == 'CodeBlock':
            [attrib, body] = value
            try:
                [_, [lang, *_], _] = attrib
            except ValueError:
                # Use default language, or don't highlight.
                lang = meta.get('minted-language')
                if lang is None:
                    return
                lang = lang['c'][0]['c']

            begin = r'\begin{minted}{' + lang + '}\n'
            end = '\n' + r'\end{minted}'

            return [RawBlock(format, begin + body + end)]
        elif key == 'Code':
            [attrib, body] = value
            try:
                [_, [lang, *_], _] = attrib
            except ValueError:
                # Use default language, or don't highlight.
                lang = meta.get('minted-language')
                if lang is None:
                    return
                lang = lang['c'][0]['c']
            
            begin = r'\mintinline{' + lang + '}{'
            end = '}'

            return [RawInline(format, begin + body + end)]

if __name__ == '__main__':
    toJSONFilter(minted)

