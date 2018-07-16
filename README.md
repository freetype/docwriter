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
docwriter [-h] [-t T] -o DIR [-p PRE] [-q | -v] files [files ...]

DocWriter Usage information

positional arguments:
  files                 list of source files to parse, wildcards are allowed

optional arguments:
  -h, --help            show this help message and exit
  -t T, --title T       set project title, as in '-t "My Project"'
  -o DIR, --output DIR  set output directory, as in '-o mydir'
  -p PRE, --prefix PRE  set documentation prefix, as in '-p ft2'
  -q, --quiet           run quietly, show only errors
  -v, --verbose         increase output verbosity
```

## Running Tests

To run all tests locally:

1.  Make sure `pytest` is installed:
    ```bash
    pip install pytest
    ```
    
2.  Run tests:
    ```bash
    python -m pytest
    ```
