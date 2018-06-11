[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; Outline Processing

-------------------------------

# Outline Processing

## Synopsis

This section contains routines used to create and destroy scalable glyph images known as &lsquo;outlines&rsquo;. These can also be measured, transformed, and converted into bitmaps and pixmaps.

## FT_Outline

Defined in FT_IMAGE_H (freetype/ftimage.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Outline_
  {
    <span class="keyword">short</span>       n_contours;      /* number of contours in glyph        */
    <span class="keyword">short</span>       n_points;        /* number of points in the glyph      */

    <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  points;          /* the outline's points               */
    <span class="keyword">char</span>*       tags;            /* the points flags                   */
    <span class="keyword">short</span>*      contours;        /* the contour end points             */

    <span class="keyword">int</span>         flags;           /* outline masks                      */

  } <b>FT_Outline</b>;
</pre>
</div>


This structure is used to describe an outline to the scan-line converter.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="n_contours">n_contours</td><td class="desc">
<p>The number of contours in the outline.</p>
</td></tr>
<tr><td class="val" id="n_points">n_points</td><td class="desc">
<p>The number of points in the outline.</p>
</td></tr>
<tr><td class="val" id="points">points</td><td class="desc">
<p>A pointer to an array of &lsquo;n_points&rsquo; <a href="../ft2-basic_types/#ft_vector">FT_Vector</a> elements, giving the outline's point coordinates.</p>
</td></tr>
<tr><td class="val" id="tags">tags</td><td class="desc">
<p>A pointer to an array of &lsquo;n_points&rsquo; chars, giving each outline point's type.</p>
<p>If bit&nbsp;0 is unset, the point is &lsquo;off&rsquo; the curve, i.e., a Bezier control point, while it is &lsquo;on&rsquo; if set.</p>
<p>Bit&nbsp;1 is meaningful for &lsquo;off&rsquo; points only. If set, it indicates a third-order Bezier arc control point; and a second-order control point if unset.</p>
<p>If bit&nbsp;2 is set, bits 5-7 contain the drop-out mode (as defined in the OpenType specification; the value is the same as the argument to the SCANMODE instruction).</p>
<p>Bits 3 and&nbsp;4 are reserved for internal purposes.</p>
</td></tr>
<tr><td class="val" id="contours">contours</td><td class="desc">
<p>An array of &lsquo;n_contours&rsquo; shorts, giving the end point of each contour within the outline. For example, the first contour is defined by the points &lsquo;0&rsquo; to &lsquo;contours[0]&rsquo;, the second one is defined by the points &lsquo;contours[0]+1&rsquo; to &lsquo;contours[1]&rsquo;, etc.</p>
</td></tr>
<tr><td class="val" id="flags">flags</td><td class="desc">
<p>A set of bit flags used to characterize the outline and give hints to the scan-converter and hinter on how to convert/grid-fit it. See <a href="../ft2-outline_processing/#ft_outline_xxx">FT_OUTLINE_XXX</a>.</p>
</td></tr>
</table>

<h4>note</h4>

The B/W rasterizer only checks bit&nbsp;2 in the &lsquo;tags&rsquo; array for the first point of each contour. The drop-out mode as given with <a href="../ft2-outline_processing/#ft_outline_xxx">FT_OUTLINE_IGNORE_DROPOUTS</a>, <a href="../ft2-outline_processing/#ft_outline_xxx">FT_OUTLINE_SMART_DROPOUTS</a>, and <a href="../ft2-outline_processing/#ft_outline_xxx">FT_OUTLINE_INCLUDE_STUBS</a> in &lsquo;flags&rsquo; is then overridden.

<hr>

## FT_Outline_New

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Outline_New</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>   library,
                  <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>      numPoints,
                  <a href="../ft2-basic_types/#ft_int">FT_Int</a>       numContours,
                  <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>  *anoutline );


  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  FT_Outline_New_Internal( <a href="../ft2-system_interface/#ft_memory">FT_Memory</a>    memory,
                           <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>      numPoints,
                           <a href="../ft2-basic_types/#ft_int">FT_Int</a>       numContours,
                           <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>  *anoutline );
</pre>
</div>


Create a new outline of a given size.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the library object from where the outline is allocated. Note however that the new outline will <strong>not</strong> necessarily be <strong>freed</strong>, when destroying the library, by <a href="../ft2-base_interface/#ft_done_freetype">FT_Done_FreeType</a>.</p>
</td></tr>
<tr><td class="val" id="numpoints">numPoints</td><td class="desc">
<p>The maximum number of points within the outline. Must be smaller than or equal to 0xFFFF (65535).</p>
</td></tr>
<tr><td class="val" id="numcontours">numContours</td><td class="desc">
<p>The maximum number of contours within the outline. This value must be in the range 0 to &lsquo;numPoints&rsquo;.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="anoutline">anoutline</td><td class="desc">
<p>A handle to the new outline.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The reason why this function takes a &lsquo;library&rsquo; parameter is simply to use the library's memory allocator.

<hr>

## FT_Outline_Done

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Outline_Done</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>   library,
                   <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline );


  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  FT_Outline_Done_Internal( <a href="../ft2-system_interface/#ft_memory">FT_Memory</a>    memory,
                            <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline );
</pre>
</div>


Destroy an outline created with <a href="../ft2-outline_processing/#ft_outline_new">FT_Outline_New</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle of the library object used to allocate the outline.</p>
</td></tr>
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A pointer to the outline object to be discarded.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

If the outline's &lsquo;owner&rsquo; field is not set, only the outline descriptor will be released.

<hr>

## FT_Outline_Copy

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Outline_Copy</b>( <span class="keyword">const</span> <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  source,
                   <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>        *target );
</pre>
</div>


Copy an outline into another one. Both objects must have the same sizes (number of points &amp; number of contours) when this function is called.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="source">source</td><td class="desc">
<p>A handle to the source outline.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="target">target</td><td class="desc">
<p>A handle to the target outline.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FT_Outline_Translate

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Outline_Translate</b>( <span class="keyword">const</span> <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline,
                        <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>             xOffset,
                        <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>             yOffset );
</pre>
</div>


Apply a simple translation to the points of an outline.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A pointer to the target outline descriptor.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="xoffset">xOffset</td><td class="desc">
<p>The horizontal offset.</p>
</td></tr>
<tr><td class="val" id="yoffset">yOffset</td><td class="desc">
<p>The vertical offset.</p>
</td></tr>
</table>

<hr>

## FT_Outline_Transform

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Outline_Transform</b>( <span class="keyword">const</span> <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline,
                        <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_matrix">FT_Matrix</a>*   matrix );
</pre>
</div>


Apply a simple 2x2 matrix to all of an outline's points. Useful for applying rotations, slanting, flipping, etc.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A pointer to the target outline descriptor.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="matrix">matrix</td><td class="desc">
<p>A pointer to the transformation matrix.</p>
</td></tr>
</table>

<h4>note</h4>

You can use <a href="../ft2-outline_processing/#ft_outline_translate">FT_Outline_Translate</a> if you need to translate the outline's points.

<hr>

## FT_Outline_Embolden

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Outline_Embolden</b>( <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline,
                       <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>       strength );
</pre>
</div>


Embolden an outline. The new outline will be at most 4&nbsp;times &lsquo;strength&rsquo; pixels wider and higher. You may think of the left and bottom borders as unchanged.

Negative &lsquo;strength&rsquo; values to reduce the outline thickness are possible also.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A handle to the target outline.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="strength">strength</td><td class="desc">
<p>How strong the glyph is emboldened. Expressed in 26.6 pixel format.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The used algorithm to increase or decrease the thickness of the glyph doesn't change the number of points; this means that certain situations like acute angles or intersections are sometimes handled incorrectly.

If you need &lsquo;better&rsquo; metrics values you should call <a href="../ft2-outline_processing/#ft_outline_get_cbox">FT_Outline_Get_CBox</a> or <a href="../ft2-outline_processing/#ft_outline_get_bbox">FT_Outline_Get_BBox</a>.

Example call:
```
  FT_Load_Glyph( face, index, FT_LOAD_DEFAULT );
  if ( face->glyph->format == FT_GLYPH_FORMAT_OUTLINE )
    FT_Outline_Embolden( &face->glyph->outline, strength );
```

To get meaningful results, font scaling values must be set with functions like <a href="../ft2-base_interface/#ft_set_char_size">FT_Set_Char_Size</a> before calling FT_Render_Glyph.

<hr>

## FT_Outline_EmboldenXY

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Outline_EmboldenXY</b>( <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline,
                         <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>       xstrength,
                         <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>       ystrength );
</pre>
</div>


Embolden an outline. The new outline will be &lsquo;xstrength&rsquo; pixels wider and &lsquo;ystrength&rsquo; pixels higher. Otherwise, it is similar to <a href="../ft2-outline_processing/#ft_outline_embolden">FT_Outline_Embolden</a>, which uses the same strength in both directions.

<h4>since</h4>

2.4.10

<hr>

## FT_Outline_Reverse

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Outline_Reverse</b>( <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline );
</pre>
</div>


Reverse the drawing direction of an outline. This is used to ensure consistent fill conventions for mirrored glyphs.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A pointer to the target outline descriptor.</p>
</td></tr>
</table>

<h4>note</h4>

This function toggles the bit flag <a href="../ft2-outline_processing/#ft_outline_xxx">FT_OUTLINE_REVERSE_FILL</a> in the outline's &lsquo;flags&rsquo; field.

It shouldn't be used by a normal client application, unless it knows what it is doing.

<hr>

## FT_Outline_Check

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Outline_Check</b>( <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline );
</pre>
</div>


Check the contents of an outline descriptor.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A handle to a source outline.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

An empty outline, or an outline with a single point only is also valid.

<hr>

## FT_Outline_Get_CBox

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Outline_Get_CBox</b>( <span class="keyword">const</span> <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline,
                       <a href="../ft2-basic_types/#ft_bbox">FT_BBox</a>           *acbox );
</pre>
</div>


Return an outline's &lsquo;control box&rsquo;. The control box encloses all the outline's points, including Bezier control points. Though it coincides with the exact bounding box for most glyphs, it can be slightly larger in some situations (like when rotating an outline that contains Bezier outside arcs).

Computing the control box is very fast, while getting the bounding box can take much more time as it needs to walk over all segments and arcs in the outline. To get the latter, you can use the &lsquo;ftbbox&rsquo; component, which is dedicated to this single task.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A pointer to the source outline descriptor.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="acbox">acbox</td><td class="desc">
<p>The outline's control box.</p>
</td></tr>
</table>

<h4>note</h4>

See <a href="../ft2-glyph_management/#ft_glyph_get_cbox">FT_Glyph_Get_CBox</a> for a discussion of tricky fonts.

<hr>

## FT_Outline_Get_BBox

Defined in FT_BBOX_H (freetype/ftbbox.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Outline_Get_BBox</b>( <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline,
                       <a href="../ft2-basic_types/#ft_bbox">FT_BBox</a>     *abbox );
</pre>
</div>


Compute the exact bounding box of an outline. This is slower than computing the control box. However, it uses an advanced algorithm that returns _very_ quickly when the two boxes coincide. Otherwise, the outline Bezier arcs are traversed to extract their extrema.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A pointer to the source outline.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="abbox">abbox</td><td class="desc">
<p>The outline's exact bounding box.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

If the font is tricky and the glyph has been loaded with <a href="../ft2-base_interface/#ft_load_xxx">FT_LOAD_NO_SCALE</a>, the resulting BBox is meaningless. To get reasonable values for the BBox it is necessary to load the glyph at a large ppem value (so that the hinting instructions can properly shift and scale the subglyphs), then extracting the BBox, which can be eventually converted back to font units.

<hr>

## FT_Outline_Get_Bitmap

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Outline_Get_Bitmap</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>        library,
                         <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*       outline,
                         <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a>  *abitmap );
</pre>
</div>


Render an outline within a bitmap. The outline's image is simply OR-ed to the target bitmap.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to a FreeType library object.</p>
</td></tr>
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A pointer to the source outline descriptor.</p>
</td></tr>
</table>

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="abitmap">abitmap</td><td class="desc">
<p>A pointer to the target bitmap descriptor.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function does NOT CREATE the bitmap, it only renders an outline image within the one you pass to it! Consequently, the various fields in &lsquo;abitmap&rsquo; should be set accordingly.

It will use the raster corresponding to the default glyph format.

The value of the &lsquo;num_grays&rsquo; field in &lsquo;abitmap&rsquo; is ignored. If you select the gray-level rasterizer, and you want less than 256 gray levels, you have to use <a href="../ft2-outline_processing/#ft_outline_render">FT_Outline_Render</a> directly.

<hr>

## FT_Outline_Render

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Outline_Render</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>         library,
                     <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*        outline,
                     <a href="../ft2-raster/#ft_raster_params">FT_Raster_Params</a>*  params );
</pre>
</div>


Render an outline within a bitmap using the current scan-convert. This function uses an <a href="../ft2-raster/#ft_raster_params">FT_Raster_Params</a> structure as an argument, allowing advanced features like direct composition, translucency, etc.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to a FreeType library object.</p>
</td></tr>
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A pointer to the source outline descriptor.</p>
</td></tr>
</table>

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="params">params</td><td class="desc">
<p>A pointer to an <a href="../ft2-raster/#ft_raster_params">FT_Raster_Params</a> structure used to describe the rendering operation.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

You should know what you are doing and how <a href="../ft2-raster/#ft_raster_params">FT_Raster_Params</a> works to use this function.

The field &lsquo;params.source&rsquo; will be set to &lsquo;outline&rsquo; before the scan converter is called, which means that the value you give to it is actually ignored.

The gray-level rasterizer always uses 256 gray levels. If you want less gray levels, you have to provide your own span callback. See the <a href="../ft2-raster/#ft_raster_flag_xxx">FT_RASTER_FLAG_DIRECT</a> value of the &lsquo;flags&rsquo; field in the <a href="../ft2-raster/#ft_raster_params">FT_Raster_Params</a> structure for more details.

<hr>

## FT_Outline_Decompose

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Outline_Decompose</b>( <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*              outline,
                        <span class="keyword">const</span> <a href="../ft2-outline_processing/#ft_outline_funcs">FT_Outline_Funcs</a>*  func_interface,
                        <span class="keyword">void</span>*                    user );
</pre>
</div>


Walk over an outline's structure to decompose it into individual segments and Bezier arcs. This function also emits &lsquo;move to&rsquo; operations to indicate the start of new contours in the outline.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A pointer to the source target.</p>
</td></tr>
<tr><td class="val" id="func_interface">func_interface</td><td class="desc">
<p>A table of &lsquo;emitters&rsquo;, i.e., function pointers called during decomposition to indicate path operations.</p>
</td></tr>
</table>

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="user">user</td><td class="desc">
<p>A typeless pointer that is passed to each emitter during the decomposition. It can be used to store the state during the decomposition.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

A contour that contains a single point only is represented by a &lsquo;move to&rsquo; operation followed by &lsquo;line to&rsquo; to the same point. In most cases, it is best to filter this out before using the outline for stroking purposes (otherwise it would result in a visible dot when round caps are used).

Similarly, the function returns success for an empty outline also (doing nothing, this is, not calling any emitter); if necessary, you should filter this out, too.

<hr>

## FT_Outline_Funcs

Defined in FT_IMAGE_H (freetype/ftimage.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Outline_Funcs_
  {
    <a href="../ft2-outline_processing/#ft_outline_movetofunc">FT_Outline_MoveToFunc</a>   move_to;
    <a href="../ft2-outline_processing/#ft_outline_linetofunc">FT_Outline_LineToFunc</a>   line_to;
    <a href="../ft2-outline_processing/#ft_outline_conictofunc">FT_Outline_ConicToFunc</a>  conic_to;
    <a href="../ft2-outline_processing/#ft_outline_cubictofunc">FT_Outline_CubicToFunc</a>  cubic_to;

    <span class="keyword">int</span>                     shift;
    <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>                  delta;

  } <b>FT_Outline_Funcs</b>;
</pre>
</div>


A structure to hold various function pointers used during outline decomposition in order to emit segments, conic, and cubic Beziers.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="move_to">move_to</td><td class="desc">
<p>The &lsquo;move to&rsquo; emitter.</p>
</td></tr>
<tr><td class="val" id="line_to">line_to</td><td class="desc">
<p>The segment emitter.</p>
</td></tr>
<tr><td class="val" id="conic_to">conic_to</td><td class="desc">
<p>The second-order Bezier arc emitter.</p>
</td></tr>
<tr><td class="val" id="cubic_to">cubic_to</td><td class="desc">
<p>The third-order Bezier arc emitter.</p>
</td></tr>
<tr><td class="val" id="shift">shift</td><td class="desc">
<p>The shift that is applied to coordinates before they are sent to the emitter.</p>
</td></tr>
<tr><td class="val" id="delta">delta</td><td class="desc">
<p>The delta that is applied to coordinates before they are sent to the emitter, but after the shift.</p>
</td></tr>
</table>

<h4>note</h4>

The point coordinates sent to the emitters are the transformed version of the original coordinates (this is important for high accuracy during scan-conversion). The transformation is simple:
```
  x' = (x << shift) - delta
  y' = (y << shift) - delta
```

Set the values of &lsquo;shift&rsquo; and &lsquo;delta&rsquo; to&nbsp;0 to get the original point coordinates.

<hr>

## FT_Outline_MoveToFunc

Defined in FT_IMAGE_H (freetype/ftimage.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">int</span>
  (*<b>FT_Outline_MoveToFunc</b>)( <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  to,
                            <span class="keyword">void</span>*             user );

#<span class="keyword">define</span> FT_Outline_MoveTo_Func  <b>FT_Outline_MoveToFunc</b>
</pre>
</div>


A function pointer type used to describe the signature of a &lsquo;move to&rsquo; function during outline walking/decomposition.

A &lsquo;move to&rsquo; is emitted to start a new contour in an outline.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="to">to</td><td class="desc">
<p>A pointer to the target point of the &lsquo;move to&rsquo;.</p>
</td></tr>
<tr><td class="val" id="user">user</td><td class="desc">
<p>A typeless pointer, which is passed from the caller of the decomposition function.</p>
</td></tr>
</table>

<h4>return</h4>

Error code. 0&nbsp;means success.

<hr>

## FT_Outline_LineToFunc

Defined in FT_IMAGE_H (freetype/ftimage.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">int</span>
  (*<b>FT_Outline_LineToFunc</b>)( <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  to,
                            <span class="keyword">void</span>*             user );

#<span class="keyword">define</span> FT_Outline_LineTo_Func  <b>FT_Outline_LineToFunc</b>
</pre>
</div>


A function pointer type used to describe the signature of a &lsquo;line to&rsquo; function during outline walking/decomposition.

A &lsquo;line to&rsquo; is emitted to indicate a segment in the outline.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="to">to</td><td class="desc">
<p>A pointer to the target point of the &lsquo;line to&rsquo;.</p>
</td></tr>
<tr><td class="val" id="user">user</td><td class="desc">
<p>A typeless pointer, which is passed from the caller of the decomposition function.</p>
</td></tr>
</table>

<h4>return</h4>

Error code. 0&nbsp;means success.

<hr>

## FT_Outline_ConicToFunc

Defined in FT_IMAGE_H (freetype/ftimage.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">int</span>
  (*<b>FT_Outline_ConicToFunc</b>)( <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  control,
                             <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  to,
                             <span class="keyword">void</span>*             user );

#<span class="keyword">define</span> FT_Outline_ConicTo_Func  <b>FT_Outline_ConicToFunc</b>
</pre>
</div>


A function pointer type used to describe the signature of a &lsquo;conic to&rsquo; function during outline walking or decomposition.

A &lsquo;conic to&rsquo; is emitted to indicate a second-order Bezier arc in the outline.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="control">control</td><td class="desc">
<p>An intermediate control point between the last position and the new target in &lsquo;to&rsquo;.</p>
</td></tr>
<tr><td class="val" id="to">to</td><td class="desc">
<p>A pointer to the target end point of the conic arc.</p>
</td></tr>
<tr><td class="val" id="user">user</td><td class="desc">
<p>A typeless pointer, which is passed from the caller of the decomposition function.</p>
</td></tr>
</table>

<h4>return</h4>

Error code. 0&nbsp;means success.

<hr>

## FT_Outline_CubicToFunc

Defined in FT_IMAGE_H (freetype/ftimage.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">int</span>
  (*<b>FT_Outline_CubicToFunc</b>)( <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  control1,
                             <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  control2,
                             <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  to,
                             <span class="keyword">void</span>*             user );

#<span class="keyword">define</span> FT_Outline_CubicTo_Func  <b>FT_Outline_CubicToFunc</b>
</pre>
</div>


A function pointer type used to describe the signature of a &lsquo;cubic to&rsquo; function during outline walking or decomposition.

A &lsquo;cubic to&rsquo; is emitted to indicate a third-order Bezier arc.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="control1">control1</td><td class="desc">
<p>A pointer to the first Bezier control point.</p>
</td></tr>
<tr><td class="val" id="control2">control2</td><td class="desc">
<p>A pointer to the second Bezier control point.</p>
</td></tr>
<tr><td class="val" id="to">to</td><td class="desc">
<p>A pointer to the target end point.</p>
</td></tr>
<tr><td class="val" id="user">user</td><td class="desc">
<p>A typeless pointer, which is passed from the caller of the decomposition function.</p>
</td></tr>
</table>

<h4>return</h4>

Error code. 0&nbsp;means success.

<hr>

## FT_Orientation

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  FT_Orientation_
  {
    <a href="../ft2-outline_processing/#ft_orientation_truetype">FT_ORIENTATION_TRUETYPE</a>   = 0,
    <a href="../ft2-outline_processing/#ft_orientation_postscript">FT_ORIENTATION_POSTSCRIPT</a> = 1,
    <a href="../ft2-outline_processing/#ft_orientation_fill_right">FT_ORIENTATION_FILL_RIGHT</a> = <a href="../ft2-outline_processing/#ft_orientation_truetype">FT_ORIENTATION_TRUETYPE</a>,
    <a href="../ft2-outline_processing/#ft_orientation_fill_left">FT_ORIENTATION_FILL_LEFT</a>  = <a href="../ft2-outline_processing/#ft_orientation_postscript">FT_ORIENTATION_POSTSCRIPT</a>,
    <a href="../ft2-outline_processing/#ft_orientation_none">FT_ORIENTATION_NONE</a>

  } <b>FT_Orientation</b>;
</pre>
</div>


A list of values used to describe an outline's contour orientation.

The TrueType and PostScript specifications use different conventions to determine whether outline contours should be filled or unfilled.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_orientation_truetype">FT_ORIENTATION_TRUETYPE</td><td class="desc">
<p>According to the TrueType specification, clockwise contours must be filled, and counter-clockwise ones must be unfilled.</p>
</td></tr>
<tr><td class="val" id="ft_orientation_postscript">FT_ORIENTATION_POSTSCRIPT</td><td class="desc">
<p>According to the PostScript specification, counter-clockwise contours must be filled, and clockwise ones must be unfilled.</p>
</td></tr>
<tr><td class="val" id="ft_orientation_fill_right">FT_ORIENTATION_FILL_RIGHT</td><td class="desc">
<p>This is identical to <a href="../ft2-outline_processing/#ft_orientation">FT_ORIENTATION_TRUETYPE</a>, but is used to remember that in TrueType, everything that is to the right of the drawing direction of a contour must be filled.</p>
</td></tr>
<tr><td class="val" id="ft_orientation_fill_left">FT_ORIENTATION_FILL_LEFT</td><td class="desc">
<p>This is identical to <a href="../ft2-outline_processing/#ft_orientation">FT_ORIENTATION_POSTSCRIPT</a>, but is used to remember that in PostScript, everything that is to the left of the drawing direction of a contour must be filled.</p>
</td></tr>
<tr><td class="val" id="ft_orientation_none">FT_ORIENTATION_NONE</td><td class="desc">
<p>The orientation cannot be determined. That is, different parts of the glyph have different orientation.</p>
</td></tr>
</table>

<hr>

## FT_Outline_Get_Orientation

Defined in FT_OUTLINE_H (freetype/ftoutln.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-outline_processing/#ft_orientation">FT_Orientation</a> )
  <b>FT_Outline_Get_Orientation</b>( <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>*  outline );
</pre>
</div>


This function analyzes a glyph outline and tries to compute its fill orientation (see <a href="../ft2-outline_processing/#ft_orientation">FT_Orientation</a>). This is done by integrating the total area covered by the outline. The positive integral corresponds to the clockwise orientation and <a href="../ft2-outline_processing/#ft_orientation">FT_ORIENTATION_POSTSCRIPT</a> is returned. The negative integral corresponds to the counter-clockwise orientation and <a href="../ft2-outline_processing/#ft_orientation">FT_ORIENTATION_TRUETYPE</a> is returned.

Note that this will return <a href="../ft2-outline_processing/#ft_orientation">FT_ORIENTATION_TRUETYPE</a> for empty outlines.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="outline">outline</td><td class="desc">
<p>A handle to the source outline.</p>
</td></tr>
</table>

<h4>return</h4>

The orientation.

<hr>

## FT_OUTLINE_XXX

Defined in FT_IMAGE_H (freetype/ftimage.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <a href="../ft2-outline_processing/#ft_outline_none">FT_OUTLINE_NONE</a>             0x0
#<span class="keyword">define</span> <a href="../ft2-outline_processing/#ft_outline_owner">FT_OUTLINE_OWNER</a>            0x1
#<span class="keyword">define</span> <a href="../ft2-outline_processing/#ft_outline_even_odd_fill">FT_OUTLINE_EVEN_ODD_FILL</a>    0x2
#<span class="keyword">define</span> <a href="../ft2-outline_processing/#ft_outline_reverse_fill">FT_OUTLINE_REVERSE_FILL</a>     0x4
#<span class="keyword">define</span> <a href="../ft2-outline_processing/#ft_outline_ignore_dropouts">FT_OUTLINE_IGNORE_DROPOUTS</a>  0x8
#<span class="keyword">define</span> <a href="../ft2-outline_processing/#ft_outline_smart_dropouts">FT_OUTLINE_SMART_DROPOUTS</a>   0x10
#<span class="keyword">define</span> <a href="../ft2-outline_processing/#ft_outline_include_stubs">FT_OUTLINE_INCLUDE_STUBS</a>    0x20

#<span class="keyword">define</span> <a href="../ft2-outline_processing/#ft_outline_high_precision">FT_OUTLINE_HIGH_PRECISION</a>   0x100
#<span class="keyword">define</span> <a href="../ft2-outline_processing/#ft_outline_single_pass">FT_OUTLINE_SINGLE_PASS</a>      0x200


  /* these constants are deprecated; use the corresponding */
  /* `<b>FT_OUTLINE_XXX</b>' values instead                       */
#<span class="keyword">define</span> ft_outline_none             <a href="../ft2-outline_processing/#ft_outline_none">FT_OUTLINE_NONE</a>
#<span class="keyword">define</span> ft_outline_owner            <a href="../ft2-outline_processing/#ft_outline_owner">FT_OUTLINE_OWNER</a>
#<span class="keyword">define</span> ft_outline_even_odd_fill    <a href="../ft2-outline_processing/#ft_outline_even_odd_fill">FT_OUTLINE_EVEN_ODD_FILL</a>
#<span class="keyword">define</span> ft_outline_reverse_fill     <a href="../ft2-outline_processing/#ft_outline_reverse_fill">FT_OUTLINE_REVERSE_FILL</a>
#<span class="keyword">define</span> ft_outline_ignore_dropouts  <a href="../ft2-outline_processing/#ft_outline_ignore_dropouts">FT_OUTLINE_IGNORE_DROPOUTS</a>
#<span class="keyword">define</span> ft_outline_high_precision   <a href="../ft2-outline_processing/#ft_outline_high_precision">FT_OUTLINE_HIGH_PRECISION</a>
#<span class="keyword">define</span> ft_outline_single_pass      <a href="../ft2-outline_processing/#ft_outline_single_pass">FT_OUTLINE_SINGLE_PASS</a>
</pre>
</div>


A list of bit-field constants use for the flags in an outline's &lsquo;flags&rsquo; field.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_outline_none">FT_OUTLINE_NONE</td><td class="desc">
<p>Value&nbsp;0 is reserved.</p>
</td></tr>
<tr><td class="val" id="ft_outline_owner">FT_OUTLINE_OWNER</td><td class="desc">
<p>If set, this flag indicates that the outline's field arrays (i.e., &lsquo;points&rsquo;, &lsquo;flags&rsquo;, and &lsquo;contours&rsquo;) are &lsquo;owned&rsquo; by the outline object, and should thus be freed when it is destroyed.</p>
</td></tr>
<tr><td class="val" id="ft_outline_even_odd_fill">FT_OUTLINE_EVEN_ODD_FILL</td><td class="desc">
<p>By default, outlines are filled using the non-zero winding rule. If set to 1, the outline will be filled using the even-odd fill rule (only works with the smooth rasterizer).</p>
</td></tr>
<tr><td class="val" id="ft_outline_reverse_fill">FT_OUTLINE_REVERSE_FILL</td><td class="desc">
<p>By default, outside contours of an outline are oriented in clock-wise direction, as defined in the TrueType specification. This flag is set if the outline uses the opposite direction (typically for Type&nbsp;1 fonts). This flag is ignored by the scan converter.</p>
</td></tr>
<tr><td class="val" id="ft_outline_ignore_dropouts">FT_OUTLINE_IGNORE_DROPOUTS</td><td class="desc">
<p>By default, the scan converter will try to detect drop-outs in an outline and correct the glyph bitmap to ensure consistent shape continuity. If set, this flag hints the scan-line converter to ignore such cases. See below for more information.</p>
</td></tr>
<tr><td class="val" id="ft_outline_smart_dropouts">FT_OUTLINE_SMART_DROPOUTS</td><td class="desc">
<p>Select smart dropout control. If unset, use simple dropout control. Ignored if <a href="../ft2-outline_processing/#ft_outline_xxx">FT_OUTLINE_IGNORE_DROPOUTS</a> is set. See below for more information.</p>
</td></tr>
<tr><td class="val" id="ft_outline_include_stubs">FT_OUTLINE_INCLUDE_STUBS</td><td class="desc">
<p>If set, turn pixels on for &lsquo;stubs&rsquo;, otherwise exclude them. Ignored if <a href="../ft2-outline_processing/#ft_outline_xxx">FT_OUTLINE_IGNORE_DROPOUTS</a> is set. See below for more information.</p>
</td></tr>
<tr><td class="val" id="ft_outline_high_precision">FT_OUTLINE_HIGH_PRECISION</td><td class="desc">
<p>This flag indicates that the scan-line converter should try to convert this outline to bitmaps with the highest possible quality. It is typically set for small character sizes. Note that this is only a hint that might be completely ignored by a given scan-converter.</p>
</td></tr>
<tr><td class="val" id="ft_outline_single_pass">FT_OUTLINE_SINGLE_PASS</td><td class="desc">
<p>This flag is set to force a given scan-converter to only use a single pass over the outline to render a bitmap glyph image. Normally, it is set for very large character sizes. It is only a hint that might be completely ignored by a given scan-converter.</p>
</td></tr>
</table>

<h4>note</h4>

The flags <a href="../ft2-outline_processing/#ft_outline_xxx">FT_OUTLINE_IGNORE_DROPOUTS</a>, <a href="../ft2-outline_processing/#ft_outline_xxx">FT_OUTLINE_SMART_DROPOUTS</a>, and <a href="../ft2-outline_processing/#ft_outline_xxx">FT_OUTLINE_INCLUDE_STUBS</a> are ignored by the smooth rasterizer.

There exists a second mechanism to pass the drop-out mode to the B/W rasterizer; see the &lsquo;tags&rsquo; field in <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>.

Please refer to the description of the &lsquo;SCANTYPE&rsquo; instruction in the OpenType specification (in file &lsquo;ttinst1.doc&rsquo;) how simple drop-outs, smart drop-outs, and stubs are defined.

<hr>

