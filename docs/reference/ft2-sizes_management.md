[Docs](ft2-index.md) &raquo; [Core API](ft2-toc.md#core-api) &raquo; Size Management

-------------------------------


# Size Management

## Synopsis

When creating a new face object (e.g., with <a href="../ft2-base_interface/#ft_new_face">FT_New_Face</a>), an <a href="../ft2-base_interface/#ft_size">FT_Size</a> object is automatically created and used to store all pixel-size dependent information, available in the &lsquo;face-&gt;size&rsquo; field.

It is however possible to create more sizes for a given face, mostly in order to manage several character pixel sizes of the same font family and style. See <a href="../ft2-sizes_management/#ft_new_size">FT_New_Size</a> and <a href="../ft2-sizes_management/#ft_done_size">FT_Done_Size</a>.

Note that <a href="../ft2-base_interface/#ft_set_pixel_sizes">FT_Set_Pixel_Sizes</a> and <a href="../ft2-base_interface/#ft_set_char_size">FT_Set_Char_Size</a> only modify the contents of the current &lsquo;active&rsquo; size; you thus need to use <a href="../ft2-sizes_management/#ft_activate_size">FT_Activate_Size</a> to change it.

99% of applications won't need the functions provided here, especially if they use the caching sub-system, so be cautious when using these.

## FT_New_Size

Defined in FT_SIZES_H (freetype/ftsizes.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_New_Size</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
               <a href="../ft2-base_interface/#ft_size">FT_Size</a>*  size );
</pre>


Create a new size object from a given face object.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

A handle to a parent face object.
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="asize">asize</td><td class="desc">

A handle to a new size object.
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

You need to call <a href="../ft2-sizes_management/#ft_activate_size">FT_Activate_Size</a> in order to select the new size for upcoming calls to <a href="../ft2-base_interface/#ft_set_pixel_sizes">FT_Set_Pixel_Sizes</a>, <a href="../ft2-base_interface/#ft_set_char_size">FT_Set_Char_Size</a>, <a href="../ft2-base_interface/#ft_load_glyph">FT_Load_Glyph</a>, <a href="../ft2-base_interface/#ft_load_char">FT_Load_Char</a>, etc.

<hr />

## FT_Done_Size

Defined in FT_SIZES_H (freetype/ftsizes.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Done_Size</b>( <a href="../ft2-base_interface/#ft_size">FT_Size</a>  size );
</pre>


Discard a given size object. Note that <a href="../ft2-base_interface/#ft_done_face">FT_Done_Face</a> automatically discards all size objects allocated with <a href="../ft2-sizes_management/#ft_new_size">FT_New_Size</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="size">size</td><td class="desc">

A handle to a target size object.
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr />

## FT_Activate_Size

Defined in FT_SIZES_H (freetype/ftsizes.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Activate_Size</b>( <a href="../ft2-base_interface/#ft_size">FT_Size</a>  size );
</pre>


Even though it is possible to create several size objects for a given face (see <a href="../ft2-sizes_management/#ft_new_size">FT_New_Size</a> for details), functions like <a href="../ft2-base_interface/#ft_load_glyph">FT_Load_Glyph</a> or <a href="../ft2-base_interface/#ft_load_char">FT_Load_Char</a> only use the one that has been activated last to determine the &lsquo;current character pixel size&rsquo;.

This function can be used to &lsquo;activate&rsquo; a previously created size object.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="size">size</td><td class="desc">

A handle to a target size object.
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

If &lsquo;face&rsquo; is the size's parent face object, this function changes the value of &lsquo;face-&gt;size&rsquo; to the input size handle.

<hr />

