#
#  tomarkdown.py
#
#    A sub-class container of the `Formatter' class to produce Markdown.
#
#  Copyright 2018 by
#  Nikhil Ramakrishnan.
#
#  This file is part of the FreeType project, and may only be used,
#  modified, and distributed under the terms of the FreeType project
#  license, LICENSE.TXT.  By continuing to use, modify, or distribute
#  this file you indicate that you have read the license and
#  understand and accept it fully.

# The parent class is contained in file `formatter.py'.


from sources import *
from content import *
from formatter import *

import time

md_nav_separator = " &raquo; "

md_header_1 = """\
[Docs](ft2-index.md) &raquo; \
"""

md_line_sep = """

-------------------------------

"""

md_newline = "\n"

md_api_ref = """\
 API Reference
"""



# Description header/footer.
description_header = ""
description_footer = ""

# Source code extracts header/footer.
source_header = """
<div class = "codehilite">
<pre>\
"""
source_footer = """\
</pre>
</div>\
"""

# Chapter header/inter/footer.
chapter_header = """\
## \
"""

md_h1 = "# "
md_h2 = "## "
md_h3 = "### "
md_h4 = "<h4>"
md_h4_inter = "</h4>"

code_header = "```"
code_footer = "```"

# Paragraph header and footer.
para_header = "<p>"
para_footer = "</p>"

# Source language keyword coloration and styling.
keyword_prefix = '<span class="keyword">'
keyword_suffix = '</span>'

# Source language keyword coloration and styling.

section_synopsis_header = '''
## Synopsis\
'''
section_synopsis_footer = ''


def  html_quote( line ):
    '''Change HTML special characters to their codes

    Follows ISO 8859-1  
    Characters changed:
    `&`, `<` and `>`.
    '''
    result = line.replace( "&", "&amp;" )
    result = result.replace( "<", "&lt;"  )
    result = result.replace( ">", "&gt;"  )
    return result

################################################################
##
##  MARKDOWN FORMATTER CLASS
##
class  HtmlFormatter( Formatter ):

    def  __init__( self, processor, project_title, file_prefix ):
        Formatter.__init__( self, processor )

        global code_header, code_footer
        global chapter_header
        global keyword_prefix, keyword_suffix

        if file_prefix:
            file_prefix = file_prefix + "-"
        else:
            file_prefix = ""

        self.headers       = processor.headers
        self.project_title = project_title
        self.file_prefix   = file_prefix
        self.toc_filename     = self.file_prefix + "toc.md"

        self.html_header = (
            md_header_1 + "Global Index"
            + md_line_sep + md_h1
            + project_title + md_api_ref
        )
        self.md_index_header = (
            md_header_1 + "Global Index"
            + md_line_sep + md_h1
            + project_title + md_api_ref
        )

        self.html_toc_header = (
            md_header_1 + "Table of Contents"
            + md_line_sep + md_h1
            + project_title + md_api_ref
        )
          
        self.html_footer = (
            '<div class="timestamp">generated on '
            + time.asctime( time.gmtime() ) + " UTC"
            + "</div>" )

        self.columns = 3

    def sluggify( self, name ):
        '''Sluggify a cross-reference
        
        Python markdown uses a similar approach to process links
        so we need to do this in order to have valid cross-references
        '''
        name = name.lower().strip()
        name = name.replace( " ",  "-")
        return name

    def  make_section_url( self, section, code = False ):
        if code:
            return "../" + self.file_prefix + section.name + "/"
        return self.file_prefix + section.name + ".md"

    def  make_block_url( self, block, name = None, code = False ):
        if name == None:
            name = block.name

        name = self.sluggify( name )

        try:
            section_url = self.make_section_url( block.section, code )
        except:
            # we already have a section
            section_url = self.make_section_url( block, code )

        return section_url + "#" + name

    def make_chapter_url( self, chapter ):
        chapter = ' '.join( chapter )
        slug_chapter = self.sluggify( chapter )
        chapter_url = ("[" + chapter + "]("
        + self.toc_filename + "#" + slug_chapter + ")"
        )
        return chapter_url

    def  make_html_word( self, word ):
        """Analyze a simple word to detect cross-references and markup."""
        # handle cross-references
        m = re_crossref.match( word )
        if m:
            try:
                name = m.group( 'name' )
                rest = m.group( 'rest' )
                block = self.identifiers[name]
                url   = self.make_block_url( block, code = True )
                # display `foo[bar]' as `foo'
                name = re.sub( r'\[.*\]', '', name )
                # normalize url, following RFC 3986
                url = url.replace( "[", "(" )
                url = url.replace( "]", ")" )
                try:
                    # for sections, display title
                    url = ( '&lsquo;<a href="' + url + '">'
                            + block.title + '</a>&rsquo;'
                            + rest )
                except:
                    url = ( '<a href="' + url + '">'
                            + name + '</a>'
                            + rest )
                # NOTE Commented due to problems with field links
                # try:
                #     # for sections, display title
                #     url = ( '[' + block.title + "]" 
                #             + '(' + url + ')'
                #             + rest )
                # except:
                #     url = ( '[' + name + ']'
                #             + '(' + url + ')'
                #             + rest )

                return url
            except:
                # we detected a cross-reference to an unknown item
                sys.stderr.write( "WARNING: undefined cross reference"
                                  + " '" + name + "'.\n" )
                return '?' + name + '?' + rest

        # handle markup for italic and bold
        # NOTE Not required
        # m = re_italic.match( word )
        # if m:
        #     name = m.group( 1 )
        #     rest = m.group( 2 )
        #     return '<i>' + name + '</i>' + rest

        # m = re_bold.match( word )
        # if m:
        #     name = m.group( 1 )
        #     rest = m.group( 2 )
        #     return '<b>' + name + '</b>' + rest

        return html_quote( word )

    def  make_html_para( self, words, in_html = False ):
        """Convert words of a paragraph into tagged Markdown text.  Also handle
           cross references."""
        line = ""
        if words:
            line = self.make_html_word( words[0] )
            for word in words[1:]:
                line = line + " " + self.make_html_word( word )
            # handle hyperlinks
            line = re_url.sub( r'<\1>', line )
            # convert `...' quotations into real left and right single quotes
            line = re.sub( r"(^|\W)`(.*?)'(\W|$)",
                           r'\1&lsquo;\2&rsquo;\3',
                           line )
            # convert tilde into non-breaking space
            line = line.replace( "~", "&nbsp;" )
        # Return
        if in_html:
            # If we are in an HTML tag, return with HTML tags
            return para_header + line + para_footer
        # Otherwise return a Markdown paragraph
        return md_newline + line

    def  make_html_code( self, lines ):
        """Convert a code sequence to HTML."""
        line = code_header + '\n'
        for l in lines:
            # NOTE Markdown REQUIRES HTML special chars in code blocks
            # line = line + html_quote( l ).rstrip() + '\n'
            line = line + l.rstrip() + '\n'

        return line + code_footer

    def  make_html_items( self, items, in_html = False ):
        """Convert a field's content into HTML."""
        lines = []
        for item in items:
            if item.lines:
                lines.append( self.make_html_code( item.lines ) )
            else:
                lines.append( self.make_html_para( item.words, in_html ) )

        return '\n'.join( lines )

    def  print_html_items( self, items, in_html = False ):
        print( self.make_html_items( items, in_html ) )

    def  print_html_field( self, field ):
        if field.name:
            print( '<table><tr valign="top"><td><b>'
                   + field.name
                   + "</b></td><td>" )

        print( self.make_html_items( field.items ) )

        if field.name:
            print( "</td></tr></table>" )

    def  html_source_quote( self, line, block_name = None ):
        result = ""
        while line:
            m = re_source_crossref.match( line )
            if m:
                name   = m.group( 2 )
                prefix = html_quote( m.group( 1 ) )
                length = len( m.group( 0 ) )

                if name == block_name:
                    # this is the current block name, if any
                    result = result + prefix + '<b>' + name + '</b>'
                    # result = result + prefix + name
                
                # Keyword highlighting
                elif re_source_keywords.match( name ):
                    # this is a C keyword
                    result = ( result + prefix
                               + keyword_prefix + name + keyword_suffix )

                elif name in self.identifiers:
                    # this is a known identifier
                    block = self.identifiers[name]
                    id = block.name

                    # link to a field ID if possible
                    try:
                      for markup in block.markups:
                          if markup.tag == 'values':
                              for field in markup.fields:
                                  if field.name:
                                      id = name

                      result = ( result + prefix
                                 + '<a href="'
                                 + self.make_block_url( block, id, code = True )
                                 + '">' + name + '</a>' )
                    except:
                      # sections don't have `markups'; however, we don't
                      # want references to sections here anyway
                      result = result + html_quote( line[:length] )

                else:
                    result = result + html_quote( line[:length] )

                line = line[length:]
            else:
                result = result + html_quote( line )
                line   = []

        return result

    def  print_html_field_list( self, fields ):
        print( '<table class="fields">' )
        for field in fields:
            print( '<tr><td class="val" id="' + self.sluggify(field.name) + '">'
                   + field.name
                   + '</td><td class="desc">' )
            self.print_html_items( field.items, in_html = True )
            print( "</td></tr>" )
        print( "</table>" )

    def  print_html_markup( self, markup ):
        table_fields = []
        for field in markup.fields:
            if field.name:
                # We begin a new series of field or value definitions.  We
                # record them in the `table_fields' list before outputting
                # all of them as a single table.
                table_fields.append( field )
            else:
                if table_fields:
                    self.print_html_field_list( table_fields )
                    table_fields = []

                self.print_html_items( field.items )

        if table_fields:
            self.print_html_field_list( table_fields )

    #
    # formatting the index
    #
    def  index_enter( self ):
        print( self.md_index_header )
        self.index_items = {}

    def  index_name_enter( self, name ):
        block = self.identifiers[name]
        url   = self.make_block_url( block, code = True )
        self.index_items[name] = url

    def  index_exit( self ):
        # `block_index' already contains the sorted list of index names
        count = len( self.block_index )
        rows  = ( count + self.columns - 1 ) // self.columns

        print( '<table class="index">' )
        for r in range( rows ):
            line = "<tr>"
            for c in range( self.columns ):
                i = r + c * rows
                if i < count:
                    bname = self.block_index[r + c * rows]
                    url   = self.index_items[bname]
                    # display `foo[bar]' as `foo (bar)'
                    bname = bname.replace( "[", " (" )
                    bname = bname.replace( "]", ")"  )
                    # normalize url, following RFC 3986
                    url = url.replace( "[", "(" )
                    url = url.replace( "]", ")" )
                    line  = ( line + '<td><a href="' + url + '">'
                              + bname + '</a></td>' )
                else:
                    line = line + '<td></td>'
            line = line + "</tr>"
            print( line )

        print( "</table>" )

        # NOTE Not needed
        # print( index_footer_start
        #        + self.file_prefix + "toc.html"
        #        + index_footer_end )

        print( self.html_footer )

        self.index_items = {}

    def  index_dump( self, index_filename = None ):
        if index_filename == None:
            index_filename = self.file_prefix + "index.md"

        Formatter.index_dump( self, index_filename )

    #
    # formatting the table of contents
    #
    def  toc_enter( self ):
        print( self.html_toc_header )
        print( "# Table of Contents" )

    def  toc_chapter_enter( self, chapter ):
        print( chapter_header + " ".join( chapter.title ) + md_newline )
        print( '<table class="toc">' )

    def  toc_section_enter( self, section ):
        print( '<tr><td class="link">'
               + '<a href="' + self.make_section_url( section, code = True ) + '">'
               + section.title + '</a></td><td class="desc">' )
        print( self.make_html_para( section.abstract, in_html = True ) )

    def  toc_section_exit( self, section ):
        print( "</td></tr>" )

    def  toc_chapter_exit( self, chapter ):
        print( "</table>" )
        # NOTE Not required
        #print( chapter_footer )

    def  toc_index( self, index_filename ):
        print( chapter_header
               + '[Global Index](' + index_filename + ')'
            )

    def  toc_exit( self ):
        # NOTE not required
        # print( toc_footer_start
        #        + self.file_prefix + "index.html"
        #        + toc_footer_end )

        print( self.html_footer )

    def  toc_dump( self, toc_filename = None, index_filename = None ):
        if toc_filename == None:
            toc_filename = self.file_prefix + "toc.md"

        if index_filename == None:
            index_filename = self.file_prefix + "index.md"

        Formatter.toc_dump( self, toc_filename, index_filename )

    #
    # formatting sections
    #
    def  section_enter( self, section ):
        try:
            print( md_header_1 +  self.make_chapter_url( section.chapter.title )
               +  md_nav_separator + section.title 
               + md_line_sep )
        except:
            sys.stderr.write("No chapter name for Section '" + section.title + "'\n")
        print( md_h1 + section.title )

        maxwidth = 0
        for b in section.blocks.values():
            if len( b.name ) > maxwidth:
                maxwidth = len( b.name )

        width = 70  # XXX magic number
        if maxwidth > 0:
            # print section synopsis
            print( section_synopsis_header )
            # NOTE Not needed as TOC is automatic
            # print( '<table class="synopsis">' )

            # columns = width // maxwidth
            # if columns < 1:
            #     columns = 1

            # count = len( section.block_names )
            # # don't handle last entry if it is empty
            # if section.block_names[-1] == "/empty/":
            #     count -= 1
            # rows  = ( count + columns - 1 ) // columns

            # for r in range( rows ):
            #     line = "<tr>"
            #     for c in range( columns ):
            #         i = r + c * rows
            #         line = line + '<td>'
            #         if i < count:
            #             name = section.block_names[i]
            #             if name == "/empty/":
            #                 # it can happen that a complete row is empty, and
            #                 # without a proper `filler' the browser might
            #                 # collapse the row to a much smaller height (or
            #                 # even omit it completely)
            #                 line = line + "&nbsp;"
            #             else:
            #                 url = name
            #                 # display `foo[bar]' as `foo'
            #                 name = re.sub( r'\[.*\]', '', name )
            #                 # normalize url, following RFC 3986
            #                 url = string.replace( url, "[", "(" )
            #                 url = string.replace( url, "]", ")" )
            #                 line = ( line + '<a href="#' + url + '">'
            #                          + name + '</a>' )

            #         line = line + '</td>'
            #     line = line + "</tr>"
            #     print( line )

            # print( "</table>" )
            #print( section_synopsis_footer )

        #print( description_header )
        print( self.make_html_items( section.description ) )
        print( description_footer )

    def  block_enter( self, block ):
        
        # place html anchor if needed
        if block.name:
            url = block.name
            # display `foo[bar]' as `foo'
            name = re.sub( r'\[.*\]', '', block.name )
            # normalize url, following RFC 3986
            url = url.replace( "[", "(" )
            url = url.replace( "]", ")" )
            # print( '<h3 id="' + url + '">' + name + '</h3>' )
            print( '## ' + name + md_newline )

        # dump the block C source lines now
        if block.code:
            header = ''
            for f in self.headers.keys():
                header_filename = os.path.normpath(block.source.filename)
                if header_filename.find( os.path.normpath( f ) ) >= 0:
                    header = self.headers[f] + ' (' + f + ')'
                    break

#           if not header:
#               sys.stderr.write(
#                 "WARNING: No header macro for"
#                 + " '" + block.source.filename + "'.\n" )

            if header:
                print( 'Defined in ' + header + '.' )

            print( source_header )
            for l in block.code:
                print( self.html_source_quote( l, block.name ) )
            print( source_footer )

    def  markup_enter( self, markup, block ):
        if markup.tag == "description":
            print( description_header )
        else:
            print( md_h4 + markup.tag + md_h4_inter )

        self.print_html_markup( markup )

    def  markup_exit( self, markup, block ):
        if markup.tag == "description":
            print( description_footer )
        else:
            print( "" )

    def  block_exit( self, block ):
        # NOTE not required
        # print( block_footer_start + self.file_prefix + "index.html"
        #        + block_footer_middle + self.file_prefix + "toc.html"
        #        + block_footer_end )
        pass
        print("<hr />\n")

    def  section_exit( self, section ):
        # NOTE not required
        # print( html_footer )
        pass

    def  section_dump_all( self ):
        for section in self.sections:
            self.section_dump( section,
                               self.file_prefix + section.name + '.md' )

# eof