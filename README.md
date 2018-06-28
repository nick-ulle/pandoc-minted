# pandoc-minted

A pandoc filter that has the LaTeX writer use [minted][] for typesetting code.

[minted]: https://github.com/gpoore/minted

# Installation

Clone this repository to somewhere safe:

```
git clone https://github.com/nick-ulle/pandoc-minted.git
```

Then create a symlink to `pandoc-minted.py` in a directory on the `$PATH`:

```
cd pandoc-minted
ln -rs pandoc-minted.py DIRECTORY/pandoc-minted
```

Note that on OS X you must omit the `r` flag.


# Usage

```
pandoc --filter pandoc-minted -o myfile.tex myfile.md
```

When you don't set the language for a code block, pandoc-minted will default to
`text`. You can change the default language with a Pandoc metadata block:

```
---
pandoc-minted:
  language: python
---
```

