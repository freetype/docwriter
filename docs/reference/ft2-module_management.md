[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; Module Management

-------------------------------

# Module Management

## Synopsis

The definitions below are used to manage modules within FreeType. Modules can be added, upgraded, and removed at runtime. Additionally, some module properties can be controlled also.

Here is a list of possible values of the &lsquo;module_name&rsquo; field in the <a href="../ft2-module_management/#ft_module_class">FT_Module_Class</a> structure.
```
  autofitter
  bdf
  cff
  gxvalid
  otvalid
  pcf
  pfr
  psaux
  pshinter
  psnames
  raster1
  sfnt
  smooth, smooth-lcd, smooth-lcdv
  truetype
  type1
  type42
  t1cid
  winfonts
```

Note that the FreeType Cache sub-system is not a FreeType module.

## FT_Module

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_ModuleRec_*  <b>FT_Module</b>;
</pre>
</div>


A handle to a given FreeType module object. A module can be a font driver, a renderer, or anything else that provides services to the former.

<hr>

## FT_Module_Constructor

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-basic_types/#ft_error">FT_Error</a>
  (*<b>FT_Module_Constructor</b>)( <a href="../ft2-module_management/#ft_module">FT_Module</a>  module );
</pre>
</div>


A function used to initialize (not create) a new module object.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="module">module</td><td class="desc">
<p>The module to initialize.</p>
</td></tr>
</table>

<hr>

## FT_Module_Destructor

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>
  (*<b>FT_Module_Destructor</b>)( <a href="../ft2-module_management/#ft_module">FT_Module</a>  module );
</pre>
</div>


A function used to finalize (not destroy) a given module object.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="module">module</td><td class="desc">
<p>The module to finalize.</p>
</td></tr>
</table>

<hr>

## FT_Module_Requester

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> FT_Module_Interface
  (*<b>FT_Module_Requester</b>)( <a href="../ft2-module_management/#ft_module">FT_Module</a>    module,
                          <span class="keyword">const</span> <span class="keyword">char</span>*  name );
</pre>
</div>


A function used to query a given module for a specific interface.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="module">module</td><td class="desc">
<p>The module to be searched.</p>
</td></tr>
<tr><td class="val" id="name">name</td><td class="desc">
<p>The name of the interface in the module.</p>
</td></tr>
</table>

<hr>

## FT_Module_Class

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Module_Class_
  {
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>               module_flags;
    <a href="../ft2-basic_types/#ft_long">FT_Long</a>                module_size;
    <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_string">FT_String</a>*       module_name;
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>               module_version;
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>               module_requires;

    <span class="keyword">const</span> <span class="keyword">void</span>*            module_interface;

    <a href="../ft2-module_management/#ft_module_constructor">FT_Module_Constructor</a>  module_init;
    <a href="../ft2-module_management/#ft_module_destructor">FT_Module_Destructor</a>   module_done;
    <a href="../ft2-module_management/#ft_module_requester">FT_Module_Requester</a>    get_interface;

  } <b>FT_Module_Class</b>;
</pre>
</div>


The module class descriptor.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="module_flags">module_flags</td><td class="desc">
<p>Bit flags describing the module.</p>
</td></tr>
<tr><td class="val" id="module_size">module_size</td><td class="desc">
<p>The size of one module object/instance in bytes.</p>
</td></tr>
<tr><td class="val" id="module_name">module_name</td><td class="desc">
<p>The name of the module.</p>
</td></tr>
<tr><td class="val" id="module_version">module_version</td><td class="desc">
<p>The version, as a 16.16 fixed number (major.minor).</p>
</td></tr>
<tr><td class="val" id="module_requires">module_requires</td><td class="desc">
<p>The version of FreeType this module requires, as a 16.16 fixed number (major.minor). Starts at version 2.0, i.e., 0x20000.</p>
</td></tr>
<tr><td class="val" id="module_init">module_init</td><td class="desc">
<p>The initializing function.</p>
</td></tr>
<tr><td class="val" id="module_done">module_done</td><td class="desc">
<p>The finalizing function.</p>
</td></tr>
<tr><td class="val" id="get_interface">get_interface</td><td class="desc">
<p>The interface requesting function.</p>
</td></tr>
</table>

<hr>

## FT_Add_Module

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Add_Module</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>              library,
                 <span class="keyword">const</span> <a href="../ft2-module_management/#ft_module_class">FT_Module_Class</a>*  clazz );
</pre>
</div>


Add a new module to a given library instance.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the library object.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="clazz">clazz</td><td class="desc">
<p>A pointer to class descriptor for the module.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

An error will be returned if a module already exists by that name, or if the module requires a version of FreeType that is too great.

<hr>

## FT_Get_Module

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-module_management/#ft_module">FT_Module</a> )
  <b>FT_Get_Module</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>   library,
                 <span class="keyword">const</span> <span class="keyword">char</span>*  module_name );
</pre>
</div>


Find a module by its name.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the library object.</p>
</td></tr>
<tr><td class="val" id="module_name">module_name</td><td class="desc">
<p>The module's name (as an ASCII string).</p>
</td></tr>
</table>

<h4>return</h4>

A module handle. 0&nbsp;if none was found.

<h4>note</h4>

FreeType's internal modules aren't documented very well, and you should look up the source code for details.

<hr>

## FT_Remove_Module

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Remove_Module</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>  library,
                    <a href="../ft2-module_management/#ft_module">FT_Module</a>   module );
</pre>
</div>


Remove a given module from a library instance.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to a library object.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="module">module</td><td class="desc">
<p>A handle to a module object.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The module object is destroyed by the function in case of success.

<hr>

## FT_Add_Default_Modules

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Add_Default_Modules</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>  library );
</pre>
</div>


Add the set of default drivers to a given library object. This is only useful when you create a library object with <a href="../ft2-module_management/#ft_new_library">FT_New_Library</a> (usually to plug a custom memory manager).

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to a new library object.</p>
</td></tr>
</table>

<hr>

## FT_Property_Set

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Property_Set</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>        library,
                   <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_string">FT_String</a>*  module_name,
                   <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_string">FT_String</a>*  property_name,
                   <span class="keyword">const</span> <span class="keyword">void</span>*       value );
</pre>
</div>


Set a property for a given module.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the library the module is part of.</p>
</td></tr>
<tr><td class="val" id="module_name">module_name</td><td class="desc">
<p>The module name.</p>
</td></tr>
<tr><td class="val" id="property_name">property_name</td><td class="desc">
<p>The property name. Properties are described in section &lsquo;<a href="../ft2-properties/#properties">Driver properties</a>&rsquo;.</p>
<p>Note that only a few modules have properties.</p>
</td></tr>
<tr><td class="val" id="value">value</td><td class="desc">
<p>A generic pointer to a variable or structure that gives the new value of the property. The exact definition of &lsquo;value&rsquo; is dependent on the property; see section &lsquo;<a href="../ft2-properties/#properties">Driver properties</a>&rsquo;.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

If &lsquo;module_name&rsquo; isn't a valid module name, or &lsquo;property_name&rsquo; doesn't specify a valid property, or if &lsquo;value&rsquo; doesn't represent a valid value for the given property, an error is returned.

The following example sets property &lsquo;bar&rsquo; (a simple integer) in module &lsquo;foo&rsquo; to value&nbsp;1.
```
  FT_UInt  bar;


  bar = 1;
  FT_Property_Set( library, "foo", "bar", &bar );
```

Note that the FreeType Cache sub-system doesn't recognize module property changes. To avoid glyph lookup confusion within the cache you should call <a href="../ft2-cache_subsystem/#ftc_manager_reset">FTC_Manager_Reset</a> to completely flush the cache if a module property gets changed after <a href="../ft2-cache_subsystem/#ftc_manager_new">FTC_Manager_New</a> has been called.

It is not possible to set properties of the FreeType Cache sub-system itself with FT_Property_Set; use ?FTC_Property_Set? instead.

<h4>since</h4>

2.4.11

<hr>

## FT_Property_Get

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Property_Get</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>        library,
                   <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_string">FT_String</a>*  module_name,
                   <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_string">FT_String</a>*  property_name,
                   <span class="keyword">void</span>*             value );
</pre>
</div>


Get a module's property value.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the library the module is part of.</p>
</td></tr>
<tr><td class="val" id="module_name">module_name</td><td class="desc">
<p>The module name.</p>
</td></tr>
<tr><td class="val" id="property_name">property_name</td><td class="desc">
<p>The property name. Properties are described in section &lsquo;<a href="../ft2-properties/#properties">Driver properties</a>&rsquo;.</p>
</td></tr>
</table>

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="value">value</td><td class="desc">
<p>A generic pointer to a variable or structure that gives the value of the property. The exact definition of &lsquo;value&rsquo; is dependent on the property; see section &lsquo;<a href="../ft2-properties/#properties">Driver properties</a>&rsquo;.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

If &lsquo;module_name&rsquo; isn't a valid module name, or &lsquo;property_name&rsquo; doesn't specify a valid property, or if &lsquo;value&rsquo; doesn't represent a valid value for the given property, an error is returned.

The following example gets property &lsquo;baz&rsquo; (a range) in module &lsquo;foo&rsquo;.
```
  typedef  range_
  {
    FT_Int32  min;
    FT_Int32  max;

  } range;

  range  baz;


  FT_Property_Get( library, "foo", "baz", &baz );
```

It is not possible to retrieve properties of the FreeType Cache sub-system with FT_Property_Get; use ?FTC_Property_Get? instead.

<h4>since</h4>

2.4.11

<hr>

## FT_Set_Default_Properties

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Set_Default_Properties</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>  library );
</pre>
</div>


If compilation option FT_CONFIG_OPTION_ENVIRONMENT_PROPERTIES is set, this function reads the &lsquo;FREETYPE_PROPERTIES&rsquo; environment variable to control driver properties. See section &lsquo;<a href="../ft2-properties/#properties">Driver properties</a>&rsquo; for more.

If the compilation option is not set, this function does nothing.

&lsquo;FREETYPE_PROPERTIES&rsquo; has the following syntax form (broken here into multiple lines for better readability).
```
  <optional whitespace>
  <module-name1> ':'
  <property-name1> '=' <property-value1>
  <whitespace>
  <module-name2> ':'
  <property-name2> '=' <property-value2>
  ...
```

Example:
```
  FREETYPE_PROPERTIES=truetype:interpreter-version=35 \
                      cff:no-stem-darkening=1 \
                      autofitter:warping=1
```

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to a new library object.</p>
</td></tr>
</table>

<h4>since</h4>

2.8

<hr>

## FT_New_Library

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_New_Library</b>( <a href="../ft2-system_interface/#ft_memory">FT_Memory</a>    memory,
                  <a href="../ft2-base_interface/#ft_library">FT_Library</a>  *alibrary );
</pre>
</div>


This function is used to create a new FreeType library instance from a given memory object. It is thus possible to use libraries with distinct memory allocators within the same program. Note, however, that the used <a href="../ft2-system_interface/#ft_memory">FT_Memory</a> structure is expected to remain valid for the life of the <a href="../ft2-base_interface/#ft_library">FT_Library</a> object.

Normally, you would call this function (followed by a call to <a href="../ft2-module_management/#ft_add_default_modules">FT_Add_Default_Modules</a> or a series of calls to <a href="../ft2-module_management/#ft_add_module">FT_Add_Module</a>, and a call to <a href="../ft2-module_management/#ft_set_default_properties">FT_Set_Default_Properties</a>) instead of <a href="../ft2-base_interface/#ft_init_freetype">FT_Init_FreeType</a> to initialize the FreeType library.

Don't use <a href="../ft2-base_interface/#ft_done_freetype">FT_Done_FreeType</a> but <a href="../ft2-module_management/#ft_done_library">FT_Done_Library</a> to destroy a library instance.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="memory">memory</td><td class="desc">
<p>A handle to the original memory object.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="alibrary">alibrary</td><td class="desc">
<p>A pointer to handle of a new library object.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

See the discussion of reference counters in the description of <a href="../ft2-module_management/#ft_reference_library">FT_Reference_Library</a>.

<hr>

## FT_Done_Library

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Done_Library</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>  library );
</pre>
</div>


Discard a given library object. This closes all drivers and discards all resource objects.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the target library.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

See the discussion of reference counters in the description of <a href="../ft2-module_management/#ft_reference_library">FT_Reference_Library</a>.

<hr>

## FT_Reference_Library

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Reference_Library</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>  library );
</pre>
</div>


A counter gets initialized to&nbsp;1 at the time an <a href="../ft2-base_interface/#ft_library">FT_Library</a> structure is created. This function increments the counter. <a href="../ft2-module_management/#ft_done_library">FT_Done_Library</a> then only destroys a library if the counter is&nbsp;1, otherwise it simply decrements the counter.

This function helps in managing life-cycles of structures that reference <a href="../ft2-base_interface/#ft_library">FT_Library</a> objects.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to a target library object.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>since</h4>

2.4.2

<hr>

## FT_Renderer

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_RendererRec_*  <b>FT_Renderer</b>;
</pre>
</div>


A handle to a given FreeType renderer. A renderer is a module in charge of converting a glyph's outline image to a bitmap. It supports a single glyph image format, and one or more target surface depths.

<hr>

## FT_Renderer_Class

Defined in FT_RENDER_H (freetype/ftrender.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Renderer_Class_
  {
    <a href="../ft2-module_management/#ft_module_class">FT_Module_Class</a>            root;

    <a href="../ft2-basic_types/#ft_glyph_format">FT_Glyph_Format</a>            glyph_format;

    FT_Renderer_RenderFunc     render_glyph;
    FT_Renderer_TransformFunc  transform_glyph;
    FT_Renderer_GetCBoxFunc    get_glyph_cbox;
    FT_Renderer_SetModeFunc    set_mode;

    <a href="../ft2-raster/#ft_raster_funcs">FT_Raster_Funcs</a>*           raster_class;

  } <b>FT_Renderer_Class</b>;
</pre>
</div>


The renderer module class descriptor.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="root">root</td><td class="desc">
<p>The root <a href="../ft2-module_management/#ft_module_class">FT_Module_Class</a> fields.</p>
</td></tr>
<tr><td class="val" id="glyph_format">glyph_format</td><td class="desc">
<p>The glyph image format this renderer handles.</p>
</td></tr>
<tr><td class="val" id="render_glyph">render_glyph</td><td class="desc">
<p>A method used to render the image that is in a given glyph slot into a bitmap.</p>
</td></tr>
<tr><td class="val" id="transform_glyph">transform_glyph</td><td class="desc">
<p>A method used to transform the image that is in a given glyph slot.</p>
</td></tr>
<tr><td class="val" id="get_glyph_cbox">get_glyph_cbox</td><td class="desc">
<p>A method used to access the glyph's cbox.</p>
</td></tr>
<tr><td class="val" id="set_mode">set_mode</td><td class="desc">
<p>A method used to pass additional parameters.</p>
</td></tr>
<tr><td class="val" id="raster_class">raster_class</td><td class="desc">
<p>For <a href="../ft2-basic_types/#ft_glyph_format">FT_GLYPH_FORMAT_OUTLINE</a> renderers only. This is a pointer to its raster's class.</p>
</td></tr>
</table>

<hr>

## FT_Get_Renderer

Defined in FT_RENDER_H (freetype/ftrender.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-module_management/#ft_renderer">FT_Renderer</a> )
  <b>FT_Get_Renderer</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>       library,
                   <a href="../ft2-basic_types/#ft_glyph_format">FT_Glyph_Format</a>  format );
</pre>
</div>


Retrieve the current renderer for a given glyph format.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the library object.</p>
</td></tr>
<tr><td class="val" id="format">format</td><td class="desc">
<p>The glyph format.</p>
</td></tr>
</table>

<h4>return</h4>

A renderer handle. 0&nbsp;if none found.

<h4>note</h4>

An error will be returned if a module already exists by that name, or if the module requires a version of FreeType that is too great.

To add a new renderer, simply use <a href="../ft2-module_management/#ft_add_module">FT_Add_Module</a>. To retrieve a renderer by its name, use <a href="../ft2-module_management/#ft_get_module">FT_Get_Module</a>.

<hr>

## FT_Set_Renderer

Defined in FT_RENDER_H (freetype/ftrender.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Set_Renderer</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>     library,
                   <a href="../ft2-module_management/#ft_renderer">FT_Renderer</a>    renderer,
                   <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>        num_params,
                   <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a>*  parameters );
</pre>
</div>


Set the current renderer to use, and set additional mode.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the library object.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="renderer">renderer</td><td class="desc">
<p>A handle to the renderer object.</p>
</td></tr>
<tr><td class="val" id="num_params">num_params</td><td class="desc">
<p>The number of additional parameters.</p>
</td></tr>
<tr><td class="val" id="parameters">parameters</td><td class="desc">
<p>Additional parameters.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

In case of success, the renderer will be used to convert glyph images in the renderer's known format into bitmaps.

This doesn't change the current renderer for other formats.

Currently, no FreeType renderer module uses &lsquo;parameters&rsquo;; you should thus always pass NULL as the value.

<hr>

## FT_Set_Debug_Hook

Defined in FT_MODULE_H (freetype/ftmodapi.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Set_Debug_Hook</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>         library,
                     <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>            hook_index,
                     FT_DebugHook_Func  debug_hook );
</pre>
</div>


Set a debug hook function for debugging the interpreter of a font format.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the library object.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="hook_index">hook_index</td><td class="desc">
<p>The index of the debug hook. You should use the values defined in &lsquo;ftobjs.h&rsquo;, e.g., &lsquo;FT_DEBUG_HOOK_TRUETYPE&rsquo;.</p>
</td></tr>
<tr><td class="val" id="debug_hook">debug_hook</td><td class="desc">
<p>The function used to debug the interpreter.</p>
</td></tr>
</table>

<h4>note</h4>

Currently, four debug hook slots are available, but only two (for the TrueType and the Type&nbsp;1 interpreter) are defined.

Since the internal headers of FreeType are no longer installed, the symbol &lsquo;FT_DEBUG_HOOK_TRUETYPE&rsquo; isn't available publicly. This is a bug and will be fixed in a forthcoming release.

<hr>

## FT_Driver

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_DriverRec_*  <b>FT_Driver</b>;
</pre>
</div>


A handle to a given FreeType font driver object. A font driver is a module capable of creating faces from font files.

<hr>

