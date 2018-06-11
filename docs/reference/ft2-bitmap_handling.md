[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; Bitmap Handling

-------------------------------

# Bitmap Handling

## Synopsis

This section contains functions for handling <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a> objects. Note that none of the functions changes the bitmap's &lsquo;flow&rsquo; (as indicated by the sign of the &lsquo;pitch&rsquo; field in &lsquo;FT_Bitmap&rsquo;).

## FT_Bitmap_Init

Defined in FT_BITMAP_H (freetype/ftbitmap.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Bitmap_Init</b>( <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a>  *abitmap );


  /* deprecated */
  FT_EXPORT( <span class="keyword">void</span> )
  FT_Bitmap_New( <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a>  *abitmap );
</pre>
</div>


Initialize a pointer to an <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a> structure.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="abitmap">abitmap</td><td class="desc">
<p>A pointer to the bitmap structure.</p>
</td></tr>
</table>

<h4>note</h4>

A deprecated name for the same function is &lsquo;FT_Bitmap_New&rsquo;.

<hr>

## FT_Bitmap_Copy

Defined in FT_BITMAP_H (freetype/ftbitmap.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Bitmap_Copy</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>        library,
                  <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a>  *source,
                  <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a>        *target );
</pre>
</div>


Copy a bitmap into another one.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to a library object.</p>
</td></tr>
<tr><td class="val" id="source">source</td><td class="desc">
<p>A handle to the source bitmap.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="target">target</td><td class="desc">
<p>A handle to the target bitmap.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FT_Bitmap_Embolden

Defined in FT_BITMAP_H (freetype/ftbitmap.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Bitmap_Embolden</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>  library,
                      <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a>*  bitmap,
                      <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>      xStrength,
                      <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>      yStrength );
</pre>
</div>


Embolden a bitmap. The new bitmap will be about &lsquo;xStrength&rsquo; pixels wider and &lsquo;yStrength&rsquo; pixels higher. The left and bottom borders are kept unchanged.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to a library object.</p>
</td></tr>
<tr><td class="val" id="xstrength">xStrength</td><td class="desc">
<p>How strong the glyph is emboldened horizontally. Expressed in 26.6 pixel format.</p>
</td></tr>
<tr><td class="val" id="ystrength">yStrength</td><td class="desc">
<p>How strong the glyph is emboldened vertically. Expressed in 26.6 pixel format.</p>
</td></tr>
</table>

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="bitmap">bitmap</td><td class="desc">
<p>A handle to the target bitmap.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The current implementation restricts &lsquo;xStrength&rsquo; to be less than or equal to&nbsp;8 if bitmap is of pixel_mode <a href="../ft2-basic_types/#ft_pixel_mode">FT_PIXEL_MODE_MONO</a>.

If you want to embolden the bitmap owned by a <a href="../ft2-base_interface/#ft_glyphslotrec">FT_GlyphSlotRec</a>, you should call <a href="../ft2-bitmap_handling/#ft_glyphslot_own_bitmap">FT_GlyphSlot_Own_Bitmap</a> on the slot first.

Bitmaps in <a href="../ft2-basic_types/#ft_pixel_mode">FT_PIXEL_MODE_GRAY2</a> and <a href="../ft2-basic_types/#ft_pixel_mode">FT_PIXEL_MODE_GRAY</a>@ format are converted to <a href="../ft2-basic_types/#ft_pixel_mode">FT_PIXEL_MODE_GRAY</a> format (i.e., 8bpp).

<hr>

## FT_Bitmap_Convert

Defined in FT_BITMAP_H (freetype/ftbitmap.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Bitmap_Convert</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>        library,
                     <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a>  *source,
                     <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a>        *target,
                     <a href="../ft2-basic_types/#ft_int">FT_Int</a>            alignment );
</pre>
</div>


Convert a bitmap object with depth 1bpp, 2bpp, 4bpp, 8bpp or 32bpp to a bitmap object with depth 8bpp, making the number of used bytes per line (a.k.a. the &lsquo;pitch&rsquo;) a multiple of &lsquo;alignment&rsquo;.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to a library object.</p>
</td></tr>
<tr><td class="val" id="source">source</td><td class="desc">
<p>The source bitmap.</p>
</td></tr>
<tr><td class="val" id="alignment">alignment</td><td class="desc">
<p>The pitch of the bitmap is a multiple of this argument. Common values are 1, 2, or 4.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="target">target</td><td class="desc">
<p>The target bitmap.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

It is possible to call <a href="../ft2-bitmap_handling/#ft_bitmap_convert">FT_Bitmap_Convert</a> multiple times without calling <a href="../ft2-bitmap_handling/#ft_bitmap_done">FT_Bitmap_Done</a> (the memory is simply reallocated).

Use <a href="../ft2-bitmap_handling/#ft_bitmap_done">FT_Bitmap_Done</a> to finally remove the bitmap object.

The &lsquo;library&rsquo; argument is taken to have access to FreeType's memory handling functions.

<hr>

## FT_GlyphSlot_Own_Bitmap

Defined in FT_BITMAP_H (freetype/ftbitmap.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_GlyphSlot_Own_Bitmap</b>( <a href="../ft2-base_interface/#ft_glyphslot">FT_GlyphSlot</a>  slot );
</pre>
</div>


Make sure that a glyph slot owns &lsquo;slot-&gt;bitmap&rsquo;.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="slot">slot</td><td class="desc">
<p>The glyph slot.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function is to be used in combination with <a href="../ft2-bitmap_handling/#ft_bitmap_embolden">FT_Bitmap_Embolden</a>.

<hr>

## FT_Bitmap_Done

Defined in FT_BITMAP_H (freetype/ftbitmap.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Bitmap_Done</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>  library,
                  <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a>  *bitmap );
</pre>
</div>


Destroy a bitmap object initialized with <a href="../ft2-bitmap_handling/#ft_bitmap_init">FT_Bitmap_Init</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to a library object.</p>
</td></tr>
<tr><td class="val" id="bitmap">bitmap</td><td class="desc">
<p>The bitmap object to be freed.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The &lsquo;library&rsquo; argument is taken to have access to FreeType's memory handling functions.

<hr>

