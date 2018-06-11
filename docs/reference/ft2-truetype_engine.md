[Docs](ft2-index.md) &raquo; [Miscellaneous](ft2-toc.md#miscellaneous) &raquo; The TrueType Engine

-------------------------------

# The TrueType Engine

## Synopsis

This section contains a function used to query the level of TrueType bytecode support compiled in this version of the library.

## FT_TrueTypeEngineType

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  FT_TrueTypeEngineType_
  {
    <a href="../ft2-truetype_engine/#ft_truetype_engine_type_none">FT_TRUETYPE_ENGINE_TYPE_NONE</a> = 0,
    <a href="../ft2-truetype_engine/#ft_truetype_engine_type_unpatented">FT_TRUETYPE_ENGINE_TYPE_UNPATENTED</a>,
    <a href="../ft2-truetype_engine/#ft_truetype_engine_type_patented">FT_TRUETYPE_ENGINE_TYPE_PATENTED</a>

  } <b>FT_TrueTypeEngineType</b>;
</pre>
</div>


A list of values describing which kind of TrueType bytecode engine is implemented in a given FT_Library instance. It is used by the <a href="../ft2-truetype_engine/#ft_get_truetype_engine_type">FT_Get_TrueType_Engine_Type</a> function.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_truetype_engine_type_none">FT_TRUETYPE_ENGINE_TYPE_NONE</td><td class="desc">
<p>The library doesn't implement any kind of bytecode interpreter.</p>
</td></tr>
<tr><td class="val" id="ft_truetype_engine_type_unpatented">FT_TRUETYPE_ENGINE_TYPE_UNPATENTED</td><td class="desc">
<p>Deprecated and removed.</p>
</td></tr>
<tr><td class="val" id="ft_truetype_engine_type_patented">FT_TRUETYPE_ENGINE_TYPE_PATENTED</td><td class="desc">
<p>The library implements a bytecode interpreter that covers the full instruction set of the TrueType virtual machine (this was governed by patents until May 2010, hence the name).</p>
</td></tr>
</table>

<h4>since</h4>

2.2

<hr>

## FT_Get_TrueType_Engine_Type

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-truetype_engine/#ft_truetypeenginetype">FT_TrueTypeEngineType</a> )
  <b>FT_Get_TrueType_Engine_Type</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>  library );
</pre>
</div>


Return an <a href="../ft2-truetype_engine/#ft_truetypeenginetype">FT_TrueTypeEngineType</a> value to indicate which level of the TrueType virtual machine a given library instance supports.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A library instance.</p>
</td></tr>
</table>

<h4>return</h4>

A value indicating which level is supported.

<h4>since</h4>

2.2

<hr>

