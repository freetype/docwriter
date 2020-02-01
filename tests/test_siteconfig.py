#
#  test_siteconfig.py
#
#    Tests for site config generation (siteconfig.py).
#
#  Copyright (C) 2018-2020 by
#  Nikhil Ramakrishnan.
#
#  This file is part of the FreeType project, and may only be used,
#  modified, and distributed under the terms of the FreeType project
#  license, LICENSE.TXT.  By continuing to use, modify, or distribute
#  this file you indicate that you have read the license and
#  understand and accept it fully.

"""Docwriter site config tests.

This module tests the validity of the `yml` configuration
generated by `siteconfig.py`.
"""
import os

import yaml

from docwriter import siteconfig
from docwriter import utils

config = siteconfig.SiteConfig()

# Config vars
site_name        = "Foo Bar Test"
site_description = "Test documentation for Foo Bar."
site_author      = "Pytest"
toc_filename     = "foo-toc.md"
index_filename   = "foo-index.md"

# Add chapters and pagess
c1_sec   = ["c1s1", "c1s2", "c1s3"]
c2_sec   = ["c2s1", "c2s2"]

pages = {}
pages['chap1'] = c1_sec
pages['chap2'] = c2_sec

def test_config( tmpdir, caplog ):
    utils.output_dir = str( tmpdir )
    # Set site config
    config.set_site_info( site_name, site_description,
                        site_author )
    # Add toc and index
    config.add_single_page( "TOC", toc_filename )
    config.add_single_page( "Index", index_filename )

    # Add chapters and pages
    for chap, parts in pages.items():
        config.start_chapter( chap )
        for sec in parts:
            config.add_chapter_page( sec, sec + ".md" )
        config.end_chapter()

    # Done, Build config
    config.build_config()

    # Open file and parse yml
    filepath = os.path.join( str( tmpdir ), 'mkdocs.yml' )
    result = open( filepath, 'rb' ).read()
    data = yaml.safe_load(result)

    # Assertions
    assert data is not None
    for record in caplog.records:
        # Strict build - there should be no warnings
        assert record.levelname != 'WARNING'
