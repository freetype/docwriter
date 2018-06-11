[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; GZIP Streams

-------------------------------

# GZIP Streams

## Synopsis

This section contains the declaration of Gzip-specific functions.

## FT_Stream_OpenGzip

Defined in FT_GZIP_H (freetype/ftgzip.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Stream_OpenGzip</b>( <a href="../ft2-system_interface/#ft_stream">FT_Stream</a>  stream,
                      <a href="../ft2-system_interface/#ft_stream">FT_Stream</a>  source );
</pre>
</div>


Open a new stream to parse gzip-compressed font files. This is mainly used to support the compressed &lsquo;*.pcf.gz&rsquo; fonts that come with XFree86.

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

The stream implementation is very basic and resets the decompression process each time seeking backwards is needed within the stream.

In certain builds of the library, gzip compression recognition is automatically handled when calling <a href="../ft2-base_interface/#ft_new_face">FT_New_Face</a> or <a href="../ft2-base_interface/#ft_open_face">FT_Open_Face</a>. This means that if no font driver is capable of handling the raw compressed file, the library will try to open a gzipped stream from it and re-open the face with it.

This function may return &lsquo;FT_Err_Unimplemented_Feature&rsquo; if your build of FreeType was not compiled with zlib support.

<hr>

## FT_Gzip_Uncompress

Defined in FT_GZIP_H (freetype/ftgzip.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Gzip_Uncompress</b>( <a href="../ft2-system_interface/#ft_memory">FT_Memory</a>       memory,
                      <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>*        output,
                      <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>*       output_len,
                      <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>*  input,
                      <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>        input_len );
</pre>
</div>


Decompress a zipped input buffer into an output buffer. This function is modeled after zlib's &lsquo;uncompress&rsquo; function.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="memory">memory</td><td class="desc">
<p>A FreeType memory handle.</p>
</td></tr>
<tr><td class="val" id="input">input</td><td class="desc">
<p>The input buffer.</p>
</td></tr>
<tr><td class="val" id="input_len">input_len</td><td class="desc">
<p>The length of the input buffer.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="output">output</td><td class="desc">
<p>The output buffer.</p>
</td></tr>
</table>

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="output_len">output_len</td><td class="desc">
<p>Before calling the function, this is the total size of the output buffer, which must be large enough to hold the entire uncompressed data (so the size of the uncompressed data must be known in advance). After calling the function, &lsquo;output_len&rsquo; is the size of the used data in &lsquo;output&rsquo;.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function may return &lsquo;FT_Err_Unimplemented_Feature&rsquo; if your build of FreeType was not compiled with zlib support.

<h4>since</h4>

2.5.1

<hr>

