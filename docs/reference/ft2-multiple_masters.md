[Docs](ft2-index.md) &raquo; [Format-Specific API](ft2-toc.md#format-specific-api) &raquo; Multiple Masters

-------------------------------

# Multiple Masters

## Synopsis

The following types and functions are used to manage Multiple Master fonts, i.e., the selection of specific design instances by setting design axis coordinates.

Besides Adobe MM fonts, the interface supports Apple's TrueType GX and OpenType variation fonts. Some of the routines only work with Adobe MM fonts, others will work with all three types. They are similar enough that a consistent interface makes sense.

## FT_MM_Axis

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_MM_Axis_
  {
    <a href="../ft2-basic_types/#ft_string">FT_String</a>*  name;
    <a href="../ft2-basic_types/#ft_long">FT_Long</a>     minimum;
    <a href="../ft2-basic_types/#ft_long">FT_Long</a>     maximum;

  } <b>FT_MM_Axis</b>;
</pre>
</div>


A structure to model a given axis in design space for Multiple Masters fonts.

This structure can't be used for TrueType GX or OpenType variation fonts.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="name">name</td><td class="desc">
<p>The axis's name.</p>
</td></tr>
<tr><td class="val" id="minimum">minimum</td><td class="desc">
<p>The axis's minimum design coordinate.</p>
</td></tr>
<tr><td class="val" id="maximum">maximum</td><td class="desc">
<p>The axis's maximum design coordinate.</p>
</td></tr>
</table>

<hr>

## FT_Multi_Master

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Multi_Master_
  {
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     num_axis;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     num_designs;
    <a href="../ft2-multiple_masters/#ft_mm_axis">FT_MM_Axis</a>  axis[T1_MAX_MM_AXIS];

  } <b>FT_Multi_Master</b>;
</pre>
</div>


A structure to model the axes and space of a Multiple Masters font.

This structure can't be used for TrueType GX or OpenType variation fonts.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="num_axis">num_axis</td><td class="desc">
<p>Number of axes. Cannot exceed&nbsp;4.</p>
</td></tr>
<tr><td class="val" id="num_designs">num_designs</td><td class="desc">
<p>Number of designs; should be normally 2^num_axis even though the Type&nbsp;1 specification strangely allows for intermediate designs to be present. This number cannot exceed&nbsp;16.</p>
</td></tr>
<tr><td class="val" id="axis">axis</td><td class="desc">
<p>A table of axis descriptors.</p>
</td></tr>
</table>

<hr>

## FT_Var_Axis

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Var_Axis_
  {
    <a href="../ft2-basic_types/#ft_string">FT_String</a>*  name;

    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>    minimum;
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>    def;
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>    maximum;

    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>    tag;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     strid;

  } <b>FT_Var_Axis</b>;
</pre>
</div>


A structure to model a given axis in design space for Multiple Masters, TrueType GX, and OpenType variation fonts.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="name">name</td><td class="desc">
<p>The axis's name. Not always meaningful for TrueType GX or OpenType variation fonts.</p>
</td></tr>
<tr><td class="val" id="minimum">minimum</td><td class="desc">
<p>The axis's minimum design coordinate.</p>
</td></tr>
<tr><td class="val" id="def">def</td><td class="desc">
<p>The axis's default design coordinate. FreeType computes meaningful default values for Adobe MM fonts.</p>
</td></tr>
<tr><td class="val" id="maximum">maximum</td><td class="desc">
<p>The axis's maximum design coordinate.</p>
</td></tr>
<tr><td class="val" id="tag">tag</td><td class="desc">
<p>The axis's tag (the equivalent to &lsquo;name&rsquo; for TrueType GX and OpenType variation fonts). FreeType provides default values for Adobe MM fonts if possible.</p>
</td></tr>
<tr><td class="val" id="strid">strid</td><td class="desc">
<p>The axis name entry in the font's &lsquo;name&rsquo; table. This is another (and often better) version of the &lsquo;name&rsquo; field for TrueType GX or OpenType variation fonts. Not meaningful for Adobe MM fonts.</p>
</td></tr>
</table>

<h4>note</h4>

The fields &lsquo;minimum&rsquo;, &lsquo;def&rsquo;, and &lsquo;maximum&rsquo; are 16.16 fractional values for TrueType GX and OpenType variation fonts. For Adobe MM fonts, the values are integers.

<hr>

## FT_Var_Named_Style

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Var_Named_Style_
  {
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>*  coords;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    strid;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    psid;   /* since 2.7.1 */

  } <b>FT_Var_Named_Style</b>;
</pre>
</div>


A structure to model a named instance in a TrueType GX or OpenType variation font.

This structure can't be used for Adobe MM fonts.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="coords">coords</td><td class="desc">
<p>The design coordinates for this instance. This is an array with one entry for each axis.</p>
</td></tr>
<tr><td class="val" id="strid">strid</td><td class="desc">
<p>The entry in &lsquo;name&rsquo; table identifying this instance.</p>
</td></tr>
<tr><td class="val" id="psid">psid</td><td class="desc">
<p>The entry in &lsquo;name&rsquo; table identifying a PostScript name for this instance. Value 0xFFFF indicates a missing entry.</p>
</td></tr>
</table>

<hr>

## FT_MM_Var

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_MM_Var_
  {
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>              num_axis;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>              num_designs;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>              num_namedstyles;
    <a href="../ft2-multiple_masters/#ft_var_axis">FT_Var_Axis</a>*         axis;
    <a href="../ft2-multiple_masters/#ft_var_named_style">FT_Var_Named_Style</a>*  namedstyle;

  } <b>FT_MM_Var</b>;
</pre>
</div>


A structure to model the axes and space of an Adobe MM, TrueType GX, or OpenType variation font.

Some fields are specific to one format and not to the others.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="num_axis">num_axis</td><td class="desc">
<p>The number of axes. The maximum value is&nbsp;4 for Adobe MM fonts; no limit in TrueType GX or OpenType variation fonts.</p>
</td></tr>
<tr><td class="val" id="num_designs">num_designs</td><td class="desc">
<p>The number of designs; should be normally 2^num_axis for Adobe MM fonts. Not meaningful for TrueType GX or OpenType variation fonts (where every glyph could have a different number of designs).</p>
</td></tr>
<tr><td class="val" id="num_namedstyles">num_namedstyles</td><td class="desc">
<p>The number of named styles; a &lsquo;named style&rsquo; is a tuple of design coordinates that has a string ID (in the &lsquo;name&rsquo; table) associated with it. The font can tell the user that, for example, [Weight=1.5,Width=1.1] is &lsquo;Bold&rsquo;. Another name for &lsquo;named style&rsquo; is &lsquo;named instance&rsquo;.</p>
<p>For Adobe Multiple Masters fonts, this value is always zero because the format does not support named styles.</p>
</td></tr>
<tr><td class="val" id="axis">axis</td><td class="desc">
<p>An axis descriptor table. TrueType GX and OpenType variation fonts contain slightly more data than Adobe MM fonts. Memory management of this pointer is done internally by FreeType.</p>
</td></tr>
<tr><td class="val" id="namedstyle">namedstyle</td><td class="desc">
<p>A named style (instance) table. Only meaningful for TrueType GX and OpenType variation fonts. Memory management of this pointer is done internally by FreeType.</p>
</td></tr>
</table>

<hr>

## FT_Get_Multi_Master

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_Multi_Master</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>           face,
                       <a href="../ft2-multiple_masters/#ft_multi_master">FT_Multi_Master</a>  *amaster );
</pre>
</div>


Retrieve a variation descriptor of a given Adobe MM font.

This function can't be used with TrueType GX or OpenType variation fonts.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="amaster">amaster</td><td class="desc">
<p>The Multiple Masters descriptor.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FT_Get_MM_Var

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_MM_Var</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>      face,
                 <a href="../ft2-multiple_masters/#ft_mm_var">FT_MM_Var</a>*  *amaster );
</pre>
</div>


Retrieve a variation descriptor for a given font.

This function works with all supported variation formats.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="amaster">amaster</td><td class="desc">
<p>The variation descriptor. Allocates a data structure, which the user must deallocate with a call to <a href="../ft2-multiple_masters/#ft_done_mm_var">FT_Done_MM_Var</a> after use.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FT_Done_MM_Var

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Done_MM_Var</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>   library,
                  <a href="../ft2-multiple_masters/#ft_mm_var">FT_MM_Var</a>   *amaster );
</pre>
</div>


Free the memory allocated by <a href="../ft2-multiple_masters/#ft_get_mm_var">FT_Get_MM_Var</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle of the face's parent library object that was used in the call to <a href="../ft2-multiple_masters/#ft_get_mm_var">FT_Get_MM_Var</a> to create &lsquo;amaster&rsquo;.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FT_Set_MM_Design_Coordinates

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Set_MM_Design_Coordinates</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                                <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>   num_coords,
                                <a href="../ft2-basic_types/#ft_long">FT_Long</a>*  coords );
</pre>
</div>


For Adobe MM fonts, choose an interpolated font design through design coordinates.

This function can't be used with TrueType GX or OpenType variation fonts.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="num_coords">num_coords</td><td class="desc">
<p>The number of available design coordinates. If it is larger than the number of axes, ignore the excess values. If it is smaller than the number of axes, use default values for the remaining axes.</p>
</td></tr>
<tr><td class="val" id="coords">coords</td><td class="desc">
<p>An array of design coordinates.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

[Since 2.8.1] To reset all axes to the default values, call the function with &lsquo;num_coords&rsquo; set to zero and &lsquo;coords&rsquo; set to NULL.

[Since 2.9] If &lsquo;num_coords&rsquo; is larger than zero, this function sets the <a href="../ft2-base_interface/#ft_face_flag_xxx">FT_FACE_FLAG_VARIATION</a> bit in <a href="../ft2-base_interface/#ft_face">FT_Face</a>'s &lsquo;face_flags&rsquo; field (i.e., <a href="../ft2-base_interface/#ft_is_variation">FT_IS_VARIATION</a> will return true). If &lsquo;num_coords&rsquo; is zero, this bit flag gets unset.

<hr>

## FT_Set_Var_Design_Coordinates

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Set_Var_Design_Coordinates</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                                 <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    num_coords,
                                 <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>*  coords );
</pre>
</div>


Choose an interpolated font design through design coordinates.

This function works with all supported variation formats.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="num_coords">num_coords</td><td class="desc">
<p>The number of available design coordinates. If it is larger than the number of axes, ignore the excess values. If it is smaller than the number of axes, use default values for the remaining axes.</p>
</td></tr>
<tr><td class="val" id="coords">coords</td><td class="desc">
<p>An array of design coordinates.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

[Since 2.8.1] To reset all axes to the default values, call the function with &lsquo;num_coords&rsquo; set to zero and &lsquo;coords&rsquo; set to NULL. [Since 2.9] &lsquo;Default values&rsquo; means the currently selected named instance (or the base font if no named instance is selected).

[Since 2.9] If &lsquo;num_coords&rsquo; is larger than zero, this function sets the <a href="../ft2-base_interface/#ft_face_flag_xxx">FT_FACE_FLAG_VARIATION</a> bit in <a href="../ft2-base_interface/#ft_face">FT_Face</a>'s &lsquo;face_flags&rsquo; field (i.e., <a href="../ft2-base_interface/#ft_is_variation">FT_IS_VARIATION</a> will return true). If &lsquo;num_coords&rsquo; is zero, this bit flag gets unset.

<hr>

## FT_Get_Var_Design_Coordinates

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_Var_Design_Coordinates</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                                 <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    num_coords,
                                 <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>*  coords );
</pre>
</div>


Get the design coordinates of the currently selected interpolated font.

This function works with all supported variation formats.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face.</p>
</td></tr>
<tr><td class="val" id="num_coords">num_coords</td><td class="desc">
<p>The number of design coordinates to retrieve. If it is larger than the number of axes, set the excess values to&nbsp;0.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="coords">coords</td><td class="desc">
<p>The design coordinates array.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>since</h4>

2.7.1

<hr>

## FT_Set_MM_Blend_Coordinates

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Set_MM_Blend_Coordinates</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                               <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    num_coords,
                               <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>*  coords );
</pre>
</div>


Choose an interpolated font design through normalized blend coordinates.

This function works with all supported variation formats.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="num_coords">num_coords</td><td class="desc">
<p>The number of available design coordinates. If it is larger than the number of axes, ignore the excess values. If it is smaller than the number of axes, use default values for the remaining axes.</p>
</td></tr>
<tr><td class="val" id="coords">coords</td><td class="desc">
<p>The design coordinates array (each element must be between 0 and 1.0 for Adobe MM fonts, and between -1.0 and 1.0 for TrueType GX and OpenType variation fonts).</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

[Since 2.8.1] To reset all axes to the default values, call the function with &lsquo;num_coords&rsquo; set to zero and &lsquo;coords&rsquo; set to NULL. [Since 2.9] &lsquo;Default values&rsquo; means the currently selected named instance (or the base font if no named instance is selected).

[Since 2.9] If &lsquo;num_coords&rsquo; is larger than zero, this function sets the <a href="../ft2-base_interface/#ft_face_flag_xxx">FT_FACE_FLAG_VARIATION</a> bit in <a href="../ft2-base_interface/#ft_face">FT_Face</a>'s &lsquo;face_flags&rsquo; field (i.e., <a href="../ft2-base_interface/#ft_is_variation">FT_IS_VARIATION</a> will return true). If &lsquo;num_coords&rsquo; is zero, this bit flag gets unset.

<hr>

## FT_Get_MM_Blend_Coordinates

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_MM_Blend_Coordinates</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                               <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    num_coords,
                               <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>*  coords );
</pre>
</div>


Get the normalized blend coordinates of the currently selected interpolated font.

This function works with all supported variation formats.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face.</p>
</td></tr>
<tr><td class="val" id="num_coords">num_coords</td><td class="desc">
<p>The number of normalized blend coordinates to retrieve. If it is larger than the number of axes, set the excess values to&nbsp;0.5 for Adobe MM fonts, and to&nbsp;0 for TrueType GX and OpenType variation fonts.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="coords">coords</td><td class="desc">
<p>The normalized blend coordinates array.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>since</h4>

2.7.1

<hr>

## FT_Set_Var_Blend_Coordinates

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Set_Var_Blend_Coordinates</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                                <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    num_coords,
                                <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>*  coords );
</pre>
</div>


This is another name of <a href="../ft2-multiple_masters/#ft_set_mm_blend_coordinates">FT_Set_MM_Blend_Coordinates</a>.

<hr>

## FT_Get_Var_Blend_Coordinates

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_Var_Blend_Coordinates</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                                <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    num_coords,
                                <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>*  coords );
</pre>
</div>


This is another name of <a href="../ft2-multiple_masters/#ft_get_mm_blend_coordinates">FT_Get_MM_Blend_Coordinates</a>.

<h4>since</h4>

2.7.1

<hr>

## FT_VAR_AXIS_FLAG_XXX

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <a href="../ft2-multiple_masters/#ft_var_axis_flag_hidden">FT_VAR_AXIS_FLAG_HIDDEN</a>  1
</pre>
</div>


A list of bit flags used in the return value of <a href="../ft2-multiple_masters/#ft_get_var_axis_flags">FT_Get_Var_Axis_Flags</a>.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_var_axis_flag_hidden">FT_VAR_AXIS_FLAG_HIDDEN</td><td class="desc">
<p>The variation axis should not be exposed to user interfaces.</p>
</td></tr>
</table>

<h4>since</h4>

2.8.1

<hr>

## FT_Get_Var_Axis_Flags

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_Var_Axis_Flags</b>( <a href="../ft2-multiple_masters/#ft_mm_var">FT_MM_Var</a>*  master,
                         <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     axis_index,
                         <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>*    flags );
</pre>
</div>


Get the &lsquo;flags&rsquo; field of an OpenType Variation Axis Record.

Not meaningful for Adobe MM fonts (&lsquo;*flags&rsquo; is always zero).

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="master">master</td><td class="desc">
<p>The variation descriptor.</p>
</td></tr>
<tr><td class="val" id="axis_index">axis_index</td><td class="desc">
<p>The index of the requested variation axis.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="flags">flags</td><td class="desc">
<p>The &lsquo;flags&rsquo; field. See <a href="../ft2-multiple_masters/#ft_var_axis_flag_xxx">FT_VAR_AXIS_FLAG_XXX</a> for possible values.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>since</h4>

2.8.1

<hr>

## FT_Set_Named_Instance

Defined in FT_MULTIPLE_MASTERS_H (freetype/ftmm.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Set_Named_Instance</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>  face,
                         <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>  instance_index );
</pre>
</div>


Set or change the current named instance.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face.</p>
</td></tr>
<tr><td class="val" id="instance_index">instance_index</td><td class="desc">
<p>The index of the requested instance, starting with value 1. If set to value 0, FreeType switches to font access without a named instance.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The function uses the value of &lsquo;instance_index&rsquo; to set bits 16-30 of the face's &lsquo;face_index&rsquo; field. It also resets any variation applied to the font, and the <a href="../ft2-base_interface/#ft_face_flag_xxx">FT_FACE_FLAG_VARIATION</a> bit of the face's &lsquo;face_flags&rsquo; field gets reset to zero (i.e., <a href="../ft2-base_interface/#ft_is_variation">FT_IS_VARIATION</a> will return false).

For Adobe MM fonts (which don't have named instances) this function simply resets the current face to the default instance.

<h4>since</h4>

2.9

<hr>

