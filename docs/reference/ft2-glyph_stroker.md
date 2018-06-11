[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; Glyph Stroker

-------------------------------

# Glyph Stroker

## Synopsis

This component generates stroked outlines of a given vectorial glyph. It also allows you to retrieve the &lsquo;outside&rsquo; and/or the &lsquo;inside&rsquo; borders of the stroke.

This can be useful to generate &lsquo;bordered&rsquo; glyph, i.e., glyphs displayed with a coloured (and anti-aliased) border around their shape.

## FT_Stroker

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_StrokerRec_*  <b>FT_Stroker</b>;
</pre>
</div>


Opaque handle to a path stroker object.

<hr>

## FT_Stroker_LineJoin

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  FT_Stroker_LineJoin_
  {
    <a href="../ft2-glyph_stroker/#ft_stroker_linejoin_round">FT_STROKER_LINEJOIN_ROUND</a>          = 0,
    <a href="../ft2-glyph_stroker/#ft_stroker_linejoin_bevel">FT_STROKER_LINEJOIN_BEVEL</a>          = 1,
    <a href="../ft2-glyph_stroker/#ft_stroker_linejoin_miter_variable">FT_STROKER_LINEJOIN_MITER_VARIABLE</a> = 2,
    <a href="../ft2-glyph_stroker/#ft_stroker_linejoin_miter">FT_STROKER_LINEJOIN_MITER</a>          = <a href="../ft2-glyph_stroker/#ft_stroker_linejoin_miter_variable">FT_STROKER_LINEJOIN_MITER_VARIABLE</a>,
    <a href="../ft2-glyph_stroker/#ft_stroker_linejoin_miter_fixed">FT_STROKER_LINEJOIN_MITER_FIXED</a>    = 3

  } <b>FT_Stroker_LineJoin</b>;
</pre>
</div>


These values determine how two joining lines are rendered in a stroker.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_stroker_linejoin_round">FT_STROKER_LINEJOIN_ROUND</td><td class="desc">
<p>Used to render rounded line joins. Circular arcs are used to join two lines smoothly.</p>
</td></tr>
<tr><td class="val" id="ft_stroker_linejoin_bevel">FT_STROKER_LINEJOIN_BEVEL</td><td class="desc">
<p>Used to render beveled line joins. The outer corner of the joined lines is filled by enclosing the triangular region of the corner with a straight line between the outer corners of each stroke.</p>
</td></tr>
<tr><td class="val" id="ft_stroker_linejoin_miter_fixed">FT_STROKER_LINEJOIN_MITER_FIXED</td><td class="desc">
<p>Used to render mitered line joins, with fixed bevels if the miter limit is exceeded. The outer edges of the strokes for the two segments are extended until they meet at an angle. If the segments meet at too sharp an angle (such that the miter would extend from the intersection of the segments a distance greater than the product of the miter limit value and the border radius), then a bevel join (see above) is used instead. This prevents long spikes being created. FT_STROKER_LINEJOIN_MITER_FIXED generates a miter line join as used in PostScript and PDF.</p>
</td></tr>
<tr><td class="val" id="ft_stroker_linejoin_miter_variable">FT_STROKER_LINEJOIN_MITER_VARIABLE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ft_stroker_linejoin_miter">FT_STROKER_LINEJOIN_MITER</td><td class="desc">
<p>Used to render mitered line joins, with variable bevels if the miter limit is exceeded. The intersection of the strokes is clipped at a line perpendicular to the bisector of the angle between the strokes, at the distance from the intersection of the segments equal to the product of the miter limit value and the border radius. This prevents long spikes being created. FT_STROKER_LINEJOIN_MITER_VARIABLE generates a mitered line join as used in XPS. FT_STROKER_LINEJOIN_MITER is an alias for FT_STROKER_LINEJOIN_MITER_VARIABLE, retained for backward compatibility.</p>
</td></tr>
</table>

<hr>

## FT_Stroker_LineCap

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  FT_Stroker_LineCap_
  {
    <a href="../ft2-glyph_stroker/#ft_stroker_linecap_butt">FT_STROKER_LINECAP_BUTT</a> = 0,
    <a href="../ft2-glyph_stroker/#ft_stroker_linecap_round">FT_STROKER_LINECAP_ROUND</a>,
    <a href="../ft2-glyph_stroker/#ft_stroker_linecap_square">FT_STROKER_LINECAP_SQUARE</a>

  } <b>FT_Stroker_LineCap</b>;
</pre>
</div>


These values determine how the end of opened sub-paths are rendered in a stroke.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_stroker_linecap_butt">FT_STROKER_LINECAP_BUTT</td><td class="desc">
<p>The end of lines is rendered as a full stop on the last point itself.</p>
</td></tr>
<tr><td class="val" id="ft_stroker_linecap_round">FT_STROKER_LINECAP_ROUND</td><td class="desc">
<p>The end of lines is rendered as a half-circle around the last point.</p>
</td></tr>
<tr><td class="val" id="ft_stroker_linecap_square">FT_STROKER_LINECAP_SQUARE</td><td class="desc">
<p>The end of lines is rendered as a square around the last point.</p>
</td></tr>
</table>

<hr>

## FT_StrokerBorder

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  FT_StrokerBorder_
  {
    <a href="../ft2-glyph_stroker/#ft_stroker_border_left">FT_STROKER_BORDER_LEFT</a> = 0,
    <a href="../ft2-glyph_stroker/#ft_stroker_border_right">FT_STROKER_BORDER_RIGHT</a>

  } <b>FT_StrokerBorder</b>;
</pre>
</div>


These values are used to select a given stroke border in <a href="../ft2-glyph_stroker/#ft_stroker_getbordercounts">FT_Stroker_GetBorderCounts</a> and <a href="../ft2-glyph_stroker/#ft_stroker_exportborder">FT_Stroker_ExportBorder</a>.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_stroker_border_left">FT_STROKER_BORDER_LEFT</td><td class="desc">
<p>Select the left border, relative to the drawing direction.</p>
</td></tr>
<tr><td class="val" id="ft_stroker_border_right">FT_STROKER_BORDER_RIGHT</td><td class="desc">
<p>Select the right border, relative to the drawing direction.</p>
</td></tr>
</table>

<h4>note</h4>

Applications are generally interested in the &lsquo;inside&rsquo; and &lsquo;outside&rsquo; borders. However, there is no direct mapping between these and the &lsquo;left&rsquo; and &lsquo;right&rsquo; ones, since this really depends on the glyph's drawing orientation, which varies between font formats.

You can however use <a href="../ft2-glyph_stroker/#ft_outline_getinsideborder">FT_Outline_GetInsideBorder</a> and <a href="../ft2-glyph_stroker/#ft_outline_getoutsideborder">FT_Outline_GetOutsideBorder</a> to get these.

<hr>

## FT_Outline_GetInsideBorder

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-glyph_stroker/#ft_strokerborder">FT_StrokerBorder</a> )
  <b>FT_Outline_GetInsideBorder</b>( <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline );
</pre>
</div>


Retrieve the <a href="../ft2-glyph_stroker/#ft_strokerborder">FT_StrokerBorder</a> value corresponding to the &lsquo;inside&rsquo; borders of a given outline.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>The source outline handle.</p>
</td></tr>
</table>

<h4>return</h4>

The border index. <a href="../ft2-glyph_stroker/#ft_strokerborder">FT_STROKER_BORDER_RIGHT</a> for empty or invalid outlines.

<hr>

## FT_Outline_GetOutsideBorder

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-glyph_stroker/#ft_strokerborder">FT_StrokerBorder</a> )
  <b>FT_Outline_GetOutsideBorder</b>( <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline );
</pre>
</div>


Retrieve the <a href="../ft2-glyph_stroker/#ft_strokerborder">FT_StrokerBorder</a> value corresponding to the &lsquo;outside&rsquo; borders of a given outline.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>The source outline handle.</p>
</td></tr>
</table>

<h4>return</h4>

The border index. <a href="../ft2-glyph_stroker/#ft_strokerborder">FT_STROKER_BORDER_LEFT</a> for empty or invalid outlines.

<hr>

## FT_Glyph_Stroke

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Glyph_Stroke</b>( <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a>    *pglyph,
                   <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>   stroker,
                   <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>      destroy );
</pre>
</div>


Stroke a given outline glyph object with a given stroker.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="pglyph">pglyph</td><td class="desc">
<p>Source glyph handle on input, new glyph handle on output.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>A stroker handle.</p>
</td></tr>
<tr><td class="val" id="destroy">destroy</td><td class="desc">
<p>A Boolean. If&nbsp;1, the source glyph object is destroyed on success.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The source glyph is untouched in case of error.

Adding stroke may yield a significantly wider and taller glyph depending on how large of a radius was used to stroke the glyph. You may need to manually adjust horizontal and vertical advance amounts to account for this added size.

<hr>

## FT_Glyph_StrokeBorder

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Glyph_StrokeBorder</b>( <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a>    *pglyph,
                         <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>   stroker,
                         <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>      inside,
                         <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>      destroy );
</pre>
</div>


Stroke a given outline glyph object with a given stroker, but only return either its inside or outside border.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="pglyph">pglyph</td><td class="desc">
<p>Source glyph handle on input, new glyph handle on output.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>A stroker handle.</p>
</td></tr>
<tr><td class="val" id="inside">inside</td><td class="desc">
<p>A Boolean. If&nbsp;1, return the inside border, otherwise the outside border.</p>
</td></tr>
<tr><td class="val" id="destroy">destroy</td><td class="desc">
<p>A Boolean. If&nbsp;1, the source glyph object is destroyed on success.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The source glyph is untouched in case of error.

Adding stroke may yield a significantly wider and taller glyph depending on how large of a radius was used to stroke the glyph. You may need to manually adjust horizontal and vertical advance amounts to account for this added size.

<hr>

## FT_Stroker_New

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Stroker_New</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>   library,
                  <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>  *astroker );
</pre>
</div>


Create a new stroker object.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>FreeType library handle.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="astroker">astroker</td><td class="desc">
<p>A new stroker object handle. NULL in case of error.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FT_Stroker_Set

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Stroker_Set</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>           stroker,
                  <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>             radius,
                  <a href="../ft2-glyph_stroker/#ft_stroker_linecap">FT_Stroker_LineCap</a>   line_cap,
                  <a href="../ft2-glyph_stroker/#ft_stroker_linejoin">FT_Stroker_LineJoin</a>  line_join,
                  <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>             miter_limit );
</pre>
</div>


Reset a stroker object's attributes.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
<tr><td class="val" id="radius">radius</td><td class="desc">
<p>The border radius.</p>
</td></tr>
<tr><td class="val" id="line_cap">line_cap</td><td class="desc">
<p>The line cap style.</p>
</td></tr>
<tr><td class="val" id="line_join">line_join</td><td class="desc">
<p>The line join style.</p>
</td></tr>
<tr><td class="val" id="miter_limit">miter_limit</td><td class="desc">
<p>The miter limit for the FT_STROKER_LINEJOIN_MITER_FIXED and FT_STROKER_LINEJOIN_MITER_VARIABLE line join styles, expressed as 16.16 fixed-point value.</p>
</td></tr>
</table>

<h4>note</h4>

The radius is expressed in the same units as the outline coordinates.

This function calls <a href="../ft2-glyph_stroker/#ft_stroker_rewind">FT_Stroker_Rewind</a> automatically.

<hr>

## FT_Stroker_Rewind

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Stroker_Rewind</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>  stroker );
</pre>
</div>


Reset a stroker object without changing its attributes. You should call this function before beginning a new series of calls to <a href="../ft2-glyph_stroker/#ft_stroker_beginsubpath">FT_Stroker_BeginSubPath</a> or <a href="../ft2-glyph_stroker/#ft_stroker_endsubpath">FT_Stroker_EndSubPath</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
</table>

<hr>

## FT_Stroker_ParseOutline

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Stroker_ParseOutline</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>   stroker,
                           <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline,
                           <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>      opened );
</pre>
</div>


A convenience function used to parse a whole outline with the stroker. The resulting outline(s) can be retrieved later by functions like <a href="../ft2-glyph_stroker/#ft_stroker_getcounts">FT_Stroker_GetCounts</a> and <a href="../ft2-glyph_stroker/#ft_stroker_export">FT_Stroker_Export</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>The source outline.</p>
</td></tr>
<tr><td class="val" id="opened">opened</td><td class="desc">
<p>A boolean. If&nbsp;1, the outline is treated as an open path instead of a closed one.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

If &lsquo;opened&rsquo; is&nbsp;0 (the default), the outline is treated as a closed path, and the stroker generates two distinct &lsquo;border&rsquo; outlines.

If &lsquo;opened&rsquo; is&nbsp;1, the outline is processed as an open path, and the stroker generates a single &lsquo;stroke&rsquo; outline.

This function calls <a href="../ft2-glyph_stroker/#ft_stroker_rewind">FT_Stroker_Rewind</a> automatically.

<hr>

## FT_Stroker_Done

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Stroker_Done</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>  stroker );
</pre>
</div>


Destroy a stroker object.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>A stroker handle. Can be NULL.</p>
</td></tr>
</table>

<hr>

## FT_Stroker_BeginSubPath

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Stroker_BeginSubPath</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>  stroker,
                           <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  to,
                           <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>     open );
</pre>
</div>


Start a new sub-path in the stroker.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
<tr><td class="val" id="to">to</td><td class="desc">
<p>A pointer to the start vector.</p>
</td></tr>
<tr><td class="val" id="open">open</td><td class="desc">
<p>A boolean. If&nbsp;1, the sub-path is treated as an open one.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function is useful when you need to stroke a path that is not stored as an <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a> object.

<hr>

## FT_Stroker_EndSubPath

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Stroker_EndSubPath</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>  stroker );
</pre>
</div>


Close the current sub-path in the stroker.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

You should call this function after <a href="../ft2-glyph_stroker/#ft_stroker_beginsubpath">FT_Stroker_BeginSubPath</a>. If the subpath was not &lsquo;opened&rsquo;, this function &lsquo;draws&rsquo; a single line segment to the start position when needed.

<hr>

## FT_Stroker_LineTo

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Stroker_LineTo</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>  stroker,
                     <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  to );
</pre>
</div>


&lsquo;Draw&rsquo; a single line segment in the stroker's current sub-path, from the last position.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
<tr><td class="val" id="to">to</td><td class="desc">
<p>A pointer to the destination point.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

You should call this function between <a href="../ft2-glyph_stroker/#ft_stroker_beginsubpath">FT_Stroker_BeginSubPath</a> and <a href="../ft2-glyph_stroker/#ft_stroker_endsubpath">FT_Stroker_EndSubPath</a>.

<hr>

## FT_Stroker_ConicTo

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Stroker_ConicTo</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>  stroker,
                      <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  control,
                      <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  to );
</pre>
</div>


&lsquo;Draw&rsquo; a single quadratic Bezier in the stroker's current sub-path, from the last position.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
<tr><td class="val" id="control">control</td><td class="desc">
<p>A pointer to a Bezier control point.</p>
</td></tr>
<tr><td class="val" id="to">to</td><td class="desc">
<p>A pointer to the destination point.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

You should call this function between <a href="../ft2-glyph_stroker/#ft_stroker_beginsubpath">FT_Stroker_BeginSubPath</a> and <a href="../ft2-glyph_stroker/#ft_stroker_endsubpath">FT_Stroker_EndSubPath</a>.

<hr>

## FT_Stroker_CubicTo

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Stroker_CubicTo</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>  stroker,
                      <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  control1,
                      <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  control2,
                      <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  to );
</pre>
</div>


&lsquo;Draw&rsquo; a single cubic Bezier in the stroker's current sub-path, from the last position.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
<tr><td class="val" id="control1">control1</td><td class="desc">
<p>A pointer to the first Bezier control point.</p>
</td></tr>
<tr><td class="val" id="control2">control2</td><td class="desc">
<p>A pointer to second Bezier control point.</p>
</td></tr>
<tr><td class="val" id="to">to</td><td class="desc">
<p>A pointer to the destination point.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

You should call this function between <a href="../ft2-glyph_stroker/#ft_stroker_beginsubpath">FT_Stroker_BeginSubPath</a> and <a href="../ft2-glyph_stroker/#ft_stroker_endsubpath">FT_Stroker_EndSubPath</a>.

<hr>

## FT_Stroker_GetBorderCounts

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Stroker_GetBorderCounts</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>        stroker,
                              <a href="../ft2-glyph_stroker/#ft_strokerborder">FT_StrokerBorder</a>  border,
                              <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>          *anum_points,
                              <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>          *anum_contours );
</pre>
</div>


Call this function once you have finished parsing your paths with the stroker. It returns the number of points and contours necessary to export one of the &lsquo;border&rsquo; or &lsquo;stroke&rsquo; outlines generated by the stroker.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
<tr><td class="val" id="border">border</td><td class="desc">
<p>The border index.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="anum_points">anum_points</td><td class="desc">
<p>The number of points.</p>
</td></tr>
<tr><td class="val" id="anum_contours">anum_contours</td><td class="desc">
<p>The number of contours.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

When an outline, or a sub-path, is &lsquo;closed&rsquo;, the stroker generates two independent &lsquo;border&rsquo; outlines, named &lsquo;left&rsquo; and &lsquo;right&rsquo;.

When the outline, or a sub-path, is &lsquo;opened&rsquo;, the stroker merges the &lsquo;border&rsquo; outlines with caps. The &lsquo;left&rsquo; border receives all points, while the &lsquo;right&rsquo; border becomes empty.

Use the function <a href="../ft2-glyph_stroker/#ft_stroker_getcounts">FT_Stroker_GetCounts</a> instead if you want to retrieve the counts associated to both borders.

<hr>

## FT_Stroker_ExportBorder

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Stroker_ExportBorder</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>        stroker,
                           <a href="../ft2-glyph_stroker/#ft_strokerborder">FT_StrokerBorder</a>  border,
                           <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*       outline );
</pre>
</div>


Call this function after <a href="../ft2-glyph_stroker/#ft_stroker_getbordercounts">FT_Stroker_GetBorderCounts</a> to export the corresponding border to your own <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a> structure.

Note that this function appends the border points and contours to your outline, but does not try to resize its arrays.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
<tr><td class="val" id="border">border</td><td class="desc">
<p>The border index.</p>
</td></tr>
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>The target outline handle.</p>
</td></tr>
</table>

<h4>note</h4>

Always call this function after <a href="../ft2-glyph_stroker/#ft_stroker_getbordercounts">FT_Stroker_GetBorderCounts</a> to get sure that there is enough room in your <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a> object to receive all new data.

When an outline, or a sub-path, is &lsquo;closed&rsquo;, the stroker generates two independent &lsquo;border&rsquo; outlines, named &lsquo;left&rsquo; and &lsquo;right&rsquo;.

When the outline, or a sub-path, is &lsquo;opened&rsquo;, the stroker merges the &lsquo;border&rsquo; outlines with caps. The &lsquo;left&rsquo; border receives all points, while the &lsquo;right&rsquo; border becomes empty.

Use the function <a href="../ft2-glyph_stroker/#ft_stroker_export">FT_Stroker_Export</a> instead if you want to retrieve all borders at once.

<hr>

## FT_Stroker_GetCounts

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Stroker_GetCounts</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>  stroker,
                        <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    *anum_points,
                        <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    *anum_contours );
</pre>
</div>


Call this function once you have finished parsing your paths with the stroker. It returns the number of points and contours necessary to export all points/borders from the stroked outline/path.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="anum_points">anum_points</td><td class="desc">
<p>The number of points.</p>
</td></tr>
<tr><td class="val" id="anum_contours">anum_contours</td><td class="desc">
<p>The number of contours.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FT_Stroker_Export

Defined in FT_STROKER_H (freetype/ftstroke.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Stroker_Export</b>( <a href="../ft2-glyph_stroker/#ft_stroker">FT_Stroker</a>   stroker,
                     <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline );
</pre>
</div>


Call this function after <a href="../ft2-glyph_stroker/#ft_stroker_getbordercounts">FT_Stroker_GetBorderCounts</a> to export all borders to your own <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a> structure.

Note that this function appends the border points and contours to your outline, but does not try to resize its arrays.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stroker">stroker</td><td class="desc">
<p>The target stroker handle.</p>
</td></tr>
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>The target outline handle.</p>
</td></tr>
</table>

<hr>

