[Docs](ft2-index.md) &raquo; [Core API](ft2-toc.md#core-api) &raquo; FreeType Version

-------------------------------


# FreeType Version

## Synopsis

Note that those functions and macros are of limited use because even a new release of FreeType with only documentation changes increases the version number.

## FT_Library_Version

Defined in FT_FREETYPE_H (freetype/freetype.h).

<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Library_Version</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>   library,
                      <a href="../ft2-basic_types/#ft_int">FT_Int</a>      *amajor,
                      <a href="../ft2-basic_types/#ft_int">FT_Int</a>      *aminor,
                      <a href="../ft2-basic_types/#ft_int">FT_Int</a>      *apatch );
</pre>


Return the version of the FreeType library being used. This is useful when dynamically linking to the library, since one cannot use the macros <a href="../ft2-version/#freetype_xxx">FREETYPE_MAJOR</a>, <a href="../ft2-version/#freetype_xxx">FREETYPE_MINOR</a>, and <a href="../ft2-version/#freetype_xxx">FREETYPE_PATCH</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">

A source library handle.
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="amajor">amajor</td><td class="desc">

The major version number.
</td></tr>
<tr><td class="val" id="aminor">aminor</td><td class="desc">

The minor version number.
</td></tr>
<tr><td class="val" id="apatch">apatch</td><td class="desc">

The patch version number.
</td></tr>
</table>

<h4>note</h4>

The reason why this function takes a &lsquo;library&rsquo; argument is because certain programs implement library initialization in a custom way that doesn't use <a href="../ft2-base_interface/#ft_init_freetype">FT_Init_FreeType</a>.

In such cases, the library version might not be available before the library object has been created.

<hr />

## FT_Face_CheckTrueTypePatents

Defined in FT_FREETYPE_H (freetype/freetype.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_bool">FT_Bool</a> )
  <b>FT_Face_CheckTrueTypePatents</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>  face );
</pre>


Deprecated, does nothing.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

A face handle.
</td></tr>
</table>

<h4>return</h4>

Always returns false.

<h4>note</h4>

Since May 2010, TrueType hinting is no longer patented.

<h4>since</h4>

2.3.5

<hr />

## FT_Face_SetUnpatentedHinting

Defined in FT_FREETYPE_H (freetype/freetype.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_bool">FT_Bool</a> )
  <b>FT_Face_SetUnpatentedHinting</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>  face,
                                <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>  value );
</pre>


Deprecated, does nothing.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

A face handle.
</td></tr>
<tr><td class="val" id="value">value</td><td class="desc">

New boolean setting.
</td></tr>
</table>

<h4>return</h4>

Always returns false.

<h4>note</h4>

Since May 2010, TrueType hinting is no longer patented.

<h4>since</h4>

2.3.5

<hr />

## FREETYPE_XXX

Defined in FT_FREETYPE_H (freetype/freetype.h).

<pre>
#define <a href="../ft2-version/#freetype_major">FREETYPE_MAJOR</a>  2
#define <a href="../ft2-version/#freetype_minor">FREETYPE_MINOR</a>  9
#define <a href="../ft2-version/#freetype_patch">FREETYPE_PATCH</a>  1
</pre>


These three macros identify the FreeType source code version. Use <a href="../ft2-version/#ft_library_version">FT_Library_Version</a> to access them at runtime.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="freetype_major">FREETYPE_MAJOR</td><td class="desc">

The major version number.
</td></tr>
<tr><td class="val" id="freetype_minor">FREETYPE_MINOR</td><td class="desc">

The minor version number.
</td></tr>
<tr><td class="val" id="freetype_patch">FREETYPE_PATCH</td><td class="desc">

The patch level.
</td></tr>
</table>

<h4>note</h4>

The version number of FreeType if built as a dynamic link library with the &lsquo;libtool&rsquo; package is _not_ controlled by these three macros.

<hr />

