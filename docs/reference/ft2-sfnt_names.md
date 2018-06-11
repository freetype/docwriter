[Docs](ft2-index.md) &raquo; [Format-Specific API](ft2-toc.md#format-specific-api) &raquo; SFNT Names

-------------------------------

# SFNT Names

## Synopsis

The TrueType and OpenType specifications allow the inclusion of a special names table (&lsquo;name&rsquo;) in font files. This table contains textual (and internationalized) information regarding the font, like family name, copyright, version, etc.

The definitions below are used to access them if available.

Note that this has nothing to do with glyph names!

## FT_SfntName

Defined in FT_SFNT_NAMES_H (freetype/ftsnames.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_SfntName_
  {
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  platform_id;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  encoding_id;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  language_id;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  name_id;

    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>*   string;      /* this string is *not* null-terminated! */
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    string_len;  /* in bytes                              */

  } <b>FT_SfntName</b>;
</pre>
</div>


A structure used to model an SFNT &lsquo;name&rsquo; table entry.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="platform_id">platform_id</td><td class="desc">
<p>The platform ID for &lsquo;string&rsquo;. See <a href="../ft2-truetype_tables/#tt_platform_xxx">TT_PLATFORM_XXX</a> for possible values.</p>
</td></tr>
<tr><td class="val" id="encoding_id">encoding_id</td><td class="desc">
<p>The encoding ID for &lsquo;string&rsquo;. See <a href="../ft2-truetype_tables/#tt_apple_id_xxx">TT_APPLE_ID_XXX</a>, <a href="../ft2-truetype_tables/#tt_mac_id_xxx">TT_MAC_ID_XXX</a>, <a href="../ft2-truetype_tables/#tt_iso_id_xxx">TT_ISO_ID_XXX</a>, <a href="../ft2-truetype_tables/#tt_ms_id_xxx">TT_MS_ID_XXX</a>, and <a href="../ft2-truetype_tables/#tt_adobe_id_xxx">TT_ADOBE_ID_XXX</a> for possible values.</p>
</td></tr>
<tr><td class="val" id="language_id">language_id</td><td class="desc">
<p>The language ID for &lsquo;string&rsquo;. See <a href="../ft2-truetype_tables/#tt_mac_langid_xxx">TT_MAC_LANGID_XXX</a> and <a href="../ft2-truetype_tables/#tt_ms_langid_xxx">TT_MS_LANGID_XXX</a> for possible values.</p>
<p>Registered OpenType values for &lsquo;language_id&rsquo; are always smaller than 0x8000; values equal or larger than 0x8000 usually indicate a language tag string (introduced in OpenType version 1.6). Use function <a href="../ft2-sfnt_names/#ft_get_sfnt_langtag">FT_Get_Sfnt_LangTag</a> with &lsquo;language_id&rsquo; as its argument to retrieve the associated language tag.</p>
</td></tr>
<tr><td class="val" id="name_id">name_id</td><td class="desc">
<p>An identifier for &lsquo;string&rsquo;. See <a href="../ft2-truetype_tables/#tt_name_id_xxx">TT_NAME_ID_XXX</a> for possible values.</p>
</td></tr>
<tr><td class="val" id="string">string</td><td class="desc">
<p>The &lsquo;name&rsquo; string. Note that its format differs depending on the (platform,encoding) pair, being either a string of bytes (without a terminating NULL byte) or containing UTF-16BE entities.</p>
</td></tr>
<tr><td class="val" id="string_len">string_len</td><td class="desc">
<p>The length of &lsquo;string&rsquo; in bytes.</p>
</td></tr>
</table>

<h4>note</h4>

Please refer to the TrueType or OpenType specification for more details.

<hr>

## FT_Get_Sfnt_Name_Count

Defined in FT_SFNT_NAMES_H (freetype/ftsnames.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_uint">FT_UInt</a> )
  <b>FT_Get_Sfnt_Name_Count</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>  face );
</pre>
</div>


Retrieve the number of name strings in the SFNT &lsquo;name&rsquo; table.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face.</p>
</td></tr>
</table>

<h4>return</h4>

The number of strings in the &lsquo;name&rsquo; table.

<h4>note</h4>

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_SFNT_NAMES&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<hr>

## FT_Get_Sfnt_Name

Defined in FT_SFNT_NAMES_H (freetype/ftsnames.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_Sfnt_Name</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>       face,
                    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>       idx,
                    <a href="../ft2-sfnt_names/#ft_sfntname">FT_SfntName</a>  *aname );
</pre>
</div>


Retrieve a string of the SFNT &lsquo;name&rsquo; table for a given index.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face.</p>
</td></tr>
<tr><td class="val" id="idx">idx</td><td class="desc">
<p>The index of the &lsquo;name&rsquo; string.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aname">aname</td><td class="desc">
<p>The indexed <a href="../ft2-sfnt_names/#ft_sfntname">FT_SfntName</a> structure.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The &lsquo;string&rsquo; array returned in the &lsquo;aname&rsquo; structure is not null-terminated. Note that you don't have to deallocate &lsquo;string&rsquo; by yourself; FreeType takes care of it if you call <a href="../ft2-base_interface/#ft_done_face">FT_Done_Face</a>.

Use <a href="../ft2-sfnt_names/#ft_get_sfnt_name_count">FT_Get_Sfnt_Name_Count</a> to get the total number of available &lsquo;name&rsquo; table entries, then do a loop until you get the right platform, encoding, and name ID.

&lsquo;name&rsquo; table format&nbsp;1 entries can use language tags also, see <a href="../ft2-sfnt_names/#ft_get_sfnt_langtag">FT_Get_Sfnt_LangTag</a>.

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_SFNT_NAMES&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<hr>

## FT_SfntLangTag

Defined in FT_SFNT_NAMES_H (freetype/ftsnames.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_SfntLangTag_
  {
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>*  string;      /* this string is *not* null-terminated! */
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>   string_len;  /* in bytes                              */

  } <b>FT_SfntLangTag</b>;
</pre>
</div>


A structure to model a language tag entry from an SFNT &lsquo;name&rsquo; table.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="string">string</td><td class="desc">
<p>The language tag string, encoded in UTF-16BE (without trailing NULL bytes).</p>
</td></tr>
<tr><td class="val" id="string_len">string_len</td><td class="desc">
<p>The length of &lsquo;string&rsquo; in <strong>bytes</strong>.</p>
</td></tr>
</table>

<h4>note</h4>

Please refer to the TrueType or OpenType specification for more details.

<h4>since</h4>

2.8

<hr>

## FT_Get_Sfnt_LangTag

Defined in FT_SFNT_NAMES_H (freetype/ftsnames.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_Sfnt_LangTag</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>          face,
                       <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>          langID,
                       <a href="../ft2-sfnt_names/#ft_sfntlangtag">FT_SfntLangTag</a>  *alangTag );
</pre>
</div>


Retrieve the language tag associated with a language ID of an SFNT &lsquo;name&rsquo; table entry.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the source face.</p>
</td></tr>
<tr><td class="val" id="langid">langID</td><td class="desc">
<p>The language ID, as returned by <a href="../ft2-sfnt_names/#ft_get_sfnt_name">FT_Get_Sfnt_Name</a>. This is always a value larger than 0x8000.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="alangtag">alangTag</td><td class="desc">
<p>The language tag associated with the &lsquo;name&rsquo; table entry's language ID.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The &lsquo;string&rsquo; array returned in the &lsquo;alangTag&rsquo; structure is not null-terminated. Note that you don't have to deallocate &lsquo;string&rsquo; by yourself; FreeType takes care of it if you call <a href="../ft2-base_interface/#ft_done_face">FT_Done_Face</a>.

Only &lsquo;name&rsquo; table format&nbsp;1 supports language tags. For format&nbsp;0 tables, this function always returns FT_Err_Invalid_Table. For invalid format&nbsp;1 language ID values, FT_Err_Invalid_Argument is returned.

This function always returns an error if the config macro &lsquo;TT_CONFIG_OPTION_SFNT_NAMES&rsquo; is not defined in &lsquo;ftoption.h&rsquo;.

<h4>since</h4>

2.8

<hr>

