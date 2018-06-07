# Glyph Color Management

## Synopsis

The functions described here allow access and manipulation of color palette entries in OpenType's &lsquo;CPAL&rsquo; table.

## FT_Color

Defined in FT_COLOR_H (freetype/ftcolor.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Color_
  {
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>  blue;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>  green;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>  red;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>  alpha;

  } <b>FT_Color</b>;
</pre>


This structure models a BGRA color value of a &lsquo;CPAL&rsquo; palette entry.

The used color space is sRGB; the colors are not pre-multiplied, and alpha values must be explicitly set.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="blue">blue</td><td class="desc">

Blue value.
</td></tr>
<tr><td class="val" id="green">green</td><td class="desc">

Green value.
</td></tr>
<tr><td class="val" id="red">red</td><td class="desc">

Red value.
</td></tr>
<tr><td class="val" id="alpha">alpha</td><td class="desc">

Alpha value, giving the red, green, and blue color's opacity.
</td></tr>
</table>

<h4>since</h4>

2.10

<hr />

## FT_Palette_Get_Size

Defined in FT_COLOR_H (freetype/ftcolor.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Palette_Get_Size</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>     face,
                       <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>*  anum_palettes,
                       <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>*  anum_palette_entries );
</pre>


Get the number of palettes in the &lsquo;CPAL&rsquo; table and the number of entries in a palette (all palettes have the same number of entries).

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

The source face handle.
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="anum_palettes">anum_palettes</td><td class="desc">

The number of palettes.
</td></tr>
<tr><td class="val" id="anum_palette_entries">anum_palette_entries</td><td class="desc">

The number of entries in a single palette.
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_COLOR_LAYERS&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<h4>since</h4>

2.10

<hr />

## FT_Palette_Get_Name_IDs

Defined in FT_COLOR_H (freetype/ftcolor.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Palette_Get_Name_IDs</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>           face,
                           <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>*  palette_name_ids );
</pre>


Get the palette name IDs, which correspond to entries like &lsquo;dark&rsquo; or &lsquo;light&rsquo; in the font's &lsquo;name&rsquo; table.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

The source face handle.
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="palette_name_ids">palette_name_ids</td><td class="desc">

A read-only array of palette name IDs. NULL if the font's &lsquo;CPAL&rsquo; table doesn't contain appropriate data.

Use function <a href="../ft2-sfnt_names/#ft_get_sfnt_name">FT_Get_Sfnt_Name</a> to map name IDs to a name strings.
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The number of palettes can be retrieved with <a href="../ft2-color_management/#ft_palette_get_size">FT_Palette_Get_Size</a>.

An empty name ID in the &lsquo;CPAL&rsquo; table gets represented as value 0xFFFF.

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_COLOR_LAYERS&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<h4>since</h4>

2.10

<hr />

## FT_PALETTE_XXX

Defined in FT_COLOR_H (freetype/ftcolor.h).

<pre>
#define <a href="../ft2-color_management/#ft_palette_usable_with_light_background">FT_PALETTE_USABLE_WITH_LIGHT_BACKGROUND</a>  0x01
#define <a href="../ft2-color_management/#ft_palette_usable_with_dark_background">FT_PALETTE_USABLE_WITH_DARK_BACKGROUND</a>   0x02
</pre>


A list of bit field constants returned by function <a href="../ft2-color_management/#ft_palette_get_types">FT_Palette_Get_Types</a> to indicate for which background a given palette is usable.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_palette_usable_with_light_background">FT_PALETTE_USABLE_WITH_LIGHT_BACKGROUND</td><td class="desc">

The palette is appropriate to use when displaying the font on a light background such as white.
</td></tr>
<tr><td class="val" id="ft_palette_usable_with_dark_background">FT_PALETTE_USABLE_WITH_DARK_BACKGROUND</td><td class="desc">

The palette is appropriate to use when displaying the font on a dark background such as black.
</td></tr>
</table>

<h4>note</h4>

The number of palette types can be retrieved with <a href="../ft2-color_management/#ft_palette_get_size">FT_Palette_Get_Size</a>.

<h4>since</h4>

2.10

<hr />

## FT_Palette_Get_Types

Defined in FT_COLOR_H (freetype/ftcolor.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Palette_Get_Types</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>           face,
                        <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>*  apalette_types );
</pre>


Get the palette types. Possible values are an ORed combination of <a href="../ft2-color_management/#ft_palette_xxx">FT_PALETTE_USABLE_WITH_LIGHT_BACKGROUND</a> and <a href="../ft2-color_management/#ft_palette_xxx">FT_PALETTE_USABLE_WITH_DARK_BACKGROUND</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

The source face handle.
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="apalette_types">apalette_types</td><td class="desc">

A read-only array of palette types. NULL if the font's &lsquo;CPAL&rsquo; table doesn't contain appropriate data.
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The number of palette types can be retrieved with <a href="../ft2-color_management/#ft_palette_get_size">FT_Palette_Get_Size</a>.

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_COLOR_LAYERS&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<h4>since</h4>

2.10

<hr />

## FT_Palette_Get_Entry_Name_IDs

Defined in FT_COLOR_H (freetype/ftcolor.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Palette_Get_Entry_Name_IDs</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>           face,
                                 <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>*  palette_entry_name_ids );
</pre>


Get the palette entry name IDs. In each palette, entries with the same index have the same function. For example, index&nbsp;0 might correspond to string &lsquo;outline&rsquo; in the font's &lsquo;name&rsquo; table to indicate that this palette entry is used for outlines, index&nbsp;1 might correspond to &lsquo;fill&rsquo; to indicate the filling color palette entry, etc.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

The source face handle.
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aentry_names">aentry_names</td><td class="desc">

A read-only array of palette entry name IDs. NULL if the font's &lsquo;CPAL&rsquo; table doesn't contain appropriate data.

Use function <a href="../ft2-sfnt_names/#ft_get_sfnt_name">FT_Get_Sfnt_Name</a> to map entry name IDs to a name strings.
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The number of palette entries can be retrieved with <a href="../ft2-color_management/#ft_palette_get_size">FT_Palette_Get_Size</a>.

An empty entry name ID in the &lsquo;CPAL&rsquo; table gets represented as value 0xFFFF.

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_COLOR_LAYERS&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<h4>since</h4>

2.10

<hr />

## FT_Palette_Select

Defined in FT_COLOR_H (freetype/ftcolor.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Palette_Select</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>     face,
                     <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>   palette_index,
                     <a href="../ft2-color_management/#ft_color">FT_Color</a>*  *apalette_entries );
</pre>


This function has two purposes.

(1) It activates a palette for rendering color glyphs, and

(2) it retrieves all (unmodified) color entries of this palette. This function returns a read-write array, which means that a calling application can modify the palette entries on demand.

A corollary of (2) is that calling the function, then modifying some values, then calling the function again with the same arguments resets all color entries to the original &lsquo;CPAL&rsquo; values; all user modifications are lost.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

The source face handle.
</td></tr>
<tr><td class="val" id="palette_index">palette_index</td><td class="desc">

The palette index.
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="apalette_entries">apalette_entries</td><td class="desc">

An array of color entries for a palette with index &lsquo;palette_index&rsquo;. If &lsquo;apalette_entries&rsquo; is set to NULL, no array gets returned (and no color entries can be modified).
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The number of color entries can be retrieved with <a href="../ft2-color_management/#ft_palette_get_size">FT_Palette_Get_Size</a>.

The array pointed to by &lsquo;apalette_entries&rsquo; is owned and managed by FreeType.

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_COLOR_LAYERS&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<h4>since</h4>

2.10

<hr />

## FT_Palette_Set_Foreground_Color

Defined in FT_COLOR_H (freetype/ftcolor.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Palette_Set_Foreground_Color</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                                   <a href="../ft2-color_management/#ft_color">FT_Color</a>  foreground_color );
</pre>


&lsquo;CPAL&rsquo; uses color index 0xFFFF to indicate a &lsquo;text foreground color&rsquo;. This function sets this value.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

The source face handle.
</td></tr>
<tr><td class="val" id="foreground_color">foreground_color</td><td class="desc">

An &lsquo;FT_Color&rsquo; structure to define the text foreground color.
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_COLOR_LAYERS&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<h4>since</h4>

2.10

<hr />

