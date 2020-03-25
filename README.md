[![Build Status](https://travis-ci.com/freetype/docwriter.svg?branch=master)](https://travis-ci.com/freetype/docwriter)
[![PyPI version](https://badge.fury.io/py/docwriter.svg)](https://pypi.org/project/docwriter/)

# FreeType Docwriter

Docwriter is an API documentation generator for the FreeType Library that extracts and builds
Markdown docs from the FreeType header files.

## Installation

Run `pip install docwriter` (see (4) below for an automated `virtualenv` usage). It requires
Python >= 3.5 to run.

## Steps to Generate Docs
1.  Ensure `docwriter` is installed using `pip`.

2.  Clone the freetype2 repository from
    [here](http://git.savannah.gnu.org/cgit/freetype/freetype2.git/).

3.  The FreeType build system can be used to generate the docs:

    ```bash
    sh autogen.sh
    ./configure
    make refdoc
    ```

4. Alternatively, step 1 and the make target can be replaced with `make refdoc-venv`. This installs
   all requirements automatically in a separate virtual environment. More information on
   `virtualenv` usage can be found
   [here](http://git.savannah.gnu.org/cgit/freetype/freetype2.git/tree/docs/README).

## Development Usage
1.  Clone this repository.
2.  Clone the freetype2 repository from
    [here](http://git.savannah.gnu.org/cgit/freetype/freetype2.git/).
3.  Run `pip install -r requirements.txt` in your environment (`virtualenv` recommended).
4.  Copy the `include/` directory from `freetype2` to `docwriter`.
5.  Run in the `docwriter` directory:

    ```bash
    python -m docwriter                      \
            --prefix=ft2                     \
            --title=FreeType-2.9.1           \
            --site=reference                 \
            --output=./docs                  \
            ./include/freetype/*.h           \
            ./include/freetype/config/*.h    \
            ./include/freetype/cache/*.h
    ```
6.  The markdown files are generated in `docs/markdown/`. Static site can be built by running
    `mkdocs build` in `docs/`. Read more about Mkdocs
    [here](https://www.mkdocs.org/#building-the-site).

## Usage Information

```
docwriter [-h] [-t T] -o DIR [-p PRE] [-s DIR] [-q | -v] files [files ...]

DocWriter Usage information

positional arguments:
  files                 list of source files to parse, wildcards are allowed

optional arguments:
  -h, --help            show this help message and exit
  -t T, --title T       set project title, as in '-t "My Project"'
  -o DIR, --output DIR  set output directory, as in '-o mydir'
  -p PRE, --prefix PRE  set documentation prefix, as in '-p ft2'
  -s DIR, --site DIR    set 'site_dir' in mkdocs.yml [default=site]
  -q, --quiet           run quietly, show only errors
  -v, --verbose         increase output verbosity
```

## Running Tests

To test on all supported Python versions:

1.  Make sure `tox` is installed:
    ```bash
    pip install tox
    ```

2.  Ensure that all Python versions that you need to run the tests on are installed.

3.  Run tests:
    ```bash
    tox
    ```

To run specifc tests, use the `-e` argument. For example,

```bash
tox -e py37,py38
```

will run tests only on Python 3.7 and 3.8 (assuming they are installed). See [tox.ini](tox.ini) for
all available environments.

More information on running specific tox environments can be found
[here](https://tox.readthedocs.io/en/latest/example/general.html#selecting-one-or-more-environments-to-run-tests-against).

### Regression Tests

Regression tests require internet access, `git`, and other FreeType [build
dependencies](http://git.savannah.gnu.org/cgit/freetype/freetype2.git/tree/README.git), and are
time-consuming. These tests are largely meant to run on Travis CI, but can also be run locally:

```bash
tox -e regression
```

## License

This library is licensed under the [FreeType License](https://www.freetype.org/license.html).

## History

This library was originally written by David Turner as `docmaker` which collected and presented
documentation in HTML. It has since been modified multiple times, including a major refactor to
allow multiple output formats. The current `docwriter` is the biggest rewrite, with lots of changes
and additions that allow it to be more flexible, readable, maintainable and usable.
