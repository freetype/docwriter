[Docs](ft2-index.md) &raquo; [Miscellaneous](ft2-toc.md#miscellaneous) &raquo; Incremental Loading

-------------------------------

# Incremental Loading

## Synopsis

This section contains various functions used to perform so-called &lsquo;incremental&rsquo; glyph loading. This is a mode where all glyphs loaded from a given <a href="../ft2-base_interface/#ft_face">FT_Face</a> are provided by the client application.

Apart from that, all other tables are loaded normally from the font file. This mode is useful when FreeType is used within another engine, e.g., a PostScript Imaging Processor.

To enable this mode, you must use <a href="../ft2-base_interface/#ft_open_face">FT_Open_Face</a>, passing an <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a> with the <a href="../ft2-parameter_tags/#ft_param_tag_incremental">FT_PARAM_TAG_INCREMENTAL</a> tag and an <a href="../ft2-incremental/#ft_incremental_interface">FT_Incremental_Interface</a> value. See the comments for <a href="../ft2-incremental/#ft_incremental_interfacerec">FT_Incremental_InterfaceRec</a> for an example.

## FT_Incremental

Defined in FT_INCREMENTAL_H (freetype/ftincrem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_IncrementalRec_*  <b>FT_Incremental</b>;
</pre>
</div>


An opaque type describing a user-provided object used to implement &lsquo;incremental&rsquo; glyph loading within FreeType. This is used to support embedded fonts in certain environments (e.g., PostScript interpreters), where the glyph data isn't in the font file, or must be overridden by different values.

<h4>note</h4>

It is up to client applications to create and implement <a href="../ft2-incremental/#ft_incremental">FT_Incremental</a> objects, as long as they provide implementations for the methods <a href="../ft2-incremental/#ft_incremental_getglyphdatafunc">FT_Incremental_GetGlyphDataFunc</a>, <a href="../ft2-incremental/#ft_incremental_freeglyphdatafunc">FT_Incremental_FreeGlyphDataFunc</a> and <a href="../ft2-incremental/#ft_incremental_getglyphmetricsfunc">FT_Incremental_GetGlyphMetricsFunc</a>.

See the description of <a href="../ft2-incremental/#ft_incremental_interfacerec">FT_Incremental_InterfaceRec</a> to understand how to use incremental objects with FreeType.

<hr>

## FT_Incremental_MetricsRec

Defined in FT_INCREMENTAL_H (freetype/ftincrem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Incremental_MetricsRec_
  {
    <a href="../ft2-basic_types/#ft_long">FT_Long</a>  bearing_x;
    <a href="../ft2-basic_types/#ft_long">FT_Long</a>  bearing_y;
    <a href="../ft2-basic_types/#ft_long">FT_Long</a>  advance;
    <a href="../ft2-basic_types/#ft_long">FT_Long</a>  advance_v;     /* since 2.3.12 */

  } <b>FT_Incremental_MetricsRec</b>;
</pre>
</div>


A small structure used to contain the basic glyph metrics returned by the <a href="../ft2-incremental/#ft_incremental_getglyphmetricsfunc">FT_Incremental_GetGlyphMetricsFunc</a> method.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="bearing_x">bearing_x</td><td class="desc">
<p>Left bearing, in font units.</p>
</td></tr>
<tr><td class="val" id="bearing_y">bearing_y</td><td class="desc">
<p>Top bearing, in font units.</p>
</td></tr>
<tr><td class="val" id="advance">advance</td><td class="desc">
<p>Horizontal component of glyph advance, in font units.</p>
</td></tr>
<tr><td class="val" id="advance_v">advance_v</td><td class="desc">
<p>Vertical component of glyph advance, in font units.</p>
</td></tr>
</table>

<h4>note</h4>

These correspond to horizontal or vertical metrics depending on the value of the &lsquo;vertical&rsquo; argument to the function <a href="../ft2-incremental/#ft_incremental_getglyphmetricsfunc">FT_Incremental_GetGlyphMetricsFunc</a>.

<hr>

## FT_Incremental_Metrics

Defined in FT_INCREMENTAL_H (freetype/ftincrem.h).

<div class = "codehilite">
<pre>
   <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_Incremental_MetricsRec_*  <b>FT_Incremental_Metrics</b>;
</pre>
</div>


A handle to an <a href="../ft2-incremental/#ft_incremental_metricsrec">FT_Incremental_MetricsRec</a> structure.

<hr>

## FT_Incremental_GetGlyphDataFunc

Defined in FT_INCREMENTAL_H (freetype/ftincrem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-basic_types/#ft_error">FT_Error</a>
  (*<b>FT_Incremental_GetGlyphDataFunc</b>)( <a href="../ft2-incremental/#ft_incremental">FT_Incremental</a>  incremental,
                                      <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>         glyph_index,
                                      <a href="../ft2-basic_types/#ft_data">FT_Data</a>*        adata );
</pre>
</div>


A function called by FreeType to access a given glyph's data bytes during <a href="../ft2-base_interface/#ft_load_glyph">FT_Load_Glyph</a> or <a href="../ft2-base_interface/#ft_load_char">FT_Load_Char</a> if incremental loading is enabled.

Note that the format of the glyph's data bytes depends on the font file format. For TrueType, it must correspond to the raw bytes within the &lsquo;glyf&rsquo; table. For PostScript formats, it must correspond to the **unencrypted** charstring bytes, without any &lsquo;lenIV&rsquo; header. It is undefined for any other format.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="incremental">incremental</td><td class="desc">
<p>Handle to an opaque <a href="../ft2-incremental/#ft_incremental">FT_Incremental</a> handle provided by the client application.</p>
</td></tr>
<tr><td class="val" id="glyph_index">glyph_index</td><td class="desc">
<p>Index of relevant glyph.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="adata">adata</td><td class="desc">
<p>A structure describing the returned glyph data bytes (which will be accessed as a read-only byte block).</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

If this function returns successfully the method <a href="../ft2-incremental/#ft_incremental_freeglyphdatafunc">FT_Incremental_FreeGlyphDataFunc</a> will be called later to release the data bytes.

Nested calls to <a href="../ft2-incremental/#ft_incremental_getglyphdatafunc">FT_Incremental_GetGlyphDataFunc</a> can happen for compound glyphs.

<hr>

## FT_Incremental_FreeGlyphDataFunc

Defined in FT_INCREMENTAL_H (freetype/ftincrem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>
  (*<b>FT_Incremental_FreeGlyphDataFunc</b>)( <a href="../ft2-incremental/#ft_incremental">FT_Incremental</a>  incremental,
                                       <a href="../ft2-basic_types/#ft_data">FT_Data</a>*        data );
</pre>
</div>


A function used to release the glyph data bytes returned by a successful call to <a href="../ft2-incremental/#ft_incremental_getglyphdatafunc">FT_Incremental_GetGlyphDataFunc</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="incremental">incremental</td><td class="desc">
<p>A handle to an opaque <a href="../ft2-incremental/#ft_incremental">FT_Incremental</a> handle provided by the client application.</p>
</td></tr>
<tr><td class="val" id="data">data</td><td class="desc">
<p>A structure describing the glyph data bytes (which will be accessed as a read-only byte block).</p>
</td></tr>
</table>

<hr>

## FT_Incremental_GetGlyphMetricsFunc

Defined in FT_INCREMENTAL_H (freetype/ftincrem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-basic_types/#ft_error">FT_Error</a>
  (*<b>FT_Incremental_GetGlyphMetricsFunc</b>)
                      ( <a href="../ft2-incremental/#ft_incremental">FT_Incremental</a>              incremental,
                        <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>                     glyph_index,
                        <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>                     vertical,
                        <a href="../ft2-incremental/#ft_incremental_metricsrec">FT_Incremental_MetricsRec</a>  *ametrics );
</pre>
</div>


A function used to retrieve the basic metrics of a given glyph index before accessing its data. This is necessary because, in certain formats like TrueType, the metrics are stored in a different place from the glyph images proper.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="incremental">incremental</td><td class="desc">
<p>A handle to an opaque <a href="../ft2-incremental/#ft_incremental">FT_Incremental</a> handle provided by the client application.</p>
</td></tr>
<tr><td class="val" id="glyph_index">glyph_index</td><td class="desc">
<p>Index of relevant glyph.</p>
</td></tr>
<tr><td class="val" id="vertical">vertical</td><td class="desc">
<p>If true, return vertical metrics.</p>
</td></tr>
<tr><td class="val" id="ametrics">ametrics</td><td class="desc">
<p>This parameter is used for both input and output. The original glyph metrics, if any, in font units. If metrics are not available all the values must be set to zero.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="ametrics">ametrics</td><td class="desc">
<p>The replacement glyph metrics in font units.</p>
</td></tr>
</table>

<hr>

## FT_Incremental_FuncsRec

Defined in FT_INCREMENTAL_H (freetype/ftincrem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Incremental_FuncsRec_
  {
    <a href="../ft2-incremental/#ft_incremental_getglyphdatafunc">FT_Incremental_GetGlyphDataFunc</a>     get_glyph_data;
    <a href="../ft2-incremental/#ft_incremental_freeglyphdatafunc">FT_Incremental_FreeGlyphDataFunc</a>    free_glyph_data;
    <a href="../ft2-incremental/#ft_incremental_getglyphmetricsfunc">FT_Incremental_GetGlyphMetricsFunc</a>  get_glyph_metrics;

  } <b>FT_Incremental_FuncsRec</b>;
</pre>
</div>


A table of functions for accessing fonts that load data incrementally. Used in <a href="../ft2-incremental/#ft_incremental_interfacerec">FT_Incremental_InterfaceRec</a>.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="get_glyph_data">get_glyph_data</td><td class="desc">
<p>The function to get glyph data. Must not be null.</p>
</td></tr>
<tr><td class="val" id="free_glyph_data">free_glyph_data</td><td class="desc">
<p>The function to release glyph data. Must not be null.</p>
</td></tr>
<tr><td class="val" id="get_glyph_metrics">get_glyph_metrics</td><td class="desc">
<p>The function to get glyph metrics. May be null if the font does not provide overriding glyph metrics.</p>
</td></tr>
</table>

<hr>

## FT_Incremental_InterfaceRec

Defined in FT_INCREMENTAL_H (freetype/ftincrem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Incremental_InterfaceRec_
  {
    <span class="keyword">const</span> <a href="../ft2-incremental/#ft_incremental_funcsrec">FT_Incremental_FuncsRec</a>*  funcs;
    <a href="../ft2-incremental/#ft_incremental">FT_Incremental</a>                  object;

  } <b>FT_Incremental_InterfaceRec</b>;
</pre>
</div>


A structure to be used with <a href="../ft2-base_interface/#ft_open_face">FT_Open_Face</a> to indicate that the user wants to support incremental glyph loading. You should use it with <a href="../ft2-parameter_tags/#ft_param_tag_incremental">FT_PARAM_TAG_INCREMENTAL</a> as in the following example:
```
  FT_Incremental_InterfaceRec  inc_int;
  FT_Parameter                 parameter;
  FT_Open_Args                 open_args;


  // set up incremental descriptor
  inc_int.funcs  = my_funcs;
  inc_int.object = my_object;

  // set up optional parameter
  parameter.tag  = FT_PARAM_TAG_INCREMENTAL;
  parameter.data = &inc_int;

  // set up FT_Open_Args structure
  open_args.flags      = FT_OPEN_PATHNAME | FT_OPEN_PARAMS;
  open_args.pathname   = my_font_pathname;
  open_args.num_params = 1;
  open_args.params     = &parameter; // we use one optional argument

  // open the font
  error = FT_Open_Face( library, &open_args, index, &face );
  ...
```

<hr>

## FT_Incremental_Interface

Defined in FT_INCREMENTAL_H (freetype/ftincrem.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-incremental/#ft_incremental_interfacerec">FT_Incremental_InterfaceRec</a>*   <b>FT_Incremental_Interface</b>;
</pre>
</div>


A pointer to an <a href="../ft2-incremental/#ft_incremental_interfacerec">FT_Incremental_InterfaceRec</a> structure.

<hr>

