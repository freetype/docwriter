[Docs](ft2-index.md) &raquo; [Miscellaneous](ft2-toc.md#miscellaneous) &raquo; TrueTypeGX/AAT Validation

-------------------------------

# TrueTypeGX/AAT Validation

## Synopsis

This section contains the declaration of functions to validate some TrueTypeGX tables (feat, mort, morx, bsln, just, kern, opbd, trak, prop, lcar).

## FT_TrueTypeGX_Validate

Defined in FT_GX_VALIDATE_H (freetype/ftgxval.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_TrueTypeGX_Validate</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                          <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>   validation_flags,
                          <a href="../ft2-basic_types/#ft_bytes">FT_Bytes</a>  tables[<a href="../ft2-gx_validation/#ft_validate_gx_length">FT_VALIDATE_GX_LENGTH</a>],
                          <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>   table_length );
</pre>
</div>


Validate various TrueTypeGX tables to assure that all offsets and indices are valid. The idea is that a higher-level library that actually does the text layout can access those tables without error checking (which can be quite time consuming).

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
<tr><td class="val" id="validation_flags">validation_flags</td><td class="desc">
<p>A bit field that specifies the tables to be validated. See <a href="../ft2-gx_validation/#ft_validate_gxxxx">FT_VALIDATE_GXXXX</a> for possible values.</p>
</td></tr>
<tr><td class="val" id="table_length">table_length</td><td class="desc">
<p>The size of the &lsquo;tables&rsquo; array. Normally, <a href="../ft2-gx_validation/#ft_validate_gx_length">FT_VALIDATE_GX_LENGTH</a> should be passed.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="tables">tables</td><td class="desc">
<p>The array where all validated sfnt tables are stored. The array itself must be allocated by a client.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function only works with TrueTypeGX fonts, returning an error otherwise.

After use, the application should deallocate the buffers pointed to by each &lsquo;tables&rsquo; element, by calling <a href="../ft2-gx_validation/#ft_truetypegx_free">FT_TrueTypeGX_Free</a>. A NULL value indicates that the table either doesn't exist in the font, the application hasn't asked for validation, or the validator doesn't have the ability to validate the sfnt table.

<hr>

## FT_TrueTypeGX_Free

Defined in FT_GX_VALIDATE_H (freetype/ftgxval.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_TrueTypeGX_Free</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                      <a href="../ft2-basic_types/#ft_bytes">FT_Bytes</a>  table );
</pre>
</div>


Free the buffer allocated by TrueTypeGX validator.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
<tr><td class="val" id="table">table</td><td class="desc">
<p>The pointer to the buffer allocated by <a href="../ft2-gx_validation/#ft_truetypegx_validate">FT_TrueTypeGX_Validate</a>.</p>
</td></tr>
</table>

<h4>note</h4>

This function must be used to free the buffer allocated by <a href="../ft2-gx_validation/#ft_truetypegx_validate">FT_TrueTypeGX_Validate</a> only.

<hr>

## FT_ClassicKern_Validate

Defined in FT_GX_VALIDATE_H (freetype/ftgxval.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_ClassicKern_Validate</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                           <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    validation_flags,
                           <a href="../ft2-basic_types/#ft_bytes">FT_Bytes</a>  *ckern_table );
</pre>
</div>


Validate classic (16-bit format) kern table to assure that the offsets and indices are valid. The idea is that a higher-level library that actually does the text layout can access those tables without error checking (which can be quite time consuming).

The &lsquo;kern&rsquo; table validator in <a href="../ft2-gx_validation/#ft_truetypegx_validate">FT_TrueTypeGX_Validate</a> deals with both the new 32-bit format and the classic 16-bit format, while FT_ClassicKern_Validate only supports the classic 16-bit format.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
<tr><td class="val" id="validation_flags">validation_flags</td><td class="desc">
<p>A bit field that specifies the dialect to be validated. See <a href="../ft2-gx_validation/#ft_validate_ckernxxx">FT_VALIDATE_CKERNXXX</a> for possible values.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="ckern_table">ckern_table</td><td class="desc">
<p>A pointer to the kern table.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

After use, the application should deallocate the buffers pointed to by &lsquo;ckern_table&rsquo;, by calling <a href="../ft2-gx_validation/#ft_classickern_free">FT_ClassicKern_Free</a>. A NULL value indicates that the table doesn't exist in the font.

<hr>

## FT_ClassicKern_Free

Defined in FT_GX_VALIDATE_H (freetype/ftgxval.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_ClassicKern_Free</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>   face,
                       <a href="../ft2-basic_types/#ft_bytes">FT_Bytes</a>  table );
</pre>
</div>


Free the buffer allocated by classic Kern validator.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
<tr><td class="val" id="table">table</td><td class="desc">
<p>The pointer to the buffer that is allocated by <a href="../ft2-gx_validation/#ft_classickern_validate">FT_ClassicKern_Validate</a>.</p>
</td></tr>
</table>

<h4>note</h4>

This function must be used to free the buffer allocated by <a href="../ft2-gx_validation/#ft_classickern_validate">FT_ClassicKern_Validate</a> only.

<hr>

## FT_VALIDATE_GX_LENGTH

Defined in FT_GX_VALIDATE_H (freetype/ftgxval.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_VALIDATE_GX_LENGTH</b>  ( FT_VALIDATE_GX_LAST_INDEX + 1 )
</pre>
</div>


The number of tables checked in this module. Use it as a parameter for the &lsquo;table-length&rsquo; argument of function <a href="../ft2-gx_validation/#ft_truetypegx_validate">FT_TrueTypeGX_Validate</a>.

<hr>

## FT_VALIDATE_GXXXX

Defined in FT_GX_VALIDATE_H (freetype/ftgxval.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_feat">FT_VALIDATE_feat</a>  FT_VALIDATE_GX_BITFIELD( feat )
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_mort">FT_VALIDATE_mort</a>  FT_VALIDATE_GX_BITFIELD( mort )
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_morx">FT_VALIDATE_morx</a>  FT_VALIDATE_GX_BITFIELD( morx )
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_bsln">FT_VALIDATE_bsln</a>  FT_VALIDATE_GX_BITFIELD( bsln )
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_just">FT_VALIDATE_just</a>  FT_VALIDATE_GX_BITFIELD( just )
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_kern">FT_VALIDATE_kern</a>  FT_VALIDATE_GX_BITFIELD( kern )
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_opbd">FT_VALIDATE_opbd</a>  FT_VALIDATE_GX_BITFIELD( opbd )
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_trak">FT_VALIDATE_trak</a>  FT_VALIDATE_GX_BITFIELD( trak )
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_prop">FT_VALIDATE_prop</a>  FT_VALIDATE_GX_BITFIELD( prop )
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_lcar">FT_VALIDATE_lcar</a>  FT_VALIDATE_GX_BITFIELD( lcar )

#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_gx">FT_VALIDATE_GX</a>  ( <a href="../ft2-gx_validation/#ft_validate_feat">FT_VALIDATE_feat</a> | \
                          <a href="../ft2-gx_validation/#ft_validate_mort">FT_VALIDATE_mort</a> | \
                          <a href="../ft2-gx_validation/#ft_validate_morx">FT_VALIDATE_morx</a> | \
                          <a href="../ft2-gx_validation/#ft_validate_bsln">FT_VALIDATE_bsln</a> | \
                          <a href="../ft2-gx_validation/#ft_validate_just">FT_VALIDATE_just</a> | \
                          <a href="../ft2-gx_validation/#ft_validate_kern">FT_VALIDATE_kern</a> | \
                          <a href="../ft2-gx_validation/#ft_validate_opbd">FT_VALIDATE_opbd</a> | \
                          <a href="../ft2-gx_validation/#ft_validate_trak">FT_VALIDATE_trak</a> | \
                          <a href="../ft2-gx_validation/#ft_validate_prop">FT_VALIDATE_prop</a> | \
                          <a href="../ft2-gx_validation/#ft_validate_lcar">FT_VALIDATE_lcar</a> )
</pre>
</div>


A list of bit-field constants used with <a href="../ft2-gx_validation/#ft_truetypegx_validate">FT_TrueTypeGX_Validate</a> to indicate which TrueTypeGX/AAT Type tables should be validated.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_validate_feat">FT_VALIDATE_feat</td><td class="desc">
<p>Validate &lsquo;feat&rsquo; table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_mort">FT_VALIDATE_mort</td><td class="desc">
<p>Validate &lsquo;mort&rsquo; table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_morx">FT_VALIDATE_morx</td><td class="desc">
<p>Validate &lsquo;morx&rsquo; table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_bsln">FT_VALIDATE_bsln</td><td class="desc">
<p>Validate &lsquo;bsln&rsquo; table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_just">FT_VALIDATE_just</td><td class="desc">
<p>Validate &lsquo;just&rsquo; table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_kern">FT_VALIDATE_kern</td><td class="desc">
<p>Validate &lsquo;kern&rsquo; table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_opbd">FT_VALIDATE_opbd</td><td class="desc">
<p>Validate &lsquo;opbd&rsquo; table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_trak">FT_VALIDATE_trak</td><td class="desc">
<p>Validate &lsquo;trak&rsquo; table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_prop">FT_VALIDATE_prop</td><td class="desc">
<p>Validate &lsquo;prop&rsquo; table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_lcar">FT_VALIDATE_lcar</td><td class="desc">
<p>Validate &lsquo;lcar&rsquo; table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_gx">FT_VALIDATE_GX</td><td class="desc">
<p>Validate all TrueTypeGX tables (feat, mort, morx, bsln, just, kern, opbd, trak, prop and lcar).</p>
</td></tr>
</table>

<hr>

## FT_VALIDATE_CKERNXXX

Defined in FT_GX_VALIDATE_H (freetype/ftgxval.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_ms">FT_VALIDATE_MS</a>     ( FT_VALIDATE_GX_START &lt;&lt; 0 )
#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_apple">FT_VALIDATE_APPLE</a>  ( FT_VALIDATE_GX_START &lt;&lt; 1 )

#<span class="keyword">define</span> <a href="../ft2-gx_validation/#ft_validate_ckern">FT_VALIDATE_CKERN</a>  ( <a href="../ft2-gx_validation/#ft_validate_ms">FT_VALIDATE_MS</a> | <a href="../ft2-gx_validation/#ft_validate_apple">FT_VALIDATE_APPLE</a> )
</pre>
</div>


A list of bit-field constants used with <a href="../ft2-gx_validation/#ft_classickern_validate">FT_ClassicKern_Validate</a> to indicate the classic kern dialect or dialects. If the selected type doesn't fit, <a href="../ft2-gx_validation/#ft_classickern_validate">FT_ClassicKern_Validate</a> regards the table as invalid.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_validate_ms">FT_VALIDATE_MS</td><td class="desc">
<p>Handle the &lsquo;kern&rsquo; table as a classic Microsoft kern table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_apple">FT_VALIDATE_APPLE</td><td class="desc">
<p>Handle the &lsquo;kern&rsquo; table as a classic Apple kern table.</p>
</td></tr>
<tr><td class="val" id="ft_validate_ckern">FT_VALIDATE_CKERN</td><td class="desc">
<p>Handle the &lsquo;kern&rsquo; as either classic Apple or Microsoft kern table.</p>
</td></tr>
</table>

<hr>

