[Docs](ft2-index.md) &raquo; [Miscellaneous](ft2-toc.md#miscellaneous) &raquo; Glyph Color Management

-------------------------------

# Glyph Color Management

## Synopsis

The functions described here allow access and manipulation of color palette entries in OpenType's &lsquo;CPAL&rsquo; table.

## FT_Color

Defined in FT_COLOR_H (freetype/ftcolor.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Color_
  {
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>  blue;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>  green;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>  red;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>  alpha;

  } <b>FT_Color</b>;
</pre>
</div>


This structure models a BGRA color value of a &lsquo;CPAL&rsquo; palette entry.

The used color space is sRGB; the colors are not pre-multiplied, and alpha values must be explicitly set.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="blue">blue</td><td class="desc">
<p>Blue value.</p>
</td></tr>
<tr><td class="val" id="green">green</td><td class="desc">
<p>Green value.</p>
</td></tr>
<tr><td class="val" id="red">red</td><td class="desc">
<p>Red value.</p>
</td></tr>
<tr><td class="val" id="alpha">alpha</td><td class="desc">
<p>Alpha value, giving the red, green, and blue color's opacity.</p>
</td></tr>
</table>

<h4>since</h4>

2.10

<hr>

## FT_PALETTE_XXX

Defined in FT_COLOR_H (freetype/ftcolor.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <a href="../ft2-color_management/#ft_palette_usable_with_light_background">FT_PALETTE_USABLE_WITH_LIGHT_BACKGROUND</a>  0x01
#<span class="keyword">define</span> <a href="../ft2-color_management/#ft_palette_usable_with_dark_background">FT_PALETTE_USABLE_WITH_DARK_BACKGROUND</a>   0x02
</pre>
</div>


A list of bit field constants used in the &lsquo;palette_types&rsquo; array of the <a href="../ft2-color_management/#ft_palette">FT_Palette</a> structure to indicate for which background a palette with a given index is usable.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_palette_usable_with_light_background">FT_PALETTE_USABLE_WITH_LIGHT_BACKGROUND</td><td class="desc">
<p>The palette is appropriate to use when displaying the font on a light background such as white.</p>
</td></tr>
<tr><td class="val" id="ft_palette_usable_with_dark_background">FT_PALETTE_USABLE_WITH_DARK_BACKGROUND</td><td class="desc">
<p>The palette is appropriate to use when displaying the font on a dark background such as black.</p>
</td></tr>
</table>

<h4>since</h4>

2.10

<hr>

## FT_Palette

Defined in FT_COLOR_H (freetype/ftcolor.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Palette_ {
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>         num_palettes;
    <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>*  palette_name_ids;
    <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>*  palette_types;

    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>         num_palette_entries;
    <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>*  palette_entry_name_ids;

  } <b>FT_Palette</b>;
</pre>
</div>


This structure holds the data of the &lsquo;CPAL&rsquo; table.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="num_palettes">num_palettes</td><td class="desc">
<p>The number of palettes.</p>
</td></tr>
<tr><td class="val" id="palette_name_ids">palette_name_ids</td><td class="desc">
<p>A read-only array of palette name IDs with &lsquo;num_palettes&rsquo; elements, corresponding to entries like &lsquo;dark&rsquo; or &lsquo;light&rsquo; in the font's &lsquo;name&rsquo; table.</p>
<p>An empty name ID in the &lsquo;CPAL&rsquo; table gets represented as value 0xFFFF.</p>
<p>NULL if the font's &lsquo;CPAL&rsquo; table doesn't contain appropriate data.</p>
</td></tr>
<tr><td class="val" id="palette_types">palette_types</td><td class="desc">
<p>A read-only array of palette types with &lsquo;num_palettes&rsquo; elements. Possible values are an ORed combination of <a href="../ft2-color_management/#ft_palette_xxx">FT_PALETTE_USABLE_WITH_LIGHT_BACKGROUND</a> and <a href="../ft2-color_management/#ft_palette_xxx">FT_PALETTE_USABLE_WITH_DARK_BACKGROUND</a>.</p>
<p>NULL if the font's &lsquo;CPAL&rsquo; table doesn't contain appropriate data.</p>
</td></tr>
<tr><td class="val" id="num_palette_entries">num_palette_entries</td><td class="desc">
<p>The number of entries in a single palette. All palettes have the same size.</p>
</td></tr>
<tr><td class="val" id="palette_entry_name_ids">palette_entry_name_ids</td><td class="desc">
<p>A read-only array of palette entry name IDs with &lsquo;num_palette_entries&rsquo;. In each palette, entries with the same index have the same function. For example, index&nbsp;0 might correspond to string &lsquo;outline&rsquo; in the font's &lsquo;name&rsquo; table to indicate that this palette entry is used for outlines, index&nbsp;1 might correspond to &lsquo;fill&rsquo; to indicate the filling color palette entry, etc.</p>
<p>An empty entry name ID in the &lsquo;CPAL&rsquo; table gets represented as value 0xFFFF.</p>
<p>NULL if the font's &lsquo;CPAL&rsquo; table doesn't contain appropriate data.</p>
</td></tr>
</table>

<h4>note</h4>

Use function <a href="../ft2-sfnt_names/#ft_get_sfnt_name">FT_Get_Sfnt_Name</a> to map name IDs and entry name IDs to name strings.

<h4>since</h4>

2.10

<hr>

## FT_Palette_Get

Defined in FT_COLOR_H (freetype/ftcolor.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Palette_Get</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>      face,
                  <a href="../ft2-color_management/#ft_palette">FT_Palette</a>  *apalette );
</pre>
</div>


Retrieve the face's color palette data.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>The source face handle.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="apalette">apalette</td><td class="desc">
<p>A pointer to an <a href="../ft2-color_management/#ft_palette">FT_Palette</a> structure.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

All arrays in the returned <a href="../ft2-color_management/#ft_palette">FT_Palette</a> structure are read-only.

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_COLOR_LAYERS&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<h4>since</h4>

2.10

<hr>

## FT_Palette_Select

Defined in FT_COLOR_H (freetype/ftcolor.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Palette_Select</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>     face,
                     <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>   palette_index,
                     <a href="../ft2-color_management/#ft_color">FT_Color</a>*  *apalette_entries );
</pre>
</div>


This function has two purposes.

(1) It activates a palette for rendering color glyphs, and

(2) it retrieves all (unmodified) color entries of this palette. This function returns a read-write array, which means that a calling application can modify the palette entries on demand.

A corollary of (2) is that calling the function, then modifying some values, then calling the function again with the same arguments resets all color entries to the original &lsquo;CPAL&rsquo; values; all user modifications are lost.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>The source face handle.</p>
</td></tr>
<tr><td class="val" id="palette_index">palette_index</td><td class="desc">
<p>The palette index.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="apalette_entries">apalette_entries</td><td class="desc">
<p>An array of color entries for a palette with index &lsquo;palette_index&rsquo;. If &lsquo;apalette_entries&rsquo; is set to NULL, no array gets returned (and no color entries can be modified).</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The number of color entries is given by the &lsquo;num_palette_entries&rsquo; field in the <a href="../ft2-color_management/#ft_palette">FT_Palette</a> structure.

The array pointed to by &lsquo;apalette_entries&rsquo; is owned and managed by FreeType.

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_COLOR_LAYERS&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<h4>since</h4>

2.10

<hr>

## FT_Palette_Set_Foreground_Color

Defined in FT_COLOR_H (freetype/ftcolor.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Palette_Set_Foreground_Color</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                                   <a href="../ft2-color_management/#ft_color">FT_Color</a>  foreground_color );
</pre>
</div>


&lsquo;CPAL&rsquo; uses color index 0xFFFF to indicate a &lsquo;text foreground color&rsquo;. This function sets this value.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>The source face handle.</p>
</td></tr>
<tr><td class="val" id="foreground_color">foreground_color</td><td class="desc">
<p>An &lsquo;FT_Color&rsquo; structure to define the text foreground color.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

If this function isn't called, the text foreground color is set to white opaque (BGRA value 0xFFFFFFFF) if <a href="../ft2-color_management/#ft_palette_xxx">FT_PALETTE_USABLE_WITH_DARK_BACKGROUND</a> is present for the current palette, and black opaque (BGRA value 0x000000FF) otherwise, including the case that no palette types are available in the &lsquo;CPAL&rsquo; table.

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_COLOR_LAYERS&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<h4>since</h4>

2.10

<hr>

