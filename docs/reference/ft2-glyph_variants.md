[Docs](ft2-index.md) &raquo; [Core API](ft2-toc.md#core-api) &raquo; Unicode Variation Sequences

-------------------------------

# Unicode Variation Sequences

## Synopsis

Many characters, especially for CJK scripts, have variant forms. They are a sort of grey area somewhere between being totally irrelevant and semantically distinct; for this reason, the Unicode consortium decided to introduce Variation Sequences (VS), consisting of a Unicode base character and a variation selector instead of further extending the already huge number of characters.

Unicode maintains two different sets, namely &lsquo;Standardized Variation Sequences&rsquo; and registered &lsquo;Ideographic Variation Sequences&rsquo; (IVS), collected in the &lsquo;Ideographic Variation Database&rsquo; (IVD).

<https://unicode.org/Public/UCD/latest/ucd/StandardizedVariants.txt> <https://unicode.org/reports/tr37/> <https://unicode.org/ivd/>

To date (January 2017), the character with the most ideographic variations is U+9089, having 32 such IVS.

Three Mongolian Variation Selectors have the values U+180B-U+180D; 256 generic Variation Selectors are encoded in the ranges U+FE00-U+FE0F and U+E0100-U+E01EF. IVS currently use Variation Selectors from the range U+E0100-U+E01EF only.

A VS consists of the base character value followed by a single Variation Selector. For example, to get the first variation of U+9089, you have to write the character sequence &lsquo;U+9089 U+E0100&rsquo;.

Adobe and MS decided to support both standardized and ideographic VS with a new cmap subtable (format&nbsp;14). It is an odd subtable because it is not a mapping of input code points to glyphs, but contains lists of all variations supported by the font.

A variation may be either &lsquo;default&rsquo; or &lsquo;non-default&rsquo; for a given font. A default variation is the one you will get for that code point if you look it up in the standard Unicode cmap. A non-default variation is a different glyph.

## FT_Face_GetCharVariantIndex

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_uint">FT_UInt</a> )
  <b>FT_Face_GetCharVariantIndex</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                               <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  charcode,
                               <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  variantSelector );
</pre>
</div>


Return the glyph index of a given character code as modified by the variation selector.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face object.</p>
</td></tr>
<tr><td class="val" id="charcode">charcode</td><td class="desc">
<p>The character code point in Unicode.</p>
</td></tr>
<tr><td class="val" id="variantselector">variantSelector</td><td class="desc">
<p>The Unicode code point of the variation selector.</p>
</td></tr>
</table>

<h4>return</h4>

The glyph index. 0&nbsp;means either &lsquo;undefined character code&rsquo;, or &lsquo;undefined selector code&rsquo;, or &lsquo;no variation selector cmap subtable&rsquo;, or &lsquo;current CharMap is not Unicode&rsquo;.

<h4>note</h4>

If you use FreeType to manipulate the contents of font files directly, be aware that the glyph index returned by this function doesn't always correspond to the internal indices used within the file. This is done to ensure that value&nbsp;0 always corresponds to the &lsquo;missing glyph&rsquo;.

This function is only meaningful if a) the font has a variation selector cmap sub table, and b) the current charmap has a Unicode encoding.

<h4>since</h4>

2.3.6

<hr>

## FT_Face_GetCharVariantIsDefault

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_int">FT_Int</a> )
  <b>FT_Face_GetCharVariantIsDefault</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                                   <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  charcode,
                                   <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  variantSelector );
</pre>
</div>


Check whether this variation of this Unicode character is the one to be found in the &lsquo;cmap&rsquo;.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face object.</p>
</td></tr>
<tr><td class="val" id="charcode">charcode</td><td class="desc">
<p>The character codepoint in Unicode.</p>
</td></tr>
<tr><td class="val" id="variantselector">variantSelector</td><td class="desc">
<p>The Unicode codepoint of the variation selector.</p>
</td></tr>
</table>

<h4>return</h4>

1&nbsp;if found in the standard (Unicode) cmap, 0&nbsp;if found in the variation selector cmap, or -1 if it is not a variation.

<h4>note</h4>

This function is only meaningful if the font has a variation selector cmap subtable.

<h4>since</h4>

2.3.6

<hr>

## FT_Face_GetVariantSelectors

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_uint32">FT_UInt32</a>* )
  <b>FT_Face_GetVariantSelectors</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>  face );
</pre>
</div>


Return a zero-terminated list of Unicode variation selectors found in the font.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face object.</p>
</td></tr>
</table>

<h4>return</h4>

A pointer to an array of selector code points, or NULL if there is no valid variation selector cmap subtable.

<h4>note</h4>

The last item in the array is&nbsp;0; the array is owned by the <a href="../ft2-base_interface/#ft_face">FT_Face</a> object but can be overwritten or released on the next call to a FreeType function.

<h4>since</h4>

2.3.6

<hr>

## FT_Face_GetVariantsOfChar

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_uint32">FT_UInt32</a>* )
  <b>FT_Face_GetVariantsOfChar</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                             <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  charcode );
</pre>
</div>


Return a zero-terminated list of Unicode variation selectors found for the specified character code.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face object.</p>
</td></tr>
<tr><td class="val" id="charcode">charcode</td><td class="desc">
<p>The character codepoint in Unicode.</p>
</td></tr>
</table>

<h4>return</h4>

A pointer to an array of variation selector code points that are active for the given character, or NULL if the corresponding list is empty.

<h4>note</h4>

The last item in the array is&nbsp;0; the array is owned by the <a href="../ft2-base_interface/#ft_face">FT_Face</a> object but can be overwritten or released on the next call to a FreeType function.

<h4>since</h4>

2.3.6

<hr>

## FT_Face_GetCharsOfVariant

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_uint32">FT_UInt32</a>* )
  <b>FT_Face_GetCharsOfVariant</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                             <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  variantSelector );
</pre>
</div>


Return a zero-terminated list of Unicode character codes found for the specified variation selector.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face object.</p>
</td></tr>
<tr><td class="val" id="variantselector">variantSelector</td><td class="desc">
<p>The variation selector code point in Unicode.</p>
</td></tr>
</table>

<h4>return</h4>

A list of all the code points that are specified by this selector (both default and non-default codes are returned) or NULL if there is no valid cmap or the variation selector is invalid.

<h4>note</h4>

The last item in the array is&nbsp;0; the array is owned by the <a href="../ft2-base_interface/#ft_face">FT_Face</a> object but can be overwritten or released on the next call to a FreeType function.

<h4>since</h4>

2.3.6

<hr>

