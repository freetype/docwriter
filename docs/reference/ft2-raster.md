[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; Scanline Converter

-------------------------------


# Scanline Converter

## Synopsis

This section contains technical definitions.

## FT_Raster

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_RasterRec_*  <b>FT_Raster</b>;
</pre>


An opaque handle (pointer) to a raster object. Each object can be used independently to convert an outline into a bitmap or pixmap.

<hr />

## FT_Span

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Span_
  {
    <span class="keyword">short</span>           x;
    <span class="keyword">unsigned</span> <span class="keyword">short</span>  len;
    <span class="keyword">unsigned</span> <span class="keyword">char</span>   coverage;

  } <b>FT_Span</b>;
</pre>


A structure used to model a single span of gray pixels when rendering an anti-aliased bitmap.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="x">x</td><td class="desc">

The span's horizontal start position.
</td></tr>
<tr><td class="val" id="len">len</td><td class="desc">

The span's length in pixels.
</td></tr>
<tr><td class="val" id="coverage">coverage</td><td class="desc">

The span color/coverage, ranging from 0 (background) to 255 (foreground).
</td></tr>
</table>

<h4>note</h4>

This structure is used by the span drawing callback type named <a href="../ft2-raster/#ft_spanfunc">FT_SpanFunc</a> that takes the y&nbsp;coordinate of the span as a parameter.

The coverage value is always between 0 and 255. If you want less gray values, the callback function has to reduce them.

<hr />

## FT_SpanFunc

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>
  (*<b>FT_SpanFunc</b>)( <span class="keyword">int</span>             y,
                  <span class="keyword">int</span>             count,
                  <span class="keyword">const</span> <a href="../ft2-raster/#ft_span">FT_Span</a>*  spans,
                  <span class="keyword">void</span>*           user );

#define FT_Raster_Span_Func  <b>FT_SpanFunc</b>
</pre>


A function used as a call-back by the anti-aliased renderer in order to let client applications draw themselves the gray pixel spans on each scan line.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="y">y</td><td class="desc">

The scanline's y&nbsp;coordinate.
</td></tr>
<tr><td class="val" id="count">count</td><td class="desc">

The number of spans to draw on this scanline.
</td></tr>
<tr><td class="val" id="spans">spans</td><td class="desc">

A table of &lsquo;count&rsquo; spans to draw on the scanline.
</td></tr>
<tr><td class="val" id="user">user</td><td class="desc">

User-supplied data that is passed to the callback.
</td></tr>
</table>

<h4>note</h4>

This callback allows client applications to directly render the gray spans of the anti-aliased bitmap to any kind of surfaces.

This can be used to write anti-aliased outlines directly to a given background bitmap, and even perform translucency.

<hr />

## FT_Raster_Params

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Raster_Params_
  {
    <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a>*        target;
    <span class="keyword">const</span> <span class="keyword">void</span>*             source;
    <span class="keyword">int</span>                     flags;
    <a href="../ft2-raster/#ft_spanfunc">FT_SpanFunc</a>             gray_spans;
    <a href="../ft2-raster/#ft_spanfunc">FT_SpanFunc</a>             black_spans;  /* unused */
    <a href="../ft2-raster/#ft_raster_bittest_func">FT_Raster_BitTest_Func</a>  bit_test;     /* unused */
    <a href="../ft2-raster/#ft_raster_bitset_func">FT_Raster_BitSet_Func</a>   bit_set;      /* unused */
    <span class="keyword">void</span>*                   user;
    <a href="../ft2-basic_types/#ft_bbox">FT_BBox</a>                 clip_box;

  } <b>FT_Raster_Params</b>;
</pre>


A structure to hold the arguments used by a raster's render function.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="target">target</td><td class="desc">

The target bitmap.
</td></tr>
<tr><td class="val" id="source">source</td><td class="desc">

A pointer to the source glyph image (e.g., an <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>).
</td></tr>
<tr><td class="val" id="flags">flags</td><td class="desc">

The rendering flags.
</td></tr>
<tr><td class="val" id="gray_spans">gray_spans</td><td class="desc">

The gray span drawing callback.
</td></tr>
<tr><td class="val" id="black_spans">black_spans</td><td class="desc">

Unused.
</td></tr>
<tr><td class="val" id="bit_test">bit_test</td><td class="desc">

Unused.
</td></tr>
<tr><td class="val" id="bit_set">bit_set</td><td class="desc">

Unused.
</td></tr>
<tr><td class="val" id="user">user</td><td class="desc">

User-supplied data that is passed to each drawing callback.
</td></tr>
<tr><td class="val" id="clip_box">clip_box</td><td class="desc">

An optional clipping box. It is only used in direct rendering mode. Note that coordinates here should be expressed in _integer_ pixels (and not in 26.6 fixed-point units).
</td></tr>
</table>

<h4>note</h4>

An anti-aliased glyph bitmap is drawn if the <a href="../ft2-raster/#ft_raster_flag_xxx">FT_RASTER_FLAG_AA</a> bit flag is set in the &lsquo;flags&rsquo; field, otherwise a monochrome bitmap is generated.

If the <a href="../ft2-raster/#ft_raster_flag_xxx">FT_RASTER_FLAG_DIRECT</a> bit flag is set in &lsquo;flags&rsquo;, the raster will call the &lsquo;gray_spans&rsquo; callback to draw gray pixel spans. This allows direct composition over a pre-existing bitmap through user-provided callbacks to perform the span drawing and composition. Not supported by the monochrome rasterizer.

<hr />

## FT_RASTER_FLAG_XXX

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
#define <a href="../ft2-raster/#ft_raster_flag_default">FT_RASTER_FLAG_DEFAULT</a>  0x0
#define <a href="../ft2-raster/#ft_raster_flag_aa">FT_RASTER_FLAG_AA</a>       0x1
#define <a href="../ft2-raster/#ft_raster_flag_direct">FT_RASTER_FLAG_DIRECT</a>   0x2
#define <a href="../ft2-raster/#ft_raster_flag_clip">FT_RASTER_FLAG_CLIP</a>     0x4

  /* these constants are deprecated; use the corresponding */
  /* `<b>FT_RASTER_FLAG_XXX</b>' values instead                   */
#define ft_raster_flag_default  <a href="../ft2-raster/#ft_raster_flag_default">FT_RASTER_FLAG_DEFAULT</a>
#define ft_raster_flag_aa       <a href="../ft2-raster/#ft_raster_flag_aa">FT_RASTER_FLAG_AA</a>
#define ft_raster_flag_direct   <a href="../ft2-raster/#ft_raster_flag_direct">FT_RASTER_FLAG_DIRECT</a>
#define ft_raster_flag_clip     <a href="../ft2-raster/#ft_raster_flag_clip">FT_RASTER_FLAG_CLIP</a>
</pre>


A list of bit flag constants as used in the &lsquo;flags&rsquo; field of a <a href="../ft2-raster/#ft_raster_params">FT_Raster_Params</a> structure.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_raster_flag_default">FT_RASTER_FLAG_DEFAULT</td><td class="desc">

This value is 0.
</td></tr>
<tr><td class="val" id="ft_raster_flag_aa">FT_RASTER_FLAG_AA</td><td class="desc">

This flag is set to indicate that an anti-aliased glyph image should be generated. Otherwise, it will be monochrome (1-bit).
</td></tr>
<tr><td class="val" id="ft_raster_flag_direct">FT_RASTER_FLAG_DIRECT</td><td class="desc">

This flag is set to indicate direct rendering. In this mode, client applications must provide their own span callback. This lets them directly draw or compose over an existing bitmap. If this bit is not set, the target pixmap's buffer _must_ be zeroed before rendering.

Direct rendering is only possible with anti-aliased glyphs.
</td></tr>
<tr><td class="val" id="ft_raster_flag_clip">FT_RASTER_FLAG_CLIP</td><td class="desc">

This flag is only used in direct rendering mode. If set, the output will be clipped to a box specified in the &lsquo;clip_box&rsquo; field of the <a href="../ft2-raster/#ft_raster_params">FT_Raster_Params</a> structure.

Note that by default, the glyph bitmap is clipped to the target pixmap, except in direct rendering mode where all spans are generated if no clipping box is set.
</td></tr>
</table>

<hr />

## FT_Raster_NewFunc

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">int</span>
  (*<b>FT_Raster_NewFunc</b>)( <span class="keyword">void</span>*       memory,
                        <a href="../ft2-raster/#ft_raster">FT_Raster</a>*  raster );

#define FT_Raster_New_Func  <b>FT_Raster_NewFunc</b>
</pre>


A function used to create a new raster object.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="memory">memory</td><td class="desc">

A handle to the memory allocator.
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="raster">raster</td><td class="desc">

A handle to the new raster object.
</td></tr>
</table>

<h4>return</h4>

Error code. 0&nbsp;means success.

<h4>note</h4>

The &lsquo;memory&rsquo; parameter is a typeless pointer in order to avoid un-wanted dependencies on the rest of the FreeType code. In practice, it is an <a href="../ft2-system_interface/#ft_memory">FT_Memory</a> object, i.e., a handle to the standard FreeType memory allocator. However, this field can be completely ignored by a given raster implementation.

<hr />

## FT_Raster_DoneFunc

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>
  (*<b>FT_Raster_DoneFunc</b>)( <a href="../ft2-raster/#ft_raster">FT_Raster</a>  raster );

#define FT_Raster_Done_Func  <b>FT_Raster_DoneFunc</b>
</pre>


A function used to destroy a given raster object.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="raster">raster</td><td class="desc">

A handle to the raster object.
</td></tr>
</table>

<hr />

## FT_Raster_ResetFunc

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>
  (*<b>FT_Raster_ResetFunc</b>)( <a href="../ft2-raster/#ft_raster">FT_Raster</a>       raster,
                          <span class="keyword">unsigned</span> <span class="keyword">char</span>*  pool_base,
                          <span class="keyword">unsigned</span> <span class="keyword">long</span>   pool_size );

#define FT_Raster_Reset_Func  <b>FT_Raster_ResetFunc</b>
</pre>


FreeType used to provide an area of memory called the &lsquo;render pool&rsquo; available to all registered rasterizers. This was not thread safe, however, and now FreeType never allocates this pool.

This function is called after a new raster object is created.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="raster">raster</td><td class="desc">

A handle to the new raster object.
</td></tr>
<tr><td class="val" id="pool_base">pool_base</td><td class="desc">

Previously, the address in memory of the render pool. Set this to NULL.
</td></tr>
<tr><td class="val" id="pool_size">pool_size</td><td class="desc">

Previously, the size in bytes of the render pool. Set this to 0.
</td></tr>
</table>

<h4>note</h4>

Rasterizers should rely on dynamic or stack allocation if they want to (a handle to the memory allocator is passed to the rasterizer constructor).

<hr />

## FT_Raster_SetModeFunc

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">int</span>
  (*<b>FT_Raster_SetModeFunc</b>)( <a href="../ft2-raster/#ft_raster">FT_Raster</a>      raster,
                            <span class="keyword">unsigned</span> <span class="keyword">long</span>  mode,
                            <span class="keyword">void</span>*          args );

#define FT_Raster_Set_Mode_Func  <b>FT_Raster_SetModeFunc</b>
</pre>


This function is a generic facility to change modes or attributes in a given raster. This can be used for debugging purposes, or simply to allow implementation-specific &lsquo;features&rsquo; in a given raster module.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="raster">raster</td><td class="desc">

A handle to the new raster object.
</td></tr>
<tr><td class="val" id="mode">mode</td><td class="desc">

A 4-byte tag used to name the mode or property.
</td></tr>
<tr><td class="val" id="args">args</td><td class="desc">

A pointer to the new mode/property to use.
</td></tr>
</table>

<hr />

## FT_Raster_RenderFunc

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">int</span>
  (*<b>FT_Raster_RenderFunc</b>)( <a href="../ft2-raster/#ft_raster">FT_Raster</a>                raster,
                           <span class="keyword">const</span> <a href="../ft2-raster/#ft_raster_params">FT_Raster_Params</a>*  params );

#define FT_Raster_Render_Func  <b>FT_Raster_RenderFunc</b>
</pre>


Invoke a given raster to scan-convert a given glyph image into a target bitmap.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="raster">raster</td><td class="desc">

A handle to the raster object.
</td></tr>
<tr><td class="val" id="params">params</td><td class="desc">

A pointer to an <a href="../ft2-raster/#ft_raster_params">FT_Raster_Params</a> structure used to store the rendering parameters.
</td></tr>
</table>

<h4>return</h4>

Error code. 0&nbsp;means success.

<h4>note</h4>

The exact format of the source image depends on the raster's glyph format defined in its <a href="../ft2-raster/#ft_raster_funcs">FT_Raster_Funcs</a> structure. It can be an <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a> or anything else in order to support a large array of glyph formats.

Note also that the render function can fail and return a &lsquo;FT_Err_Unimplemented_Feature&rsquo; error code if the raster used does not support direct composition.

XXX: For now, the standard raster doesn't support direct composition but this should change for the final release (see the files &lsquo;demos/src/ftgrays.c&rsquo; and &lsquo;demos/src/ftgrays2.c&rsquo; for examples of distinct implementations that support direct composition).

<hr />

## FT_Raster_Funcs

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Raster_Funcs_
  {
    <a href="../ft2-basic_types/#ft_glyph_format">FT_Glyph_Format</a>        glyph_format;

    <a href="../ft2-raster/#ft_raster_newfunc">FT_Raster_NewFunc</a>      raster_new;
    <a href="../ft2-raster/#ft_raster_resetfunc">FT_Raster_ResetFunc</a>    raster_reset;
    <a href="../ft2-raster/#ft_raster_setmodefunc">FT_Raster_SetModeFunc</a>  raster_set_mode;
    <a href="../ft2-raster/#ft_raster_renderfunc">FT_Raster_RenderFunc</a>   raster_render;
    <a href="../ft2-raster/#ft_raster_donefunc">FT_Raster_DoneFunc</a>     raster_done;

  } <b>FT_Raster_Funcs</b>;
</pre>


A structure used to describe a given raster class to the library.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="glyph_format">glyph_format</td><td class="desc">

The supported glyph format for this raster.
</td></tr>
<tr><td class="val" id="raster_new">raster_new</td><td class="desc">

The raster constructor.
</td></tr>
<tr><td class="val" id="raster_reset">raster_reset</td><td class="desc">

Used to reset the render pool within the raster.
</td></tr>
<tr><td class="val" id="raster_render">raster_render</td><td class="desc">

A function to render a glyph into a given bitmap.
</td></tr>
<tr><td class="val" id="raster_done">raster_done</td><td class="desc">

The raster destructor.
</td></tr>
</table>

<hr />

## FT_Raster_BitTest_Func

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">int</span>
  (*<b>FT_Raster_BitTest_Func</b>)( <span class="keyword">int</span>    y,
                             <span class="keyword">int</span>    x,
                             <span class="keyword">void</span>*  user );
</pre>


Deprecated, unimplemented.

<hr />

## FT_Raster_BitSet_Func

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>
  (*<b>FT_Raster_BitSet_Func</b>)( <span class="keyword">int</span>    y,
                            <span class="keyword">int</span>    x,
                            <span class="keyword">void</span>*  user );
</pre>


Deprecated, unimplemented.

<hr />

