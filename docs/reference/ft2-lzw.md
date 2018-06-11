[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; LZW Streams

-------------------------------

# LZW Streams

## Synopsis

This section contains the declaration of LZW-specific functions.

## FT_Stream_OpenLZW

Defined in FT_LZW_H (freetype/ftlzw.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Stream_OpenLZW</b>( <a href="../ft2-system_interface/#ft_stream">FT_Stream</a>  stream,
                     <a href="../ft2-system_interface/#ft_stream">FT_Stream</a>  source );
</pre>
</div>


Open a new stream to parse LZW-compressed font files. This is mainly used to support the compressed &lsquo;*.pcf.Z&rsquo; fonts that come with XFree86.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stream">stream</td><td class="desc">
<p>The target embedding stream.</p>
</td></tr>
<tr><td class="val" id="source">source</td><td class="desc">
<p>The source stream.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The source stream must be opened _before_ calling this function.

Calling the internal function &lsquo;FT_Stream_Close&rsquo; on the new stream will **not** call &lsquo;FT_Stream_Close&rsquo; on the source stream. None of the stream objects will be released to the heap.

The stream implementation is very basic and resets the decompression process each time seeking backwards is needed within the stream

In certain builds of the library, LZW compression recognition is automatically handled when calling <a href="../ft2-base_interface/#ft_new_face">FT_New_Face</a> or <a href="../ft2-base_interface/#ft_open_face">FT_Open_Face</a>. This means that if no font driver is capable of handling the raw compressed file, the library will try to open a LZW stream from it and re-open the face with it.

This function may return &lsquo;FT_Err_Unimplemented_Feature&rsquo; if your build of FreeType was not compiled with LZW support.

<hr>

