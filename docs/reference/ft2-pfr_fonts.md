[Docs](ft2-index.md) &raquo; [Format-Specific API](ft2-toc.md#format-specific-api) &raquo; PFR Fonts

-------------------------------

# PFR Fonts

## Synopsis

This section contains the declaration of PFR-specific functions.

## FT_Get_PFR_Metrics

Defined in FT_PFR_H (freetype/ftpfr.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_PFR_Metrics</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                      <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>   *aoutline_resolution,
                      <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>   *ametrics_resolution,
                      <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  *ametrics_x_scale,
                      <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  *ametrics_y_scale );
</pre>
</div>


Return the outline and metrics resolutions of a given PFR face.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>Handle to the input face. It can be a non-PFR face.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aoutline_resolution">aoutline_resolution</td><td class="desc">
<p>Outline resolution. This is equivalent to &lsquo;face-&gt;units_per_EM&rsquo; for non-PFR fonts. Optional (parameter can be NULL).</p>
</td></tr>
<tr><td class="val" id="ametrics_resolution">ametrics_resolution</td><td class="desc">
<p>Metrics resolution. This is equivalent to &lsquo;outline_resolution&rsquo; for non-PFR fonts. Optional (parameter can be NULL).</p>
</td></tr>
<tr><td class="val" id="ametrics_x_scale">ametrics_x_scale</td><td class="desc">
<p>A 16.16 fixed-point number used to scale distance expressed in metrics units to device subpixels. This is equivalent to &lsquo;face-&gt;size-&gt;x_scale&rsquo;, but for metrics only. Optional (parameter can be NULL).</p>
</td></tr>
<tr><td class="val" id="ametrics_y_scale">ametrics_y_scale</td><td class="desc">
<p>Same as &lsquo;ametrics_x_scale&rsquo; but for the vertical direction. optional (parameter can be NULL).</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

If the input face is not a PFR, this function will return an error. However, in all cases, it will return valid values.

<hr>

## FT_Get_PFR_Kerning

Defined in FT_PFR_H (freetype/ftpfr.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_PFR_Kerning</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>     face,
                      <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     left,
                      <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     right,
                      <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>  *avector );
</pre>
</div>


Return the kerning pair corresponding to two glyphs in a PFR face. The distance is expressed in metrics units, unlike the result of <a href="../ft2-base_interface/#ft_get_kerning">FT_Get_Kerning</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
<tr><td class="val" id="left">left</td><td class="desc">
<p>Index of the left glyph.</p>
</td></tr>
<tr><td class="val" id="right">right</td><td class="desc">
<p>Index of the right glyph.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="avector">avector</td><td class="desc">
<p>A kerning vector.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function always return distances in original PFR metrics units. This is unlike <a href="../ft2-base_interface/#ft_get_kerning">FT_Get_Kerning</a> with the <a href="../ft2-base_interface/#ft_kerning_mode">FT_KERNING_UNSCALED</a> mode, which always returns distances converted to outline units.

You can use the value of the &lsquo;x_scale&rsquo; and &lsquo;y_scale&rsquo; parameters returned by <a href="../ft2-pfr_fonts/#ft_get_pfr_metrics">FT_Get_PFR_Metrics</a> to scale these to device subpixels.

<hr>

## FT_Get_PFR_Advance

Defined in FT_PFR_H (freetype/ftpfr.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_PFR_Advance</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                      <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>   gindex,
                      <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>   *aadvance );
</pre>
</div>


Return a given glyph advance, expressed in original metrics units, from a PFR font.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
<tr><td class="val" id="gindex">gindex</td><td class="desc">
<p>The glyph index.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aadvance">aadvance</td><td class="desc">
<p>The glyph advance in metrics units.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

You can use the &lsquo;x_scale&rsquo; or &lsquo;y_scale&rsquo; results of <a href="../ft2-pfr_fonts/#ft_get_pfr_metrics">FT_Get_PFR_Metrics</a> to convert the advance to device subpixels (i.e., 1/64th of pixels).

<hr>

