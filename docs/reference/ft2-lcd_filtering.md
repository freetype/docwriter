[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; LCD Filtering

-------------------------------


# LCD Filtering

## Synopsis

Should you #define FT_CONFIG_OPTION_SUBPIXEL_RENDERING in your &lsquo;ftoption.h&rsquo;, which enables patented ClearType-style rendering, the LCD-optimized glyph bitmaps should be filtered to reduce color fringes inherent to this technology. The default FreeType LCD rendering uses different technology, and API described below, although available, does nothing.

ClearType-style LCD rendering exploits the color-striped structure of LCD pixels, increasing the available resolution in the direction of the stripe (usually horizontal RGB) by a factor of&nbsp;3. Using the subpixels coverages unfiltered can create severe color fringes especially when rendering thin features. Indeed, to produce black-on-white text, the color components must be dimmed equally.

A good 5-tap FIR filter should be applied to subpixel coverages regardless of pixel boundaries and should have these properties:

1) It should be symmetrical, like {&nbsp;a, b, c, b, a&nbsp;}, to avoid any shifts in appearance.

2) It should be color-balanced, meaning a&nbsp;+ b&nbsp;=&nbsp;c, to reduce color fringes by distributing the computed coverage for one subpixel to all subpixels equally.

3) It should be normalized, meaning 2a&nbsp;+ 2b&nbsp;+ c&nbsp;=&nbsp;1.0 to maintain overall brightness.

Use the <a href="../ft2-lcd_filtering/#ft_library_setlcdfilter">FT_Library_SetLcdFilter</a> API to specify a low-pass filter, which is then applied to subpixel-rendered bitmaps generated through <a href="../ft2-base_interface/#ft_render_glyph">FT_Render_Glyph</a>. The filter affects glyph bitmaps rendered through <a href="../ft2-base_interface/#ft_render_glyph">FT_Render_Glyph</a>, <a href="../ft2-base_interface/#ft_load_glyph">FT_Load_Glyph</a>, and <a href="../ft2-base_interface/#ft_load_char">FT_Load_Char</a>. It does _not_ affect the output of <a href="../ft2-outline_processing/#ft_outline_render">FT_Outline_Render</a> and <a href="../ft2-outline_processing/#ft_outline_get_bitmap">FT_Outline_Get_Bitmap</a>.

If this feature is activated, the dimensions of LCD glyph bitmaps are either wider or taller than the dimensions of the corresponding outline with regard to the pixel grid. For example, for <a href="../ft2-base_interface/#ft_render_mode">FT_RENDER_MODE_LCD</a>, the filter adds 2&nbsp;subpixels to the left, and 2&nbsp;subpixels to the right. The bitmap offset values are adjusted accordingly, so clients shouldn't need to modify their layout and glyph positioning code when enabling the filter.

Only filtering along with gamma-corrected alpha blending can completely remove color fringes. Boxy 3-tap filter {0, 1/3, 1/3, 1/3, 0} is sharper but is less forgiving of non-ideal gamma curves of a screen (viewing angles!), beveled filters are fuzzier but more tolerant.

Each of the 3&nbsp;alpha values (subpixels) is independently used to blend one color channel. That is, red alpha blends the red channel of the text color with the red channel of the background pixel. The distribution of density values by the color-balanced filter assumes alpha blending is done in linear space; only then color artifacts cancel out.

## FT_LcdFilter

Defined in FT_LCD_FILTER_H (freetype/ftlcdfil.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  FT_LcdFilter_
  {
    <a href="../ft2-lcd_filtering/#ft_lcd_filter_none">FT_LCD_FILTER_NONE</a>    = 0,
    <a href="../ft2-lcd_filtering/#ft_lcd_filter_default">FT_LCD_FILTER_DEFAULT</a> = 1,
    <a href="../ft2-lcd_filtering/#ft_lcd_filter_light">FT_LCD_FILTER_LIGHT</a>   = 2,
    <a href="../ft2-lcd_filtering/#ft_lcd_filter_legacy1">FT_LCD_FILTER_LEGACY1</a> = 3,
    <a href="../ft2-lcd_filtering/#ft_lcd_filter_legacy">FT_LCD_FILTER_LEGACY</a>  = 16,

    FT_LCD_FILTER_MAX   /* do not remove */

  } <b>FT_LcdFilter</b>;
</pre>


A list of values to identify various types of LCD filters.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_lcd_filter_none">FT_LCD_FILTER_NONE</td><td class="desc">

Do not perform filtering. When used with subpixel rendering, this results in sometimes severe color fringes.
</td></tr>
<tr><td class="val" id="ft_lcd_filter_default">FT_LCD_FILTER_DEFAULT</td><td class="desc">

This is a beveled, normalized, and color-balanced five-tap filter with weights of [0x08 0x4D 0x56 0x4D 0x08] in 1/256th units.
</td></tr>
<tr><td class="val" id="ft_lcd_filter_light">FT_LCD_FILTER_LIGHT</td><td class="desc">

this is a boxy, normalized, and color-balanced three-tap filter with weights of [0x00 0x55 0x56 0x55 0x00] in 1/256th units.
</td></tr>
<tr><td class="val" id="ft_lcd_filter_legacy">FT_LCD_FILTER_LEGACY</td><td class="desc">


</td></tr>
<tr><td class="val" id="ft_lcd_filter_legacy1">FT_LCD_FILTER_LEGACY1</td><td class="desc">

This filter corresponds to the original libXft color filter. It provides high contrast output but can exhibit really bad color fringes if glyphs are not extremely well hinted to the pixel grid. This filter is only provided for comparison purposes, and might be disabled or stay unsupported in the future. The second value is provided for compatibility with FontConfig, which historically used different enumeration, sometimes incorrectly forwarded to FreeType.
</td></tr>
</table>

<h4>since</h4>

2.3.0 (&lsquo;FT_LCD_FILTER_LEGACY1&rsquo; since 2.6.2)

<hr />

## FT_Library_SetLcdFilter

Defined in FT_LCD_FILTER_H (freetype/ftlcdfil.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Library_SetLcdFilter</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>    library,
                           <a href="../ft2-lcd_filtering/#ft_lcdfilter">FT_LcdFilter</a>  filter );
</pre>


This function is used to apply color filtering to LCD decimated bitmaps, like the ones used when calling <a href="../ft2-base_interface/#ft_render_glyph">FT_Render_Glyph</a> with <a href="../ft2-base_interface/#ft_render_mode">FT_RENDER_MODE_LCD</a> or <a href="../ft2-base_interface/#ft_render_mode">FT_RENDER_MODE_LCD_V</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">

A handle to the target library instance.
</td></tr>
<tr><td class="val" id="filter">filter</td><td class="desc">

The filter type.

You can use <a href="../ft2-lcd_filtering/#ft_lcdfilter">FT_LCD_FILTER_NONE</a> here to disable this feature, or <a href="../ft2-lcd_filtering/#ft_lcdfilter">FT_LCD_FILTER_DEFAULT</a> to use a default filter that should work well on most LCD screens.
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This feature is always disabled by default. Clients must make an explicit call to this function with a &lsquo;filter&rsquo; value other than <a href="../ft2-lcd_filtering/#ft_lcdfilter">FT_LCD_FILTER_NONE</a> in order to enable it.

Due to *PATENTS* covering subpixel rendering, this function doesn't do anything except returning &lsquo;FT_Err_Unimplemented_Feature&rsquo; if the configuration macro FT_CONFIG_OPTION_SUBPIXEL_RENDERING is not defined in your build of the library, which should correspond to all default builds of FreeType.

<h4>since</h4>

2.3.0

<hr />

## FT_Library_SetLcdFilterWeights

Defined in FT_LCD_FILTER_H (freetype/ftlcdfil.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Library_SetLcdFilterWeights</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>      library,
                                  <span class="keyword">unsigned</span> <span class="keyword">char</span>  *weights );
</pre>


This function can be used to enable LCD filter with custom weights, instead of using presets in <a href="../ft2-lcd_filtering/#ft_library_setlcdfilter">FT_Library_SetLcdFilter</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">

A handle to the target library instance.
</td></tr>
<tr><td class="val" id="weights">weights</td><td class="desc">

A pointer to an array; the function copies the first five bytes and uses them to specify the filter weights in 1/256th units.
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

Due to *PATENTS* covering subpixel rendering, this function doesn't do anything except returning &lsquo;FT_Err_Unimplemented_Feature&rsquo; if the configuration macro FT_CONFIG_OPTION_SUBPIXEL_RENDERING is not defined in your build of the library, which should correspond to all default builds of FreeType.

LCD filter weights can also be set per face using <a href="../ft2-base_interface/#ft_face_properties">FT_Face_Properties</a> with <a href="../ft2-parameter_tags/#ft_param_tag_lcd_filter_weights">FT_PARAM_TAG_LCD_FILTER_WEIGHTS</a>.

<h4>since</h4>

2.4.0

<hr />

## FT_LcdFiveTapFilter

Defined in FT_LCD_FILTER_H (freetype/ftlcdfil.h).

<pre>
#define FT_LCD_FILTER_FIVE_TAPS  5

  <span class="keyword">typedef</span> <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>  <b>FT_LcdFiveTapFilter</b>[FT_LCD_FILTER_FIVE_TAPS];
</pre>


A typedef for passing the five LCD filter weights to <a href="../ft2-base_interface/#ft_face_properties">FT_Face_Properties</a> within an <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a> structure.

<h4>since</h4>

2.8

<hr />

