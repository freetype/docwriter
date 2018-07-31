#
#  setup.py
#
#    Package setup rules for docwriter
#
#  Copyright 2018 by
#  Nikhil Ramakrishnan.
#
#  This file is part of the FreeType project, and may only be used,
#  modified, and distributed under the terms of the FreeType project
#  license, LICENSE.TXT.  By continuing to use, modify, or distribute
#  this file you indicate that you have read the license and
#  understand and accept it fully.

from setuptools import setup, find_packages

long_description = (
    "Docwriter is an API documentation generator for FreeeType that "
    "extracts and builds Markdown docs from the FreeType header files."
)

# Load list of dependencies
with open("requirements.txt") as data:
    install_requires = [
        line for line in data.read().split("\n")
            if line and not line.startswith("#")
    ]

# Package description
setup(
    name = 'docwriter',
    version = '0.1',
    url = 'https://github.com/freetype/docwriter',
    license = 'FreeType License',
    description = 'API reference documentation generator for FreeType.',
    long_description = long_description,
    author = 'Nikhil Ramakrishnan',
    author_email = 'freetype-devel@nongnu.org',
    keywords = 'freetype docwriter',
    packages = find_packages(),
    include_package_data = True,
    install_requires = install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Text Processing',
    ],
)
