#
#  siteconfig.py
#
#    Build site configuration and write to mkdocs.yml.
#
#  Copyright 2018 by
#  Nikhil Ramakrishnan.
#
#  This file is part of the FreeType project, and may only be used,
#  modified, and distributed under the terms of the FreeType project
#  license, LICENSE.TXT.  By continuing to use, modify, or distribute
#  this file you indicate that you have read the license and
#  understand and accept it fully.

from __future__ import print_function
import sys
import utils

try:
    import yaml
except ImportError:
    sys.stderr.write("Error: Could not find module 'pyyaml'. Please run"
                     + "'pip install -r requirements.txt' to install.")

# Config file name
config_filename = "mkdocs.yml"

# Docs directory and site directory
docs_dir = "markdown"
site_dir = "site"

# Basic site configuration default values
site_name = "FreeType API Reference"
site_description = "API Reference documentation for FreeType"
site_author = "FreeType Contributors"

# Theme configuration default values
theme_conf = {}
theme_conf['name'] = "material"
theme_conf['logo'] = "images/favico.ico"
theme_conf['language'] = "en"

# Markdown extensions
md_extensions = '''\
markdown_extensions:
  - toc:
      permalink: true
  - pymdownx.superfences:
      disable_indented_code_blocks: true
  - codehilite:
      guess_lang: false
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.magiclink
  - pymdownx.smartsymbols
'''

# Extra scripts
extra_scripts = '''\
extra_css:
  - 'stylesheets/extra.css'

extra_javascript:
  - 'javascripts/extra.js'
'''

# Other config
other_config = '''\
copyright: Copyright 2018 \
<a href = "http://git.savannah.gnu.org/cgit/freetype/freetype2.git/tree/docs/LICENSE.TXT">\
The FreeType Project</a>.
'''

def add_config( yml_string, config_name ):
    config = None
    try:
        config = yaml.safe_load( yml_string )
    except:
        sys.stderr.write("WARNING: Malformed '"+ config_name +"' config, ignoring.\n")
    return config

# Parse all configurations and save as Python objects
md_extensions = add_config( md_extensions, "markdown_extensions" )
yml_extra     = add_config( extra_scripts, "extra scripts" )
yml_other     = add_config( other_config, "other" )


class Chapter:
    def __init__( self, title ):
        self.title = title
        self.pages = []

    def add_page( self, section_title, filename ):
        cur_page = {}
        cur_page[section_title] = filename
        self.pages.append( cur_page )

    def get_pages( self ):
        conf = {}
        conf[self.title] = self.pages
        return conf


class SiteConfig:
    '''Site configuration generator class

    This class is used to generate site configuration based on
    supplied and default values.
    '''
    def __init__( self ):
        self.site_config   = {}
        self.pages         = []
        self.chapter       = None
        self.sections      = []
        self.md_extensions = []

        global site_name, site_description, site_author
        global docs_dir, site_dir
        global theme_conf

        # Set configurations
        self.site_name   = site_name
        self.site_desc   = site_description
        self.site_author = site_author
        self.docs_dir    = docs_dir
        self.site_dir    = site_dir
        self.theme_conf  = theme_conf

    def set_site_info( self, name, description = None, author = None ):
        '''Set the basic site information'''
        if name:
            self.site_name = name
        else:
            # Site name is required, throw warning and revert to default
            sys.stderr.write("WARNING: Site name not specified,"
                             + " reverting to default.\n")

        if description:
            self.site_desc = description
        if author:
            self.site_author = author

    def add_single_page( self, section_title, filename ):
        '''Add a single page to the list of pages'''
        cur_page = {}
        cur_page[section_title] = filename
        self.pages.append( cur_page )

    def add_chapter_page(self, section_title, filename):
        '''Add a page to a chapter.

        Chapter must be set first using `start_chapter()`
        If not set, `add_single_page()` will be called internally
        '''
        if self.chapter:
            self.chapter.add_page( section_title, filename )
        else:
            sys.stderr.write("WARNING: Section '"+ section_title
                             + "' added without starting chapter.\n")
            self.add_single_page( section_title, filename )

    def start_chapter( self, chap ):
        '''Start a chapter'''
        if self.chapter:
            chap_pages = self.chapter.get_pages()
            self.pages.append( chap_pages )

        self.chapter = Chapter( chap )

    def end_chapter( self ):
        '''Explicitly end a chapter'''
        if self.chapter:
            chap_pages = self.chapter.get_pages()
            self.pages.append( chap_pages )
            self.chapter = None

    def build_site_config( self ):
        '''Add basic Project information to config'''
        self.site_config['site_name'] = self.site_name
        if site_description:
            self.site_config['site_description'] = self.site_desc
        if site_author:
            self.site_config['site_author'] = self.site_author
        if docs_dir:
            self.site_config['docs_dir'] = self.docs_dir
        if site_dir:
            self.site_config['site_dir'] = self.site_dir

    def build_theme_config( self ):
        # internal: build theme config
        if theme_conf != {}:
            self.site_config['theme'] = self.theme_conf

    def build_pages( self ):
        # internal: build pages config
        if self.pages != []:
            self.site_config['pages'] = self.pages

    def populate_config( self, data ):
        # internal: Add a given not None object to site_config
        if data:
            self.site_config.update( data )

    def write_config( self, name ):
        '''Write all values in site_config to output stream'''
        if self.site_config != {}:
            print( "# " + name )
            print( yaml.dump( self.site_config, default_flow_style=False ) )
            self.site_config.clear()

    def write_config_order( self, name, order ):
        '''Write all values in site_config to output stream in order'''
        if self.site_config != {}:
            print( "# " + name )
            for key in order:
                if key in self.site_config:
                    temp_config = {}
                    temp_config[key] = self.site_config[key]
                    print( yaml.dump( temp_config, default_flow_style=False ).rstrip() )

            # print an empty line
            print()
            self.site_config.clear()

    def build_config( self ):
        '''Build the YAML configuration'''
        # End chapter if started
        self.end_chapter()

        # Open yml file
        output = utils.open_output( config_filename, config = True )

        # Build basic site info
        self.build_site_config()
        order = ['site_name', 'site_author', 'docs_dir', 'site_dir']
        self.write_config_order( "Project information", order )

        # Build theme configuration
        self.build_theme_config()
        self.write_config( "Configuration" )

        # Build pages
        self.build_pages()
        self.write_config( "Pages" )

        # Add extra CSS and Javascript
        self.populate_config( yml_extra )
        self.write_config( "Customization" )

        # Add Markdown extensions
        self.populate_config( md_extensions )
        self.write_config( "Extensions" )

        # Add other options
        self.populate_config( yml_other )
        self.write_config( "Other Options" )

        # Close the file
        utils.close_output( output )

# eof
