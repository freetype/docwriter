[Docs](ft2-index.md) &raquo; [Format-Specific API](ft2-toc.md#format-specific-api) &raquo; Type 1 Tables

-------------------------------

# Type 1 Tables

## Synopsis

This section contains the definition of Type 1-specific tables, including structures related to other PostScript font formats.

## PS_FontInfoRec

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  PS_FontInfoRec_
  {
    <a href="../ft2-basic_types/#ft_string">FT_String</a>*  version;
    <a href="../ft2-basic_types/#ft_string">FT_String</a>*  notice;
    <a href="../ft2-basic_types/#ft_string">FT_String</a>*  full_name;
    <a href="../ft2-basic_types/#ft_string">FT_String</a>*  family_name;
    <a href="../ft2-basic_types/#ft_string">FT_String</a>*  weight;
    <a href="../ft2-basic_types/#ft_long">FT_Long</a>     italic_angle;
    <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>     is_fixed_pitch;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>    underline_position;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>   underline_thickness;

  } <b>PS_FontInfoRec</b>;
</pre>
</div>


A structure used to model a Type&nbsp;1 or Type&nbsp;2 FontInfo dictionary. Note that for Multiple Master fonts, each instance has its own FontInfo dictionary.

<hr>

## PS_FontInfo

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> PS_FontInfoRec_*  <b>PS_FontInfo</b>;
</pre>
</div>


A handle to a <a href="../ft2-type1_tables/#ps_fontinforec">PS_FontInfoRec</a> structure.

<hr>

## PS_PrivateRec

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  PS_PrivateRec_
  {
    <a href="../ft2-basic_types/#ft_int">FT_Int</a>     unique_id;
    <a href="../ft2-basic_types/#ft_int">FT_Int</a>     lenIV;

    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    num_blue_values;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    num_other_blues;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    num_family_blues;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    num_family_other_blues;

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   blue_values[14];
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   other_blues[10];

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   family_blues      [14];
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   family_other_blues[10];

    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>   blue_scale;
    <a href="../ft2-basic_types/#ft_int">FT_Int</a>     blue_shift;
    <a href="../ft2-basic_types/#ft_int">FT_Int</a>     blue_fuzz;

    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  standard_width[1];
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  standard_height[1];

    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    num_snap_widths;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    num_snap_heights;
    <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>    force_bold;
    <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>    round_stem_up;

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   snap_widths [13];  /* including std width  */
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   snap_heights[13];  /* including std height */

    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>   expansion_factor;

    <a href="../ft2-basic_types/#ft_long">FT_Long</a>    language_group;
    <a href="../ft2-basic_types/#ft_long">FT_Long</a>    password;

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   min_feature[2];

  } <b>PS_PrivateRec</b>;
</pre>
</div>


A structure used to model a Type&nbsp;1 or Type&nbsp;2 private dictionary. Note that for Multiple Master fonts, each instance has its own Private dictionary.

<hr>

## PS_Private

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> PS_PrivateRec_*  <b>PS_Private</b>;
</pre>
</div>


A handle to a <a href="../ft2-type1_tables/#ps_privaterec">PS_PrivateRec</a> structure.

<hr>

## CID_FaceDictRec

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  CID_FaceDictRec_
  {
    <a href="../ft2-type1_tables/#ps_privaterec">PS_PrivateRec</a>  private_dict;

    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>        len_buildchar;
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>       forcebold_threshold;
    <a href="../ft2-basic_types/#ft_pos">FT_Pos</a>         stroke_width;
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>       expansion_factor;

    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>        paint_type;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>        font_type;
    <a href="../ft2-basic_types/#ft_matrix">FT_Matrix</a>      font_matrix;
    <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>      font_offset;

    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>        num_subrs;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>       subrmap_offset;
    <a href="../ft2-basic_types/#ft_int">FT_Int</a>         sd_bytes;

  } <b>CID_FaceDictRec</b>;
</pre>
</div>


A structure used to represent data in a CID top-level dictionary.

<hr>

## CID_FaceDict

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> CID_FaceDictRec_*  <b>CID_FaceDict</b>;
</pre>
</div>


A handle to a <a href="../ft2-type1_tables/#cid_facedictrec">CID_FaceDictRec</a> structure.

<hr>

## CID_FaceInfoRec

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  CID_FaceInfoRec_
  {
    <a href="../ft2-basic_types/#ft_string">FT_String</a>*      cid_font_name;
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>        cid_version;
    <a href="../ft2-basic_types/#ft_int">FT_Int</a>          cid_font_type;

    <a href="../ft2-basic_types/#ft_string">FT_String</a>*      registry;
    <a href="../ft2-basic_types/#ft_string">FT_String</a>*      ordering;
    <a href="../ft2-basic_types/#ft_int">FT_Int</a>          supplement;

    <a href="../ft2-type1_tables/#ps_fontinforec">PS_FontInfoRec</a>  font_info;
    <a href="../ft2-basic_types/#ft_bbox">FT_BBox</a>         font_bbox;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>        uid_base;

    <a href="../ft2-basic_types/#ft_int">FT_Int</a>          num_xuid;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>        xuid[16];

    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>        cidmap_offset;
    <a href="../ft2-basic_types/#ft_int">FT_Int</a>          fd_bytes;
    <a href="../ft2-basic_types/#ft_int">FT_Int</a>          gd_bytes;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>        cid_count;

    <a href="../ft2-basic_types/#ft_int">FT_Int</a>          num_dicts;
    <a href="../ft2-type1_tables/#cid_facedict">CID_FaceDict</a>    font_dicts;

    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>        data_offset;

  } <b>CID_FaceInfoRec</b>;
</pre>
</div>


A structure used to represent CID Face information.

<hr>

## CID_FaceInfo

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> CID_FaceInfoRec_*  <b>CID_FaceInfo</b>;
</pre>
</div>


A handle to a <a href="../ft2-type1_tables/#cid_faceinforec">CID_FaceInfoRec</a> structure.

<hr>

## FT_Has_PS_Glyph_Names

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_int">FT_Int</a> )
  <b>FT_Has_PS_Glyph_Names</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>  face );
</pre>
</div>


Return true if a given face provides reliable PostScript glyph names. This is similar to using the <a href="../ft2-base_interface/#ft_has_glyph_names">FT_HAS_GLYPH_NAMES</a> macro, except that certain fonts (mostly TrueType) contain incorrect glyph name tables.

When this function returns true, the caller is sure that the glyph names returned by <a href="../ft2-base_interface/#ft_get_glyph_name">FT_Get_Glyph_Name</a> are reliable.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>face handle</p>
</td></tr>
</table>

<h4>return</h4>

Boolean. True if glyph names are reliable.

<hr>

## FT_Get_PS_Font_Info

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_PS_Font_Info</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>      face,
                       <a href="../ft2-type1_tables/#ps_fontinfo">PS_FontInfo</a>  afont_info );
</pre>
</div>


Retrieve the <a href="../ft2-type1_tables/#ps_fontinforec">PS_FontInfoRec</a> structure corresponding to a given PostScript font.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>PostScript face handle.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="afont_info">afont_info</td><td class="desc">
<p>Output font info structure pointer.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

String pointers within the <a href="../ft2-type1_tables/#ps_fontinforec">PS_FontInfoRec</a> structure are owned by the face and don't need to be freed by the caller. Missing entries in the font's FontInfo dictionary are represented by NULL pointers.

If the font's format is not PostScript-based, this function will return the &lsquo;FT_Err_Invalid_Argument&rsquo; error code.

<hr>

## FT_Get_PS_Font_Private

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_PS_Font_Private</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>     face,
                          <a href="../ft2-type1_tables/#ps_private">PS_Private</a>  afont_private );
</pre>
</div>


Retrieve the <a href="../ft2-type1_tables/#ps_privaterec">PS_PrivateRec</a> structure corresponding to a given PostScript font.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>PostScript face handle.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="afont_private">afont_private</td><td class="desc">
<p>Output private dictionary structure pointer.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The string pointers within the <a href="../ft2-type1_tables/#ps_privaterec">PS_PrivateRec</a> structure are owned by the face and don't need to be freed by the caller.

If the font's format is not PostScript-based, this function returns the &lsquo;FT_Err_Invalid_Argument&rsquo; error code.

<hr>

## FT_Get_PS_Font_Value

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_long">FT_Long</a> )
  <b>FT_Get_PS_Font_Value</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>       face,
                        <a href="../ft2-type1_tables/#ps_dict_keys">PS_Dict_Keys</a>  key,
                        <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>       idx,
                        <span class="keyword">void</span>         *value,
                        <a href="../ft2-basic_types/#ft_long">FT_Long</a>       value_len );
</pre>
</div>


Retrieve the value for the supplied key from a PostScript font.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>PostScript face handle.</p>
</td></tr>
<tr><td class="val" id="key">key</td><td class="desc">
<p>An enumeration value representing the dictionary key to retrieve.</p>
</td></tr>
<tr><td class="val" id="idx">idx</td><td class="desc">
<p>For array values, this specifies the index to be returned.</p>
</td></tr>
<tr><td class="val" id="value">value</td><td class="desc">
<p>A pointer to memory into which to write the value.</p>
</td></tr>
<tr><td class="val" id="valen_len">valen_len</td><td class="desc">
<p>The size, in bytes, of the memory supplied for the value.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="value">value</td><td class="desc">
<p>The value matching the above key, if it exists.</p>
</td></tr>
</table>

<h4>return</h4>

The amount of memory (in bytes) required to hold the requested value (if it exists, -1 otherwise).

<h4>note</h4>

The values returned are not pointers into the internal structures of the face, but are &lsquo;fresh&rsquo; copies, so that the memory containing them belongs to the calling application. This also enforces the &lsquo;read-only&rsquo; nature of these values, i.e., this function cannot be used to manipulate the face.

&lsquo;value&rsquo; is a void pointer because the values returned can be of various types.

If either &lsquo;value&rsquo; is NULL or &lsquo;value_len&rsquo; is too small, just the required memory size for the requested entry is returned.

The &lsquo;idx&rsquo; parameter is used, not only to retrieve elements of, for example, the FontMatrix or FontBBox, but also to retrieve name keys from the CharStrings dictionary, and the charstrings themselves. It is ignored for atomic values.

PS_DICT_BLUE_SCALE returns a value that is scaled up by 1000. To get the value as in the font stream, you need to divide by 65536000.0 (to remove the FT_Fixed scale, and the x1000 scale).

IMPORTANT: Only key/value pairs read by the FreeType interpreter can be retrieved. So, for example, PostScript procedures such as NP, ND, and RD are not available. Arbitrary keys are, obviously, not be available either.

If the font's format is not PostScript-based, this function returns the &lsquo;FT_Err_Invalid_Argument&rsquo; error code.

<h4>since</h4>

2.4.8

<hr>

## T1_Blend_Flags

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  T1_Blend_Flags_
  {
    /* required fields in a FontInfo blend dictionary */
    <a href="../ft2-type1_tables/#t1_blend_underline_position">T1_BLEND_UNDERLINE_POSITION</a> = 0,
    <a href="../ft2-type1_tables/#t1_blend_underline_thickness">T1_BLEND_UNDERLINE_THICKNESS</a>,
    <a href="../ft2-type1_tables/#t1_blend_italic_angle">T1_BLEND_ITALIC_ANGLE</a>,

    /* required fields in a Private blend dictionary */
    <a href="../ft2-type1_tables/#t1_blend_blue_values">T1_BLEND_BLUE_VALUES</a>,
    <a href="../ft2-type1_tables/#t1_blend_other_blues">T1_BLEND_OTHER_BLUES</a>,
    <a href="../ft2-type1_tables/#t1_blend_standard_width">T1_BLEND_STANDARD_WIDTH</a>,
    <a href="../ft2-type1_tables/#t1_blend_standard_height">T1_BLEND_STANDARD_HEIGHT</a>,
    <a href="../ft2-type1_tables/#t1_blend_stem_snap_widths">T1_BLEND_STEM_SNAP_WIDTHS</a>,
    <a href="../ft2-type1_tables/#t1_blend_stem_snap_heights">T1_BLEND_STEM_SNAP_HEIGHTS</a>,
    <a href="../ft2-type1_tables/#t1_blend_blue_scale">T1_BLEND_BLUE_SCALE</a>,
    <a href="../ft2-type1_tables/#t1_blend_blue_shift">T1_BLEND_BLUE_SHIFT</a>,
    <a href="../ft2-type1_tables/#t1_blend_family_blues">T1_BLEND_FAMILY_BLUES</a>,
    <a href="../ft2-type1_tables/#t1_blend_family_other_blues">T1_BLEND_FAMILY_OTHER_BLUES</a>,
    <a href="../ft2-type1_tables/#t1_blend_force_bold">T1_BLEND_FORCE_BOLD</a>,

    T1_BLEND_MAX    /* do not remove */

  } <b>T1_Blend_Flags</b>;


  /* these constants are deprecated; use the corresponding */
  /* `<b>T1_Blend_Flags</b>' values instead                       */
#<span class="keyword">define</span> t1_blend_underline_position   <a href="../ft2-type1_tables/#t1_blend_underline_position">T1_BLEND_UNDERLINE_POSITION</a>
#<span class="keyword">define</span> t1_blend_underline_thickness  <a href="../ft2-type1_tables/#t1_blend_underline_thickness">T1_BLEND_UNDERLINE_THICKNESS</a>
#<span class="keyword">define</span> t1_blend_italic_angle         <a href="../ft2-type1_tables/#t1_blend_italic_angle">T1_BLEND_ITALIC_ANGLE</a>
#<span class="keyword">define</span> t1_blend_blue_values          <a href="../ft2-type1_tables/#t1_blend_blue_values">T1_BLEND_BLUE_VALUES</a>
#<span class="keyword">define</span> t1_blend_other_blues          <a href="../ft2-type1_tables/#t1_blend_other_blues">T1_BLEND_OTHER_BLUES</a>
#<span class="keyword">define</span> t1_blend_standard_widths      <a href="../ft2-type1_tables/#t1_blend_standard_width">T1_BLEND_STANDARD_WIDTH</a>
#<span class="keyword">define</span> t1_blend_standard_height      <a href="../ft2-type1_tables/#t1_blend_standard_height">T1_BLEND_STANDARD_HEIGHT</a>
#<span class="keyword">define</span> t1_blend_stem_snap_widths     <a href="../ft2-type1_tables/#t1_blend_stem_snap_widths">T1_BLEND_STEM_SNAP_WIDTHS</a>
#<span class="keyword">define</span> t1_blend_stem_snap_heights    <a href="../ft2-type1_tables/#t1_blend_stem_snap_heights">T1_BLEND_STEM_SNAP_HEIGHTS</a>
#<span class="keyword">define</span> t1_blend_blue_scale           <a href="../ft2-type1_tables/#t1_blend_blue_scale">T1_BLEND_BLUE_SCALE</a>
#<span class="keyword">define</span> t1_blend_blue_shift           <a href="../ft2-type1_tables/#t1_blend_blue_shift">T1_BLEND_BLUE_SHIFT</a>
#<span class="keyword">define</span> t1_blend_family_blues         <a href="../ft2-type1_tables/#t1_blend_family_blues">T1_BLEND_FAMILY_BLUES</a>
#<span class="keyword">define</span> t1_blend_family_other_blues   <a href="../ft2-type1_tables/#t1_blend_family_other_blues">T1_BLEND_FAMILY_OTHER_BLUES</a>
#<span class="keyword">define</span> t1_blend_force_bold           <a href="../ft2-type1_tables/#t1_blend_force_bold">T1_BLEND_FORCE_BOLD</a>
#<span class="keyword">define</span> t1_blend_max                  T1_BLEND_MAX
</pre>
</div>


A set of flags used to indicate which fields are present in a given blend dictionary (font info or private). Used to support Multiple Masters fonts.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="t1_blend_underline_position">T1_BLEND_UNDERLINE_POSITION</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_underline_thickness">T1_BLEND_UNDERLINE_THICKNESS</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_italic_angle">T1_BLEND_ITALIC_ANGLE</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_blue_values">T1_BLEND_BLUE_VALUES</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_other_blues">T1_BLEND_OTHER_BLUES</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_standard_width">T1_BLEND_STANDARD_WIDTH</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_standard_height">T1_BLEND_STANDARD_HEIGHT</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_stem_snap_widths">T1_BLEND_STEM_SNAP_WIDTHS</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_stem_snap_heights">T1_BLEND_STEM_SNAP_HEIGHTS</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_blue_scale">T1_BLEND_BLUE_SCALE</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_blue_shift">T1_BLEND_BLUE_SHIFT</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_family_blues">T1_BLEND_FAMILY_BLUES</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_family_other_blues">T1_BLEND_FAMILY_OTHER_BLUES</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_blend_force_bold">T1_BLEND_FORCE_BOLD</td><td class="desc">

</td></tr>
</table>

<hr>

## T1_EncodingType

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  T1_EncodingType_
  {
    <a href="../ft2-type1_tables/#t1_encoding_type_none">T1_ENCODING_TYPE_NONE</a> = 0,
    <a href="../ft2-type1_tables/#t1_encoding_type_array">T1_ENCODING_TYPE_ARRAY</a>,
    <a href="../ft2-type1_tables/#t1_encoding_type_standard">T1_ENCODING_TYPE_STANDARD</a>,
    <a href="../ft2-type1_tables/#t1_encoding_type_isolatin1">T1_ENCODING_TYPE_ISOLATIN1</a>,
    <a href="../ft2-type1_tables/#t1_encoding_type_expert">T1_ENCODING_TYPE_EXPERT</a>

  } <b>T1_EncodingType</b>;
</pre>
</div>


An enumeration describing the &lsquo;Encoding&rsquo; entry in a Type 1 dictionary.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="t1_encoding_type_none">T1_ENCODING_TYPE_NONE</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_encoding_type_array">T1_ENCODING_TYPE_ARRAY</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_encoding_type_standard">T1_ENCODING_TYPE_STANDARD</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_encoding_type_isolatin1">T1_ENCODING_TYPE_ISOLATIN1</td><td class="desc">

</td></tr>
<tr><td class="val" id="t1_encoding_type_expert">T1_ENCODING_TYPE_EXPERT</td><td class="desc">

</td></tr>
</table>

<h4>since</h4>

2.4.8

<hr>

## PS_Dict_Keys

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  PS_Dict_Keys_
  {
    /* conventionally in the font dictionary */
    <a href="../ft2-type1_tables/#ps_dict_font_type">PS_DICT_FONT_TYPE</a>,              /* <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>         */
    <a href="../ft2-type1_tables/#ps_dict_font_matrix">PS_DICT_FONT_MATRIX</a>,            /* <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>        */
    <a href="../ft2-type1_tables/#ps_dict_font_bbox">PS_DICT_FONT_BBOX</a>,              /* <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>        */
    <a href="../ft2-type1_tables/#ps_dict_paint_type">PS_DICT_PAINT_TYPE</a>,             /* <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>         */
    <a href="../ft2-type1_tables/#ps_dict_font_name">PS_DICT_FONT_NAME</a>,              /* <a href="../ft2-basic_types/#ft_string">FT_String</a>*      */
    <a href="../ft2-type1_tables/#ps_dict_unique_id">PS_DICT_UNIQUE_ID</a>,              /* <a href="../ft2-basic_types/#ft_int">FT_Int</a>          */
    <a href="../ft2-type1_tables/#ps_dict_num_char_strings">PS_DICT_NUM_CHAR_STRINGS</a>,       /* <a href="../ft2-basic_types/#ft_int">FT_Int</a>          */
    <a href="../ft2-type1_tables/#ps_dict_char_string_key">PS_DICT_CHAR_STRING_KEY</a>,        /* <a href="../ft2-basic_types/#ft_string">FT_String</a>*      */
    <a href="../ft2-type1_tables/#ps_dict_char_string">PS_DICT_CHAR_STRING</a>,            /* <a href="../ft2-basic_types/#ft_string">FT_String</a>*      */
    <a href="../ft2-type1_tables/#ps_dict_encoding_type">PS_DICT_ENCODING_TYPE</a>,          /* <a href="../ft2-type1_tables/#t1_encodingtype">T1_EncodingType</a> */
    <a href="../ft2-type1_tables/#ps_dict_encoding_entry">PS_DICT_ENCODING_ENTRY</a>,         /* <a href="../ft2-basic_types/#ft_string">FT_String</a>*      */

    /* conventionally in the font Private dictionary */
    <a href="../ft2-type1_tables/#ps_dict_num_subrs">PS_DICT_NUM_SUBRS</a>,              /* <a href="../ft2-basic_types/#ft_int">FT_Int</a>     */
    <a href="../ft2-type1_tables/#ps_dict_subr">PS_DICT_SUBR</a>,                   /* <a href="../ft2-basic_types/#ft_string">FT_String</a>* */
    <a href="../ft2-type1_tables/#ps_dict_std_hw">PS_DICT_STD_HW</a>,                 /* <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  */
    <a href="../ft2-type1_tables/#ps_dict_std_vw">PS_DICT_STD_VW</a>,                 /* <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  */
    <a href="../ft2-type1_tables/#ps_dict_num_blue_values">PS_DICT_NUM_BLUE_VALUES</a>,        /* <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    */
    <a href="../ft2-type1_tables/#ps_dict_blue_value">PS_DICT_BLUE_VALUE</a>,             /* <a href="../ft2-basic_types/#ft_short">FT_Short</a>   */
    <a href="../ft2-type1_tables/#ps_dict_blue_fuzz">PS_DICT_BLUE_FUZZ</a>,              /* <a href="../ft2-basic_types/#ft_int">FT_Int</a>     */
    <a href="../ft2-type1_tables/#ps_dict_num_other_blues">PS_DICT_NUM_OTHER_BLUES</a>,        /* <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    */
    <a href="../ft2-type1_tables/#ps_dict_other_blue">PS_DICT_OTHER_BLUE</a>,             /* <a href="../ft2-basic_types/#ft_short">FT_Short</a>   */
    <a href="../ft2-type1_tables/#ps_dict_num_family_blues">PS_DICT_NUM_FAMILY_BLUES</a>,       /* <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    */
    <a href="../ft2-type1_tables/#ps_dict_family_blue">PS_DICT_FAMILY_BLUE</a>,            /* <a href="../ft2-basic_types/#ft_short">FT_Short</a>   */
    <a href="../ft2-type1_tables/#ps_dict_num_family_other_blues">PS_DICT_NUM_FAMILY_OTHER_BLUES</a>, /* <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    */
    <a href="../ft2-type1_tables/#ps_dict_family_other_blue">PS_DICT_FAMILY_OTHER_BLUE</a>,      /* <a href="../ft2-basic_types/#ft_short">FT_Short</a>   */
    <a href="../ft2-type1_tables/#ps_dict_blue_scale">PS_DICT_BLUE_SCALE</a>,             /* <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>   */
    <a href="../ft2-type1_tables/#ps_dict_blue_shift">PS_DICT_BLUE_SHIFT</a>,             /* <a href="../ft2-basic_types/#ft_int">FT_Int</a>     */
    <a href="../ft2-type1_tables/#ps_dict_num_stem_snap_h">PS_DICT_NUM_STEM_SNAP_H</a>,        /* <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    */
    <a href="../ft2-type1_tables/#ps_dict_stem_snap_h">PS_DICT_STEM_SNAP_H</a>,            /* <a href="../ft2-basic_types/#ft_short">FT_Short</a>   */
    <a href="../ft2-type1_tables/#ps_dict_num_stem_snap_v">PS_DICT_NUM_STEM_SNAP_V</a>,        /* <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    */
    <a href="../ft2-type1_tables/#ps_dict_stem_snap_v">PS_DICT_STEM_SNAP_V</a>,            /* <a href="../ft2-basic_types/#ft_short">FT_Short</a>   */
    <a href="../ft2-type1_tables/#ps_dict_force_bold">PS_DICT_FORCE_BOLD</a>,             /* <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>    */
    <a href="../ft2-type1_tables/#ps_dict_rnd_stem_up">PS_DICT_RND_STEM_UP</a>,            /* <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>    */
    <a href="../ft2-type1_tables/#ps_dict_min_feature">PS_DICT_MIN_FEATURE</a>,            /* <a href="../ft2-basic_types/#ft_short">FT_Short</a>   */
    <a href="../ft2-type1_tables/#ps_dict_len_iv">PS_DICT_LEN_IV</a>,                 /* <a href="../ft2-basic_types/#ft_int">FT_Int</a>     */
    <a href="../ft2-type1_tables/#ps_dict_password">PS_DICT_PASSWORD</a>,               /* <a href="../ft2-basic_types/#ft_long">FT_Long</a>    */
    <a href="../ft2-type1_tables/#ps_dict_language_group">PS_DICT_LANGUAGE_GROUP</a>,         /* <a href="../ft2-basic_types/#ft_long">FT_Long</a>    */

    /* conventionally in the font FontInfo dictionary */
    <a href="../ft2-type1_tables/#ps_dict_version">PS_DICT_VERSION</a>,                /* <a href="../ft2-basic_types/#ft_string">FT_String</a>* */
    <a href="../ft2-type1_tables/#ps_dict_notice">PS_DICT_NOTICE</a>,                 /* <a href="../ft2-basic_types/#ft_string">FT_String</a>* */
    <a href="../ft2-type1_tables/#ps_dict_full_name">PS_DICT_FULL_NAME</a>,              /* <a href="../ft2-basic_types/#ft_string">FT_String</a>* */
    <a href="../ft2-type1_tables/#ps_dict_family_name">PS_DICT_FAMILY_NAME</a>,            /* <a href="../ft2-basic_types/#ft_string">FT_String</a>* */
    <a href="../ft2-type1_tables/#ps_dict_weight">PS_DICT_WEIGHT</a>,                 /* <a href="../ft2-basic_types/#ft_string">FT_String</a>* */
    <a href="../ft2-type1_tables/#ps_dict_is_fixed_pitch">PS_DICT_IS_FIXED_PITCH</a>,         /* <a href="../ft2-basic_types/#ft_bool">FT_Bool</a>    */
    <a href="../ft2-type1_tables/#ps_dict_underline_position">PS_DICT_UNDERLINE_POSITION</a>,     /* <a href="../ft2-basic_types/#ft_short">FT_Short</a>   */
    <a href="../ft2-type1_tables/#ps_dict_underline_thickness">PS_DICT_UNDERLINE_THICKNESS</a>,    /* <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  */
    <a href="../ft2-type1_tables/#ps_dict_fs_type">PS_DICT_FS_TYPE</a>,                /* <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  */
    <a href="../ft2-type1_tables/#ps_dict_italic_angle">PS_DICT_ITALIC_ANGLE</a>,           /* <a href="../ft2-basic_types/#ft_long">FT_Long</a>    */

    PS_DICT_MAX = <a href="../ft2-type1_tables/#ps_dict_italic_angle">PS_DICT_ITALIC_ANGLE</a>

  } <b>PS_Dict_Keys</b>;
</pre>
</div>


An enumeration used in calls to <a href="../ft2-type1_tables/#ft_get_ps_font_value">FT_Get_PS_Font_Value</a> to identify the Type&nbsp;1 dictionary entry to retrieve.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ps_dict_font_type">PS_DICT_FONT_TYPE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_font_matrix">PS_DICT_FONT_MATRIX</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_font_bbox">PS_DICT_FONT_BBOX</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_paint_type">PS_DICT_PAINT_TYPE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_font_name">PS_DICT_FONT_NAME</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_unique_id">PS_DICT_UNIQUE_ID</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_num_char_strings">PS_DICT_NUM_CHAR_STRINGS</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_char_string_key">PS_DICT_CHAR_STRING_KEY</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_char_string">PS_DICT_CHAR_STRING</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_encoding_type">PS_DICT_ENCODING_TYPE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_encoding_entry">PS_DICT_ENCODING_ENTRY</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_num_subrs">PS_DICT_NUM_SUBRS</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_subr">PS_DICT_SUBR</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_std_hw">PS_DICT_STD_HW</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_std_vw">PS_DICT_STD_VW</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_num_blue_values">PS_DICT_NUM_BLUE_VALUES</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_blue_value">PS_DICT_BLUE_VALUE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_blue_fuzz">PS_DICT_BLUE_FUZZ</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_num_other_blues">PS_DICT_NUM_OTHER_BLUES</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_other_blue">PS_DICT_OTHER_BLUE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_num_family_blues">PS_DICT_NUM_FAMILY_BLUES</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_family_blue">PS_DICT_FAMILY_BLUE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_num_family_other_blues">PS_DICT_NUM_FAMILY_OTHER_BLUES</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_family_other_blue">PS_DICT_FAMILY_OTHER_BLUE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_blue_scale">PS_DICT_BLUE_SCALE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_blue_shift">PS_DICT_BLUE_SHIFT</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_num_stem_snap_h">PS_DICT_NUM_STEM_SNAP_H</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_stem_snap_h">PS_DICT_STEM_SNAP_H</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_num_stem_snap_v">PS_DICT_NUM_STEM_SNAP_V</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_stem_snap_v">PS_DICT_STEM_SNAP_V</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_force_bold">PS_DICT_FORCE_BOLD</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_rnd_stem_up">PS_DICT_RND_STEM_UP</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_min_feature">PS_DICT_MIN_FEATURE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_len_iv">PS_DICT_LEN_IV</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_password">PS_DICT_PASSWORD</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_language_group">PS_DICT_LANGUAGE_GROUP</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_version">PS_DICT_VERSION</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_notice">PS_DICT_NOTICE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_full_name">PS_DICT_FULL_NAME</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_family_name">PS_DICT_FAMILY_NAME</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_weight">PS_DICT_WEIGHT</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_is_fixed_pitch">PS_DICT_IS_FIXED_PITCH</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_underline_position">PS_DICT_UNDERLINE_POSITION</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_underline_thickness">PS_DICT_UNDERLINE_THICKNESS</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_fs_type">PS_DICT_FS_TYPE</td><td class="desc">

</td></tr>
<tr><td class="val" id="ps_dict_italic_angle">PS_DICT_ITALIC_ANGLE</td><td class="desc">

</td></tr>
</table>

<h4>since</h4>

2.4.8

<hr>

## T1_FontInfo

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-type1_tables/#ps_fontinforec">PS_FontInfoRec</a>  <b>T1_FontInfo</b>;
</pre>
</div>


This type is equivalent to <a href="../ft2-type1_tables/#ps_fontinforec">PS_FontInfoRec</a>. It is deprecated but kept to maintain source compatibility between various versions of FreeType.

<hr>

## T1_Private

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-type1_tables/#ps_privaterec">PS_PrivateRec</a>  <b>T1_Private</b>;
</pre>
</div>


This type is equivalent to <a href="../ft2-type1_tables/#ps_privaterec">PS_PrivateRec</a>. It is deprecated but kept to maintain source compatibility between various versions of FreeType.

<hr>

## CID_FontDict

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-type1_tables/#cid_facedictrec">CID_FaceDictRec</a>  <b>CID_FontDict</b>;
</pre>
</div>


This type is equivalent to <a href="../ft2-type1_tables/#cid_facedictrec">CID_FaceDictRec</a>. It is deprecated but kept to maintain source compatibility between various versions of FreeType.

<hr>

## CID_Info

Defined in FT_TYPE1_TABLES_H (freetype/t1tables.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-type1_tables/#cid_faceinforec">CID_FaceInfoRec</a>  <b>CID_Info</b>;
</pre>
</div>


This type is equivalent to <a href="../ft2-type1_tables/#cid_faceinforec">CID_FaceInfoRec</a>. It is deprecated but kept to maintain source compatibility between various versions of FreeType.

<hr>

