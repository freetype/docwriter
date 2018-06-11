[Docs](ft2-index.md) &raquo; [Format-Specific API](ft2-toc.md#format-specific-api) &raquo; Gasp Table

-------------------------------

# Gasp Table

## Synopsis

The function <a href="../ft2-gasp_table/#ft_get_gasp">FT_Get_Gasp</a> can be used to query a TrueType or OpenType font for specific entries in its &lsquo;gasp&rsquo; table, if any. This is mainly useful when implementing native TrueType hinting with the bytecode interpreter to duplicate the Windows text rendering results.

## FT_GASP_XXX

Defined in FT_GASP_H (freetype/ftgasp.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <a href="../ft2-gasp_table/#ft_gasp_no_table">FT_GASP_NO_TABLE</a>               -1
#<span class="keyword">define</span> <a href="../ft2-gasp_table/#ft_gasp_do_gridfit">FT_GASP_DO_GRIDFIT</a>           0x01
#<span class="keyword">define</span> <a href="../ft2-gasp_table/#ft_gasp_do_gray">FT_GASP_DO_GRAY</a>              0x02
#<span class="keyword">define</span> <a href="../ft2-gasp_table/#ft_gasp_symmetric_gridfit">FT_GASP_SYMMETRIC_GRIDFIT</a>    0x04
#<span class="keyword">define</span> <a href="../ft2-gasp_table/#ft_gasp_symmetric_smoothing">FT_GASP_SYMMETRIC_SMOOTHING</a>  0x08
</pre>
</div>


A list of values and/or bit-flags returned by the <a href="../ft2-gasp_table/#ft_get_gasp">FT_Get_Gasp</a> function.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_gasp_no_table">FT_GASP_NO_TABLE</td><td class="desc">
<p>This special value means that there is no GASP table in this face. It is up to the client to decide what to do.</p>
</td></tr>
<tr><td class="val" id="ft_gasp_do_gridfit">FT_GASP_DO_GRIDFIT</td><td class="desc">
<p>Grid-fitting and hinting should be performed at the specified ppem. This <strong>really</strong> means TrueType bytecode interpretation. If this bit is not set, no hinting gets applied.</p>
</td></tr>
<tr><td class="val" id="ft_gasp_do_gray">FT_GASP_DO_GRAY</td><td class="desc">
<p>Anti-aliased rendering should be performed at the specified ppem. If not set, do monochrome rendering.</p>
</td></tr>
<tr><td class="val" id="ft_gasp_symmetric_smoothing">FT_GASP_SYMMETRIC_SMOOTHING</td><td class="desc">
<p>If set, smoothing along multiple axes must be used with ClearType.</p>
</td></tr>
<tr><td class="val" id="ft_gasp_symmetric_gridfit">FT_GASP_SYMMETRIC_GRIDFIT</td><td class="desc">
<p>Grid-fitting must be used with ClearType's symmetric smoothing.</p>
</td></tr>
</table>

<h4>note</h4>

The bit-flags &lsquo;FT_GASP_DO_GRIDFIT&rsquo; and &lsquo;FT_GASP_DO_GRAY&rsquo; are to be used for standard font rasterization only. Independently of that, &lsquo;FT_GASP_SYMMETRIC_SMOOTHING&rsquo; and &lsquo;FT_GASP_SYMMETRIC_GRIDFIT&rsquo; are to be used if ClearType is enabled (and &lsquo;FT_GASP_DO_GRIDFIT&rsquo; and &lsquo;FT_GASP_DO_GRAY&rsquo; are consequently ignored).

&lsquo;ClearType&rsquo; is Microsoft's implementation of LCD rendering, partly protected by patents.

<h4>since</h4>

2.3.0

<hr>

## FT_Get_Gasp

Defined in FT_GASP_H (freetype/ftgasp.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_int">FT_Int</a> )
  <b>FT_Get_Gasp</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>  face,
               <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>  ppem );
</pre>
</div>


For a TrueType or OpenType font file, return the rasterizer behaviour flags from the font's &lsquo;gasp&rsquo; table corresponding to a given character pixel size.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>The source face handle.</p>
</td></tr>
<tr><td class="val" id="ppem">ppem</td><td class="desc">
<p>The vertical character pixel size.</p>
</td></tr>
</table>

<h4>return</h4>

Bit flags (see <a href="../ft2-gasp_table/#ft_gasp_xxx">FT_GASP_XXX</a>), or <a href="../ft2-gasp_table/#ft_gasp_xxx">FT_GASP_NO_TABLE</a> if there is no &lsquo;gasp&rsquo; table in the face.

<h4>note</h4>

If you want to use the MM functionality of OpenType variation fonts (i.e., using <a href="../ft2-multiple_masters/#ft_set_var_design_coordinates">FT_Set_Var_Design_Coordinates</a> and friends), call this function **after** setting an instance since the return values can change.

<h4>since</h4>

2.3.0

<hr>

