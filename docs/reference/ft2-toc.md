[Docs](ft2-index.md) &raquo; Table of Contents

-------------------------------

# FreeType-2.9.1 API Reference

# Table of Contents
## General Remarks

<table class="toc">
<tr><td class="link"><a href="../ft2-header_inclusion/">FreeType's header inclusion scheme</a></td><td class="desc">
<p>How client applications should include FreeType header files.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-user_allocation/">User allocation</a></td><td class="desc">
<p>How client applications should allocate FreeType data structures.</p>
</td></tr>
</table>
## Core API

<table class="toc">
<tr><td class="link"><a href="../ft2-version/">FreeType Version</a></td><td class="desc">
<p>Functions and macros related to FreeType versions.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-basic_types/">Basic Data Types</a></td><td class="desc">
<p>The basic data types defined by the library.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-base_interface/">Base Interface</a></td><td class="desc">
<p>The FreeType&nbsp;2 base font interface.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-glyph_variants/">Unicode Variation Sequences</a></td><td class="desc">
<p>The FreeType&nbsp;2 interface to Unicode Variation Sequences (UVS), using the SFNT cmap format&nbsp;14.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-glyph_management/">Glyph Management</a></td><td class="desc">
<p>Generic interface to manage individual glyph data.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-mac_specific/">Mac Specific Interface</a></td><td class="desc">
<p>Only available on the Macintosh.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-sizes_management/">Size Management</a></td><td class="desc">
<p>Managing multiple sizes per face.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-header_file_macros/">Header File Macros</a></td><td class="desc">
<p>Macro definitions used to #include specific header files.</p>
</td></tr>
</table>
## Format-Specific API

<table class="toc">
<tr><td class="link"><a href="../ft2-multiple_masters/">Multiple Masters</a></td><td class="desc">
<p>How to manage Multiple Masters fonts.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-truetype_tables/">TrueType Tables</a></td><td class="desc">
<p>TrueType specific table types and functions.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-type1_tables/">Type 1 Tables</a></td><td class="desc">
<p>Type&nbsp;1 (PostScript) specific font tables.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-sfnt_names/">SFNT Names</a></td><td class="desc">
<p>Access the names embedded in TrueType and OpenType files.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-bdf_fonts/">BDF and PCF Files</a></td><td class="desc">
<p>BDF and PCF specific API.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-cid_fonts/">CID Fonts</a></td><td class="desc">
<p>CID-keyed font specific API.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-pfr_fonts/">PFR Fonts</a></td><td class="desc">
<p>PFR/TrueDoc specific API.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-winfnt_fonts/">Window FNT Files</a></td><td class="desc">
<p>Windows FNT specific API.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-font_formats/">Font Formats</a></td><td class="desc">
<p>Getting the font format.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-gasp_table/">Gasp Table</a></td><td class="desc">
<p>Retrieving TrueType &lsquo;gasp&rsquo; table entries.</p>
</td></tr>
</table>
## Controlling FreeType Modules

<table class="toc">
<tr><td class="link"><a href="../ft2-auto_hinter/">The auto-hinter</a></td><td class="desc">
<p>Controlling the auto-hinting module.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-cff_driver/">The CFF driver</a></td><td class="desc">
<p>Controlling the CFF driver module.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-t1_cid_driver/">The Type 1 and CID drivers</a></td><td class="desc">
<p>Controlling the Type&nbsp;1 and CID driver modules.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-tt_driver/">The TrueType driver</a></td><td class="desc">
<p>Controlling the TrueType driver module.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-pcf_driver/">The PCF driver</a></td><td class="desc">
<p>Controlling the PCF driver module.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-properties/">Driver properties</a></td><td class="desc">
<p>Controlling driver modules.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-parameter_tags/">Parameter Tags</a></td><td class="desc">
<p>Macros for driver property and font loading parameter tags.</p>
</td></tr>
</table>
## Cache Sub-System

<table class="toc">
<tr><td class="link"><a href="../ft2-cache_subsystem/">Cache Sub-System</a></td><td class="desc">
<p>How to cache face, size, and glyph data with FreeType&nbsp;2.</p>
</td></tr>
</table>
## Support API

<table class="toc">
<tr><td class="link"><a href="../ft2-computations/">Computations</a></td><td class="desc">
<p>Crunching fixed numbers and vectors.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-list_processing/">List Processing</a></td><td class="desc">
<p>Simple management of lists.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-outline_processing/">Outline Processing</a></td><td class="desc">
<p>Functions to create, transform, and render vectorial glyph images.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-quick_advance/">Quick retrieval of advance values</a></td><td class="desc">
<p>Retrieve horizontal and vertical advance values without processing glyph outlines, if possible.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-bitmap_handling/">Bitmap Handling</a></td><td class="desc">
<p>Handling FT_Bitmap objects.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-raster/">Scanline Converter</a></td><td class="desc">
<p>How vectorial outlines are converted into bitmaps and pixmaps.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-glyph_stroker/">Glyph Stroker</a></td><td class="desc">
<p>Generating bordered and stroked glyphs.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-system_interface/">System Interface</a></td><td class="desc">
<p>How FreeType manages memory and i/o.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-module_management/">Module Management</a></td><td class="desc">
<p>How to add, upgrade, remove, and control modules from FreeType.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-gzip/">GZIP Streams</a></td><td class="desc">
<p>Using gzip-compressed font files.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-lzw/">LZW Streams</a></td><td class="desc">
<p>Using LZW-compressed font files.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-bzip2/">BZIP2 Streams</a></td><td class="desc">
<p>Using bzip2-compressed font files.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-lcd_rendering/">Subpixel Rendering</a></td><td class="desc">
<p>API to control subpixel rendering.</p>
</td></tr>
</table>
## Error Codes

<table class="toc">
<tr><td class="link"><a href="../ft2-error_enumerations/">Error Enumerations</a></td><td class="desc">
<p>How to handle errors and error strings.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-error_code_values/">Error Code Values</a></td><td class="desc">
<p>All possible error codes returned by FreeType functions.</p>
</td></tr>
</table>
## Miscellaneous

<table class="toc">
<tr><td class="link"><a href="../ft2-ot_validation/">OpenType Validation</a></td><td class="desc">
<p>An API to validate OpenType tables.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-incremental/">Incremental Loading</a></td><td class="desc">
<p>Custom Glyph Loading.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-truetype_engine/">The TrueType Engine</a></td><td class="desc">
<p>TrueType bytecode support.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-color_management/">Glyph Color Management</a></td><td class="desc">
<p>Retrieving and manipulating OpenType's &lsquo;CPAL&rsquo; table data.</p>
</td></tr>
<tr><td class="link"><a href="../ft2-gx_validation/">TrueTypeGX/AAT Validation</a></td><td class="desc">
<p>An API to validate TrueTypeGX/AAT tables.</p>
</td></tr>
</table>
## [Global Index](ft2-index.md)
<div class="timestamp">generated on Sun Jun 10 18:20:16 2018 UTC</div>
