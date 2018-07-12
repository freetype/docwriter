[![Build Status](https://travis-ci.com/nikramakrishnan/freetype-docwriter.svg?branch=master)](https://travis-ci.com/nikramakrishnan/freetype-docwriter)
[![Code Health](https://landscape.io/github/nikramakrishnan/freetype-docwriter/master/landscape.svg?style=flat)](https://landscape.io/github/nikramakrishnan/freetype-docwriter/master)

# FreeType Docwriter

Markdown documentation generator for the FreeType library.

## Setup Instructions

1.  Clone this repository.
2.  Clone the freetype2 repository from [here](http://git.savannah.gnu.org/cgit/freetype/freetype2.git/).
3.  Convert the `include/` folder to markdown using the 
    [freetype-docs](https://github.com/nikramakrishnan/freetype-docs/tree/markdown) repository.
5.  Copy files from `include_mark/`.
6.  Run:

    ```bash
    python -B docwriter.py --prefix=ft2 --title=FreeType-2.9.1 --output=./docs/reference \
    ./include_mark/freetype/*.h ./include_mark/freetype/config/*.h ./include_mark/freetype/cache/*.h
    ```

## Usage Information

```
docwriter [options] file1 [file2 ...]

Note: Wildcard names are supported

using the following options:

  -h : print this page
  -t : set project title, as in '-t "My Project"'
  -o : set output directory, as in '-o mydir'
  -p : set documentation prefix, as in '-p ft2'
  -q : run quietly, show only errors
  -v : verbose

  --title  : same as -t, as in '--title="My Project"'
  --output : same as -o, as in '--output=mydir'
  --prefix : same as -p, as in '--prefix=ft2'
  --quiet  : same as -q
  --verbose: same as -v
```
