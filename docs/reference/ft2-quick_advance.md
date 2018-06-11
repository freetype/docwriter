[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; Quick retrieval of advance values

-------------------------------

# Quick retrieval of advance values

## Synopsis

This section contains functions to quickly extract advance values without handling glyph outlines, if possible.

## FT_Get_Advance

Defined in FT_ADVANCES_H (freetype/ftadvanc.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_Advance</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                  <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    gindex,
                  <a href="../ft2-basic_types/#ft_int32">FT_Int32</a>   load_flags,
                  <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  *padvance );
</pre>
</div>


Retrieve the advance value of a given glyph outline in an <a href="../ft2-base_interface/#ft_face">FT_Face</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>The source <a href="../ft2-base_interface/#ft_face">FT_Face</a> handle.</p>
</td></tr>
<tr><td class="val" id="gindex">gindex</td><td class="desc">
<p>The glyph index.</p>
</td></tr>
<tr><td class="val" id="load_flags">load_flags</td><td class="desc">
<p>A set of bit flags similar to those used when calling <a href="../ft2-base_interface/#ft_load_glyph">FT_Load_Glyph</a>, used to determine what kind of advances you need.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="padvance">padvance</td><td class="desc">
<p>The advance value. If scaling is performed (based on the value of &lsquo;load_flags&rsquo;), the advance value is in 16.16 format. Otherwise, it is in font units.</p>
<p>If <a href="../ft2-base_interface/#ft_load_xxx">FT_LOAD_VERTICAL_LAYOUT</a> is set, this is the vertical advance corresponding to a vertical layout. Otherwise, it is the horizontal advance in a horizontal layout.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0 means success.

<h4>note</h4>

This function may fail if you use <a href="../ft2-quick_advance/#ft_advance_flag_fast_only">FT_ADVANCE_FLAG_FAST_ONLY</a> and if the corresponding font backend doesn't have a quick way to retrieve the advances.

A scaled advance is returned in 16.16 format but isn't transformed by the affine transformation specified by <a href="../ft2-base_interface/#ft_set_transform">FT_Set_Transform</a>.

<hr>

## FT_Get_Advances

Defined in FT_ADVANCES_H (freetype/ftadvanc.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_Advances</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                   <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    start,
                   <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    count,
                   <a href="../ft2-basic_types/#ft_int32">FT_Int32</a>   load_flags,
                   <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  *padvances );
</pre>
</div>


Retrieve the advance values of several glyph outlines in an <a href="../ft2-base_interface/#ft_face">FT_Face</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>The source <a href="../ft2-base_interface/#ft_face">FT_Face</a> handle.</p>
</td></tr>
<tr><td class="val" id="start">start</td><td class="desc">
<p>The first glyph index.</p>
</td></tr>
<tr><td class="val" id="count">count</td><td class="desc">
<p>The number of advance values you want to retrieve.</p>
</td></tr>
<tr><td class="val" id="load_flags">load_flags</td><td class="desc">
<p>A set of bit flags similar to those used when calling <a href="../ft2-base_interface/#ft_load_glyph">FT_Load_Glyph</a>.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="padvance">padvance</td><td class="desc">
<p>The advance values. This array, to be provided by the caller, must contain at least &lsquo;count&rsquo; elements.</p>
<p>If scaling is performed (based on the value of &lsquo;load_flags&rsquo;), the advance values are in 16.16 format. Otherwise, they are in font units.</p>
<p>If <a href="../ft2-base_interface/#ft_load_xxx">FT_LOAD_VERTICAL_LAYOUT</a> is set, these are the vertical advances corresponding to a vertical layout. Otherwise, they are the horizontal advances in a horizontal layout.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0 means success.

<h4>note</h4>

This function may fail if you use <a href="../ft2-quick_advance/#ft_advance_flag_fast_only">FT_ADVANCE_FLAG_FAST_ONLY</a> and if the corresponding font backend doesn't have a quick way to retrieve the advances.

Scaled advances are returned in 16.16 format but aren't transformed by the affine transformation specified by <a href="../ft2-base_interface/#ft_set_transform">FT_Set_Transform</a>.

<hr>

## FT_ADVANCE_FLAG_FAST_ONLY

Defined in FT_ADVANCES_H (freetype/ftadvanc.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_ADVANCE_FLAG_FAST_ONLY</b>  0x20000000L
</pre>
</div>


A bit-flag to be OR-ed with the &lsquo;flags&rsquo; parameter of the <a href="../ft2-quick_advance/#ft_get_advance">FT_Get_Advance</a> and <a href="../ft2-quick_advance/#ft_get_advances">FT_Get_Advances</a> functions.

If set, it indicates that you want these functions to fail if the corresponding hinting mode or font driver doesn't allow for very quick advance computation.

Typically, glyphs that are either unscaled, unhinted, bitmapped, or light-hinted can have their advance width computed very quickly.

Normal and bytecode hinted modes that require loading, scaling, and hinting of the glyph outline, are extremely slow by comparison.

<hr>

