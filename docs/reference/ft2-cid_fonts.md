[Docs](ft2-index.md) &raquo; [Format-Specific API](ft2-toc.md#format-specific-api) &raquo; CID Fonts

-------------------------------

# CID Fonts

## Synopsis

This section contains the declaration of CID-keyed font specific functions.

## FT_Get_CID_Registry_Ordering_Supplement

Defined in FT_CID_H (freetype/ftcid.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_CID_Registry_Ordering_Supplement</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>       face,
                                           <span class="keyword">const</span> <span class="keyword">char</span>*  *registry,
                                           <span class="keyword">const</span> <span class="keyword">char</span>*  *ordering,
                                           <a href="../ft2-basic_types/#ft_int">FT_Int</a>       *supplement );
</pre>
</div>


Retrieve the Registry/Ordering/Supplement triple (also known as the "R/O/S") from a CID-keyed font.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="registry">registry</td><td class="desc">
<p>The registry, as a C&nbsp;string, owned by the face.</p>
</td></tr>
<tr><td class="val" id="ordering">ordering</td><td class="desc">
<p>The ordering, as a C&nbsp;string, owned by the face.</p>
</td></tr>
<tr><td class="val" id="supplement">supplement</td><td class="desc">
<p>The supplement.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function only works with CID faces, returning an error otherwise.

<h4>since</h4>

2.3.6

<hr>

## FT_Get_CID_Is_Internally_CID_Keyed

Defined in FT_CID_H (freetype/ftcid.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_CID_Is_Internally_CID_Keyed</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                                      <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>  *is_cid );
</pre>
</div>


Retrieve the type of the input face, CID keyed or not. In contrast to the <a href="../ft2-base_interface/#ft_is_cid_keyed">FT_IS_CID_KEYED</a> macro this function returns successfully also for CID-keyed fonts in an SFNT wrapper.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="is_cid">is_cid</td><td class="desc">
<p>The type of the face as an <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function only works with CID faces and OpenType fonts, returning an error otherwise.

<h4>since</h4>

2.3.9

<hr>

## FT_Get_CID_From_Glyph_Index

Defined in FT_CID_H (freetype/ftcid.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_CID_From_Glyph_Index</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                               <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>   glyph_index,
                               <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>  *cid );
</pre>
</div>


Retrieve the CID of the input glyph index.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
<tr><td class="val" id="glyph_index">glyph_index</td><td class="desc">
<p>The input glyph index.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="cid">cid</td><td class="desc">
<p>The CID as an <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function only works with CID faces and OpenType fonts, returning an error otherwise.

<h4>since</h4>

2.3.9

<hr>

