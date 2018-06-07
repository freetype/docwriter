[Docs](ft2-index.md) &raquo; [Core API](ft2-toc.md#core-api) &raquo; Basic Data Types

-------------------------------


# Basic Data Types

## Synopsis

This section contains the basic data types defined by FreeType&nbsp;2, ranging from simple scalar types to bitmap descriptors. More font-specific structures are defined in a different section.

## FT_Byte

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">unsigned</span> <span class="keyword">char</span>  <b>FT_Byte</b>;
</pre>


A simple typedef for the _unsigned_ char type.

<hr />

## FT_Bytes

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>*  <b>FT_Bytes</b>;
</pre>


A typedef for constant memory areas.

<hr />

## FT_Char

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> <span class="keyword">char</span>  <b>FT_Char</b>;
</pre>


A simple typedef for the _signed_ char type.

<hr />

## FT_Int

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> <span class="keyword">int</span>  <b>FT_Int</b>;
</pre>


A typedef for the int type.

<hr />

## FT_UInt

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">unsigned</span> <span class="keyword">int</span>  <b>FT_UInt</b>;
</pre>


A typedef for the unsigned int type.

<hr />

## FT_Int16

Defined in FT_CONFIG_CONFIG_H (freetype/config/ftconfig.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> <span class="keyword">short</span>  <b>FT_Int16</b>;
</pre>


A typedef for a 16bit signed integer type.

<hr />

## FT_UInt16

Defined in FT_CONFIG_CONFIG_H (freetype/config/ftconfig.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">unsigned</span> <span class="keyword">short</span>  <b>FT_UInt16</b>;
</pre>


A typedef for a 16bit unsigned integer type.

<hr />

## FT_Int32

Defined in FT_CONFIG_CONFIG_H (freetype/config/ftconfig.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> XXX  <b>FT_Int32</b>;
</pre>


A typedef for a 32bit signed integer type. The size depends on the configuration.

<hr />

## FT_UInt32

Defined in FT_CONFIG_CONFIG_H (freetype/config/ftconfig.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">unsigned</span> XXX  <b>FT_UInt32</b>;
</pre>
<hr />

## FT_Int64

Defined in FT_CONFIG_CONFIG_H (freetype/config/ftconfig.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> XXX  <b>FT_Int64</b>;
</pre>
<hr />

## FT_UInt64

Defined in FT_CONFIG_CONFIG_H (freetype/config/ftconfig.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">unsigned</span> XXX  <b>FT_UInt64</b>;
</pre>
<hr />

## FT_Short

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> <span class="keyword">short</span>  <b>FT_Short</b>;
</pre>


A typedef for signed short.

<hr />

## FT_UShort

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">unsigned</span> <span class="keyword">short</span>  <b>FT_UShort</b>;
</pre>


A typedef for unsigned short.

<hr />

## FT_Long

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> <span class="keyword">long</span>  <b>FT_Long</b>;
</pre>


A typedef for signed long.

<hr />

## FT_ULong

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">unsigned</span> <span class="keyword">long</span>  <b>FT_ULong</b>;
</pre>


A typedef for unsigned long.

<hr />

## FT_Bool

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">unsigned</span> <span class="keyword">char</span>  <b>FT_Bool</b>;
</pre>


A typedef of unsigned char, used for simple booleans. As usual, values 1 and&nbsp;0 represent true and false, respectively.

<hr />

## FT_Offset

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> size_t  <b>FT_Offset</b>;
</pre>


This is equivalent to the ANSI&nbsp;C &lsquo;size_t&rsquo; type, i.e., the largest _unsigned_ integer type used to express a file size or position, or a memory block size.

<hr />

## FT_PtrDist

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> ft_ptrdiff_t  <b>FT_PtrDist</b>;
</pre>


This is equivalent to the ANSI&nbsp;C &lsquo;ptrdiff_t&rsquo; type, i.e., the largest _signed_ integer type used to express the distance between two pointers.

<hr />

## FT_String

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">char</span>  <b>FT_String</b>;
</pre>


A simple typedef for the char type, usually used for strings.

<hr />

## FT_Tag

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <a href="../ft2-basic_types/#ft_uint32">FT_UInt32</a>  <b>FT_Tag</b>;
</pre>


A typedef for 32-bit tags (as used in the SFNT format).

<hr />

## FT_Error

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">int</span>  <b>FT_Error</b>;
</pre>


The FreeType error code type. A value of&nbsp;0 is always interpreted as a successful operation.

<hr />

## FT_Fixed

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> <span class="keyword">long</span>  <b>FT_Fixed</b>;
</pre>


This type is used to store 16.16 fixed-point values, like scaling values or matrix coefficients.

<hr />

## FT_Pointer

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>*  <b>FT_Pointer</b>;
</pre>


A simple typedef for a typeless pointer.

<hr />

## FT_Pos

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> <span class="keyword">long</span>  <b>FT_Pos</b>;
</pre>


The type FT_Pos is used to store vectorial coordinates. Depending on the context, these can represent distances in integer font units, or 16.16, or 26.6 fixed-point pixel coordinates.

<hr />

## FT_Vector

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Vector_
  {
    <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>  x;
    <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>  y;

  } <b>FT_Vector</b>;
</pre>


A simple structure used to store a 2D vector; coordinates are of the FT_Pos type.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="x">x</td><td class="desc">

The horizontal coordinate.
</td></tr>
<tr><td class="val" id="y">y</td><td class="desc">

The vertical coordinate.
</td></tr>
</table>

<hr />

## FT_BBox

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_BBox_
  {
    <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>  xMin, yMin;
    <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>  xMax, yMax;

  } <b>FT_BBox</b>;
</pre>


A structure used to hold an outline's bounding box, i.e., the coordinates of its extrema in the horizontal and vertical directions.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="xmin">xMin</td><td class="desc">

The horizontal minimum (left-most).
</td></tr>
<tr><td class="val" id="ymin">yMin</td><td class="desc">

The vertical minimum (bottom-most).
</td></tr>
<tr><td class="val" id="xmax">xMax</td><td class="desc">

The horizontal maximum (right-most).
</td></tr>
<tr><td class="val" id="ymax">yMax</td><td class="desc">

The vertical maximum (top-most).
</td></tr>
</table>

<h4>note</h4>

The bounding box is specified with the coordinates of the lower left and the upper right corner. In PostScript, those values are often called (llx,lly) and (urx,ury), respectively.

If &lsquo;yMin&rsquo; is negative, this value gives the glyph's descender. Otherwise, the glyph doesn't descend below the baseline. Similarly, if &lsquo;ymax&rsquo; is positive, this value gives the glyph's ascender.

&lsquo;xMin&rsquo; gives the horizontal distance from the glyph's origin to the left edge of the glyph's bounding box. If &lsquo;xMin&rsquo; is negative, the glyph extends to the left of the origin.

<hr />

## FT_Matrix

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Matrix_
  {
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  xx, xy;
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  yx, yy;

  } <b>FT_Matrix</b>;
</pre>


A simple structure used to store a 2x2 matrix. Coefficients are in 16.16 fixed-point format. The computation performed is:
```
   x' = x*xx + y*xy
   y' = x*yx + y*yy
```

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="xx">xx</td><td class="desc">

Matrix coefficient.
</td></tr>
<tr><td class="val" id="xy">xy</td><td class="desc">

Matrix coefficient.
</td></tr>
<tr><td class="val" id="yx">yx</td><td class="desc">

Matrix coefficient.
</td></tr>
<tr><td class="val" id="yy">yy</td><td class="desc">

Matrix coefficient.
</td></tr>
</table>

<hr />

## FT_FWord

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> <span class="keyword">short</span>  <b>FT_FWord</b>;   /* distance in FUnits */
</pre>


A signed 16-bit integer used to store a distance in original font units.

<hr />

## FT_UFWord

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">unsigned</span> <span class="keyword">short</span>  <b>FT_UFWord</b>;  /* <span class="keyword">unsigned</span> distance */
</pre>


An unsigned 16-bit integer used to store a distance in original font units.

<hr />

## FT_F2Dot14

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> <span class="keyword">short</span>  <b>FT_F2Dot14</b>;
</pre>


A signed 2.14 fixed-point type used for unit vectors.

<hr />

## FT_UnitVector

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_UnitVector_
  {
    <a href="../ft2-basic_types/#ft_f2dot14">FT_F2Dot14</a>  x;
    <a href="../ft2-basic_types/#ft_f2dot14">FT_F2Dot14</a>  y;

  } <b>FT_UnitVector</b>;
</pre>


A simple structure used to store a 2D vector unit vector. Uses FT_F2Dot14 types.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="x">x</td><td class="desc">

Horizontal coordinate.
</td></tr>
<tr><td class="val" id="y">y</td><td class="desc">

Vertical coordinate.
</td></tr>
</table>

<hr />

## FT_F26Dot6

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">signed</span> <span class="keyword">long</span>  <b>FT_F26Dot6</b>;
</pre>


A signed 26.6 fixed-point type used for vectorial pixel coordinates.

<hr />

## FT_Data

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Data_
  {
    <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>*  pointer;
    <a href="../ft2-basic_types/#ft_int">FT_Int</a>          length;

  } <b>FT_Data</b>;
</pre>


Read-only binary data represented as a pointer and a length.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="pointer">pointer</td><td class="desc">

The data.
</td></tr>
<tr><td class="val" id="length">length</td><td class="desc">

The length of the data in bytes.
</td></tr>
</table>

<hr />

## FT_MAKE_TAG

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
#define <b>FT_MAKE_TAG</b>( _x1, _x2, _x3, _x4 ) \
          (<a href="../ft2-basic_types/#ft_tag">FT_Tag</a>)                        \
          ( ( (<a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>)_x1 &lt;&lt; 24 ) |     \
            ( (<a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>)_x2 &lt;&lt; 16 ) |     \
            ( (<a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>)_x3 &lt;&lt;  8 ) |     \
              (<a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>)_x4         )
</pre>


This macro converts four-letter tags that are used to label TrueType tables into an unsigned long, to be used within FreeType.

<h4>note</h4>

The produced values *must* be 32-bit integers. Don't redefine this macro.

<hr />

## FT_Generic

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Generic_
  {
    <span class="keyword">void</span>*                 data;
    <a href="../ft2-basic_types/#ft_generic_finalizer">FT_Generic_Finalizer</a>  finalizer;

  } <b>FT_Generic</b>;
</pre>


Client applications often need to associate their own data to a variety of FreeType core objects. For example, a text layout API might want to associate a glyph cache to a given size object.

Some FreeType object contains a &lsquo;generic&rsquo; field, of type FT_Generic, which usage is left to client applications and font servers.

It can be used to store a pointer to client-specific data, as well as the address of a &lsquo;finalizer&rsquo; function, which will be called by FreeType when the object is destroyed (for example, the previous client example would put the address of the glyph cache destructor in the &lsquo;finalizer&rsquo; field).

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="data">data</td><td class="desc">

A typeless pointer to any client-specified data. This field is completely ignored by the FreeType library.
</td></tr>
<tr><td class="val" id="finalizer">finalizer</td><td class="desc">

A pointer to a &lsquo;generic finalizer&rsquo; function, which will be called when the object is destroyed. If this field is set to NULL, no code will be called.
</td></tr>
</table>

<hr />

## FT_Generic_Finalizer

Defined in FT_TYPES_H (freetype/fttypes.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>  (*<b>FT_Generic_Finalizer</b>)( <span class="keyword">void</span>*  object );
</pre>


Describe a function used to destroy the &lsquo;client&rsquo; data of any FreeType object. See the description of the <a href="../ft2-basic_types/#ft_generic">FT_Generic</a> type for details of usage.

<h4>input</h4>

The address of the FreeType object that is under finalization. Its client data is accessed through its &lsquo;generic&rsquo; field.

<hr />

## FT_Bitmap

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Bitmap_
  {
    <span class="keyword">unsigned</span> <span class="keyword">int</span>    rows;
    <span class="keyword">unsigned</span> <span class="keyword">int</span>    width;
    <span class="keyword">int</span>             pitch;
    <span class="keyword">unsigned</span> <span class="keyword">char</span>*  buffer;
    <span class="keyword">unsigned</span> <span class="keyword">short</span>  num_grays;
    <span class="keyword">unsigned</span> <span class="keyword">char</span>   pixel_mode;
    <span class="keyword">unsigned</span> <span class="keyword">char</span>   palette_mode;
    <span class="keyword">void</span>*           palette;

  } <b>FT_Bitmap</b>;
</pre>


A structure used to describe a bitmap or pixmap to the raster. Note that we now manage pixmaps of various depths through the &lsquo;pixel_mode&rsquo; field.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="rows">rows</td><td class="desc">

The number of bitmap rows.
</td></tr>
<tr><td class="val" id="width">width</td><td class="desc">

The number of pixels in bitmap row.
</td></tr>
<tr><td class="val" id="pitch">pitch</td><td class="desc">

The pitch's absolute value is the number of bytes taken by one bitmap row, including padding. However, the pitch is positive when the bitmap has a &lsquo;down&rsquo; flow, and negative when it has an &lsquo;up&rsquo; flow. In all cases, the pitch is an offset to add to a bitmap pointer in order to go down one row.

Note that &lsquo;padding&rsquo; means the alignment of a bitmap to a byte border, and FreeType functions normally align to the smallest possible integer value.

For the B/W rasterizer, &lsquo;pitch&rsquo; is always an even number.

To change the pitch of a bitmap (say, to make it a multiple of 4), use <a href="../ft2-bitmap_handling/#ft_bitmap_convert">FT_Bitmap_Convert</a>. Alternatively, you might use callback functions to directly render to the application's surface; see the file &lsquo;example2.cpp&rsquo; in the tutorial for a demonstration.
</td></tr>
<tr><td class="val" id="buffer">buffer</td><td class="desc">

A typeless pointer to the bitmap buffer. This value should be aligned on 32-bit boundaries in most cases.
</td></tr>
<tr><td class="val" id="num_grays">num_grays</td><td class="desc">

This field is only used with <a href="../ft2-basic_types/#ft_pixel_mode">FT_PIXEL_MODE_GRAY</a>; it gives the number of gray levels used in the bitmap.
</td></tr>
<tr><td class="val" id="pixel_mode">pixel_mode</td><td class="desc">

The pixel mode, i.e., how pixel bits are stored. See <a href="../ft2-basic_types/#ft_pixel_mode">FT_Pixel_Mode</a> for possible values.
</td></tr>
<tr><td class="val" id="palette_mode">palette_mode</td><td class="desc">

This field is intended for paletted pixel modes; it indicates how the palette is stored. Not used currently.
</td></tr>
<tr><td class="val" id="palette">palette</td><td class="desc">

A typeless pointer to the bitmap palette; this field is intended for paletted pixel modes. Not used currently.
</td></tr>
</table>

<hr />

## FT_Pixel_Mode

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  FT_Pixel_Mode_
  {
    <a href="../ft2-basic_types/#ft_pixel_mode_none">FT_PIXEL_MODE_NONE</a> = 0,
    <a href="../ft2-basic_types/#ft_pixel_mode_mono">FT_PIXEL_MODE_MONO</a>,
    <a href="../ft2-basic_types/#ft_pixel_mode_gray">FT_PIXEL_MODE_GRAY</a>,
    <a href="../ft2-basic_types/#ft_pixel_mode_gray2">FT_PIXEL_MODE_GRAY2</a>,
    <a href="../ft2-basic_types/#ft_pixel_mode_gray4">FT_PIXEL_MODE_GRAY4</a>,
    <a href="../ft2-basic_types/#ft_pixel_mode_lcd">FT_PIXEL_MODE_LCD</a>,
    <a href="../ft2-basic_types/#ft_pixel_mode_lcd_v">FT_PIXEL_MODE_LCD_V</a>,
    <a href="../ft2-basic_types/#ft_pixel_mode_bgra">FT_PIXEL_MODE_BGRA</a>,

    FT_PIXEL_MODE_MAX      /* do not remove */

  } <b>FT_Pixel_Mode</b>;


  /* these constants are deprecated; use the corresponding `<b>FT_Pixel_Mode</b>' */
  /* values instead.                                                       */
#define ft_pixel_mode_none   <a href="../ft2-basic_types/#ft_pixel_mode_none">FT_PIXEL_MODE_NONE</a>
#define ft_pixel_mode_mono   <a href="../ft2-basic_types/#ft_pixel_mode_mono">FT_PIXEL_MODE_MONO</a>
#define ft_pixel_mode_grays  <a href="../ft2-basic_types/#ft_pixel_mode_gray">FT_PIXEL_MODE_GRAY</a>
#define ft_pixel_mode_pal2   <a href="../ft2-basic_types/#ft_pixel_mode_gray2">FT_PIXEL_MODE_GRAY2</a>
#define ft_pixel_mode_pal4   <a href="../ft2-basic_types/#ft_pixel_mode_gray4">FT_PIXEL_MODE_GRAY4</a>
</pre>


An enumeration type used to describe the format of pixels in a given bitmap. Note that additional formats may be added in the future.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_pixel_mode_none">FT_PIXEL_MODE_NONE</td><td class="desc">

Value&nbsp;0 is reserved.
</td></tr>
<tr><td class="val" id="ft_pixel_mode_mono">FT_PIXEL_MODE_MONO</td><td class="desc">

A monochrome bitmap, using 1&nbsp;bit per pixel. Note that pixels are stored in most-significant order (MSB), which means that the left-most pixel in a byte has value 128.
</td></tr>
<tr><td class="val" id="ft_pixel_mode_gray">FT_PIXEL_MODE_GRAY</td><td class="desc">

An 8-bit bitmap, generally used to represent anti-aliased glyph images. Each pixel is stored in one byte. Note that the number of &lsquo;gray&rsquo; levels is stored in the &lsquo;num_grays&rsquo; field of the <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a> structure (it generally is 256).
</td></tr>
<tr><td class="val" id="ft_pixel_mode_gray2">FT_PIXEL_MODE_GRAY2</td><td class="desc">

A 2-bit per pixel bitmap, used to represent embedded anti-aliased bitmaps in font files according to the OpenType specification. We haven't found a single font using this format, however.
</td></tr>
<tr><td class="val" id="ft_pixel_mode_gray4">FT_PIXEL_MODE_GRAY4</td><td class="desc">

A 4-bit per pixel bitmap, representing embedded anti-aliased bitmaps in font files according to the OpenType specification. We haven't found a single font using this format, however.
</td></tr>
<tr><td class="val" id="ft_pixel_mode_lcd">FT_PIXEL_MODE_LCD</td><td class="desc">

An 8-bit bitmap, representing RGB or BGR decimated glyph images used for display on LCD displays; the bitmap is three times wider than the original glyph image. See also <a href="../ft2-base_interface/#ft_render_mode">FT_RENDER_MODE_LCD</a>.
</td></tr>
<tr><td class="val" id="ft_pixel_mode_lcd_v">FT_PIXEL_MODE_LCD_V</td><td class="desc">

An 8-bit bitmap, representing RGB or BGR decimated glyph images used for display on rotated LCD displays; the bitmap is three times taller than the original glyph image. See also <a href="../ft2-base_interface/#ft_render_mode">FT_RENDER_MODE_LCD_V</a>.
</td></tr>
<tr><td class="val" id="ft_pixel_mode_bgra">FT_PIXEL_MODE_BGRA</td><td class="desc">

[Since 2.5] An image with four 8-bit channels per pixel, representing a color image (such as emoticons) with alpha channel. For each pixel, the format is BGRA, which means, the blue channel comes first in memory. The color channels are pre-multiplied and in the sRGB colorspace. For example, full red at half-translucent opacity will be represented as &lsquo;00,00,80,80&rsquo;, not &lsquo;00,00,FF,80&rsquo;. See also <a href="../ft2-base_interface/#ft_load_xxx">FT_LOAD_COLOR</a>.
</td></tr>
</table>

<hr />

## FT_Glyph_Format

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  FT_Glyph_Format_
  {
    <a href="../ft2-basic_types/#ft_image_tag">FT_IMAGE_TAG</a>( <a href="../ft2-basic_types/#ft_glyph_format_none">FT_GLYPH_FORMAT_NONE</a>, 0, 0, 0, 0 ),

    <a href="../ft2-basic_types/#ft_image_tag">FT_IMAGE_TAG</a>( <a href="../ft2-basic_types/#ft_glyph_format_composite">FT_GLYPH_FORMAT_COMPOSITE</a>, 'c', 'o', 'm', 'p' ),
    <a href="../ft2-basic_types/#ft_image_tag">FT_IMAGE_TAG</a>( <a href="../ft2-basic_types/#ft_glyph_format_bitmap">FT_GLYPH_FORMAT_BITMAP</a>,    'b', 'i', 't', 's' ),
    <a href="../ft2-basic_types/#ft_image_tag">FT_IMAGE_TAG</a>( <a href="../ft2-basic_types/#ft_glyph_format_outline">FT_GLYPH_FORMAT_OUTLINE</a>,   'o', 'u', 't', 'l' ),
    <a href="../ft2-basic_types/#ft_image_tag">FT_IMAGE_TAG</a>( <a href="../ft2-basic_types/#ft_glyph_format_plotter">FT_GLYPH_FORMAT_PLOTTER</a>,   'p', 'l', 'o', 't' )

  } <b>FT_Glyph_Format</b>;


  /* these constants are deprecated; use the corresponding */
  /* `<b>FT_Glyph_Format</b>' values instead.                     */
#define ft_glyph_format_none       <a href="../ft2-basic_types/#ft_glyph_format_none">FT_GLYPH_FORMAT_NONE</a>
#define ft_glyph_format_composite  <a href="../ft2-basic_types/#ft_glyph_format_composite">FT_GLYPH_FORMAT_COMPOSITE</a>
#define ft_glyph_format_bitmap     <a href="../ft2-basic_types/#ft_glyph_format_bitmap">FT_GLYPH_FORMAT_BITMAP</a>
#define ft_glyph_format_outline    <a href="../ft2-basic_types/#ft_glyph_format_outline">FT_GLYPH_FORMAT_OUTLINE</a>
#define ft_glyph_format_plotter    <a href="../ft2-basic_types/#ft_glyph_format_plotter">FT_GLYPH_FORMAT_PLOTTER</a>
</pre>


An enumeration type used to describe the format of a given glyph image. Note that this version of FreeType only supports two image formats, even though future font drivers will be able to register their own format.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_glyph_format_none">FT_GLYPH_FORMAT_NONE</td><td class="desc">

The value&nbsp;0 is reserved.
</td></tr>
<tr><td class="val" id="ft_glyph_format_composite">FT_GLYPH_FORMAT_COMPOSITE</td><td class="desc">

The glyph image is a composite of several other images. This format is _only_ used with <a href="../ft2-base_interface/#ft_load_xxx">FT_LOAD_NO_RECURSE</a>, and is used to report compound glyphs (like accented characters).
</td></tr>
<tr><td class="val" id="ft_glyph_format_bitmap">FT_GLYPH_FORMAT_BITMAP</td><td class="desc">

The glyph image is a bitmap, and can be described as an <a href="../ft2-basic_types/#ft_bitmap">FT_Bitmap</a>. You generally need to access the &lsquo;bitmap&rsquo; field of the <a href="../ft2-base_interface/#ft_glyphslotrec">FT_GlyphSlotRec</a> structure to read it.
</td></tr>
<tr><td class="val" id="ft_glyph_format_outline">FT_GLYPH_FORMAT_OUTLINE</td><td class="desc">

The glyph image is a vectorial outline made of line segments and Bezier arcs; it can be described as an <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>; you generally want to access the &lsquo;outline&rsquo; field of the <a href="../ft2-base_interface/#ft_glyphslotrec">FT_GlyphSlotRec</a> structure to read it.
</td></tr>
<tr><td class="val" id="ft_glyph_format_plotter">FT_GLYPH_FORMAT_PLOTTER</td><td class="desc">

The glyph image is a vectorial path with no inside and outside contours. Some Type&nbsp;1 fonts, like those in the Hershey family, contain glyphs in this format. These are described as <a href="../ft2-outline_processing/#ft_outline">FT_Outline</a>, but FreeType isn't currently capable of rendering them correctly.
</td></tr>
</table>

<hr />

## FT_IMAGE_TAG

Defined in FT_IMAGE_H (freetype/ftimage.h).

<pre>
#ifndef <b>FT_IMAGE_TAG</b>
#define <b>FT_IMAGE_TAG</b>( value, _x1, _x2, _x3, _x4 )  \
          value = ( ( (<span class="keyword">unsigned</span> <span class="keyword">long</span>)_x1 &lt;&lt; 24 ) | \
                    ( (<span class="keyword">unsigned</span> <span class="keyword">long</span>)_x2 &lt;&lt; 16 ) | \
                    ( (<span class="keyword">unsigned</span> <span class="keyword">long</span>)_x3 &lt;&lt; 8  ) | \
                      (<span class="keyword">unsigned</span> <span class="keyword">long</span>)_x4         )
#endif /* <b>FT_IMAGE_TAG</b> */
</pre>


This macro converts four-letter tags to an unsigned long type.

<h4>note</h4>

Since many 16-bit compilers don't like 32-bit enumerations, you should redefine this macro in case of problems to something like this:
```
  #define FT_IMAGE_TAG( value, _x1, _x2, _x3, _x4 )  value
```

to get a simple enumeration without assigning special numbers.

<hr />

