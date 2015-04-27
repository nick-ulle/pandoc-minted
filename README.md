# pandocfilters-minted

A pandoc filter that has the LaTeX writer use [minted][] for typesetting code.

[minted]: https://github.com/gpoore/minted

Usage:

    pandoc --filter ./minted.py -o myfile.tex myfile.md

Minted is only used for code where the language has been specified; you can
set a default language using the pandoc metadata field `minted-language`.
