[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; System Interface

-------------------------------

# System Interface

## Synopsis

This section contains various definitions related to memory management and i/o access. You need to understand this information if you want to use a custom memory manager or you own i/o streams.

## FT_Memory

Defined in FT_SYSTEM_H (freetype/ftsystem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_MemoryRec_*  <b>FT_Memory</b>;
</pre>
</div>


A handle to a given memory manager object, defined with an <a href="../ft2-system_interface/#ft_memoryrec">FT_MemoryRec</a> structure.

<hr>

## FT_Alloc_Func

Defined in FT_SYSTEM_H (freetype/ftsystem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>*
  (*<b>FT_Alloc_Func</b>)( <a href="../ft2-system_interface/#ft_memory">FT_Memory</a>  memory,
                    <span class="keyword">long</span>       size );
</pre>
</div>


A function used to allocate &lsquo;size&rsquo; bytes from &lsquo;memory&rsquo;.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="memory">memory</td><td class="desc">
<p>A handle to the source memory manager.</p>
</td></tr>
<tr><td class="val" id="size">size</td><td class="desc">
<p>The size in bytes to allocate.</p>
</td></tr>
</table>

<h4>return</h4>

Address of new memory block. 0&nbsp;in case of failure.

<hr>

## FT_Free_Func

Defined in FT_SYSTEM_H (freetype/ftsystem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>
  (*<b>FT_Free_Func</b>)( <a href="../ft2-system_interface/#ft_memory">FT_Memory</a>  memory,
                   <span class="keyword">void</span>*      block );
</pre>
</div>


A function used to release a given block of memory.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="memory">memory</td><td class="desc">
<p>A handle to the source memory manager.</p>
</td></tr>
<tr><td class="val" id="block">block</td><td class="desc">
<p>The address of the target memory block.</p>
</td></tr>
</table>

<hr>

## FT_Realloc_Func

Defined in FT_SYSTEM_H (freetype/ftsystem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>*
  (*<b>FT_Realloc_Func</b>)( <a href="../ft2-system_interface/#ft_memory">FT_Memory</a>  memory,
                      <span class="keyword">long</span>       cur_size,
                      <span class="keyword">long</span>       new_size,
                      <span class="keyword">void</span>*      block );
</pre>
</div>


A function used to re-allocate a given block of memory.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="memory">memory</td><td class="desc">
<p>A handle to the source memory manager.</p>
</td></tr>
<tr><td class="val" id="cur_size">cur_size</td><td class="desc">
<p>The block's current size in bytes.</p>
</td></tr>
<tr><td class="val" id="new_size">new_size</td><td class="desc">
<p>The block's requested new size.</p>
</td></tr>
<tr><td class="val" id="block">block</td><td class="desc">
<p>The block's current address.</p>
</td></tr>
</table>

<h4>return</h4>

New block address. 0&nbsp;in case of memory shortage.

<h4>note</h4>

In case of error, the old block must still be available.

<hr>

## FT_MemoryRec

Defined in FT_SYSTEM_H (freetype/ftsystem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">struct</span>  FT_MemoryRec_
  {
    <span class="keyword">void</span>*            user;
    <a href="../ft2-system_interface/#ft_alloc_func">FT_Alloc_Func</a>    alloc;
    <a href="../ft2-system_interface/#ft_free_func">FT_Free_Func</a>     free;
    <a href="../ft2-system_interface/#ft_realloc_func">FT_Realloc_Func</a>  realloc;
  };
</pre>
</div>


A structure used to describe a given memory manager to FreeType&nbsp;2.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="user">user</td><td class="desc">
<p>A generic typeless pointer for user data.</p>
</td></tr>
<tr><td class="val" id="alloc">alloc</td><td class="desc">
<p>A pointer type to an allocation function.</p>
</td></tr>
<tr><td class="val" id="free">free</td><td class="desc">
<p>A pointer type to an memory freeing function.</p>
</td></tr>
<tr><td class="val" id="realloc">realloc</td><td class="desc">
<p>A pointer type to a reallocation function.</p>
</td></tr>
</table>

<hr>

## FT_Stream

Defined in FT_SYSTEM_H (freetype/ftsystem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_StreamRec_*  <b>FT_Stream</b>;
</pre>
</div>


A handle to an input stream.

<h4>also</h4>

See <a href="../ft2-system_interface/#ft_streamrec">FT_StreamRec</a> for the publicly accessible fields of a given stream object.

<hr>

## FT_StreamDesc

Defined in FT_SYSTEM_H (freetype/ftsystem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">union</span>  FT_StreamDesc_
  {
    <span class="keyword">long</span>   value;
    <span class="keyword">void</span>*  pointer;

  } <b>FT_StreamDesc</b>;
</pre>
</div>


A union type used to store either a long or a pointer. This is used to store a file descriptor or a &lsquo;FILE*&rsquo; in an input stream.

<hr>

## FT_Stream_IoFunc

Defined in FT_SYSTEM_H (freetype/ftsystem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">unsigned</span> <span class="keyword">long</span>
  (*<b>FT_Stream_IoFunc</b>)( <a href="../ft2-system_interface/#ft_stream">FT_Stream</a>       stream,
                       <span class="keyword">unsigned</span> <span class="keyword">long</span>   offset,
                       <span class="keyword">unsigned</span> <span class="keyword">char</span>*  buffer,
                       <span class="keyword">unsigned</span> <span class="keyword">long</span>   count );
</pre>
</div>


A function used to seek and read data from a given input stream.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stream">stream</td><td class="desc">
<p>A handle to the source stream.</p>
</td></tr>
<tr><td class="val" id="offset">offset</td><td class="desc">
<p>The offset of read in stream (always from start).</p>
</td></tr>
<tr><td class="val" id="buffer">buffer</td><td class="desc">
<p>The address of the read buffer.</p>
</td></tr>
<tr><td class="val" id="count">count</td><td class="desc">
<p>The number of bytes to read from the stream.</p>
</td></tr>
</table>

<h4>return</h4>

The number of bytes effectively read by the stream.

<h4>note</h4>

This function might be called to perform a seek or skip operation with a &lsquo;count&rsquo; of&nbsp;0. A non-zero return value then indicates an error.

<hr>

## FT_Stream_CloseFunc

Defined in FT_SYSTEM_H (freetype/ftsystem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>
  (*<b>FT_Stream_CloseFunc</b>)( <a href="../ft2-system_interface/#ft_stream">FT_Stream</a>  stream );
</pre>
</div>


A function used to close a given input stream.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="stream">stream</td><td class="desc">
<p>A handle to the target stream.</p>
</td></tr>
</table>

<hr>

## FT_StreamRec

Defined in FT_SYSTEM_H (freetype/ftsystem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_StreamRec_
  {
    <span class="keyword">unsigned</span> <span class="keyword">char</span>*       base;
    <span class="keyword">unsigned</span> <span class="keyword">long</span>        size;
    <span class="keyword">unsigned</span> <span class="keyword">long</span>        pos;

    <a href="../ft2-system_interface/#ft_streamdesc">FT_StreamDesc</a>        descriptor;
    <a href="../ft2-system_interface/#ft_streamdesc">FT_StreamDesc</a>        pathname;
    <a href="../ft2-system_interface/#ft_stream_iofunc">FT_Stream_IoFunc</a>     read;
    <a href="../ft2-system_interface/#ft_stream_closefunc">FT_Stream_CloseFunc</a>  close;

    <a href="../ft2-system_interface/#ft_memory">FT_Memory</a>            memory;
    <span class="keyword">unsigned</span> <span class="keyword">char</span>*       cursor;
    <span class="keyword">unsigned</span> <span class="keyword">char</span>*       limit;

  } <b>FT_StreamRec</b>;
</pre>
</div>


A structure used to describe an input stream.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="base">base</td><td class="desc">
<p>For memory-based streams, this is the address of the first stream byte in memory. This field should always be set to NULL for disk-based streams.</p>
</td></tr>
<tr><td class="val" id="size">size</td><td class="desc">
<p>The stream size in bytes.</p>
<p>In case of compressed streams where the size is unknown before actually doing the decompression, the value is set to 0x7FFFFFFF. (Note that this size value can occur for normal streams also; it is thus just a hint.)</p>
</td></tr>
<tr><td class="val" id="pos">pos</td><td class="desc">
<p>The current position within the stream.</p>
</td></tr>
<tr><td class="val" id="descriptor">descriptor</td><td class="desc">
<p>This field is a union that can hold an integer or a pointer. It is used by stream implementations to store file descriptors or &lsquo;FILE*&rsquo; pointers.</p>
</td></tr>
<tr><td class="val" id="pathname">pathname</td><td class="desc">
<p>This field is completely ignored by FreeType. However, it is often useful during debugging to use it to store the stream's filename (where available).</p>
</td></tr>
<tr><td class="val" id="read">read</td><td class="desc">
<p>The stream's input function.</p>
</td></tr>
<tr><td class="val" id="close">close</td><td class="desc">
<p>The stream's close function.</p>
</td></tr>
<tr><td class="val" id="memory">memory</td><td class="desc">
<p>The memory manager to use to preload frames. This is set internally by FreeType and shouldn't be touched by stream implementations.</p>
</td></tr>
<tr><td class="val" id="cursor">cursor</td><td class="desc">
<p>This field is set and used internally by FreeType when parsing frames.</p>
</td></tr>
<tr><td class="val" id="limit">limit</td><td class="desc">
<p>This field is set and used internally by FreeType when parsing frames.</p>
</td></tr>
</table>

<hr>

