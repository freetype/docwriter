[Docs](ft2-index.md) &raquo; [Miscellaneous](ft2-toc.md#miscellaneous) &raquo; OpenType Validation

-------------------------------

# OpenType Validation

## Synopsis

This section contains the declaration of functions to validate some OpenType tables (BASE, GDEF, GPOS, GSUB, JSTF, MATH).

## FT_OpenType_Validate

Defined in FT_OPENTYPE_VALIDATE_H (freetype/ftotval.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_OpenType_Validate</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                        <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    validation_flags,
                        <a href="../ft2-basic_types/#ft_bytes">FT_Bytes</a>  *BASE_table,
                        <a href="../ft2-basic_types/#ft_bytes">FT_Bytes</a>  *GDEF_table,
                        <a href="../ft2-basic_types/#ft_bytes">FT_Bytes</a>  *GPOS_table,
                        <a href="../ft2-basic_types/#ft_bytes">FT_Bytes</a>  *GSUB_table,
                        <a href="../ft2-basic_types/#ft_bytes">FT_Bytes</a>  *JSTF_table );
</pre>
</div>


Validate various OpenType tables to assure that all offsets and indices are valid. The idea is that a higher-level library that actually does the text layout can access those tables without error checking (which can be quite time consuming).

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
<tr><td class="val" id="validation_flags">validation_flags</td><td class="desc">
<p>A bit field that specifies the tables to be validated. See <a href="../ft2-ot_validation/#ft_validate_otxxx">FT_VALIDATE_OTXXX</a> for possible values.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="base_table">BASE_table</td><td class="desc">
<p>A pointer to the BASE table.</p>
</td></tr>
<tr><td class="val" id="gdef_table">GDEF_table</td><td class="desc">
<p>A pointer to the GDEF table.</p>
</td></tr>
<tr><td class="val" id="gpos_table">GPOS_table</td><td class="desc">
<p>A pointer to the GPOS table.</p>
</td></tr>
<tr><td class="val" id="gsub_table">GSUB_table</td><td class="desc">
<p>A pointer to the GSUB table.</p>
</td></tr>
<tr><td class="val" id="jstf_table">JSTF_table</td><td class="desc">
<p>A pointer to the JSTF table.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function only works with OpenType fonts, returning an error otherwise.

After use, the application should deallocate the five tables with <a href="../ft2-ot_validation/#ft_opentype_free">FT_OpenType_Free</a>. A NULL value indicates that the table either doesn't exist in the font, or the application hasn't asked for validation.

<hr>

## FT_OpenType_Free

Defined in FT_OPENTYPE_VALIDATE_H (freetype/ftotval.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_OpenType_Free</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                    <a href="../ft2-basic_types/#ft_bytes">FT_Bytes</a>  table );
</pre>
</div>


Free the buffer allocated by OpenType validator.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
<tr><td class="val" id="table">table</td><td class="desc">
<p>The pointer to the buffer that is allocated by <a href="../ft2-ot_validation/#ft_opentype_validate">FT_OpenType_Validate</a>.</p>
</td></tr>
</table>

<h4>note</h4>

This function must be used to free the buffer allocated by <a href="../ft2-ot_validation/#ft_opentype_validate">FT_OpenType_Validate</a> only.

<hr>

## FT_VALIDATE_OTXXX

Defined in FT_OPENTYPE_VALIDATE_H (freetype/ftotval.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <a href="../ft2-ot_validation/#ft_validate_base">FT_VALIDATE_BASE</a>  0x0100
#<span class="keyword">define</span> <a href="../ft2-ot_validation/#ft_validate_gdef">FT_VALIDATE_GDEF</a>  0x0200
#<span class="keyword">define</span> <a href="../ft2-ot_validation/#ft_validate_gpos">FT_VALIDATE_GPOS</a>  0x0400
#<span class="keyword">define</span> <a href="../ft2-ot_validation/#ft_validate_gsub">FT_VALIDATE_GSUB</a>  0x0800
#<span class="keyword">define</span> <a href="../ft2-ot_validation/#ft_validate_jstf">FT_VALIDATE_JSTF</a>  0x1000
#<span class="keyword">define</span> <a href="../ft2-ot_validation/#ft_validate_math">FT_VALIDATE_MATH</a>  0x2000

#<span class="keyword">define</span> <a href="../ft2-ot_validation/#ft_validate_ot">FT_VALIDATE_OT</a>  ( <a href="../ft2-ot_validation/#ft_validate_base">FT_VALIDATE_BASE</a> | \
                          <a href="../ft2-ot_validation/#ft_validate_gdef">FT_VALIDATE_GDEF</a> | \
                          <a href="../ft2-ot_validation/#ft_validate_gpos">FT_VALIDATE_GPOS</a> | \
                          <a href="../ft2-ot_validation/#ft_validate_gsub">FT_VALIDATE_GSUB</a> | \
                          <a href="../ft2-ot_validation/#ft_validate_jstf">FT_VALIDATE_JSTF</a> | \
                          <a href="../ft2-ot_validation/#ft_validate_math">FT_VALIDATE_MATH</a> )
</pre>
</div>


A list of bit-field constants used with <a href="../ft2-ot_validation/#ft_opentype_validate">FT_OpenType_Validate</a> to indicate which OpenType tables should be validated.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_validate_base">FT_VALIDATE_BASE</td><td class="desc">
<p>Validate BASE table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_gdef">FT_VALIDATE_GDEF</td><td class="desc">
<p>Validate GDEF table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_gpos">FT_VALIDATE_GPOS</td><td class="desc">
<p>Validate GPOS table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_gsub">FT_VALIDATE_GSUB</td><td class="desc">
<p>Validate GSUB table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_jstf">FT_VALIDATE_JSTF</td><td class="desc">
<p>Validate JSTF table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_math">FT_VALIDATE_MATH</td><td class="desc">
<p>Validate MATH table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_ot">FT_VALIDATE_OT</td><td class="desc">
<p>Validate all OpenType tables (BASE, GDEF, GPOS, GSUB, JSTF, MATH).</p>
</td></tr>
</table>

<hr>

