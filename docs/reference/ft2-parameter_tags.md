[Docs](ft2-index.md) &raquo; [Controlling FreeType Modules](ft2-toc.md#controlling-freetype-modules) &raquo; Parameter Tags

-------------------------------

# Parameter Tags

## Synopsis

This section contains macros for the <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a> structure that are used with various functions to activate some special functionality or different behaviour of various components of FreeType.

## FT_PARAM_TAG_IGNORE_TYPOGRAPHIC_FAMILY


<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_PARAM_TAG_IGNORE_TYPOGRAPHIC_FAMILY</b> \
          <a href="../ft2-basic_types/#ft_make_tag">FT_MAKE_TAG</a>( 'i', 'g', 'p', 'f' )


  /* this constant is deprecated */
#<span class="keyword">define</span> FT_PARAM_TAG_IGNORE_PREFERRED_FAMILY \
          <b>FT_PARAM_TAG_IGNORE_TYPOGRAPHIC_FAMILY</b>
</pre>
</div>


A tag for <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a> to make <a href="../ft2-base_interface/#ft_open_face">FT_Open_Face</a> ignore typographic family names in the &lsquo;name&rsquo; table (introduced in OpenType version 1.4). Use this for backward compatibility with legacy systems that have a four-faces-per-family restriction.

<h4>since</h4>

2.8

<hr>

## FT_PARAM_TAG_IGNORE_TYPOGRAPHIC_SUBFAMILY


<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_PARAM_TAG_IGNORE_TYPOGRAPHIC_SUBFAMILY</b> \
          <a href="../ft2-basic_types/#ft_make_tag">FT_MAKE_TAG</a>( 'i', 'g', 'p', 's' )


  /* this constant is deprecated */
#<span class="keyword">define</span> FT_PARAM_TAG_IGNORE_PREFERRED_SUBFAMILY \
          <b>FT_PARAM_TAG_IGNORE_TYPOGRAPHIC_SUBFAMILY</b>
</pre>
</div>


A tag for <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a> to make <a href="../ft2-base_interface/#ft_open_face">FT_Open_Face</a> ignore typographic subfamily names in the &lsquo;name&rsquo; table (introduced in OpenType version 1.4). Use this for backward compatibility with legacy systems that have a four-faces-per-family restriction.

<h4>since</h4>

2.8

<hr>

## FT_PARAM_TAG_INCREMENTAL


<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_PARAM_TAG_INCREMENTAL</b> \
          <a href="../ft2-basic_types/#ft_make_tag">FT_MAKE_TAG</a>( 'i', 'n', 'c', 'r' )
</pre>
</div>


An <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a> tag to be used with <a href="../ft2-base_interface/#ft_open_face">FT_Open_Face</a> to indicate incremental glyph loading.

<hr>

## FT_PARAM_TAG_LCD_FILTER_WEIGHTS


<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_PARAM_TAG_LCD_FILTER_WEIGHTS</b> \
          <a href="../ft2-basic_types/#ft_make_tag">FT_MAKE_TAG</a>( 'l', 'c', 'd', 'f' )
</pre>
</div>


An <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a> tag to be used with <a href="../ft2-base_interface/#ft_face_properties">FT_Face_Properties</a>. The corresponding argument specifies the five LCD filter weights for a given face (if using <a href="../ft2-base_interface/#ft_load_target_xxx">FT_LOAD_TARGET_LCD</a>, for example), overriding the global default values or the values set up with <a href="../ft2-lcd_rendering/#ft_library_setlcdfilterweights">FT_Library_SetLcdFilterWeights</a>.

<h4>since</h4>

2.8

<hr>

## FT_PARAM_TAG_RANDOM_SEED


<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_PARAM_TAG_RANDOM_SEED</b> \
          <a href="../ft2-basic_types/#ft_make_tag">FT_MAKE_TAG</a>( 's', 'e', 'e', 'd' )
</pre>
</div>


An <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a> tag to be used with <a href="../ft2-base_interface/#ft_face_properties">FT_Face_Properties</a>. The corresponding 32bit signed integer argument overrides the font driver's random seed value with a face-specific one; see <a href="../ft2-properties/#random-seed">random-seed</a>.

<h4>since</h4>

2.8

<hr>

## FT_PARAM_TAG_STEM_DARKENING


<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_PARAM_TAG_STEM_DARKENING</b> \
          <a href="../ft2-basic_types/#ft_make_tag">FT_MAKE_TAG</a>( 'd', 'a', 'r', 'k' )
</pre>
</div>


An <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a> tag to be used with <a href="../ft2-base_interface/#ft_face_properties">FT_Face_Properties</a>. The corresponding Boolean argument specifies whether to apply stem darkening, overriding the global default values or the values set up with <a href="../ft2-module_management/#ft_property_set">FT_Property_Set</a> (see <a href="../ft2-properties/#no-stem-darkening">no-stem-darkening</a>).

This is a passive setting that only takes effect if the font driver or autohinter honors it, which the CFF, Type&nbsp;1, and CID drivers always do, but the autohinter only in &lsquo;light&rsquo; hinting mode (as of version 2.9).

<h4>since</h4>

2.8

<hr>

## FT_PARAM_TAG_UNPATENTED_HINTING


<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_PARAM_TAG_UNPATENTED_HINTING</b> \
          <a href="../ft2-basic_types/#ft_make_tag">FT_MAKE_TAG</a>( 'u', 'n', 'p', 'a' )
</pre>
</div>


Deprecated, no effect.

Previously: A constant used as the tag of an <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a> structure to indicate that unpatented methods only should be used by the TrueType bytecode interpreter for a typeface opened by <a href="../ft2-base_interface/#ft_open_face">FT_Open_Face</a>.

<hr>

