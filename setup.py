#
#  setup.py
#
#    Package setup rules for docwriter.
#
#  Copyright (C) 2018-2020 by
#  Nikhil Ramakrishnan.
#
#  This file is part of the FreeType project, and may only be used,
#  modified, and distributed under the terms of the FreeType project
#  license, LICENSE.TXT.  By continuing to use, modify, or distribute
#  this file you indicate that you have read the license and
#  understand and accept it fully.

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

# Load list of dependencies
with open("requirements.txt") as data:
    install_requires = [
        line for line in data.read().split("\n")
            if line and not line.startswith("#")
    ]

# Package description
setup(
    name = 'docwriter',
    use_scm_version = True,
    setup_requires = ['setuptools_scm'],
    url = 'https://github.com/freetype/docwriter',
    license = 'FreeType License',
    description = 'API reference documentation generator for FreeType.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Nikhil Ramakrishnan',
    author_email = 'freetype-devel@nongnu.org',
    keywords = 'freetype docwriter',
    packages = find_packages(),
    include_package_data = True,
    install_requires = install_requires,
    python_requires='>=3.5',
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
