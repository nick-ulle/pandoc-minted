# pandoc-minted

A pandoc filter that has the LaTeX writer use [minted][] for typesetting code.

[minted]: https://github.com/gpoore/minted

# Installation

Clone this repository to somewhere safe:

```
git clone https://github.com/nick-ulle/pandoc-minted.git
```

Then symlink to `pandoc-minted.py` from a `$PATH` directory:

Linux:
```
cd pandoc-minted
ln -rs pandoc-minted.py DIRECTORY/pandoc-minted
```

Mac:
```
cd pandoc-minted
ln -s [FULL-PATH]/pandoc-minted.py [FULL-PATH]
```
, where the latter path is a directory that is in the `$PATH`. Note that the full paths are needed on the ln command (on Mac at least).


# Usage

```
pandoc --filter pandoc-minted.py -o myfile.tex myfile.md
```

When you don't set the language for a code block, pandoc-minted will default to
`text`. You can change the default language with a Pandoc metadata block:

```
---
pandoc-minted:
  language: python
---
```

