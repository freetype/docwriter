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

# Load list of dependencies
with open("requirements.txt") as data:
    install_requires = [
        line for line in data.read().split("\n")
            if line and not line.startswith("#")
    ]

# Package description
setup(
    name = 'docwritertest',
    version = '0.1',
    url = 'https://github.com/nikramakrishnan/freetype-docwriter',
    license = 'FreeType License',
    description = 'Generate API reference documentation for FreeType.',
    author = 'Nikhil Ramakrishnan',
    author_email = 'ramakrishnan.nikhil@gmail.com',
    keywords = 'freetype, docwriter',
    packages = find_packages(),
    include_package_data = True,
    install_requires = install_requires,
)
