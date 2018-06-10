[Docs](ft2-index.md) &raquo; [Format-Specific API](ft2-toc.md#format-specific-api) &raquo; TrueType Tables

-------------------------------


# TrueType Tables

## Synopsis

This section contains definitions of some basic tables specific to TrueType and OpenType as well as some routines used to access and process them.

## TT_Header

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  TT_Header_
  {
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>   Table_Version;
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>   Font_Revision;

    <a href="../ft2-basic_types/#ft_long">FT_Long</a>    CheckSum_Adjust;
    <a href="../ft2-basic_types/#ft_long">FT_Long</a>    Magic_Number;

    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  Flags;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  Units_Per_EM;

    <a href="../ft2-basic_types/#ft_long">FT_Long</a>    Created [2];
    <a href="../ft2-basic_types/#ft_long">FT_Long</a>    Modified[2];

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   xMin;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   yMin;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   xMax;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   yMax;

    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  Mac_Style;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  Lowest_Rec_PPEM;

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   Font_Direction;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   Index_To_Loc_Format;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   Glyph_Data_Format;

  } <b>TT_Header</b>;
</pre>


A structure to model a TrueType font header table. All fields follow the OpenType specification.

<hr />

## TT_HoriHeader

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  TT_HoriHeader_
  {
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>   Version;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   Ascender;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   Descender;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   Line_Gap;

    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  advance_Width_Max;      /* advance width maximum */

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   min_Left_Side_Bearing;  /* minimum left-sb       */
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   min_Right_Side_Bearing; /* minimum right-sb      */
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   xMax_Extent;            /* xmax extents          */
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   caret_Slope_Rise;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   caret_Slope_Run;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   caret_Offset;

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   Reserved[4];

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   metric_Data_Format;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  number_Of_HMetrics;

    /* The following fields are not defined by the OpenType specification */
    /* but they are used to connect the metrics header to the relevant    */
    /* `hmtx' table.                                                      */

    <span class="keyword">void</span>*      long_metrics;
    <span class="keyword">void</span>*      short_metrics;

  } <b>TT_HoriHeader</b>;
</pre>


A structure to model a TrueType horizontal header, the &lsquo;hhea&rsquo; table, as well as the corresponding horizontal metrics table, &lsquo;hmtx&rsquo;.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="version">Version</td><td class="desc">

The table version.
</td></tr>
<tr><td class="val" id="ascender">Ascender</td><td class="desc">

The font's ascender, i.e., the distance from the baseline to the top-most of all glyph points found in the font.

This value is invalid in many fonts, as it is usually set by the font designer, and often reflects only a portion of the glyphs found in the font (maybe ASCII).

You should use the &lsquo;sTypoAscender&rsquo; field of the &lsquo;OS/2&rsquo; table instead if you want the correct one.
</td></tr>
<tr><td class="val" id="descender">Descender</td><td class="desc">

The font's descender, i.e., the distance from the baseline to the bottom-most of all glyph points found in the font. It is negative.

This value is invalid in many fonts, as it is usually set by the font designer, and often reflects only a portion of the glyphs found in the font (maybe ASCII).

You should use the &lsquo;sTypoDescender&rsquo; field of the &lsquo;OS/2&rsquo; table instead if you want the correct one.
</td></tr>
<tr><td class="val" id="line_gap">Line_Gap</td><td class="desc">

The font's line gap, i.e., the distance to add to the ascender and descender to get the BTB, i.e., the baseline-to-baseline distance for the font.
</td></tr>
<tr><td class="val" id="advance_width_max">advance_Width_Max</td><td class="desc">

This field is the maximum of all advance widths found in the font. It can be used to compute the maximum width of an arbitrary string of text.
</td></tr>
<tr><td class="val" id="min_left_side_bearing">min_Left_Side_Bearing</td><td class="desc">

The minimum left side bearing of all glyphs within the font.
</td></tr>
<tr><td class="val" id="min_right_side_bearing">min_Right_Side_Bearing</td><td class="desc">

The minimum right side bearing of all glyphs within the font.
</td></tr>
<tr><td class="val" id="xmax_extent">xMax_Extent</td><td class="desc">

The maximum horizontal extent (i.e., the &lsquo;width&rsquo; of a glyph's bounding box) for all glyphs in the font.
</td></tr>
<tr><td class="val" id="caret_slope_rise">caret_Slope_Rise</td><td class="desc">

The rise coefficient of the cursor's slope of the cursor (slope=rise/run).
</td></tr>
<tr><td class="val" id="caret_slope_run">caret_Slope_Run</td><td class="desc">

The run coefficient of the cursor's slope.
</td></tr>
<tr><td class="val" id="caret_offset">caret_Offset</td><td class="desc">

The cursor's offset for slanted fonts.
</td></tr>
<tr><td class="val" id="reserved">Reserved</td><td class="desc">

8&nbsp;reserved bytes.
</td></tr>
<tr><td class="val" id="metric_data_format">metric_Data_Format</td><td class="desc">

Always&nbsp;0.
</td></tr>
<tr><td class="val" id="number_of_hmetrics">number_Of_HMetrics</td><td class="desc">

Number of HMetrics entries in the &lsquo;hmtx&rsquo; table -- this value can be smaller than the total number of glyphs in the font.
</td></tr>
<tr><td class="val" id="long_metrics">long_metrics</td><td class="desc">

A pointer into the &lsquo;hmtx&rsquo; table.
</td></tr>
<tr><td class="val" id="short_metrics">short_metrics</td><td class="desc">

A pointer into the &lsquo;hmtx&rsquo; table.
</td></tr>
</table>

<h4>note</h4>

For an OpenType variation font, the values of the following fields can change after a call to <a href="../ft2-multiple_masters/#ft_set_var_design_coordinates">FT_Set_Var_Design_Coordinates</a> (and friends) if the font contains an &lsquo;MVAR&rsquo; table: &lsquo;caret_Slope_Rise&rsquo;, &lsquo;caret_Slope_Run&rsquo;, and &lsquo;caret_Offset&rsquo;.

<hr />

## TT_VertHeader

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  TT_VertHeader_
  {
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>   Version;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   Ascender;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   Descender;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   Line_Gap;

    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  advance_Height_Max;      /* advance height maximum */

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   min_Top_Side_Bearing;    /* minimum top-sb          */
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   min_Bottom_Side_Bearing; /* minimum bottom-sb       */
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   yMax_Extent;             /* ymax extents            */
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   caret_Slope_Rise;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   caret_Slope_Run;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   caret_Offset;

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   Reserved[4];

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   metric_Data_Format;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  number_Of_VMetrics;

    /* The following fields are not defined by the OpenType specification */
    /* but they are used to connect the metrics header to the relevant    */
    /* `vmtx' table.                                                      */

    <span class="keyword">void</span>*      long_metrics;
    <span class="keyword">void</span>*      short_metrics;

  } <b>TT_VertHeader</b>;
</pre>


A structure used to model a TrueType vertical header, the &lsquo;vhea&rsquo; table, as well as the corresponding vertical metrics table, &lsquo;vmtx&rsquo;.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="version">Version</td><td class="desc">

The table version.
</td></tr>
<tr><td class="val" id="ascender">Ascender</td><td class="desc">

The font's ascender, i.e., the distance from the baseline to the top-most of all glyph points found in the font.

This value is invalid in many fonts, as it is usually set by the font designer, and often reflects only a portion of the glyphs found in the font (maybe ASCII).

You should use the &lsquo;sTypoAscender&rsquo; field of the &lsquo;OS/2&rsquo; table instead if you want the correct one.
</td></tr>
<tr><td class="val" id="descender">Descender</td><td class="desc">

The font's descender, i.e., the distance from the baseline to the bottom-most of all glyph points found in the font. It is negative.

This value is invalid in many fonts, as it is usually set by the font designer, and often reflects only a portion of the glyphs found in the font (maybe ASCII).

You should use the &lsquo;sTypoDescender&rsquo; field of the &lsquo;OS/2&rsquo; table instead if you want the correct one.
</td></tr>
<tr><td class="val" id="line_gap">Line_Gap</td><td class="desc">

The font's line gap, i.e., the distance to add to the ascender and descender to get the BTB, i.e., the baseline-to-baseline distance for the font.
</td></tr>
<tr><td class="val" id="advance_height_max">advance_Height_Max</td><td class="desc">

This field is the maximum of all advance heights found in the font. It can be used to compute the maximum height of an arbitrary string of text.
</td></tr>
<tr><td class="val" id="min_top_side_bearing">min_Top_Side_Bearing</td><td class="desc">

The minimum top side bearing of all glyphs within the font.
</td></tr>
<tr><td class="val" id="min_bottom_side_bearing">min_Bottom_Side_Bearing</td><td class="desc">

The minimum bottom side bearing of all glyphs within the font.
</td></tr>
<tr><td class="val" id="ymax_extent">yMax_Extent</td><td class="desc">

The maximum vertical extent (i.e., the &lsquo;height&rsquo; of a glyph's bounding box) for all glyphs in the font.
</td></tr>
<tr><td class="val" id="caret_slope_rise">caret_Slope_Rise</td><td class="desc">

The rise coefficient of the cursor's slope of the cursor (slope=rise/run).
</td></tr>
<tr><td class="val" id="caret_slope_run">caret_Slope_Run</td><td class="desc">

The run coefficient of the cursor's slope.
</td></tr>
<tr><td class="val" id="caret_offset">caret_Offset</td><td class="desc">

The cursor's offset for slanted fonts.
</td></tr>
<tr><td class="val" id="reserved">Reserved</td><td class="desc">

8&nbsp;reserved bytes.
</td></tr>
<tr><td class="val" id="metric_data_format">metric_Data_Format</td><td class="desc">

Always&nbsp;0.
</td></tr>
<tr><td class="val" id="number_of_vmetrics">number_Of_VMetrics</td><td class="desc">

Number of VMetrics entries in the &lsquo;vmtx&rsquo; table -- this value can be smaller than the total number of glyphs in the font.
</td></tr>
<tr><td class="val" id="long_metrics">long_metrics</td><td class="desc">

A pointer into the &lsquo;vmtx&rsquo; table.
</td></tr>
<tr><td class="val" id="short_metrics">short_metrics</td><td class="desc">

A pointer into the &lsquo;vmtx&rsquo; table.
</td></tr>
</table>

<h4>note</h4>

For an OpenType variation font, the values of the following fields can change after a call to <a href="../ft2-multiple_masters/#ft_set_var_design_coordinates">FT_Set_Var_Design_Coordinates</a> (and friends) if the font contains an &lsquo;MVAR&rsquo; table: &lsquo;Ascender&rsquo;, &lsquo;Descender&rsquo;, &lsquo;Line_Gap&rsquo;, &lsquo;caret_Slope_Rise&rsquo;, &lsquo;caret_Slope_Run&rsquo;, and &lsquo;caret_Offset&rsquo;.

<hr />

## TT_OS2

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  TT_OS2_
  {
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  version;                /* 0x0001 - more or 0xFFFF */
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   xAvgCharWidth;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  usWeightClass;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  usWidthClass;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  fsType;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   ySubscriptXSize;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   ySubscriptYSize;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   ySubscriptXOffset;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   ySubscriptYOffset;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   ySuperscriptXSize;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   ySuperscriptYSize;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   ySuperscriptXOffset;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   ySuperscriptYOffset;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   yStrikeoutSize;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   yStrikeoutPosition;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   sFamilyClass;

    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    panose[10];

    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   ulUnicodeRange1;        /* Bits 0-31   */
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   ulUnicodeRange2;        /* Bits 32-63  */
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   ulUnicodeRange3;        /* Bits 64-95  */
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   ulUnicodeRange4;        /* Bits 96-127 */

    <a href="../ft2-basic_types/#ft_char">FT_Char</a>    achVendID[4];

    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  fsSelection;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  usFirstCharIndex;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  usLastCharIndex;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   sTypoAscender;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   sTypoDescender;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   sTypoLineGap;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  usWinAscent;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  usWinDescent;

    /* only version 1 and higher: */

    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   ulCodePageRange1;       /* Bits 0-31   */
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   ulCodePageRange2;       /* Bits 32-63  */

    /* only version 2 and higher: */

    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   sxHeight;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>   sCapHeight;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  usDefaultChar;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  usBreakChar;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  usMaxContext;

    /* only version 5 and higher: */

    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  usLowerOpticalPointSize;       /* in twips (1/20th points) */
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  usUpperOpticalPointSize;       /* in twips (1/20th points) */

  } <b>TT_OS2</b>;
</pre>


A structure to model a TrueType &lsquo;OS/2&rsquo; table. All fields comply to the OpenType specification.

Note that we now support old Mac fonts that do not include an &lsquo;OS/2&rsquo; table. In this case, the &lsquo;version&rsquo; field is always set to 0xFFFF.

<h4>note</h4>

For an OpenType variation font, the values of the following fields can change after a call to <a href="../ft2-multiple_masters/#ft_set_var_design_coordinates">FT_Set_Var_Design_Coordinates</a> (and friends) if the font contains an &lsquo;MVAR&rsquo; table: &lsquo;sCapHeight&rsquo;, &lsquo;sTypoAscender&rsquo;, &lsquo;sTypoDescender&rsquo;, &lsquo;sTypoLineGap&rsquo;, &lsquo;sxHeight&rsquo;, &lsquo;usWinAscent&rsquo;, &lsquo;usWinDescent&rsquo;, &lsquo;yStrikeoutPosition&rsquo;, &lsquo;yStrikeoutSize&rsquo;, &lsquo;ySubscriptXOffset&rsquo;, &lsquo;ySubScriptXSize&rsquo;, &lsquo;ySubscriptYOffset&rsquo;, &lsquo;ySubscriptYSize&rsquo;, &lsquo;ySuperscriptXOffset&rsquo;, &lsquo;ySuperscriptXSize&rsquo;, &lsquo;ySuperscriptYOffset&rsquo;, and &lsquo;ySuperscriptYSize&rsquo;.

Possible values for bits in the &lsquo;ulUnicodeRangeX&rsquo; fields are given by the <a href="../ft2-truetype_tables/#tt_ucr_xxx">TT_UCR_XXX</a> macros.

<hr />

## TT_Postscript

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  TT_Postscript_
  {
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  FormatType;
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  italicAngle;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>  underlinePosition;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>  underlineThickness;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  isFixedPitch;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  minMemType42;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  maxMemType42;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  minMemType1;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  maxMemType1;

    /* Glyph names follow in the `post' table, but we don't */
    /* load them by default.                                */

  } <b>TT_Postscript</b>;
</pre>


A structure to model a TrueType &lsquo;post&rsquo; table. All fields comply to the OpenType specification. This structure does not reference a font's PostScript glyph names; use <a href="../ft2-base_interface/#ft_get_glyph_name">FT_Get_Glyph_Name</a> to retrieve them.

<h4>note</h4>

For an OpenType variation font, the values of the following fields can change after a call to <a href="../ft2-multiple_masters/#ft_set_var_design_coordinates">FT_Set_Var_Design_Coordinates</a> (and friends) if the font contains an &lsquo;MVAR&rsquo; table: &lsquo;underlinePosition&rsquo; and &lsquo;underlineThickness&rsquo;.

<hr />

## TT_PCLT

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  TT_PCLT_
  {
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>   Version;
    <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   FontNumber;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  Pitch;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  xHeight;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  Style;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  TypeFamily;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  CapHeight;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  SymbolSet;
    <a href="../ft2-basic_types/#ft_char">FT_Char</a>    TypeFace[16];
    <a href="../ft2-basic_types/#ft_char">FT_Char</a>    CharacterComplement[8];
    <a href="../ft2-basic_types/#ft_char">FT_Char</a>    FileName[6];
    <a href="../ft2-basic_types/#ft_char">FT_Char</a>    StrokeWeight;
    <a href="../ft2-basic_types/#ft_char">FT_Char</a>    WidthType;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    SerifStyle;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>    Reserved;

  } <b>TT_PCLT</b>;
</pre>


A structure to model a TrueType &lsquo;PCLT&rsquo; table. All fields comply to the OpenType specification.

<hr />

## TT_MaxProfile

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  TT_MaxProfile_
  {
    <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>   version;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  numGlyphs;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxPoints;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxContours;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxCompositePoints;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxCompositeContours;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxZones;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxTwilightPoints;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxStorage;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxFunctionDefs;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxInstructionDefs;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxStackElements;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxSizeOfInstructions;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxComponentElements;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>  maxComponentDepth;

  } <b>TT_MaxProfile</b>;
</pre>


The maximum profile (&lsquo;maxp&rsquo;) table contains many max values, which can be used to pre-allocate arrays for speeding up glyph loading and hinting.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="version">version</td><td class="desc">

The version number.
</td></tr>
<tr><td class="val" id="numglyphs">numGlyphs</td><td class="desc">

The number of glyphs in this TrueType font.
</td></tr>
<tr><td class="val" id="maxpoints">maxPoints</td><td class="desc">

The maximum number of points in a non-composite TrueType glyph. See also &lsquo;maxCompositePoints&rsquo;.
</td></tr>
<tr><td class="val" id="maxcontours">maxContours</td><td class="desc">

The maximum number of contours in a non-composite TrueType glyph. See also &lsquo;maxCompositeContours&rsquo;.
</td></tr>
<tr><td class="val" id="maxcompositepoints">maxCompositePoints</td><td class="desc">

The maximum number of points in a composite TrueType glyph. See also &lsquo;maxPoints&rsquo;.
</td></tr>
<tr><td class="val" id="maxcompositecontours">maxCompositeContours</td><td class="desc">

The maximum number of contours in a composite TrueType glyph. See also &lsquo;maxContours&rsquo;.
</td></tr>
<tr><td class="val" id="maxzones">maxZones</td><td class="desc">

The maximum number of zones used for glyph hinting.
</td></tr>
<tr><td class="val" id="maxtwilightpoints">maxTwilightPoints</td><td class="desc">

The maximum number of points in the twilight zone used for glyph hinting.
</td></tr>
<tr><td class="val" id="maxstorage">maxStorage</td><td class="desc">

The maximum number of elements in the storage area used for glyph hinting.
</td></tr>
<tr><td class="val" id="maxfunctiondefs">maxFunctionDefs</td><td class="desc">

The maximum number of function definitions in the TrueType bytecode for this font.
</td></tr>
<tr><td class="val" id="maxinstructiondefs">maxInstructionDefs</td><td class="desc">

The maximum number of instruction definitions in the TrueType bytecode for this font.
</td></tr>
<tr><td class="val" id="maxstackelements">maxStackElements</td><td class="desc">

The maximum number of stack elements used during bytecode interpretation.
</td></tr>
<tr><td class="val" id="maxsizeofinstructions">maxSizeOfInstructions</td><td class="desc">

The maximum number of TrueType opcodes used for glyph hinting.
</td></tr>
<tr><td class="val" id="maxcomponentelements">maxComponentElements</td><td class="desc">

The maximum number of simple (i.e., non-composite) glyphs in a composite glyph.
</td></tr>
<tr><td class="val" id="maxcomponentdepth">maxComponentDepth</td><td class="desc">

The maximum nesting depth of composite glyphs.
</td></tr>
</table>

<h4>note</h4>

This structure is only used during font loading.

<hr />

## FT_Sfnt_Tag

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  <span class="keyword">typedef</span> <span class="keyword">enum</span>  FT_Sfnt_Tag_
  {
    <a href="../ft2-truetype_tables/#ft_sfnt_head">FT_SFNT_HEAD</a>,
    <a href="../ft2-truetype_tables/#ft_sfnt_maxp">FT_SFNT_MAXP</a>,
    <a href="../ft2-truetype_tables/#ft_sfnt_os2">FT_SFNT_OS2</a>,
    <a href="../ft2-truetype_tables/#ft_sfnt_hhea">FT_SFNT_HHEA</a>,
    <a href="../ft2-truetype_tables/#ft_sfnt_vhea">FT_SFNT_VHEA</a>,
    <a href="../ft2-truetype_tables/#ft_sfnt_post">FT_SFNT_POST</a>,
    <a href="../ft2-truetype_tables/#ft_sfnt_pclt">FT_SFNT_PCLT</a>,

    FT_SFNT_MAX

  } <b>FT_Sfnt_Tag</b>;

  /* these constants are deprecated; use the corresponding `<b>FT_Sfnt_Tag</b>' */
  /* values instead                                                      */
#define ft_sfnt_head  <a href="../ft2-truetype_tables/#ft_sfnt_head">FT_SFNT_HEAD</a>
#define ft_sfnt_maxp  <a href="../ft2-truetype_tables/#ft_sfnt_maxp">FT_SFNT_MAXP</a>
#define ft_sfnt_os2   <a href="../ft2-truetype_tables/#ft_sfnt_os2">FT_SFNT_OS2</a>
#define ft_sfnt_hhea  <a href="../ft2-truetype_tables/#ft_sfnt_hhea">FT_SFNT_HHEA</a>
#define ft_sfnt_vhea  <a href="../ft2-truetype_tables/#ft_sfnt_vhea">FT_SFNT_VHEA</a>
#define ft_sfnt_post  <a href="../ft2-truetype_tables/#ft_sfnt_post">FT_SFNT_POST</a>
#define ft_sfnt_pclt  <a href="../ft2-truetype_tables/#ft_sfnt_pclt">FT_SFNT_PCLT</a>
</pre>


An enumeration to specify indices of SFNT tables loaded and parsed by FreeType during initialization of an SFNT font. Used in the <a href="../ft2-truetype_tables/#ft_get_sfnt_table">FT_Get_Sfnt_Table</a> API function.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_sfnt_head">FT_SFNT_HEAD</td><td class="desc">

To access the font's <a href="../ft2-truetype_tables/#tt_header">TT_Header</a> structure.
</td></tr>
<tr><td class="val" id="ft_sfnt_maxp">FT_SFNT_MAXP</td><td class="desc">

To access the font's <a href="../ft2-truetype_tables/#tt_maxprofile">TT_MaxProfile</a> structure.
</td></tr>
<tr><td class="val" id="ft_sfnt_os2">FT_SFNT_OS2</td><td class="desc">

To access the font's <a href="../ft2-truetype_tables/#tt_os2">TT_OS2</a> structure.
</td></tr>
<tr><td class="val" id="ft_sfnt_hhea">FT_SFNT_HHEA</td><td class="desc">

To access the font's <a href="../ft2-truetype_tables/#tt_horiheader">TT_HoriHeader</a> structure.
</td></tr>
<tr><td class="val" id="ft_sfnt_vhea">FT_SFNT_VHEA</td><td class="desc">

To access the font's <a href="../ft2-truetype_tables/#tt_vertheader">TT_VertHeader</a> structure.
</td></tr>
<tr><td class="val" id="ft_sfnt_post">FT_SFNT_POST</td><td class="desc">

To access the font's <a href="../ft2-truetype_tables/#tt_postscript">TT_Postscript</a> structure.
</td></tr>
<tr><td class="val" id="ft_sfnt_pclt">FT_SFNT_PCLT</td><td class="desc">

To access the font's <a href="../ft2-truetype_tables/#tt_pclt">TT_PCLT</a> structure.
</td></tr>
</table>

<hr />

## FT_Get_Sfnt_Table

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  FT_EXPORT( <span class="keyword">void</span>* )
  <b>FT_Get_Sfnt_Table</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>      face,
                     <a href="../ft2-truetype_tables/#ft_sfnt_tag">FT_Sfnt_Tag</a>  tag );
</pre>


Return a pointer to a given SFNT table stored within a face.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

A handle to the source.
</td></tr>
<tr><td class="val" id="tag">tag</td><td class="desc">

The index of the SFNT table.
</td></tr>
</table>

<h4>return</h4>

A type-less pointer to the table. This will be NULL in case of error, or if the corresponding table was not found *OR* loaded from the file.

Use a typecast according to &lsquo;tag&rsquo; to access the structure elements.

<h4>note</h4>

The table is owned by the face object and disappears with it.

This function is only useful to access SFNT tables that are loaded by the sfnt, truetype, and opentype drivers. See <a href="../ft2-truetype_tables/#ft_sfnt_tag">FT_Sfnt_Tag</a> for a list.

Here an example how to access the &lsquo;vhea&rsquo; table:
```
  TT_VertHeader*  vert_header;


  vert_header =
    (TT_VertHeader*)FT_Get_Sfnt_Table( face, FT_SFNT_VHEA );
```

<hr />

## FT_Load_Sfnt_Table

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Load_Sfnt_Table</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                      <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>   tag,
                      <a href="../ft2-basic_types/#ft_long">FT_Long</a>    offset,
                      <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>*   buffer,
                      <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>*  length );
</pre>


Load any SFNT font table into client memory.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

A handle to the source face.
</td></tr>
<tr><td class="val" id="tag">tag</td><td class="desc">

The four-byte tag of the table to load. Use value&nbsp;0 if you want to access the whole font file. Otherwise, you can use one of the definitions found in the <a href="../ft2-header_file_macros/#ft_truetype_tags_h">FT_TRUETYPE_TAGS_H</a> file, or forge a new one with <a href="../ft2-basic_types/#ft_make_tag">FT_MAKE_TAG</a>.
</td></tr>
<tr><td class="val" id="offset">offset</td><td class="desc">

The starting offset in the table (or file if tag&nbsp;==&nbsp;0).
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="buffer">buffer</td><td class="desc">

The target buffer address. The client must ensure that the memory array is big enough to hold the data.
</td></tr>
</table>

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="length">length</td><td class="desc">

If the &lsquo;length&rsquo; parameter is NULL, try to load the whole table. Return an error code if it fails.

Else, if &lsquo;*length&rsquo; is&nbsp;0, exit immediately while returning the table's (or file) full size in it.

Else the number of bytes to read from the table or file, from the starting offset.
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

If you need to determine the table's length you should first call this function with &lsquo;*length&rsquo; set to&nbsp;0, as in the following example:
```
  FT_ULong  length = 0;


  error = FT_Load_Sfnt_Table( face, tag, 0, NULL, &length );
  if ( error ) { ... table does not exist ... }

  buffer = malloc( length );
  if ( buffer == NULL ) { ... not enough memory ... }

  error = FT_Load_Sfnt_Table( face, tag, 0, buffer, &length );
  if ( error ) { ... could not load table ... }
```

Note that structures like <a href="../ft2-truetype_tables/#tt_header">TT_Header</a> or <a href="../ft2-truetype_tables/#tt_os2">TT_OS2</a> can't be used with this function; they are limited to <a href="../ft2-truetype_tables/#ft_get_sfnt_table">FT_Get_Sfnt_Table</a>. Reason is that those structures depend on the processor architecture, with varying size (e.g. 32bit vs. 64bit) or order (big endian vs. little endian).

<hr />

## FT_Sfnt_Table_Info

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Sfnt_Table_Info</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>    face,
                      <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>    table_index,
                      <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  *tag,
                      <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>  *length );
</pre>


Return information on an SFNT table.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">

A handle to the source face.
</td></tr>
<tr><td class="val" id="table_index">table_index</td><td class="desc">

The index of an SFNT table. The function returns FT_Err_Table_Missing for an invalid value.
</td></tr>
</table>

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="tag">tag</td><td class="desc">

The name tag of the SFNT table. If the value is NULL, &lsquo;table_index&rsquo; is ignored, and &lsquo;length&rsquo; returns the number of SFNT tables in the font.
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="length">length</td><td class="desc">

The length of the SFNT table (or the number of SFNT tables, depending on &lsquo;tag&rsquo;).
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

While parsing fonts, FreeType handles SFNT tables with length zero as missing.

<hr />

## FT_Get_CMap_Language_ID

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a> )
  <b>FT_Get_CMap_Language_ID</b>( <a href="../ft2-base_interface/#ft_charmap">FT_CharMap</a>  charmap );
</pre>


Return cmap language ID as specified in the OpenType standard. Definitions of language ID values are in file <a href="../ft2-header_file_macros/#ft_truetype_ids_h">FT_TRUETYPE_IDS_H</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="charmap">charmap</td><td class="desc">

The target charmap.
</td></tr>
</table>

<h4>return</h4>

The language ID of &lsquo;charmap&rsquo;. If &lsquo;charmap&rsquo; doesn't belong to an SFNT face, just return&nbsp;0 as the default value.

For a format&nbsp;14 cmap (to access Unicode IVS), the return value is 0xFFFFFFFF.

<hr />

## FT_Get_CMap_Format

Defined in FT_TRUETYPE_TABLES_H (freetype/tttables.h).

<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_long">FT_Long</a> )
  <b>FT_Get_CMap_Format</b>( <a href="../ft2-base_interface/#ft_charmap">FT_CharMap</a>  charmap );
</pre>


Return the format of an SFNT &lsquo;cmap&rsquo; table.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="charmap">charmap</td><td class="desc">

The target charmap.
</td></tr>
</table>

<h4>return</h4>

The format of &lsquo;charmap&rsquo;. If &lsquo;charmap&rsquo; doesn't belong to an SFNT face, return -1.

<hr />

## FT_PARAM_TAG_UNPATENTED_HINTING


<pre>
#define <b>FT_PARAM_TAG_UNPATENTED_HINTING</b> \
          <a href="../ft2-basic_types/#ft_make_tag">FT_MAKE_TAG</a>( 'u', 'n', 'p', 'a' )
</pre>


Deprecated, no effect.

Previously: A constant used as the tag of an <a href="../ft2-base_interface/#ft_parameter">FT_Parameter</a> structure to indicate that unpatented methods only should be used by the TrueType bytecode interpreter for a typeface opened by <a href="../ft2-base_interface/#ft_open_face">FT_Open_Face</a>.

<hr />

## TT_PLATFORM_XXX

Defined in FT_TRUETYPE_IDS_H (freetype/ttnameid.h).

<pre>
#define <a href="../ft2-truetype_tables/#tt_platform_apple_unicode">TT_PLATFORM_APPLE_UNICODE</a>  0
#define <a href="../ft2-truetype_tables/#tt_platform_macintosh">TT_PLATFORM_MACINTOSH</a>      1
#define <a href="../ft2-truetype_tables/#tt_platform_iso">TT_PLATFORM_ISO</a>            2 /* deprecated */
#define <a href="../ft2-truetype_tables/#tt_platform_microsoft">TT_PLATFORM_MICROSOFT</a>      3
#define <a href="../ft2-truetype_tables/#tt_platform_custom">TT_PLATFORM_CUSTOM</a>         4
#define <a href="../ft2-truetype_tables/#tt_platform_adobe">TT_PLATFORM_ADOBE</a>          7 /* artificial */
</pre>


A list of valid values for the &lsquo;platform_id&rsquo; identifier code in <a href="../ft2-base_interface/#ft_charmaprec">FT_CharMapRec</a> and <a href="../ft2-sfnt_names/#ft_sfntname">FT_SfntName</a> structures.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="tt_platform_apple_unicode">TT_PLATFORM_APPLE_UNICODE</td><td class="desc">

Used by Apple to indicate a Unicode character map and/or name entry. See <a href="../ft2-truetype_tables/#tt_apple_id_xxx">TT_APPLE_ID_XXX</a> for corresponding &lsquo;encoding_id&rsquo; values. Note that name entries in this format are coded as big-endian UCS-2 character codes _only_.
</td></tr>
<tr><td class="val" id="tt_platform_macintosh">TT_PLATFORM_MACINTOSH</td><td class="desc">

Used by Apple to indicate a MacOS-specific charmap and/or name entry. See <a href="../ft2-truetype_tables/#tt_mac_id_xxx">TT_MAC_ID_XXX</a> for corresponding &lsquo;encoding_id&rsquo; values. Note that most TrueType fonts contain an Apple roman charmap to be usable on MacOS systems (even if they contain a Microsoft charmap as well).
</td></tr>
<tr><td class="val" id="tt_platform_iso">TT_PLATFORM_ISO</td><td class="desc">

This value was used to specify ISO/IEC 10646 charmaps. It is however now deprecated. See <a href="../ft2-truetype_tables/#tt_iso_id_xxx">TT_ISO_ID_XXX</a> for a list of corresponding &lsquo;encoding_id&rsquo; values.
</td></tr>
<tr><td class="val" id="tt_platform_microsoft">TT_PLATFORM_MICROSOFT</td><td class="desc">

Used by Microsoft to indicate Windows-specific charmaps. See <a href="../ft2-truetype_tables/#tt_ms_id_xxx">TT_MS_ID_XXX</a> for a list of corresponding &lsquo;encoding_id&rsquo; values. Note that most fonts contain a Unicode charmap using (TT_PLATFORM_MICROSOFT, <a href="../ft2-truetype_tables/#tt_ms_id_xxx">TT_MS_ID_UNICODE_CS</a>).
</td></tr>
<tr><td class="val" id="tt_platform_custom">TT_PLATFORM_CUSTOM</td><td class="desc">

Used to indicate application-specific charmaps.
</td></tr>
<tr><td class="val" id="tt_platform_adobe">TT_PLATFORM_ADOBE</td><td class="desc">

This value isn't part of any font format specification, but is used by FreeType to report Adobe-specific charmaps in an <a href="../ft2-base_interface/#ft_charmaprec">FT_CharMapRec</a> structure. See <a href="../ft2-truetype_tables/#tt_adobe_id_xxx">TT_ADOBE_ID_XXX</a>.
</td></tr>
</table>

<hr />

## TT_APPLE_ID_XXX

Defined in FT_TRUETYPE_IDS_H (freetype/ttnameid.h).

<pre>
#define <a href="../ft2-truetype_tables/#tt_apple_id_default">TT_APPLE_ID_DEFAULT</a>           0 /* Unicode 1.0                   */
#define <a href="../ft2-truetype_tables/#tt_apple_id_unicode_1_1">TT_APPLE_ID_UNICODE_1_1</a>       1 /* specify Hangul at U+34xx      */
#define <a href="../ft2-truetype_tables/#tt_apple_id_iso_10646">TT_APPLE_ID_ISO_10646</a>         2 /* deprecated                    */
#define <a href="../ft2-truetype_tables/#tt_apple_id_unicode_2_0">TT_APPLE_ID_UNICODE_2_0</a>       3 /* or later                      */
#define <a href="../ft2-truetype_tables/#tt_apple_id_unicode_32">TT_APPLE_ID_UNICODE_32</a>        4 /* 2.0 or later, full repertoire */
#define <a href="../ft2-truetype_tables/#tt_apple_id_variant_selector">TT_APPLE_ID_VARIANT_SELECTOR</a>  5 /* variation selector data       */
#define <a href="../ft2-truetype_tables/#tt_apple_id_full_unicode">TT_APPLE_ID_FULL_UNICODE</a>      6 /* used with type 13 cmaps       */
</pre>


A list of valid values for the &lsquo;encoding_id&rsquo; for <a href="../ft2-truetype_tables/#tt_platform_xxx">TT_PLATFORM_APPLE_UNICODE</a> charmaps and name entries.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="tt_apple_id_default">TT_APPLE_ID_DEFAULT</td><td class="desc">

Unicode version 1.0.
</td></tr>
<tr><td class="val" id="tt_apple_id_unicode_1_1">TT_APPLE_ID_UNICODE_1_1</td><td class="desc">

Unicode 1.1; specifies Hangul characters starting at U+34xx.
</td></tr>
<tr><td class="val" id="tt_apple_id_iso_10646">TT_APPLE_ID_ISO_10646</td><td class="desc">

Deprecated (identical to preceding).
</td></tr>
<tr><td class="val" id="tt_apple_id_unicode_2_0">TT_APPLE_ID_UNICODE_2_0</td><td class="desc">

Unicode 2.0 and beyond (UTF-16 BMP only).
</td></tr>
<tr><td class="val" id="tt_apple_id_unicode_32">TT_APPLE_ID_UNICODE_32</td><td class="desc">

Unicode 3.1 and beyond, using UTF-32.
</td></tr>
<tr><td class="val" id="tt_apple_id_variant_selector">TT_APPLE_ID_VARIANT_SELECTOR</td><td class="desc">

From Adobe, not Apple. Not a normal cmap. Specifies variations on a real cmap.
</td></tr>
<tr><td class="val" id="tt_apple_id_full_unicode">TT_APPLE_ID_FULL_UNICODE</td><td class="desc">

Used for fallback fonts that provide complete Unicode coverage with a type&nbsp;13 cmap.
</td></tr>
</table>

<hr />

## TT_MAC_ID_XXX

Defined in FT_TRUETYPE_IDS_H (freetype/ttnameid.h).

<pre>
#define TT_MAC_ID_ROMAN                 0
#define TT_MAC_ID_JAPANESE              1
#define TT_MAC_ID_TRADITIONAL_CHINESE   2
#define TT_MAC_ID_KOREAN                3
#define TT_MAC_ID_ARABIC                4
#define TT_MAC_ID_HEBREW                5
#define TT_MAC_ID_GREEK                 6
#define TT_MAC_ID_RUSSIAN               7
#define TT_MAC_ID_RSYMBOL               8
#define TT_MAC_ID_DEVANAGARI            9
#define TT_MAC_ID_GURMUKHI             10
#define TT_MAC_ID_GUJARATI             11
#define TT_MAC_ID_ORIYA                12
#define TT_MAC_ID_BENGALI              13
#define TT_MAC_ID_TAMIL                14
#define TT_MAC_ID_TELUGU               15
#define TT_MAC_ID_KANNADA              16
#define TT_MAC_ID_MALAYALAM            17
#define TT_MAC_ID_SINHALESE            18
#define TT_MAC_ID_BURMESE              19
#define TT_MAC_ID_KHMER                20
#define TT_MAC_ID_THAI                 21
#define TT_MAC_ID_LAOTIAN              22
#define TT_MAC_ID_GEORGIAN             23
#define TT_MAC_ID_ARMENIAN             24
#define TT_MAC_ID_MALDIVIAN            25
#define TT_MAC_ID_SIMPLIFIED_CHINESE   25
#define TT_MAC_ID_TIBETAN              26
#define TT_MAC_ID_MONGOLIAN            27
#define TT_MAC_ID_GEEZ                 28
#define TT_MAC_ID_SLAVIC               29
#define TT_MAC_ID_VIETNAMESE           30
#define TT_MAC_ID_SINDHI               31
#define TT_MAC_ID_UNINTERP             32
</pre>


A list of valid values for the &lsquo;encoding_id&rsquo; for <a href="../ft2-truetype_tables/#tt_platform_xxx">TT_PLATFORM_MACINTOSH</a> charmaps and name entries.

<hr />

## TT_ISO_ID_XXX

Defined in FT_TRUETYPE_IDS_H (freetype/ttnameid.h).

<pre>
#define <a href="../ft2-truetype_tables/#tt_iso_id_7bit_ascii">TT_ISO_ID_7BIT_ASCII</a>  0
#define <a href="../ft2-truetype_tables/#tt_iso_id_10646">TT_ISO_ID_10646</a>       1
#define <a href="../ft2-truetype_tables/#tt_iso_id_8859_1">TT_ISO_ID_8859_1</a>      2
</pre>


A list of valid values for the &lsquo;encoding_id&rsquo; for <a href="../ft2-truetype_tables/#tt_platform_xxx">TT_PLATFORM_ISO</a> charmaps and name entries.

Their use is now deprecated.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="tt_iso_id_7bit_ascii">TT_ISO_ID_7BIT_ASCII</td><td class="desc">

ASCII.
</td></tr>
<tr><td class="val" id="tt_iso_id_10646">TT_ISO_ID_10646</td><td class="desc">

ISO/10646.
</td></tr>
<tr><td class="val" id="tt_iso_id_8859_1">TT_ISO_ID_8859_1</td><td class="desc">

Also known as Latin-1.
</td></tr>
</table>

<hr />

## TT_MS_ID_XXX

Defined in FT_TRUETYPE_IDS_H (freetype/ttnameid.h).

<pre>
#define <a href="../ft2-truetype_tables/#tt_ms_id_symbol_cs">TT_MS_ID_SYMBOL_CS</a>    0
#define <a href="../ft2-truetype_tables/#tt_ms_id_unicode_cs">TT_MS_ID_UNICODE_CS</a>   1
#define <a href="../ft2-truetype_tables/#tt_ms_id_sjis">TT_MS_ID_SJIS</a>         2
#define <a href="../ft2-truetype_tables/#tt_ms_id_prc">TT_MS_ID_PRC</a>          3
#define <a href="../ft2-truetype_tables/#tt_ms_id_big_5">TT_MS_ID_BIG_5</a>        4
#define <a href="../ft2-truetype_tables/#tt_ms_id_wansung">TT_MS_ID_WANSUNG</a>      5
#define <a href="../ft2-truetype_tables/#tt_ms_id_johab">TT_MS_ID_JOHAB</a>        6
#define <a href="../ft2-truetype_tables/#tt_ms_id_ucs_4">TT_MS_ID_UCS_4</a>       10

  /* this value is deprecated */
#define TT_MS_ID_GB2312  <a href="../ft2-truetype_tables/#tt_ms_id_prc">TT_MS_ID_PRC</a>
</pre>


A list of valid values for the &lsquo;encoding_id&rsquo; for <a href="../ft2-truetype_tables/#tt_platform_xxx">TT_PLATFORM_MICROSOFT</a> charmaps and name entries.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="tt_ms_id_symbol_cs">TT_MS_ID_SYMBOL_CS</td><td class="desc">

Microsoft symbol encoding. See <a href="../ft2-base_interface/#ft_encoding">FT_ENCODING_MS_SYMBOL</a>.
</td></tr>
<tr><td class="val" id="tt_ms_id_unicode_cs">TT_MS_ID_UNICODE_CS</td><td class="desc">

Microsoft WGL4 charmap, matching Unicode. See <a href="../ft2-base_interface/#ft_encoding">FT_ENCODING_UNICODE</a>.
</td></tr>
<tr><td class="val" id="tt_ms_id_sjis">TT_MS_ID_SJIS</td><td class="desc">

Shift JIS Japanese encoding. See <a href="../ft2-base_interface/#ft_encoding">FT_ENCODING_SJIS</a>.
</td></tr>
<tr><td class="val" id="tt_ms_id_prc">TT_MS_ID_PRC</td><td class="desc">

Chinese encodings as used in the People's Republic of China (PRC). This means the encodings GB&nbsp;2312 and its supersets GBK and GB&nbsp;18030. See <a href="../ft2-base_interface/#ft_encoding">FT_ENCODING_PRC</a>.
</td></tr>
<tr><td class="val" id="tt_ms_id_big_5">TT_MS_ID_BIG_5</td><td class="desc">

Traditional Chinese as used in Taiwan and Hong Kong. See <a href="../ft2-base_interface/#ft_encoding">FT_ENCODING_BIG5</a>.
</td></tr>
<tr><td class="val" id="tt_ms_id_wansung">TT_MS_ID_WANSUNG</td><td class="desc">

Korean Extended Wansung encoding. See <a href="../ft2-base_interface/#ft_encoding">FT_ENCODING_WANSUNG</a>.
</td></tr>
<tr><td class="val" id="tt_ms_id_johab">TT_MS_ID_JOHAB</td><td class="desc">

Korean Johab encoding. See <a href="../ft2-base_interface/#ft_encoding">FT_ENCODING_JOHAB</a>.
</td></tr>
<tr><td class="val" id="tt_ms_id_ucs_4">TT_MS_ID_UCS_4</td><td class="desc">

UCS-4 or UTF-32 charmaps. This has been added to the OpenType specification version 1.4 (mid-2001).
</td></tr>
</table>

<hr />

## TT_ADOBE_ID_XXX

Defined in FT_TRUETYPE_IDS_H (freetype/ttnameid.h).

<pre>
#define <a href="../ft2-truetype_tables/#tt_adobe_id_standard">TT_ADOBE_ID_STANDARD</a>  0
#define <a href="../ft2-truetype_tables/#tt_adobe_id_expert">TT_ADOBE_ID_EXPERT</a>    1
#define <a href="../ft2-truetype_tables/#tt_adobe_id_custom">TT_ADOBE_ID_CUSTOM</a>    2
#define <a href="../ft2-truetype_tables/#tt_adobe_id_latin_1">TT_ADOBE_ID_LATIN_1</a>   3
</pre>


A list of valid values for the &lsquo;encoding_id&rsquo; for <a href="../ft2-truetype_tables/#tt_platform_xxx">TT_PLATFORM_ADOBE</a> charmaps. This is a FreeType-specific extension!

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="tt_adobe_id_standard">TT_ADOBE_ID_STANDARD</td><td class="desc">

Adobe standard encoding.
</td></tr>
<tr><td class="val" id="tt_adobe_id_expert">TT_ADOBE_ID_EXPERT</td><td class="desc">

Adobe expert encoding.
</td></tr>
<tr><td class="val" id="tt_adobe_id_custom">TT_ADOBE_ID_CUSTOM</td><td class="desc">

Adobe custom encoding.
</td></tr>
<tr><td class="val" id="tt_adobe_id_latin_1">TT_ADOBE_ID_LATIN_1</td><td class="desc">

Adobe Latin&nbsp;1 encoding.
</td></tr>
</table>

<hr />

## TT_MAC_LANGID_XXX

Defined in FT_TRUETYPE_IDS_H (freetype/ttnameid.h).

<pre>
#define TT_MAC_LANGID_ENGLISH                       0
#define TT_MAC_LANGID_FRENCH                        1
#define TT_MAC_LANGID_GERMAN                        2
#define TT_MAC_LANGID_ITALIAN                       3
#define TT_MAC_LANGID_DUTCH                         4
#define TT_MAC_LANGID_SWEDISH                       5
#define TT_MAC_LANGID_SPANISH                       6
#define TT_MAC_LANGID_DANISH                        7
#define TT_MAC_LANGID_PORTUGUESE                    8
#define TT_MAC_LANGID_NORWEGIAN                     9
#define TT_MAC_LANGID_HEBREW                       10
#define TT_MAC_LANGID_JAPANESE                     11
#define TT_MAC_LANGID_ARABIC                       12
#define TT_MAC_LANGID_FINNISH                      13
#define TT_MAC_LANGID_GREEK                        14
#define TT_MAC_LANGID_ICELANDIC                    15
#define TT_MAC_LANGID_MALTESE                      16
#define TT_MAC_LANGID_TURKISH                      17
#define TT_MAC_LANGID_CROATIAN                     18
#define TT_MAC_LANGID_CHINESE_TRADITIONAL          19
#define TT_MAC_LANGID_URDU                         20
#define TT_MAC_LANGID_HINDI                        21
#define TT_MAC_LANGID_THAI                         22
#define TT_MAC_LANGID_KOREAN                       23
#define TT_MAC_LANGID_LITHUANIAN                   24
#define TT_MAC_LANGID_POLISH                       25
#define TT_MAC_LANGID_HUNGARIAN                    26
#define TT_MAC_LANGID_ESTONIAN                     27
#define TT_MAC_LANGID_LETTISH                      28
#define TT_MAC_LANGID_SAAMISK                      29
#define TT_MAC_LANGID_FAEROESE                     30
#define TT_MAC_LANGID_FARSI                        31
#define TT_MAC_LANGID_RUSSIAN                      32
#define TT_MAC_LANGID_CHINESE_SIMPLIFIED           33
#define TT_MAC_LANGID_FLEMISH                      34
#define TT_MAC_LANGID_IRISH                        35
#define TT_MAC_LANGID_ALBANIAN                     36
#define TT_MAC_LANGID_ROMANIAN                     37
#define TT_MAC_LANGID_CZECH                        38
#define TT_MAC_LANGID_SLOVAK                       39
#define TT_MAC_LANGID_SLOVENIAN                    40
#define TT_MAC_LANGID_YIDDISH                      41
#define TT_MAC_LANGID_SERBIAN                      42
#define TT_MAC_LANGID_MACEDONIAN                   43
#define TT_MAC_LANGID_BULGARIAN                    44
#define TT_MAC_LANGID_UKRAINIAN                    45
#define TT_MAC_LANGID_BYELORUSSIAN                 46
#define TT_MAC_LANGID_UZBEK                        47
#define TT_MAC_LANGID_KAZAKH                       48
#define TT_MAC_LANGID_AZERBAIJANI                  49
#define TT_MAC_LANGID_AZERBAIJANI_CYRILLIC_SCRIPT  49
#define TT_MAC_LANGID_AZERBAIJANI_ARABIC_SCRIPT    50
#define TT_MAC_LANGID_ARMENIAN                     51
#define TT_MAC_LANGID_GEORGIAN                     52
#define TT_MAC_LANGID_MOLDAVIAN                    53
#define TT_MAC_LANGID_KIRGHIZ                      54
#define TT_MAC_LANGID_TAJIKI                       55
#define TT_MAC_LANGID_TURKMEN                      56
#define TT_MAC_LANGID_MONGOLIAN                    57
#define TT_MAC_LANGID_MONGOLIAN_MONGOLIAN_SCRIPT   57
#define TT_MAC_LANGID_MONGOLIAN_CYRILLIC_SCRIPT    58
#define TT_MAC_LANGID_PASHTO                       59
#define TT_MAC_LANGID_KURDISH                      60
#define TT_MAC_LANGID_KASHMIRI                     61
#define TT_MAC_LANGID_SINDHI                       62
#define TT_MAC_LANGID_TIBETAN                      63
#define TT_MAC_LANGID_NEPALI                       64
#define TT_MAC_LANGID_SANSKRIT                     65
#define TT_MAC_LANGID_MARATHI                      66
#define TT_MAC_LANGID_BENGALI                      67
#define TT_MAC_LANGID_ASSAMESE                     68
#define TT_MAC_LANGID_GUJARATI                     69
#define TT_MAC_LANGID_PUNJABI                      70
#define TT_MAC_LANGID_ORIYA                        71
#define TT_MAC_LANGID_MALAYALAM                    72
#define TT_MAC_LANGID_KANNADA                      73
#define TT_MAC_LANGID_TAMIL                        74
#define TT_MAC_LANGID_TELUGU                       75
#define TT_MAC_LANGID_SINHALESE                    76
#define TT_MAC_LANGID_BURMESE                      77
#define TT_MAC_LANGID_KHMER                        78
#define TT_MAC_LANGID_LAO                          79
#define TT_MAC_LANGID_VIETNAMESE                   80
#define TT_MAC_LANGID_INDONESIAN                   81
#define TT_MAC_LANGID_TAGALOG                      82
#define TT_MAC_LANGID_MALAY_ROMAN_SCRIPT           83
#define TT_MAC_LANGID_MALAY_ARABIC_SCRIPT          84
#define TT_MAC_LANGID_AMHARIC                      85
#define TT_MAC_LANGID_TIGRINYA                     86
#define TT_MAC_LANGID_GALLA                        87
#define TT_MAC_LANGID_SOMALI                       88
#define TT_MAC_LANGID_SWAHILI                      89
#define TT_MAC_LANGID_RUANDA                       90
#define TT_MAC_LANGID_RUNDI                        91
#define TT_MAC_LANGID_CHEWA                        92
#define TT_MAC_LANGID_MALAGASY                     93
#define TT_MAC_LANGID_ESPERANTO                    94
#define TT_MAC_LANGID_WELSH                       128
#define TT_MAC_LANGID_BASQUE                      129
#define TT_MAC_LANGID_CATALAN                     130
#define TT_MAC_LANGID_LATIN                       131
#define TT_MAC_LANGID_QUECHUA                     132
#define TT_MAC_LANGID_GUARANI                     133
#define TT_MAC_LANGID_AYMARA                      134
#define TT_MAC_LANGID_TATAR                       135
#define TT_MAC_LANGID_UIGHUR                      136
#define TT_MAC_LANGID_DZONGKHA                    137
#define TT_MAC_LANGID_JAVANESE                    138
#define TT_MAC_LANGID_SUNDANESE                   139

  /* The following codes are new as of 2000-03-10 */
#define TT_MAC_LANGID_GALICIAN                    140
#define TT_MAC_LANGID_AFRIKAANS                   141
#define TT_MAC_LANGID_BRETON                      142
#define TT_MAC_LANGID_INUKTITUT                   143
#define TT_MAC_LANGID_SCOTTISH_GAELIC             144
#define TT_MAC_LANGID_MANX_GAELIC                 145
#define TT_MAC_LANGID_IRISH_GAELIC                146
#define TT_MAC_LANGID_TONGAN                      147
#define TT_MAC_LANGID_GREEK_POLYTONIC             148
#define TT_MAC_LANGID_GREELANDIC                  149
#define TT_MAC_LANGID_AZERBAIJANI_ROMAN_SCRIPT    150
</pre>


Possible values of the language identifier field in the name records of the SFNT &lsquo;name&rsquo; table if the &lsquo;platform&rsquo; identifier code is <a href="../ft2-truetype_tables/#tt_platform_xxx">TT_PLATFORM_MACINTOSH</a>. These values are also used as return values for function <a href="../ft2-truetype_tables/#ft_get_cmap_language_id">FT_Get_CMap_Language_ID</a>.

The canonical source for Apple's IDs is

<https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6name.html>

<hr />

## TT_MS_LANGID_XXX

Defined in FT_TRUETYPE_IDS_H (freetype/ttnameid.h).

<pre>
#define TT_MS_LANGID_ARABIC_SAUDI_ARABIA               0x0401
#define TT_MS_LANGID_ARABIC_IRAQ                       0x0801
#define TT_MS_LANGID_ARABIC_EGYPT                      0x0C01
#define TT_MS_LANGID_ARABIC_LIBYA                      0x1001
#define TT_MS_LANGID_ARABIC_ALGERIA                    0x1401
#define TT_MS_LANGID_ARABIC_MOROCCO                    0x1801
#define TT_MS_LANGID_ARABIC_TUNISIA                    0x1C01
#define TT_MS_LANGID_ARABIC_OMAN                       0x2001
#define TT_MS_LANGID_ARABIC_YEMEN                      0x2401
#define TT_MS_LANGID_ARABIC_SYRIA                      0x2801
#define TT_MS_LANGID_ARABIC_JORDAN                     0x2C01
#define TT_MS_LANGID_ARABIC_LEBANON                    0x3001
#define TT_MS_LANGID_ARABIC_KUWAIT                     0x3401
#define TT_MS_LANGID_ARABIC_UAE                        0x3801
#define TT_MS_LANGID_ARABIC_BAHRAIN                    0x3C01
#define TT_MS_LANGID_ARABIC_QATAR                      0x4001
#define TT_MS_LANGID_BULGARIAN_BULGARIA                0x0402
#define TT_MS_LANGID_CATALAN_CATALAN                   0x0403
#define TT_MS_LANGID_CHINESE_TAIWAN                    0x0404
#define TT_MS_LANGID_CHINESE_PRC                       0x0804
#define TT_MS_LANGID_CHINESE_HONG_KONG                 0x0C04
#define TT_MS_LANGID_CHINESE_SINGAPORE                 0x1004
#define TT_MS_LANGID_CHINESE_MACAO                     0x1404
#define TT_MS_LANGID_CZECH_CZECH_REPUBLIC              0x0405
#define TT_MS_LANGID_DANISH_DENMARK                    0x0406
#define TT_MS_LANGID_GERMAN_GERMANY                    0x0407
#define TT_MS_LANGID_GERMAN_SWITZERLAND                0x0807
#define TT_MS_LANGID_GERMAN_AUSTRIA                    0x0C07
#define TT_MS_LANGID_GERMAN_LUXEMBOURG                 0x1007
#define TT_MS_LANGID_GERMAN_LIECHTENSTEIN              0x1407
#define TT_MS_LANGID_GREEK_GREECE                      0x0408
#define TT_MS_LANGID_ENGLISH_UNITED_STATES             0x0409
#define TT_MS_LANGID_ENGLISH_UNITED_KINGDOM            0x0809
#define TT_MS_LANGID_ENGLISH_AUSTRALIA                 0x0C09
#define TT_MS_LANGID_ENGLISH_CANADA                    0x1009
#define TT_MS_LANGID_ENGLISH_NEW_ZEALAND               0x1409
#define TT_MS_LANGID_ENGLISH_IRELAND                   0x1809
#define TT_MS_LANGID_ENGLISH_SOUTH_AFRICA              0x1C09
#define TT_MS_LANGID_ENGLISH_JAMAICA                   0x2009
#define TT_MS_LANGID_ENGLISH_CARIBBEAN                 0x2409
#define TT_MS_LANGID_ENGLISH_BELIZE                    0x2809
#define TT_MS_LANGID_ENGLISH_TRINIDAD                  0x2C09
#define TT_MS_LANGID_ENGLISH_ZIMBABWE                  0x3009
#define TT_MS_LANGID_ENGLISH_PHILIPPINES               0x3409
#define TT_MS_LANGID_ENGLISH_INDIA                     0x4009
#define TT_MS_LANGID_ENGLISH_MALAYSIA                  0x4409
#define TT_MS_LANGID_ENGLISH_SINGAPORE                 0x4809
#define TT_MS_LANGID_SPANISH_SPAIN_TRADITIONAL_SORT    0x040A
#define TT_MS_LANGID_SPANISH_MEXICO                    0x080A
#define TT_MS_LANGID_SPANISH_SPAIN_MODERN_SORT         0x0C0A
#define TT_MS_LANGID_SPANISH_GUATEMALA                 0x100A
#define TT_MS_LANGID_SPANISH_COSTA_RICA                0x140A
#define TT_MS_LANGID_SPANISH_PANAMA                    0x180A
#define TT_MS_LANGID_SPANISH_DOMINICAN_REPUBLIC        0x1C0A
#define TT_MS_LANGID_SPANISH_VENEZUELA                 0x200A
#define TT_MS_LANGID_SPANISH_COLOMBIA                  0x240A
#define TT_MS_LANGID_SPANISH_PERU                      0x280A
#define TT_MS_LANGID_SPANISH_ARGENTINA                 0x2C0A
#define TT_MS_LANGID_SPANISH_ECUADOR                   0x300A
#define TT_MS_LANGID_SPANISH_CHILE                     0x340A
#define TT_MS_LANGID_SPANISH_URUGUAY                   0x380A
#define TT_MS_LANGID_SPANISH_PARAGUAY                  0x3C0A
#define TT_MS_LANGID_SPANISH_BOLIVIA                   0x400A
#define TT_MS_LANGID_SPANISH_EL_SALVADOR               0x440A
#define TT_MS_LANGID_SPANISH_HONDURAS                  0x480A
#define TT_MS_LANGID_SPANISH_NICARAGUA                 0x4C0A
#define TT_MS_LANGID_SPANISH_PUERTO_RICO               0x500A
#define TT_MS_LANGID_SPANISH_UNITED_STATES             0x540A
#define TT_MS_LANGID_FINNISH_FINLAND                   0x040B
#define TT_MS_LANGID_FRENCH_FRANCE                     0x040C
#define TT_MS_LANGID_FRENCH_BELGIUM                    0x080C
#define TT_MS_LANGID_FRENCH_CANADA                     0x0C0C
#define TT_MS_LANGID_FRENCH_SWITZERLAND                0x100C
#define TT_MS_LANGID_FRENCH_LUXEMBOURG                 0x140C
#define TT_MS_LANGID_FRENCH_MONACO                     0x180C
#define TT_MS_LANGID_HEBREW_ISRAEL                     0x040D
#define TT_MS_LANGID_HUNGARIAN_HUNGARY                 0x040E
#define TT_MS_LANGID_ICELANDIC_ICELAND                 0x040F
#define TT_MS_LANGID_ITALIAN_ITALY                     0x0410
#define TT_MS_LANGID_ITALIAN_SWITZERLAND               0x0810
#define TT_MS_LANGID_JAPANESE_JAPAN                    0x0411
#define TT_MS_LANGID_KOREAN_KOREA                      0x0412
#define TT_MS_LANGID_DUTCH_NETHERLANDS                 0x0413
#define TT_MS_LANGID_DUTCH_BELGIUM                     0x0813
#define TT_MS_LANGID_NORWEGIAN_NORWAY_BOKMAL           0x0414
#define TT_MS_LANGID_NORWEGIAN_NORWAY_NYNORSK          0x0814
#define TT_MS_LANGID_POLISH_POLAND                     0x0415
#define TT_MS_LANGID_PORTUGUESE_BRAZIL                 0x0416
#define TT_MS_LANGID_PORTUGUESE_PORTUGAL               0x0816
#define TT_MS_LANGID_ROMANSH_SWITZERLAND               0x0417
#define TT_MS_LANGID_ROMANIAN_ROMANIA                  0x0418
#define TT_MS_LANGID_RUSSIAN_RUSSIA                    0x0419
#define TT_MS_LANGID_CROATIAN_CROATIA                  0x041A
#define TT_MS_LANGID_SERBIAN_SERBIA_LATIN              0x081A
#define TT_MS_LANGID_SERBIAN_SERBIA_CYRILLIC           0x0C1A
#define TT_MS_LANGID_CROATIAN_BOSNIA_HERZEGOVINA       0x101A
#define TT_MS_LANGID_BOSNIAN_BOSNIA_HERZEGOVINA        0x141A
#define TT_MS_LANGID_SERBIAN_BOSNIA_HERZ_LATIN         0x181A
#define TT_MS_LANGID_SERBIAN_BOSNIA_HERZ_CYRILLIC      0x1C1A
#define TT_MS_LANGID_BOSNIAN_BOSNIA_HERZ_CYRILLIC      0x201A
#define TT_MS_LANGID_SLOVAK_SLOVAKIA                   0x041B
#define TT_MS_LANGID_ALBANIAN_ALBANIA                  0x041C
#define TT_MS_LANGID_SWEDISH_SWEDEN                    0x041D
#define TT_MS_LANGID_SWEDISH_FINLAND                   0x081D
#define TT_MS_LANGID_THAI_THAILAND                     0x041E
#define TT_MS_LANGID_TURKISH_TURKEY                    0x041F
#define TT_MS_LANGID_URDU_PAKISTAN                     0x0420
#define TT_MS_LANGID_INDONESIAN_INDONESIA              0x0421
#define TT_MS_LANGID_UKRAINIAN_UKRAINE                 0x0422
#define TT_MS_LANGID_BELARUSIAN_BELARUS                0x0423
#define TT_MS_LANGID_SLOVENIAN_SLOVENIA                0x0424
#define TT_MS_LANGID_ESTONIAN_ESTONIA                  0x0425
#define TT_MS_LANGID_LATVIAN_LATVIA                    0x0426
#define TT_MS_LANGID_LITHUANIAN_LITHUANIA              0x0427
#define TT_MS_LANGID_TAJIK_TAJIKISTAN                  0x0428
#define TT_MS_LANGID_VIETNAMESE_VIET_NAM               0x042A
#define TT_MS_LANGID_ARMENIAN_ARMENIA                  0x042B
#define TT_MS_LANGID_AZERI_AZERBAIJAN_LATIN            0x042C
#define TT_MS_LANGID_AZERI_AZERBAIJAN_CYRILLIC         0x082C
#define TT_MS_LANGID_BASQUE_BASQUE                     0x042D
#define TT_MS_LANGID_UPPER_SORBIAN_GERMANY             0x042E
#define TT_MS_LANGID_LOWER_SORBIAN_GERMANY             0x082E
#define TT_MS_LANGID_MACEDONIAN_MACEDONIA              0x042F
#define TT_MS_LANGID_SETSWANA_SOUTH_AFRICA             0x0432
#define TT_MS_LANGID_ISIXHOSA_SOUTH_AFRICA             0x0434
#define TT_MS_LANGID_ISIZULU_SOUTH_AFRICA              0x0435
#define TT_MS_LANGID_AFRIKAANS_SOUTH_AFRICA            0x0436
#define TT_MS_LANGID_GEORGIAN_GEORGIA                  0x0437
#define TT_MS_LANGID_FAEROESE_FAEROE_ISLANDS           0x0438
#define TT_MS_LANGID_HINDI_INDIA                       0x0439
#define TT_MS_LANGID_MALTESE_MALTA                     0x043A
#define TT_MS_LANGID_SAMI_NORTHERN_NORWAY              0x043B
#define TT_MS_LANGID_SAMI_NORTHERN_SWEDEN              0x083B
#define TT_MS_LANGID_SAMI_NORTHERN_FINLAND             0x0C3B
#define TT_MS_LANGID_SAMI_LULE_NORWAY                  0x103B
#define TT_MS_LANGID_SAMI_LULE_SWEDEN                  0x143B
#define TT_MS_LANGID_SAMI_SOUTHERN_NORWAY              0x183B
#define TT_MS_LANGID_SAMI_SOUTHERN_SWEDEN              0x1C3B
#define TT_MS_LANGID_SAMI_SKOLT_FINLAND                0x203B
#define TT_MS_LANGID_SAMI_INARI_FINLAND                0x243B
#define TT_MS_LANGID_IRISH_IRELAND                     0x083C
#define TT_MS_LANGID_MALAY_MALAYSIA                    0x043E
#define TT_MS_LANGID_MALAY_BRUNEI_DARUSSALAM           0x083E
#define TT_MS_LANGID_KAZAKH_KAZAKHSTAN                 0x043F
#define TT_MS_LANGID_KYRGYZ_KYRGYZSTAN /* Cyrillic*/   0x0440
#define TT_MS_LANGID_KISWAHILI_KENYA                   0x0441
#define TT_MS_LANGID_TURKMEN_TURKMENISTAN              0x0442
#define TT_MS_LANGID_UZBEK_UZBEKISTAN_LATIN            0x0443
#define TT_MS_LANGID_UZBEK_UZBEKISTAN_CYRILLIC         0x0843
#define TT_MS_LANGID_TATAR_RUSSIA                      0x0444
#define TT_MS_LANGID_BENGALI_INDIA                     0x0445
#define TT_MS_LANGID_BENGALI_BANGLADESH                0x0845
#define TT_MS_LANGID_PUNJABI_INDIA                     0x0446
#define TT_MS_LANGID_GUJARATI_INDIA                    0x0447
#define TT_MS_LANGID_ODIA_INDIA                        0x0448
#define TT_MS_LANGID_TAMIL_INDIA                       0x0449
#define TT_MS_LANGID_TELUGU_INDIA                      0x044A
#define TT_MS_LANGID_KANNADA_INDIA                     0x044B
#define TT_MS_LANGID_MALAYALAM_INDIA                   0x044C
#define TT_MS_LANGID_ASSAMESE_INDIA                    0x044D
#define TT_MS_LANGID_MARATHI_INDIA                     0x044E
#define TT_MS_LANGID_SANSKRIT_INDIA                    0x044F
#define TT_MS_LANGID_MONGOLIAN_MONGOLIA /* Cyrillic */ 0x0450
#define TT_MS_LANGID_MONGOLIAN_PRC                     0x0850
#define TT_MS_LANGID_TIBETAN_PRC                       0x0451
#define TT_MS_LANGID_WELSH_UNITED_KINGDOM              0x0452
#define TT_MS_LANGID_KHMER_CAMBODIA                    0x0453
#define TT_MS_LANGID_LAO_LAOS                          0x0454
#define TT_MS_LANGID_GALICIAN_GALICIAN                 0x0456
#define TT_MS_LANGID_KONKANI_INDIA                     0x0457
#define TT_MS_LANGID_SYRIAC_SYRIA                      0x045A
#define TT_MS_LANGID_SINHALA_SRI_LANKA                 0x045B
#define TT_MS_LANGID_INUKTITUT_CANADA                  0x045D
#define TT_MS_LANGID_INUKTITUT_CANADA_LATIN            0x085D
#define TT_MS_LANGID_AMHARIC_ETHIOPIA                  0x045E
#define TT_MS_LANGID_TAMAZIGHT_ALGERIA                 0x085F
#define TT_MS_LANGID_NEPALI_NEPAL                      0x0461
#define TT_MS_LANGID_FRISIAN_NETHERLANDS               0x0462
#define TT_MS_LANGID_PASHTO_AFGHANISTAN                0x0463
#define TT_MS_LANGID_FILIPINO_PHILIPPINES              0x0464
#define TT_MS_LANGID_DHIVEHI_MALDIVES                  0x0465
#define TT_MS_LANGID_HAUSA_NIGERIA                     0x0468
#define TT_MS_LANGID_YORUBA_NIGERIA                    0x046A
#define TT_MS_LANGID_QUECHUA_BOLIVIA                   0x046B
#define TT_MS_LANGID_QUECHUA_ECUADOR                   0x086B
#define TT_MS_LANGID_QUECHUA_PERU                      0x0C6B
#define TT_MS_LANGID_SESOTHO_SA_LEBOA_SOUTH_AFRICA     0x046C
#define TT_MS_LANGID_BASHKIR_RUSSIA                    0x046D
#define TT_MS_LANGID_LUXEMBOURGISH_LUXEMBOURG          0x046E
#define TT_MS_LANGID_GREENLANDIC_GREENLAND             0x046F
#define TT_MS_LANGID_IGBO_NIGERIA                      0x0470
#define TT_MS_LANGID_YI_PRC                            0x0478
#define TT_MS_LANGID_MAPUDUNGUN_CHILE                  0x047A
#define TT_MS_LANGID_MOHAWK_MOHAWK                     0x047C
#define TT_MS_LANGID_BRETON_FRANCE                     0x047E
#define TT_MS_LANGID_UIGHUR_PRC                        0x0480
#define TT_MS_LANGID_MAORI_NEW_ZEALAND                 0x0481
#define TT_MS_LANGID_OCCITAN_FRANCE                    0x0482
#define TT_MS_LANGID_CORSICAN_FRANCE                   0x0483
#define TT_MS_LANGID_ALSATIAN_FRANCE                   0x0484
#define TT_MS_LANGID_YAKUT_RUSSIA                      0x0485
#define TT_MS_LANGID_KICHE_GUATEMALA                   0x0486
#define TT_MS_LANGID_KINYARWANDA_RWANDA                0x0487
#define TT_MS_LANGID_WOLOF_SENEGAL                     0x0488
#define TT_MS_LANGID_DARI_AFGHANISTAN                  0x048C
</pre>


Possible values of the language identifier field in the name records of the SFNT &lsquo;name&rsquo; table if the &lsquo;platform&rsquo; identifier code is <a href="../ft2-truetype_tables/#tt_platform_xxx">TT_PLATFORM_MICROSOFT</a>. These values are also used as return values for function <a href="../ft2-truetype_tables/#ft_get_cmap_language_id">FT_Get_CMap_Language_ID</a>.

The canonical source for Microsoft's IDs is

<https://www.microsoft.com/globaldev/reference/lcid-all.mspx> ,

however, we only provide macros for language identifiers present in the OpenType specification: Microsoft has abandoned the concept of LCIDs (language code identifiers), and format&nbsp;1 of the &lsquo;name&rsquo; table provides a better mechanism for languages not covered here.

More legacy values not listed in the reference can be found in the <a href="../ft2-header_file_macros/#ft_truetype_ids_h">FT_TRUETYPE_IDS_H</a> header file.

<hr />

## TT_NAME_ID_XXX

Defined in FT_TRUETYPE_IDS_H (freetype/ttnameid.h).

<pre>
#define TT_NAME_ID_COPYRIGHT              0
#define TT_NAME_ID_FONT_FAMILY            1
#define TT_NAME_ID_FONT_SUBFAMILY         2
#define TT_NAME_ID_UNIQUE_ID              3
#define TT_NAME_ID_FULL_NAME              4
#define TT_NAME_ID_VERSION_STRING         5
#define TT_NAME_ID_PS_NAME                6
#define TT_NAME_ID_TRADEMARK              7

  /* the following values are from the OpenType spec */
#define TT_NAME_ID_MANUFACTURER           8
#define TT_NAME_ID_DESIGNER               9
#define TT_NAME_ID_DESCRIPTION            10
#define TT_NAME_ID_VENDOR_URL             11
#define TT_NAME_ID_DESIGNER_URL           12
#define TT_NAME_ID_LICENSE                13
#define TT_NAME_ID_LICENSE_URL            14
  /* number 15 is reserved */
#define TT_NAME_ID_TYPOGRAPHIC_FAMILY     16
#define TT_NAME_ID_TYPOGRAPHIC_SUBFAMILY  17
#define TT_NAME_ID_MAC_FULL_NAME          18

  /* The following code is new as of 2000-01-21 */
#define TT_NAME_ID_SAMPLE_TEXT            19

  /* This is new in OpenType 1.3 */
#define TT_NAME_ID_CID_FINDFONT_NAME      20

  /* This is new in OpenType 1.5 */
#define TT_NAME_ID_WWS_FAMILY             21
#define TT_NAME_ID_WWS_SUBFAMILY          22

  /* This is new in OpenType 1.7 */
#define TT_NAME_ID_LIGHT_BACKGROUND       23
#define TT_NAME_ID_DARK_BACKGROUND        24

  /* This is new in OpenType 1.8 */
#define TT_NAME_ID_VARIATIONS_PREFIX      25

  /* these two values are deprecated */
#define TT_NAME_ID_PREFERRED_FAMILY     TT_NAME_ID_TYPOGRAPHIC_FAMILY
#define TT_NAME_ID_PREFERRED_SUBFAMILY  TT_NAME_ID_TYPOGRAPHIC_SUBFAMILY
</pre>


Possible values of the &lsquo;name&rsquo; identifier field in the name records of an SFNT &lsquo;name&rsquo; table. These values are platform independent.

<hr />

## TT_UCR_XXX

Defined in FT_TRUETYPE_IDS_H (freetype/ttnameid.h).

<pre>
  /* ulUnicodeRange1 */
  /* --------------- */

  /* Bit  0   Basic Latin */
#define TT_UCR_BASIC_LATIN                     (1L &lt;&lt;  0) /* U+0020-U+007E */
  /* Bit  1   C1 Controls and Latin-1 Supplement */
#define TT_UCR_LATIN1_SUPPLEMENT               (1L &lt;&lt;  1) /* U+0080-U+00FF */
  /* Bit  2   Latin Extended-A */
#define TT_UCR_LATIN_EXTENDED_A                (1L &lt;&lt;  2) /* U+0100-U+017F */
  /* Bit  3   Latin Extended-B */
#define TT_UCR_LATIN_EXTENDED_B                (1L &lt;&lt;  3) /* U+0180-U+024F */
  /* Bit  4   IPA Extensions                 */
  /*          Phonetic Extensions            */
  /*          Phonetic Extensions Supplement */
#define TT_UCR_IPA_EXTENSIONS                  (1L &lt;&lt;  4) /* U+0250-U+02AF */
                                                          /* U+1D00-U+1D7F */
                                                          /* U+1D80-U+1DBF */
  /* Bit  5   Spacing Modifier Letters */
  /*          Modifier Tone Letters    */
#define TT_UCR_SPACING_MODIFIER                (1L &lt;&lt;  5) /* U+02B0-U+02FF */
                                                          /* U+A700-U+A71F */
  /* Bit  6   Combining Diacritical Marks            */
  /*          Combining Diacritical Marks Supplement */
#define TT_UCR_COMBINING_DIACRITICAL_MARKS     (1L &lt;&lt;  6) /* U+0300-U+036F */
                                                          /* U+1DC0-U+1DFF */
  /* Bit  7   Greek and Coptic */
#define TT_UCR_GREEK                           (1L &lt;&lt;  7) /* U+0370-U+03FF */
  /* Bit  8   Coptic */
#define TT_UCR_COPTIC                          (1L &lt;&lt;  8) /* U+2C80-U+2CFF */
  /* Bit  9   Cyrillic            */
  /*          Cyrillic Supplement */
  /*          Cyrillic Extended-A */
  /*          Cyrillic Extended-B */
#define TT_UCR_CYRILLIC                        (1L &lt;&lt;  9) /* U+0400-U+04FF */
                                                          /* U+0500-U+052F */
                                                          /* U+2DE0-U+2DFF */
                                                          /* U+A640-U+A69F */
  /* Bit 10   Armenian */
#define TT_UCR_ARMENIAN                        (1L &lt;&lt; 10) /* U+0530-U+058F */
  /* Bit 11   Hebrew */
#define TT_UCR_HEBREW                          (1L &lt;&lt; 11) /* U+0590-U+05FF */
  /* Bit 12   Vai */
#define TT_UCR_VAI                             (1L &lt;&lt; 12) /* U+A500-U+A63F */
  /* Bit 13   Arabic            */
  /*          Arabic Supplement */
#define TT_UCR_ARABIC                          (1L &lt;&lt; 13) /* U+0600-U+06FF */
                                                          /* U+0750-U+077F */
  /* Bit 14   NKo */
#define TT_UCR_NKO                             (1L &lt;&lt; 14) /* U+07C0-U+07FF */
  /* Bit 15   Devanagari */
#define TT_UCR_DEVANAGARI                      (1L &lt;&lt; 15) /* U+0900-U+097F */
  /* Bit 16   Bengali */
#define TT_UCR_BENGALI                         (1L &lt;&lt; 16) /* U+0980-U+09FF */
  /* Bit 17   Gurmukhi */
#define TT_UCR_GURMUKHI                        (1L &lt;&lt; 17) /* U+0A00-U+0A7F */
  /* Bit 18   Gujarati */
#define TT_UCR_GUJARATI                        (1L &lt;&lt; 18) /* U+0A80-U+0AFF */
  /* Bit 19   Oriya */
#define TT_UCR_ORIYA                           (1L &lt;&lt; 19) /* U+0B00-U+0B7F */
  /* Bit 20   Tamil */
#define TT_UCR_TAMIL                           (1L &lt;&lt; 20) /* U+0B80-U+0BFF */
  /* Bit 21   Telugu */
#define TT_UCR_TELUGU                          (1L &lt;&lt; 21) /* U+0C00-U+0C7F */
  /* Bit 22   Kannada */
#define TT_UCR_KANNADA                         (1L &lt;&lt; 22) /* U+0C80-U+0CFF */
  /* Bit 23   Malayalam */
#define TT_UCR_MALAYALAM                       (1L &lt;&lt; 23) /* U+0D00-U+0D7F */
  /* Bit 24   Thai */
#define TT_UCR_THAI                            (1L &lt;&lt; 24) /* U+0E00-U+0E7F */
  /* Bit 25   Lao */
#define TT_UCR_LAO                             (1L &lt;&lt; 25) /* U+0E80-U+0EFF */
  /* Bit 26   Georgian            */
  /*          Georgian Supplement */
#define TT_UCR_GEORGIAN                        (1L &lt;&lt; 26) /* U+10A0-U+10FF */
                                                          /* U+2D00-U+2D2F */
  /* Bit 27   Balinese */
#define TT_UCR_BALINESE                        (1L &lt;&lt; 27) /* U+1B00-U+1B7F */
  /* Bit 28   Hangul Jamo */
#define TT_UCR_HANGUL_JAMO                     (1L &lt;&lt; 28) /* U+1100-U+11FF */
  /* Bit 29   Latin Extended Additional */
  /*          Latin Extended-C          */
  /*          Latin Extended-D          */
#define TT_UCR_LATIN_EXTENDED_ADDITIONAL       (1L &lt;&lt; 29) /* U+1E00-U+1EFF */
                                                          /* U+2C60-U+2C7F */
                                                          /* U+A720-U+A7FF */
  /* Bit 30   Greek Extended */
#define TT_UCR_GREEK_EXTENDED                  (1L &lt;&lt; 30) /* U+1F00-U+1FFF */
  /* Bit 31   General Punctuation      */
  /*          Supplemental Punctuation */
#define TT_UCR_GENERAL_PUNCTUATION             (1L &lt;&lt; 31) /* U+2000-U+206F */
                                                          /* U+2E00-U+2E7F */

  /* ulUnicodeRange2 */
  /* --------------- */

  /* Bit 32   Superscripts And Subscripts */
#define TT_UCR_SUPERSCRIPTS_SUBSCRIPTS         (1L &lt;&lt;  0) /* U+2070-U+209F */
  /* Bit 33   Currency Symbols */
#define TT_UCR_CURRENCY_SYMBOLS                (1L &lt;&lt;  1) /* U+20A0-U+20CF */
  /* Bit 34   Combining Diacritical Marks For Symbols */
#define TT_UCR_COMBINING_DIACRITICAL_MARKS_SYMB \
                                               (1L &lt;&lt;  2) /* U+20D0-U+20FF */
  /* Bit 35   Letterlike Symbols */
#define TT_UCR_LETTERLIKE_SYMBOLS              (1L &lt;&lt;  3) /* U+2100-U+214F */
  /* Bit 36   Number Forms */
#define TT_UCR_NUMBER_FORMS                    (1L &lt;&lt;  4) /* U+2150-U+218F */
  /* Bit 37   Arrows                           */
  /*          Supplemental Arrows-A            */
  /*          Supplemental Arrows-B            */
  /*          Miscellaneous Symbols and Arrows */
#define TT_UCR_ARROWS                          (1L &lt;&lt;  5) /* U+2190-U+21FF */
                                                          /* U+27F0-U+27FF */
                                                          /* U+2900-U+297F */
                                                          /* U+2B00-U+2BFF */
  /* Bit 38   Mathematical Operators               */
  /*          Supplemental Mathematical Operators  */
  /*          Miscellaneous Mathematical Symbols-A */
  /*          Miscellaneous Mathematical Symbols-B */
#define TT_UCR_MATHEMATICAL_OPERATORS          (1L &lt;&lt;  6) /* U+2200-U+22FF */
                                                          /* U+2A00-U+2AFF */
                                                          /* U+27C0-U+27EF */
                                                          /* U+2980-U+29FF */
  /* Bit 39 Miscellaneous Technical */
#define TT_UCR_MISCELLANEOUS_TECHNICAL         (1L &lt;&lt;  7) /* U+2300-U+23FF */
  /* Bit 40   Control Pictures */
#define TT_UCR_CONTROL_PICTURES                (1L &lt;&lt;  8) /* U+2400-U+243F */
  /* Bit 41   Optical Character Recognition */
#define TT_UCR_OCR                             (1L &lt;&lt;  9) /* U+2440-U+245F */
  /* Bit 42   Enclosed Alphanumerics */
#define TT_UCR_ENCLOSED_ALPHANUMERICS          (1L &lt;&lt; 10) /* U+2460-U+24FF */
  /* Bit 43   Box Drawing */
#define TT_UCR_BOX_DRAWING                     (1L &lt;&lt; 11) /* U+2500-U+257F */
  /* Bit 44   Block Elements */
#define TT_UCR_BLOCK_ELEMENTS                  (1L &lt;&lt; 12) /* U+2580-U+259F */
  /* Bit 45   Geometric Shapes */
#define TT_UCR_GEOMETRIC_SHAPES                (1L &lt;&lt; 13) /* U+25A0-U+25FF */
  /* Bit 46   Miscellaneous Symbols */
#define TT_UCR_MISCELLANEOUS_SYMBOLS           (1L &lt;&lt; 14) /* U+2600-U+26FF */
  /* Bit 47   Dingbats */
#define TT_UCR_DINGBATS                        (1L &lt;&lt; 15) /* U+2700-U+27BF */
  /* Bit 48   CJK Symbols and Punctuation */
#define TT_UCR_CJK_SYMBOLS                     (1L &lt;&lt; 16) /* U+3000-U+303F */
  /* Bit 49   Hiragana */
#define TT_UCR_HIRAGANA                        (1L &lt;&lt; 17) /* U+3040-U+309F */
  /* Bit 50   Katakana                     */
  /*          Katakana Phonetic Extensions */
#define TT_UCR_KATAKANA                        (1L &lt;&lt; 18) /* U+30A0-U+30FF */
                                                          /* U+31F0-U+31FF */
  /* Bit 51   Bopomofo          */
  /*          Bopomofo Extended */
#define TT_UCR_BOPOMOFO                        (1L &lt;&lt; 19) /* U+3100-U+312F */
                                                          /* U+31A0-U+31BF */
  /* Bit 52   Hangul Compatibility Jamo */
#define TT_UCR_HANGUL_COMPATIBILITY_JAMO       (1L &lt;&lt; 20) /* U+3130-U+318F */
  /* Bit 53   Phags-Pa */
#define TT_UCR_CJK_MISC                        (1L &lt;&lt; 21) /* U+A840-U+A87F */
#define TT_UCR_KANBUN  TT_UCR_CJK_MISC /* deprecated */
#define TT_UCR_PHAGSPA
  /* Bit 54   Enclosed CJK Letters and Months */
#define TT_UCR_ENCLOSED_CJK_LETTERS_MONTHS     (1L &lt;&lt; 22) /* U+3200-U+32FF */
  /* Bit 55   CJK Compatibility */
#define TT_UCR_CJK_COMPATIBILITY               (1L &lt;&lt; 23) /* U+3300-U+33FF */
  /* Bit 56   Hangul Syllables */
#define TT_UCR_HANGUL                          (1L &lt;&lt; 24) /* U+AC00-U+D7A3 */
  /* Bit 57   High Surrogates              */
  /*          High Private Use Surrogates  */
  /*          Low Surrogates               */

  /* According to OpenType specs v.1.3+,   */
  /* setting bit 57 implies that there is  */
  /* at least one codepoint beyond the     */
  /* Basic Multilingual Plane that is      */
  /* supported by this font.  So it really */
  /* means &gt;= U+10000.                     */
#define TT_UCR_SURROGATES                      (1L &lt;&lt; 25) /* U+D800-U+DB7F */
                                                          /* U+DB80-U+DBFF */
                                                          /* U+DC00-U+DFFF */
#define TT_UCR_NON_PLANE_0  TT_UCR_SURROGATES
  /* Bit 58  Phoenician */
#define TT_UCR_PHOENICIAN                      (1L &lt;&lt; 26) /*U+10900-U+1091F*/
  /* Bit 59   CJK Unified Ideographs             */
  /*          CJK Radicals Supplement            */
  /*          Kangxi Radicals                    */
  /*          Ideographic Description Characters */
  /*          CJK Unified Ideographs Extension A */
  /*          CJK Unified Ideographs Extension B */
  /*          Kanbun                             */
#define TT_UCR_CJK_UNIFIED_IDEOGRAPHS          (1L &lt;&lt; 27) /* U+4E00-U+9FFF */
                                                          /* U+2E80-U+2EFF */
                                                          /* U+2F00-U+2FDF */
                                                          /* U+2FF0-U+2FFF */
                                                          /* U+3400-U+4DB5 */
                                                          /*U+20000-U+2A6DF*/
                                                          /* U+3190-U+319F */
  /* Bit 60   Private Use */
#define TT_UCR_PRIVATE_USE                     (1L &lt;&lt; 28) /* U+E000-U+F8FF */
  /* Bit 61   CJK Strokes                             */
  /*          CJK Compatibility Ideographs            */
  /*          CJK Compatibility Ideographs Supplement */
#define TT_UCR_CJK_COMPATIBILITY_IDEOGRAPHS    (1L &lt;&lt; 29) /* U+31C0-U+31EF */
                                                          /* U+F900-U+FAFF */
                                                          /*U+2F800-U+2FA1F*/
  /* Bit 62   Alphabetic Presentation Forms */
#define TT_UCR_ALPHABETIC_PRESENTATION_FORMS   (1L &lt;&lt; 30) /* U+FB00-U+FB4F */
  /* Bit 63   Arabic Presentation Forms-A */
#define TT_UCR_ARABIC_PRESENTATION_FORMS_A     (1L &lt;&lt; 31) /* U+FB50-U+FDFF */

  /* ulUnicodeRange3 */
  /* --------------- */

  /* Bit 64   Combining Half Marks */
#define TT_UCR_COMBINING_HALF_MARKS            (1L &lt;&lt;  0) /* U+FE20-U+FE2F */
  /* Bit 65   Vertical forms          */
  /*          CJK Compatibility Forms */
#define TT_UCR_CJK_COMPATIBILITY_FORMS         (1L &lt;&lt;  1) /* U+FE10-U+FE1F */
                                                          /* U+FE30-U+FE4F */
  /* Bit 66   Small Form Variants */
#define TT_UCR_SMALL_FORM_VARIANTS             (1L &lt;&lt;  2) /* U+FE50-U+FE6F */
  /* Bit 67   Arabic Presentation Forms-B */
#define TT_UCR_ARABIC_PRESENTATION_FORMS_B     (1L &lt;&lt;  3) /* U+FE70-U+FEFE */
  /* Bit 68   Halfwidth and Fullwidth Forms */
#define TT_UCR_HALFWIDTH_FULLWIDTH_FORMS       (1L &lt;&lt;  4) /* U+FF00-U+FFEF */
  /* Bit 69   Specials */
#define TT_UCR_SPECIALS                        (1L &lt;&lt;  5) /* U+FFF0-U+FFFD */
  /* Bit 70   Tibetan */
#define TT_UCR_TIBETAN                         (1L &lt;&lt;  6) /* U+0F00-U+0FFF */
  /* Bit 71   Syriac */
#define TT_UCR_SYRIAC                          (1L &lt;&lt;  7) /* U+0700-U+074F */
  /* Bit 72   Thaana */
#define TT_UCR_THAANA                          (1L &lt;&lt;  8) /* U+0780-U+07BF */
  /* Bit 73   Sinhala */
#define TT_UCR_SINHALA                         (1L &lt;&lt;  9) /* U+0D80-U+0DFF */
  /* Bit 74   Myanmar */
#define TT_UCR_MYANMAR                         (1L &lt;&lt; 10) /* U+1000-U+109F */
  /* Bit 75   Ethiopic            */
  /*          Ethiopic Supplement */
  /*          Ethiopic Extended   */
#define TT_UCR_ETHIOPIC                        (1L &lt;&lt; 11) /* U+1200-U+137F */
                                                          /* U+1380-U+139F */
                                                          /* U+2D80-U+2DDF */
  /* Bit 76   Cherokee */
#define TT_UCR_CHEROKEE                        (1L &lt;&lt; 12) /* U+13A0-U+13FF */
  /* Bit 77   Unified Canadian Aboriginal Syllabics */
#define TT_UCR_CANADIAN_ABORIGINAL_SYLLABICS   (1L &lt;&lt; 13) /* U+1400-U+167F */
  /* Bit 78   Ogham */
#define TT_UCR_OGHAM                           (1L &lt;&lt; 14) /* U+1680-U+169F */
  /* Bit 79   Runic */
#define TT_UCR_RUNIC                           (1L &lt;&lt; 15) /* U+16A0-U+16FF */
  /* Bit 80   Khmer         */
  /*          Khmer Symbols */
#define TT_UCR_KHMER                           (1L &lt;&lt; 16) /* U+1780-U+17FF */
                                                          /* U+19E0-U+19FF */
  /* Bit 81   Mongolian */
#define TT_UCR_MONGOLIAN                       (1L &lt;&lt; 17) /* U+1800-U+18AF */
  /* Bit 82   Braille Patterns */
#define TT_UCR_BRAILLE                         (1L &lt;&lt; 18) /* U+2800-U+28FF */
  /* Bit 83   Yi Syllables */
  /*          Yi Radicals  */
#define TT_UCR_YI                              (1L &lt;&lt; 19) /* U+A000-U+A48F */
                                                          /* U+A490-U+A4CF */
  /* Bit 84   Tagalog  */
  /*          Hanunoo  */
  /*          Buhid    */
  /*          Tagbanwa */
#define TT_UCR_PHILIPPINE                      (1L &lt;&lt; 20) /* U+1700-U+171F */
                                                          /* U+1720-U+173F */
                                                          /* U+1740-U+175F */
                                                          /* U+1760-U+177F */
  /* Bit 85   Old Italic */
#define TT_UCR_OLD_ITALIC                      (1L &lt;&lt; 21) /*U+10300-U+1032F*/
  /* Bit 86   Gothic */
#define TT_UCR_GOTHIC                          (1L &lt;&lt; 22) /*U+10330-U+1034F*/
  /* Bit 87   Deseret */
#define TT_UCR_DESERET                         (1L &lt;&lt; 23) /*U+10400-U+1044F*/
  /* Bit 88   Byzantine Musical Symbols      */
  /*          Musical Symbols                */
  /*          Ancient Greek Musical Notation */
#define TT_UCR_MUSICAL_SYMBOLS                 (1L &lt;&lt; 24) /*U+1D000-U+1D0FF*/
                                                          /*U+1D100-U+1D1FF*/
                                                          /*U+1D200-U+1D24F*/
  /* Bit 89   Mathematical Alphanumeric Symbols */
#define TT_UCR_MATH_ALPHANUMERIC_SYMBOLS       (1L &lt;&lt; 25) /*U+1D400-U+1D7FF*/
  /* Bit 90   Private Use (plane 15) */
  /*          Private Use (plane 16) */
#define TT_UCR_PRIVATE_USE_SUPPLEMENTARY       (1L &lt;&lt; 26) /*U+F0000-U+FFFFD*/
                                                        /*U+100000-U+10FFFD*/
  /* Bit 91   Variation Selectors            */
  /*          Variation Selectors Supplement */
#define TT_UCR_VARIATION_SELECTORS             (1L &lt;&lt; 27) /* U+FE00-U+FE0F */
                                                          /*U+E0100-U+E01EF*/
  /* Bit 92   Tags */
#define TT_UCR_TAGS                            (1L &lt;&lt; 28) /*U+E0000-U+E007F*/
  /* Bit 93   Limbu */
#define TT_UCR_LIMBU                           (1L &lt;&lt; 29) /* U+1900-U+194F */
  /* Bit 94   Tai Le */
#define TT_UCR_TAI_LE                          (1L &lt;&lt; 30) /* U+1950-U+197F */
  /* Bit 95   New Tai Lue */
#define TT_UCR_NEW_TAI_LUE                     (1L &lt;&lt; 31) /* U+1980-U+19DF */

  /* ulUnicodeRange4 */
  /* --------------- */

  /* Bit 96   Buginese */
#define TT_UCR_BUGINESE                        (1L &lt;&lt;  0) /* U+1A00-U+1A1F */
  /* Bit 97   Glagolitic */
#define TT_UCR_GLAGOLITIC                      (1L &lt;&lt;  1) /* U+2C00-U+2C5F */
  /* Bit 98   Tifinagh */
#define TT_UCR_TIFINAGH                        (1L &lt;&lt;  2) /* U+2D30-U+2D7F */
  /* Bit 99   Yijing Hexagram Symbols */
#define TT_UCR_YIJING                          (1L &lt;&lt;  3) /* U+4DC0-U+4DFF */
  /* Bit 100  Syloti Nagri */
#define TT_UCR_SYLOTI_NAGRI                    (1L &lt;&lt;  4) /* U+A800-U+A82F */
  /* Bit 101  Linear B Syllabary */
  /*          Linear B Ideograms */
  /*          Aegean Numbers     */
#define TT_UCR_LINEAR_B                        (1L &lt;&lt;  5) /*U+10000-U+1007F*/
                                                          /*U+10080-U+100FF*/
                                                          /*U+10100-U+1013F*/
  /* Bit 102  Ancient Greek Numbers */
#define TT_UCR_ANCIENT_GREEK_NUMBERS           (1L &lt;&lt;  6) /*U+10140-U+1018F*/
  /* Bit 103  Ugaritic */
#define TT_UCR_UGARITIC                        (1L &lt;&lt;  7) /*U+10380-U+1039F*/
  /* Bit 104  Old Persian */
#define TT_UCR_OLD_PERSIAN                     (1L &lt;&lt;  8) /*U+103A0-U+103DF*/
  /* Bit 105  Shavian */
#define TT_UCR_SHAVIAN                         (1L &lt;&lt;  9) /*U+10450-U+1047F*/
  /* Bit 106  Osmanya */
#define TT_UCR_OSMANYA                         (1L &lt;&lt; 10) /*U+10480-U+104AF*/
  /* Bit 107  Cypriot Syllabary */
#define TT_UCR_CYPRIOT_SYLLABARY               (1L &lt;&lt; 11) /*U+10800-U+1083F*/
  /* Bit 108  Kharoshthi */
#define TT_UCR_KHAROSHTHI                      (1L &lt;&lt; 12) /*U+10A00-U+10A5F*/
  /* Bit 109  Tai Xuan Jing Symbols */
#define TT_UCR_TAI_XUAN_JING                   (1L &lt;&lt; 13) /*U+1D300-U+1D35F*/
  /* Bit 110  Cuneiform                         */
  /*          Cuneiform Numbers and Punctuation */
#define TT_UCR_CUNEIFORM                       (1L &lt;&lt; 14) /*U+12000-U+123FF*/
                                                          /*U+12400-U+1247F*/
  /* Bit 111  Counting Rod Numerals */
#define TT_UCR_COUNTING_ROD_NUMERALS           (1L &lt;&lt; 15) /*U+1D360-U+1D37F*/
  /* Bit 112  Sundanese */
#define TT_UCR_SUNDANESE                       (1L &lt;&lt; 16) /* U+1B80-U+1BBF */
  /* Bit 113  Lepcha */
#define TT_UCR_LEPCHA                          (1L &lt;&lt; 17) /* U+1C00-U+1C4F */
  /* Bit 114  Ol Chiki */
#define TT_UCR_OL_CHIKI                        (1L &lt;&lt; 18) /* U+1C50-U+1C7F */
  /* Bit 115  Saurashtra */
#define TT_UCR_SAURASHTRA                      (1L &lt;&lt; 19) /* U+A880-U+A8DF */
  /* Bit 116  Kayah Li */
#define TT_UCR_KAYAH_LI                        (1L &lt;&lt; 20) /* U+A900-U+A92F */
  /* Bit 117  Rejang */
#define TT_UCR_REJANG                          (1L &lt;&lt; 21) /* U+A930-U+A95F */
  /* Bit 118  Cham */
#define TT_UCR_CHAM                            (1L &lt;&lt; 22) /* U+AA00-U+AA5F */
  /* Bit 119  Ancient Symbols */
#define TT_UCR_ANCIENT_SYMBOLS                 (1L &lt;&lt; 23) /*U+10190-U+101CF*/
  /* Bit 120  Phaistos Disc */
#define TT_UCR_PHAISTOS_DISC                   (1L &lt;&lt; 24) /*U+101D0-U+101FF*/
  /* Bit 121  Carian */
  /*          Lycian */
  /*          Lydian */
#define TT_UCR_OLD_ANATOLIAN                   (1L &lt;&lt; 25) /*U+102A0-U+102DF*/
                                                          /*U+10280-U+1029F*/
                                                          /*U+10920-U+1093F*/
  /* Bit 122  Domino Tiles  */
  /*          Mahjong Tiles */
#define TT_UCR_GAME_TILES                      (1L &lt;&lt; 26) /*U+1F030-U+1F09F*/
                                                          /*U+1F000-U+1F02F*/
  /* Bit 123-127 Reserved for process-internal usage */
</pre>


Possible bit mask values for the &lsquo;ulUnicodeRangeX&rsquo; fields in an SFNT &lsquo;OS/2&rsquo; table.

<hr />
