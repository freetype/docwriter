[Docs](ft2-index.md) &raquo; [Core API](ft2-toc.md#core-api) &raquo; Header File Macros

-------------------------------


# Header File Macros

## Synopsis

The following macros are defined to the name of specific FreeType&nbsp;2 header files. They can be used directly in #include statements as in:
```
  #include FT_FREETYPE_H
  #include FT_MULTIPLE_MASTERS_H
  #include FT_GLYPH_H
```

There are several reasons why we are now using macros to name public header files. The first one is that such macros are not limited to the infamous 8.3&nbsp;naming rule required by DOS (and &lsquo;FT_MULTIPLE_MASTERS_H&rsquo; is a lot more meaningful than &lsquo;ftmm.h&rsquo;).

The second reason is that it allows for more flexibility in the way FreeType&nbsp;2 is installed on a given system.

## FT_CONFIG_CONFIG_H


<pre>
#ifndef <b>FT_CONFIG_CONFIG_H</b>
#define <b>FT_CONFIG_CONFIG_H</b>  &lt;freetype/config/ftconfig.h&gt;
#endif
</pre>


A macro used in #include statements to name the file containing FreeType&nbsp;2 configuration data.

<hr />

## FT_CONFIG_STANDARD_LIBRARY_H


<pre>
#ifndef <b>FT_CONFIG_STANDARD_LIBRARY_H</b>
#define <b>FT_CONFIG_STANDARD_LIBRARY_H</b>  &lt;freetype/config/ftstdlib.h&gt;
#endif
</pre>


A macro used in #include statements to name the file containing FreeType&nbsp;2 interface to the standard C library functions.

<hr />

## FT_CONFIG_OPTIONS_H


<pre>
#ifndef <b>FT_CONFIG_OPTIONS_H</b>
#define <b>FT_CONFIG_OPTIONS_H</b>  &lt;freetype/config/ftoption.h&gt;
#endif
</pre>


A macro used in #include statements to name the file containing FreeType&nbsp;2 project-specific configuration options.

<hr />

## FT_CONFIG_MODULES_H


<pre>
#ifndef <b>FT_CONFIG_MODULES_H</b>
#define <b>FT_CONFIG_MODULES_H</b>  &lt;freetype/config/ftmodule.h&gt;
#endif
</pre>


A macro used in #include statements to name the file containing the list of FreeType&nbsp;2 modules that are statically linked to new library instances in <a href="../ft2-base_interface/#ft_init_freetype">FT_Init_FreeType</a>.

<hr />

## FT_FREETYPE_H


<pre>
#define <b>FT_FREETYPE_H</b>  &lt;freetype/freetype.h&gt;
</pre>


A macro used in #include statements to name the file containing the base FreeType&nbsp;2 API.

<hr />

## FT_ERRORS_H


<pre>
#define <b>FT_ERRORS_H</b>  &lt;freetype/fterrors.h&gt;
</pre>


A macro used in #include statements to name the file containing the list of FreeType&nbsp;2 error codes (and messages).

It is included by <a href="../ft2-header_file_macros/#ft_freetype_h">FT_FREETYPE_H</a>.

<hr />

## FT_MODULE_ERRORS_H


<pre>
#define <b>FT_MODULE_ERRORS_H</b>  &lt;freetype/ftmoderr.h&gt;
</pre>


A macro used in #include statements to name the file containing the list of FreeType&nbsp;2 module error offsets (and messages).

<hr />

## FT_SYSTEM_H


<pre>
#define <b>FT_SYSTEM_H</b>  &lt;freetype/ftsystem.h&gt;
</pre>


A macro used in #include statements to name the file containing the FreeType&nbsp;2 interface to low-level operations (i.e., memory management and stream i/o).

It is included by <a href="../ft2-header_file_macros/#ft_freetype_h">FT_FREETYPE_H</a>.

<hr />

## FT_IMAGE_H


<pre>
#define <b>FT_IMAGE_H</b>  &lt;freetype/ftimage.h&gt;
</pre>


A macro used in #include statements to name the file containing type definitions related to glyph images (i.e., bitmaps, outlines, scan-converter parameters).

It is included by <a href="../ft2-header_file_macros/#ft_freetype_h">FT_FREETYPE_H</a>.

<hr />

## FT_TYPES_H


<pre>
#define <b>FT_TYPES_H</b>  &lt;freetype/fttypes.h&gt;
</pre>


A macro used in #include statements to name the file containing the basic data types defined by FreeType&nbsp;2.

It is included by <a href="../ft2-header_file_macros/#ft_freetype_h">FT_FREETYPE_H</a>.

<hr />

## FT_LIST_H


<pre>
#define <b>FT_LIST_H</b>  &lt;freetype/ftlist.h&gt;
</pre>


A macro used in #include statements to name the file containing the list management API of FreeType&nbsp;2.

(Most applications will never need to include this file.)

<hr />

## FT_OUTLINE_H


<pre>
#define <b>FT_OUTLINE_H</b>  &lt;freetype/ftoutln.h&gt;
</pre>


A macro used in #include statements to name the file containing the scalable outline management API of FreeType&nbsp;2.

<hr />

## FT_SIZES_H


<pre>
#define <b>FT_SIZES_H</b>  &lt;freetype/ftsizes.h&gt;
</pre>


A macro used in #include statements to name the file containing the API which manages multiple <a href="../ft2-base_interface/#ft_size">FT_Size</a> objects per face.

<hr />

## FT_MODULE_H


<pre>
#define <b>FT_MODULE_H</b>  &lt;freetype/ftmodapi.h&gt;
</pre>


A macro used in #include statements to name the file containing the module management API of FreeType&nbsp;2.

<hr />

## FT_RENDER_H


<pre>
#define <b>FT_RENDER_H</b>  &lt;freetype/ftrender.h&gt;
</pre>


A macro used in #include statements to name the file containing the renderer module management API of FreeType&nbsp;2.

<hr />

## FT_DRIVER_H


<pre>
#define <b>FT_DRIVER_H</b>  &lt;freetype/ftdriver.h&gt;
</pre>


A macro used in #include statements to name the file containing structures and macros related to the driver modules.

<hr />

## FT_AUTOHINTER_H


<pre>
#define <b>FT_AUTOHINTER_H</b>  <a href="../ft2-header_file_macros/#ft_driver_h">FT_DRIVER_H</a>
</pre>


A macro used in #include statements to name the file containing structures and macros related to the auto-hinting module.

Deprecated since version 2.9; use <a href="../ft2-header_file_macros/#ft_driver_h">FT_DRIVER_H</a> instead.

<hr />

## FT_CFF_DRIVER_H


<pre>
#define <b>FT_CFF_DRIVER_H</b>  <a href="../ft2-header_file_macros/#ft_driver_h">FT_DRIVER_H</a>
</pre>


A macro used in #include statements to name the file containing structures and macros related to the CFF driver module.

Deprecated since version 2.9; use <a href="../ft2-header_file_macros/#ft_driver_h">FT_DRIVER_H</a> instead.

<hr />

## FT_TRUETYPE_DRIVER_H


<pre>
#define <b>FT_TRUETYPE_DRIVER_H</b>  <a href="../ft2-header_file_macros/#ft_driver_h">FT_DRIVER_H</a>
</pre>


A macro used in #include statements to name the file containing structures and macros related to the TrueType driver module.

Deprecated since version 2.9; use <a href="../ft2-header_file_macros/#ft_driver_h">FT_DRIVER_H</a> instead.

<hr />

## FT_PCF_DRIVER_H


<pre>
#define <b>FT_PCF_DRIVER_H</b>  <a href="../ft2-header_file_macros/#ft_driver_h">FT_DRIVER_H</a>
</pre>


A macro used in #include statements to name the file containing structures and macros related to the PCF driver module.

Deprecated since version 2.9; use <a href="../ft2-header_file_macros/#ft_driver_h">FT_DRIVER_H</a> instead.

<hr />

## FT_TYPE1_TABLES_H


<pre>
#define <b>FT_TYPE1_TABLES_H</b>  &lt;freetype/t1tables.h&gt;
</pre>


A macro used in #include statements to name the file containing the types and API specific to the Type&nbsp;1 format.

<hr />

## FT_TRUETYPE_IDS_H


<pre>
#define <b>FT_TRUETYPE_IDS_H</b>  &lt;freetype/ttnameid.h&gt;
</pre>


A macro used in #include statements to name the file containing the enumeration values which identify name strings, languages, encodings, etc. This file really contains a _large_ set of constant macro definitions, taken from the TrueType and OpenType specifications.

<hr />

## FT_TRUETYPE_TABLES_H


<pre>
#define <b>FT_TRUETYPE_TABLES_H</b>  &lt;freetype/tttables.h&gt;
</pre>


A macro used in #include statements to name the file containing the types and API specific to the TrueType (as well as OpenType) format.

<hr />

## FT_TRUETYPE_TAGS_H


<pre>
#define <b>FT_TRUETYPE_TAGS_H</b>  &lt;freetype/tttags.h&gt;
</pre>


A macro used in #include statements to name the file containing the definitions of TrueType four-byte &lsquo;tags&rsquo; which identify blocks in SFNT-based font formats (i.e., TrueType and OpenType).

<hr />

## FT_BDF_H


<pre>
#define <b>FT_BDF_H</b>  &lt;freetype/ftbdf.h&gt;
</pre>


A macro used in #include statements to name the file containing the definitions of an API which accesses BDF-specific strings from a face.

<hr />

## FT_CID_H


<pre>
#define <b>FT_CID_H</b>  &lt;freetype/ftcid.h&gt;
</pre>


A macro used in #include statements to name the file containing the definitions of an API which access CID font information from a face.

<hr />

## FT_GZIP_H


<pre>
#define <b>FT_GZIP_H</b>  &lt;freetype/ftgzip.h&gt;
</pre>


A macro used in #include statements to name the file containing the definitions of an API which supports gzip-compressed files.

<hr />

## FT_LZW_H


<pre>
#define <b>FT_LZW_H</b>  &lt;freetype/ftlzw.h&gt;
</pre>


A macro used in #include statements to name the file containing the definitions of an API which supports LZW-compressed files.

<hr />

## FT_BZIP2_H


<pre>
#define <b>FT_BZIP2_H</b>  &lt;freetype/ftbzip2.h&gt;
</pre>


A macro used in #include statements to name the file containing the definitions of an API which supports bzip2-compressed files.

<hr />

## FT_WINFONTS_H


<pre>
#define <b>FT_WINFONTS_H</b>   &lt;freetype/ftwinfnt.h&gt;
</pre>


A macro used in #include statements to name the file containing the definitions of an API which supports Windows FNT files.

<hr />

## FT_GLYPH_H


<pre>
#define <b>FT_GLYPH_H</b>  &lt;freetype/ftglyph.h&gt;
</pre>


A macro used in #include statements to name the file containing the API of the optional glyph management component.

<hr />

## FT_BITMAP_H


<pre>
#define <b>FT_BITMAP_H</b>  &lt;freetype/ftbitmap.h&gt;
</pre>


A macro used in #include statements to name the file containing the API of the optional bitmap conversion component.

<hr />

## FT_BBOX_H


<pre>
#define <b>FT_BBOX_H</b>  &lt;freetype/ftbbox.h&gt;
</pre>


A macro used in #include statements to name the file containing the API of the optional exact bounding box computation routines.

<hr />

## FT_CACHE_H


<pre>
#define <b>FT_CACHE_H</b>  &lt;freetype/ftcache.h&gt;
</pre>


A macro used in #include statements to name the file containing the API of the optional FreeType&nbsp;2 cache sub-system.

<hr />

## FT_MAC_H


<pre>
#define <b>FT_MAC_H</b>  &lt;freetype/ftmac.h&gt;
</pre>


A macro used in #include statements to name the file containing the Macintosh-specific FreeType&nbsp;2 API. The latter is used to access fonts embedded in resource forks.

This header file must be explicitly included by client applications compiled on the Mac (note that the base API still works though).

<hr />

## FT_MULTIPLE_MASTERS_H


<pre>
#define <b>FT_MULTIPLE_MASTERS_H</b>  &lt;freetype/ftmm.h&gt;
</pre>


A macro used in #include statements to name the file containing the optional multiple-masters management API of FreeType&nbsp;2.

<hr />

## FT_SFNT_NAMES_H


<pre>
#define <b>FT_SFNT_NAMES_H</b>  &lt;freetype/ftsnames.h&gt;
</pre>


A macro used in #include statements to name the file containing the optional FreeType&nbsp;2 API which accesses embedded &lsquo;name&rsquo; strings in SFNT-based font formats (i.e., TrueType and OpenType).

<hr />

## FT_OPENTYPE_VALIDATE_H


<pre>
#define <b>FT_OPENTYPE_VALIDATE_H</b>  &lt;freetype/ftotval.h&gt;
</pre>


A macro used in #include statements to name the file containing the optional FreeType&nbsp;2 API which validates OpenType tables (BASE, GDEF, GPOS, GSUB, JSTF).

<hr />

## FT_GX_VALIDATE_H


<pre>
#define <b>FT_GX_VALIDATE_H</b>  &lt;freetype/ftgxval.h&gt;
</pre>


A macro used in #include statements to name the file containing the optional FreeType&nbsp;2 API which validates TrueTypeGX/AAT tables (feat, mort, morx, bsln, just, kern, opbd, trak, prop).

<hr />

## FT_PFR_H


<pre>
#define <b>FT_PFR_H</b>  &lt;freetype/ftpfr.h&gt;
</pre>


A macro used in #include statements to name the file containing the FreeType&nbsp;2 API which accesses PFR-specific data.

<hr />

## FT_STROKER_H


<pre>
#define <b>FT_STROKER_H</b>  &lt;freetype/ftstroke.h&gt;
</pre>


A macro used in #include statements to name the file containing the FreeType&nbsp;2 API which provides functions to stroke outline paths.

<hr />

## FT_SYNTHESIS_H


<pre>
#define <b>FT_SYNTHESIS_H</b>  &lt;freetype/ftsynth.h&gt;
</pre>


A macro used in #include statements to name the file containing the FreeType&nbsp;2 API which performs artificial obliquing and emboldening.

<hr />

## FT_FONT_FORMATS_H


<pre>
#define <b>FT_FONT_FORMATS_H</b>  &lt;freetype/ftfntfmt.h&gt;

  /* deprecated */
#define FT_XFREE86_H  <b>FT_FONT_FORMATS_H</b>
</pre>


A macro used in #include statements to name the file containing the FreeType&nbsp;2 API which provides functions specific to font formats.

<hr />

## FT_TRIGONOMETRY_H


<pre>
#define <b>FT_TRIGONOMETRY_H</b>  &lt;freetype/fttrigon.h&gt;
</pre>


A macro used in #include statements to name the file containing the FreeType&nbsp;2 API which performs trigonometric computations (e.g., cosines and arc tangents).

<hr />

## FT_LCD_FILTER_H


<pre>
#define <b>FT_LCD_FILTER_H</b>  &lt;freetype/ftlcdfil.h&gt;
</pre>


A macro used in #include statements to name the file containing the FreeType&nbsp;2 API which performs color filtering for subpixel rendering.

<hr />

## FT_INCREMENTAL_H


<pre>
#define <b>FT_INCREMENTAL_H</b>  &lt;freetype/ftincrem.h&gt;
</pre>


A macro used in #include statements to name the file containing the FreeType&nbsp;2 API which performs incremental glyph loading.

<hr />

## FT_GASP_H


<pre>
#define <b>FT_GASP_H</b>  &lt;freetype/ftgasp.h&gt;
</pre>


A macro used in #include statements to name the file containing the FreeType&nbsp;2 API which returns entries from the TrueType GASP table.

<hr />

## FT_ADVANCES_H


<pre>
#define <b>FT_ADVANCES_H</b>  &lt;freetype/ftadvanc.h&gt;
</pre>


A macro used in #include statements to name the file containing the FreeType&nbsp;2 API which returns individual and ranged glyph advances.

<hr />

## FT_COLOR_H


<pre>
#define <b>FT_COLOR_H</b>  &lt;freetype/ftcolor.h&gt;
</pre>


A macro used in #include statements to name the file containing the FreeType&nbsp;2 API which handles the OpenType CPAL table.

<hr />

