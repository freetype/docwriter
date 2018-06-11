[Docs](ft2-index.md) &raquo; [Format-Specific API](ft2-toc.md#format-specific-api) &raquo; Window FNT Files

-------------------------------

# Window FNT Files

## Synopsis

This section contains the declaration of Windows FNT specific functions.

## FT_WinFNT_ID_XXX

Defined in FT_WINFONTS_H (freetype/ftwinfnt.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp1252">FT_WinFNT_ID_CP1252</a>    0
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_default">FT_WinFNT_ID_DEFAULT</a>   1
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_symbol">FT_WinFNT_ID_SYMBOL</a>    2
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_mac">FT_WinFNT_ID_MAC</a>      77
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp932">FT_WinFNT_ID_CP932</a>   128
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp949">FT_WinFNT_ID_CP949</a>   129
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp1361">FT_WinFNT_ID_CP1361</a>  130
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp936">FT_WinFNT_ID_CP936</a>   134
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp950">FT_WinFNT_ID_CP950</a>   136
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp1253">FT_WinFNT_ID_CP1253</a>  161
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp1254">FT_WinFNT_ID_CP1254</a>  162
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp1258">FT_WinFNT_ID_CP1258</a>  163
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp1255">FT_WinFNT_ID_CP1255</a>  177
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp1256">FT_WinFNT_ID_CP1256</a>  178
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp1257">FT_WinFNT_ID_CP1257</a>  186
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp1251">FT_WinFNT_ID_CP1251</a>  204
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp874">FT_WinFNT_ID_CP874</a>   222
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_cp1250">FT_WinFNT_ID_CP1250</a>  238
#<span class="keyword">define</span> <a href="../ft2-winfnt_fonts/#ft_winfnt_id_oem">FT_WinFNT_ID_OEM</a>     255
</pre>
</div>


A list of valid values for the &lsquo;charset&rsquo; byte in <a href="../ft2-winfnt_fonts/#ft_winfnt_headerrec">FT_WinFNT_HeaderRec</a>. Exact mapping tables for the various cpXXXX encodings (except for cp1361) can be found at <ftp://ftp.unicode.org/Public> in the MAPPINGS/VENDORS/MICSFT/WINDOWS subdirectory. cp1361 is roughly a superset of MAPPINGS/OBSOLETE/EASTASIA/KSC/JOHAB.TXT.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_winfnt_id_default">FT_WinFNT_ID_DEFAULT</td><td class="desc">
<p>This is used for font enumeration and font creation as a &lsquo;don't care&rsquo; value. Valid font files don't contain this value. When querying for information about the character set of the font that is currently selected into a specified device context, this return value (of the related Windows API) simply denotes failure.</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_symbol">FT_WinFNT_ID_SYMBOL</td><td class="desc">
<p>There is no known mapping table available.</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_mac">FT_WinFNT_ID_MAC</td><td class="desc">
<p>Mac Roman encoding.</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_oem">FT_WinFNT_ID_OEM</td><td class="desc">
<p>From Michael Poettgen &lt;michael@poettgen.de&gt;:</p>
<p>The &lsquo;Windows Font Mapping&rsquo; article says that FT_WinFNT_ID_OEM is used for the charset of vector fonts, like &lsquo;modern.fon&rsquo;, &lsquo;roman.fon&rsquo;, and &lsquo;script.fon&rsquo; on Windows.</p>
<p>The &lsquo;CreateFont&rsquo; documentation says: The FT_WinFNT_ID_OEM value specifies a character set that is operating-system dependent.</p>
<p>The &lsquo;IFIMETRICS&rsquo; documentation from the &lsquo;Windows Driver Development Kit&rsquo; says: This font supports an OEM-specific character set. The OEM character set is system dependent.</p>
<p>In general OEM, as opposed to ANSI (i.e., cp1252), denotes the second default codepage that most international versions of Windows have. It is one of the OEM codepages from</p>
<p><a href="https://msdn.microsoft.com/en-us/goglobal/bb964655">https://msdn.microsoft.com/en-us/goglobal/bb964655</a>,</p>
<p>and is used for the &lsquo;DOS boxes&rsquo;, to support legacy applications. A German Windows version for example usually uses ANSI codepage 1252 and OEM codepage 850.</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp874">FT_WinFNT_ID_CP874</td><td class="desc">
<p>A superset of Thai TIS 620 and ISO 8859-11.</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp932">FT_WinFNT_ID_CP932</td><td class="desc">
<p>A superset of Japanese Shift-JIS (with minor deviations).</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp936">FT_WinFNT_ID_CP936</td><td class="desc">
<p>A superset of simplified Chinese GB 2312-1980 (with different ordering and minor deviations).</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp949">FT_WinFNT_ID_CP949</td><td class="desc">
<p>A superset of Korean Hangul KS&nbsp;C 5601-1987 (with different ordering and minor deviations).</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp950">FT_WinFNT_ID_CP950</td><td class="desc">
<p>A superset of traditional Chinese Big&nbsp;5 ETen (with different ordering and minor deviations).</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp1250">FT_WinFNT_ID_CP1250</td><td class="desc">
<p>A superset of East European ISO 8859-2 (with slightly different ordering).</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp1251">FT_WinFNT_ID_CP1251</td><td class="desc">
<p>A superset of Russian ISO 8859-5 (with different ordering).</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp1252">FT_WinFNT_ID_CP1252</td><td class="desc">
<p>ANSI encoding. A superset of ISO 8859-1.</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp1253">FT_WinFNT_ID_CP1253</td><td class="desc">
<p>A superset of Greek ISO 8859-7 (with minor modifications).</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp1254">FT_WinFNT_ID_CP1254</td><td class="desc">
<p>A superset of Turkish ISO 8859-9.</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp1255">FT_WinFNT_ID_CP1255</td><td class="desc">
<p>A superset of Hebrew ISO 8859-8 (with some modifications).</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp1256">FT_WinFNT_ID_CP1256</td><td class="desc">
<p>A superset of Arabic ISO 8859-6 (with different ordering).</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp1257">FT_WinFNT_ID_CP1257</td><td class="desc">
<p>A superset of Baltic ISO 8859-13 (with some deviations).</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp1258">FT_WinFNT_ID_CP1258</td><td class="desc">
<p>For Vietnamese. This encoding doesn't cover all necessary characters.</p>
</td></tr>
<tr><td class="val" id="ft_winfnt_id_cp1361">FT_WinFNT_ID_CP1361</td><td class="desc">
<p>Korean (Johab).</p>
</td></tr>
</table>

<hr>

## FT_WinFNT_HeaderRec

Defined in FT_WINFONTS_H (freetype/ftwinfnt.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_WinFNT_HeaderRec_
  {
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  version;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   file_size;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    copyright[60];
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  file_type;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  nominal_point_size;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  vertical_resolution;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  horizontal_resolution;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  ascent;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  internal_leading;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  external_leading;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    italic;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    underline;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    strike_out;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  weight;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    charset;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  pixel_width;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  pixel_height;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    pitch_and_family;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  avg_width;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  max_width;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    first_char;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    last_char;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    default_char;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    break_char;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  bytes_per_row;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   device_offset;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   face_name_offset;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   bits_pointer;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   bits_offset;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    reserved;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   flags;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  A_space;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  B_space;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  C_space;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  color_table_offset;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   reserved1[4];

  } <b>FT_WinFNT_HeaderRec</b>;
</pre>
</div>


Windows FNT Header info.

<hr>

## FT_WinFNT_Header

Defined in FT_WINFONTS_H (freetype/ftwinfnt.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_WinFNT_HeaderRec_*  <b>FT_WinFNT_Header</b>;
</pre>
</div>


A handle to an <a href="../ft2-winfnt_fonts/#ft_winfnt_headerrec">FT_WinFNT_HeaderRec</a> structure.

<hr>

## FT_Get_WinFNT_Header

Defined in FT_WINFONTS_H (freetype/ftwinfnt.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Get_WinFNT_Header</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>               face,
                        <a href="../ft2-winfnt_fonts/#ft_winfnt_headerrec">FT_WinFNT_HeaderRec</a>  *aheader );
</pre>
</div>


Retrieve a Windows FNT font info header.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>A handle to the input face.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aheader">aheader</td><td class="desc">
<p>The WinFNT header.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

This function only works with Windows FNT faces, returning an error otherwise.

<hr>

