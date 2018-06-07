[Docs](ft2-index.md) &raquo; Table of Contents

-------------------------------

# FreeType-2.9.1 API Reference

# Table of Contents
## General Remarks
<table class="toc">
<tr><td class="link">[FreeType's header inclusion scheme](ft2-header_inclusion.md)</td><td class="desc">

How client applications should include FreeType header files.
</td></tr>
<tr><td class="link">[User allocation](ft2-user_allocation.md)</td><td class="desc">

How client applications should allocate FreeType data structures.
</td></tr>
</table>
## Core API
<table class="toc">
<tr><td class="link">[FreeType Version](ft2-version.md)</td><td class="desc">

Functions and macros related to FreeType versions.
</td></tr>
<tr><td class="link">[Basic Data Types](ft2-basic_types.md)</td><td class="desc">

The basic data types defined by the library.
</td></tr>
<tr><td class="link">[Base Interface](ft2-base_interface.md)</td><td class="desc">

The FreeType&nbsp;2 base font interface.
</td></tr>
<tr><td class="link">[Unicode Variation Sequences](ft2-glyph_variants.md)</td><td class="desc">

The FreeType&nbsp;2 interface to Unicode Variation Sequences (UVS), using the SFNT cmap format&nbsp;14.
</td></tr>
<tr><td class="link">[Glyph Management](ft2-glyph_management.md)</td><td class="desc">

Generic interface to manage individual glyph data.
</td></tr>
<tr><td class="link">[Mac Specific Interface](ft2-mac_specific.md)</td><td class="desc">

Only available on the Macintosh.
</td></tr>
<tr><td class="link">[Size Management](ft2-sizes_management.md)</td><td class="desc">

Managing multiple sizes per face.
</td></tr>
<tr><td class="link">[Header File Macros](ft2-header_file_macros.md)</td><td class="desc">

Macro definitions used to #include specific header files.
</td></tr>
</table>
## Format-Specific API
<table class="toc">
<tr><td class="link">[Multiple Masters](ft2-multiple_masters.md)</td><td class="desc">

How to manage Multiple Masters fonts.
</td></tr>
<tr><td class="link">[TrueType Tables](ft2-truetype_tables.md)</td><td class="desc">

TrueType specific table types and functions.
</td></tr>
<tr><td class="link">[Type 1 Tables](ft2-type1_tables.md)</td><td class="desc">

Type&nbsp;1 (PostScript) specific font tables.
</td></tr>
<tr><td class="link">[SFNT Names](ft2-sfnt_names.md)</td><td class="desc">

Access the names embedded in TrueType and OpenType files.
</td></tr>
<tr><td class="link">[BDF and PCF Files](ft2-bdf_fonts.md)</td><td class="desc">

BDF and PCF specific API.
</td></tr>
<tr><td class="link">[CID Fonts](ft2-cid_fonts.md)</td><td class="desc">

CID-keyed font specific API.
</td></tr>
<tr><td class="link">[PFR Fonts](ft2-pfr_fonts.md)</td><td class="desc">

PFR/TrueDoc specific API.
</td></tr>
<tr><td class="link">[Window FNT Files](ft2-winfnt_fonts.md)</td><td class="desc">

Windows FNT specific API.
</td></tr>
<tr><td class="link">[Font Formats](ft2-font_formats.md)</td><td class="desc">

Getting the font format.
</td></tr>
<tr><td class="link">[Gasp Table](ft2-gasp_table.md)</td><td class="desc">

Retrieving TrueType &lsquo;gasp&rsquo; table entries.
</td></tr>
</table>
## Controlling FreeType Modules
<table class="toc">
<tr><td class="link">[The auto-hinter](ft2-auto_hinter.md)</td><td class="desc">

Controlling the auto-hinting module.
</td></tr>
<tr><td class="link">[The CFF driver](ft2-cff_driver.md)</td><td class="desc">

Controlling the CFF driver module.
</td></tr>
<tr><td class="link">[The Type 1 and CID drivers](ft2-t1_cid_driver.md)</td><td class="desc">

Controlling the Type&nbsp;1 and CID driver modules.
</td></tr>
<tr><td class="link">[The TrueType driver](ft2-tt_driver.md)</td><td class="desc">

Controlling the TrueType driver module.
</td></tr>
<tr><td class="link">[The PCF driver](ft2-pcf_driver.md)</td><td class="desc">

Controlling the PCF driver module.
</td></tr>
<tr><td class="link">[Driver properties](ft2-properties.md)</td><td class="desc">

Controlling driver modules.
</td></tr>
<tr><td class="link">[Parameter Tags](ft2-parameter_tags.md)</td><td class="desc">

Macros for driver property and font loading parameter tags.
</td></tr>
</table>
## Cache Sub-System
<table class="toc">
<tr><td class="link">[Cache Sub-System](ft2-cache_subsystem.md)</td><td class="desc">

How to cache face, size, and glyph data with FreeType&nbsp;2.
</td></tr>
</table>
## Support API
<table class="toc">
<tr><td class="link">[Computations](ft2-computations.md)</td><td class="desc">

Crunching fixed numbers and vectors.
</td></tr>
<tr><td class="link">[List Processing](ft2-list_processing.md)</td><td class="desc">

Simple management of lists.
</td></tr>
<tr><td class="link">[Outline Processing](ft2-outline_processing.md)</td><td class="desc">

Functions to create, transform, and render vectorial glyph images.
</td></tr>
<tr><td class="link">[Quick retrieval of advance values](ft2-quick_advance.md)</td><td class="desc">

Retrieve horizontal and vertical advance values without processing glyph outlines, if possible.
</td></tr>
<tr><td class="link">[Bitmap Handling](ft2-bitmap_handling.md)</td><td class="desc">

Handling FT_Bitmap objects.
</td></tr>
<tr><td class="link">[Scanline Converter](ft2-raster.md)</td><td class="desc">

How vectorial outlines are converted into bitmaps and pixmaps.
</td></tr>
<tr><td class="link">[Glyph Stroker](ft2-glyph_stroker.md)</td><td class="desc">

Generating bordered and stroked glyphs.
</td></tr>
<tr><td class="link">[System Interface](ft2-system_interface.md)</td><td class="desc">

How FreeType manages memory and i/o.
</td></tr>
<tr><td class="link">[Module Management](ft2-module_management.md)</td><td class="desc">

How to add, upgrade, remove, and control modules from FreeType.
</td></tr>
<tr><td class="link">[GZIP Streams](ft2-gzip.md)</td><td class="desc">

Using gzip-compressed font files.
</td></tr>
<tr><td class="link">[LZW Streams](ft2-lzw.md)</td><td class="desc">

Using LZW-compressed font files.
</td></tr>
<tr><td class="link">[BZIP2 Streams](ft2-bzip2.md)</td><td class="desc">

Using bzip2-compressed font files.
</td></tr>
<tr><td class="link">[LCD Filtering](ft2-lcd_filtering.md)</td><td class="desc">

Remove color fringes of subpixel-rendered bitmaps.
</td></tr>
</table>
## Error Codes
<table class="toc">
<tr><td class="link">[Error Enumerations](ft2-error_enumerations.md)</td><td class="desc">

How to handle errors and error strings.
</td></tr>
<tr><td class="link">[Error Code Values](ft2-error_code_values.md)</td><td class="desc">

All possible error codes returned by FreeType functions.
</td></tr>
</table>
## Miscellaneous
<table class="toc">
<tr><td class="link">[OpenType Validation](ft2-ot_validation.md)</td><td class="desc">

An API to validate OpenType tables.
</td></tr>
<tr><td class="link">[Incremental Loading](ft2-incremental.md)</td><td class="desc">

Custom Glyph Loading.
</td></tr>
<tr><td class="link">[The TrueType Engine](ft2-truetype_engine.md)</td><td class="desc">

TrueType bytecode support.
</td></tr>
<tr><td class="link">[Glyph Color Management](ft2-color_management.md)</td><td class="desc">

Retrieving and manipulating OpenType's &lsquo;CPAL&rsquo; table entries.
</td></tr>
<tr><td class="link">[TrueTypeGX/AAT Validation](ft2-gx_validation.md)</td><td class="desc">

An API to validate TrueTypeGX/AAT tables.
</td></tr>
</table>
## [Global Index](ft2-index.md)
<div class="timestamp">generated on Thu Jun  7 18:44:12 2018</div>
