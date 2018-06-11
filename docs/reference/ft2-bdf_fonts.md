[Docs](ft2-index.md) &raquo; [Format-Specific API](ft2-toc.md#format-specific-api) &raquo; BDF and PCF Files

-------------------------------

# BDF and PCF Files

## Synopsis

This section contains the declaration of functions specific to BDF and PCF fonts.

## BDF_PropertyType

Defined in FT_BDF_H (freetype/ftbdf.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  BDF_PropertyType_
  {
    <a href="../ft2-bdf_fonts/#bdf_property_type_none">BDF_PROPERTY_TYPE_NONE</a>     = 0,
    <a href="../ft2-bdf_fonts/#bdf_property_type_atom">BDF_PROPERTY_TYPE_ATOM</a>     = 1,
    <a href="../ft2-bdf_fonts/#bdf_property_type_integer">BDF_PROPERTY_TYPE_INTEGER</a>  = 2,
    <a href="../ft2-bdf_fonts/#bdf_property_type_cardinal">BDF_PROPERTY_TYPE_CARDINAL</a> = 3

  } <b>BDF_PropertyType</b>;
</pre>
</div>


A list of BDF property types.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="bdf_property_type_none">BDF_PROPERTY_TYPE_NONE</td><td class="desc">
<p>Value&nbsp;0 is used to indicate a missing property.</p>
</td></tr>
<tr><td class="val" id="bdf_property_type_atom">BDF_PROPERTY_TYPE_ATOM</td><td class="desc">
<p>Property is a string atom.</p>
</td></tr>
<tr><td class="val" id="bdf_property_type_integer">BDF_PROPERTY_TYPE_INTEGER</td><td class="desc">
<p>Property is a 32-bit signed integer.</p>
</td></tr>
<tr><td class="val" id="bdf_property_type_cardinal">BDF_PROPERTY_TYPE_CARDINAL</td><td class="desc">
<p>Property is a 32-bit unsigned integer.</p>
</td></tr>
</table>

<hr>

## BDF_Property

Defined in FT_BDF_H (freetype/ftbdf.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> BDF_PropertyRec_*  <b>BDF_Property</b>;
</pre>
</div>


A handle to a <a href="../ft2-bdf_fonts/#bdf_propertyrec">BDF_PropertyRec</a> structure to model a given BDF/PCF property.

<hr>

## BDF_PropertyRec

Defined in FT_BDF_H (freetype/ftbdf.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  BDF_PropertyRec_
  {
    <a href="../ft2-bdf_fonts/#bdf_propertytype">BDF_PropertyType</a>  type;
    <span class="keyword">union</span> {
      <span class="keyword">const</span> <span class="keyword">char</span>*     atom;
      <a href="../ft2-basic_types/#ft_int32">FT_Int32</a>        integer;
      <a href="../ft2-basic_types/#ft_uint32">FT_UInt32</a>       cardinal;

    } u;

  } <b>BDF_PropertyRec</b>;
</pre>
</div>


This structure models a given BDF/PCF property.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="type">type</td><td class="desc">
<p>The property type.</p>
</td></tr>
<tr><td class="val" id="u.atom">u.atom</td><td class="desc">
<p>The atom string, if type is <a href="../ft2-bdf_fonts/#bdf_propertytype">BDF_PROPERTY_TYPE_ATOM</a>. May be NULL, indicating an empty string.</p>
</td></tr>
<tr><td class="val" id="u.integer">u.integer</td><td class="desc">
<p>A signed integer, if type is <a href="../ft2-bdf_fonts/#bdf_propertytype">BDF_PROPERTY_TYPE_INTEGER</a>.</p>
</td></tr>
<tr><td class="val" id="u.cardinal">u.cardinal</td><td class="desc">
<p>An unsigned integer, if type is <a href="../ft2-bdf_fonts/#bdf_propertytype">BDF_PROPERTY_TYPE_CARDINAL</a>.</p>
</td></tr>
</table>

<hr>

## FT_Get_BDF_Charset_ID

Defined in FT_BDF_H (freetype/ftbdf.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_BDF_Charset_ID</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>       face,
                         <span class="keyword">const</span> <span class="keyword">char</span>*  *acharset_encoding,
                         <span class="keyword">const</span> <span class="keyword">char</span>*  *acharset_registry );
</pre>
</div>


Retrieve a BDF font character set identity, according to the BDF specification.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="acharset_encoding">acharset_encoding</td><td class="desc">
<p>Charset encoding, as a C&nbsp;string, owned by the face.</p>
</td></tr>
<tr><td class="val" id="acharset_registry">acharset_registry</td><td class="desc">
<p>Charset registry, as a C&nbsp;string, owned by the face.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function only works with BDF faces, returning an error otherwise.

<hr>

## FT_Get_BDF_Property

Defined in FT_BDF_H (freetype/ftbdf.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_BDF_Property</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>           face,
                       <span class="keyword">const</span> <span class="keyword">char</span>*       prop_name,
                       <a href="../ft2-bdf_fonts/#bdf_propertyrec">BDF_PropertyRec</a>  *aproperty );
</pre>
</div>


Retrieve a BDF property from a BDF or PCF font file.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
<tr><td class="val" id="name">name</td><td class="desc">
<p>The property name.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aproperty">aproperty</td><td class="desc">
<p>The property.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function works with BDF _and_ PCF fonts. It returns an error otherwise. It also returns an error if the property is not in the font.

A &lsquo;property&rsquo; is a either key-value pair within the STARTPROPERTIES ... ENDPROPERTIES block of a BDF font or a key-value pair from the &lsquo;info-&gt;props&rsquo; array within a &lsquo;FontRec&rsquo; structure of a PCF font.

Integer properties are always stored as &lsquo;signed&rsquo; within PCF fonts; consequently, <a href="../ft2-bdf_fonts/#bdf_propertytype">BDF_PROPERTY_TYPE_CARDINAL</a> is a possible return value for BDF fonts only.

In case of error, &lsquo;aproperty-&gt;type&rsquo; is always set to <a href="../ft2-bdf_fonts/#bdf_propertytype">BDF_PROPERTY_TYPE_NONE</a>.

<hr>

