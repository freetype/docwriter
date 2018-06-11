[Docs](ft2-index.md) &raquo; [Controlling FreeType Modules](ft2-toc.md#controlling-freetype-modules) &raquo; Driver properties

-------------------------------

# Driver properties

## Synopsis

Driver modules can be controlled by setting and unsetting properties, using the functions <a href="../ft2-module_management/#ft_property_set">FT_Property_Set</a> and <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a>. This section documents the available properties, together with auxiliary macros and structures.

## FT_HINTING_XXX

Defined in FT_DRIVER_H (freetype/ftdriver.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <a href="../ft2-properties/#ft_hinting_freetype">FT_HINTING_FREETYPE</a>  0
#<span class="keyword">define</span> <a href="../ft2-properties/#ft_hinting_adobe">FT_HINTING_ADOBE</a>     1

  /* these constants (introduced in 2.4.12) are deprecated */
#<span class="keyword">define</span> FT_CFF_HINTING_FREETYPE  <a href="../ft2-properties/#ft_hinting_freetype">FT_HINTING_FREETYPE</a>
#<span class="keyword">define</span> FT_CFF_HINTING_ADOBE     <a href="../ft2-properties/#ft_hinting_adobe">FT_HINTING_ADOBE</a>
</pre>
</div>


A list of constants used for the <a href="../ft2-properties/#hinting-engine">hinting-engine</a> property to select the hinting engine for CFF, Type&nbsp;1, and CID fonts.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_hinting_freetype">FT_HINTING_FREETYPE</td><td class="desc">
<p>Use the old FreeType hinting engine.</p>
</td></tr>
<tr><td class="val" id="ft_hinting_adobe">FT_HINTING_ADOBE</td><td class="desc">
<p>Use the hinting engine contributed by Adobe.</p>
</td></tr>
</table>

<h4>since</h4>

2.9

<hr>

## hinting-engine



Thanks to Adobe, which contributed a new hinting (and parsing) engine, an application can select between &lsquo;freetype&rsquo; and &lsquo;adobe&rsquo; if compiled with CFF_CONFIG_OPTION_OLD_ENGINE. If this configuration macro isn't defined, &lsquo;hinting-engine&rsquo; does nothing.

The same holds for the Type&nbsp;1 and CID modules if compiled with T1_CONFIG_OPTION_OLD_ENGINE.

For the &lsquo;cff&rsquo; module, the default engine is &lsquo;freetype&rsquo; if CFF_CONFIG_OPTION_OLD_ENGINE is defined, and &lsquo;adobe&rsquo; otherwise.

For both the &lsquo;type1&rsquo; and &lsquo;t1cid&rsquo; modules, the default engine is &lsquo;freetype&rsquo; if T1_CONFIG_OPTION_OLD_ENGINE is defined, and &lsquo;adobe&rsquo; otherwise.

The following example code demonstrates how to select Adobe's hinting engine for the &lsquo;cff&rsquo; module (omitting the error handling).
```
  FT_Library  library;
  FT_UInt     hinting_engine = FT_CFF_HINTING_ADOBE;


  FT_Init_FreeType( &library );

  FT_Property_Set( library, "cff",
                            "hinting-engine", &hinting_engine );
```

<h4>note</h4>

This property can be used with <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a> also.

This property can be set via the &lsquo;FREETYPE_PROPERTIES&rsquo; environment variable (using values &lsquo;adobe&rsquo; or &lsquo;freetype&rsquo;).

<h4>since</h4>

2.4.12 (for &lsquo;cff&rsquo; module)

2.9 (for &lsquo;type1&rsquo; and &lsquo;t1cid&rsquo; modules)

<hr>

## no-stem-darkening



All glyphs that pass through the auto-hinter will be emboldened unless this property is set to TRUE. The same is true for the CFF, Type&nbsp;1, and CID font modules if the &lsquo;Adobe&rsquo; engine is selected (which is the default).

Stem darkening emboldens glyphs at smaller sizes to make them more readable on common low-DPI screens when using linear alpha blending and gamma correction, see <a href="../ft2-base_interface/#ft_render_glyph">FT_Render_Glyph</a>. When not using linear alpha blending and gamma correction, glyphs will appear heavy and fuzzy!

Gamma correction essentially lightens fonts since shades of grey are shifted to higher pixel values (=&nbsp;higher brightness) to match the original intention to the reality of our screens. The side-effect is that glyphs &lsquo;thin out&rsquo;. Mac OS&nbsp;X and Adobe's proprietary font rendering library implement a counter-measure: stem darkening at smaller sizes where shades of gray dominate. By emboldening a glyph slightly in relation to its pixel size, individual pixels get higher coverage of filled-in outlines and are therefore &lsquo;blacker&rsquo;. This counteracts the &lsquo;thinning out&rsquo; of glyphs, making text remain readable at smaller sizes.

By default, the Adobe engines for CFF, Type&nbsp;1, and CID fonts darken stems at smaller sizes, regardless of hinting, to enhance contrast. Setting this property, stem darkening gets switched off.

For the auto-hinter, stem-darkening is experimental currently and thus switched off by default (this is, &lsquo;no-stem-darkening&rsquo; is set to TRUE by default). Total consistency with the CFF driver is not achieved right now because the emboldening method differs and glyphs must be scaled down on the Y-axis to keep outline points inside their precomputed blue zones. The smaller the size (especially 9ppem and down), the higher the loss of emboldening versus the CFF driver.

Note that stem darkening is never applied if <a href="../ft2-base_interface/#ft_load_xxx">FT_LOAD_NO_SCALE</a> is set.
```
  FT_Library  library;
  FT_Bool     no_stem_darkening = TRUE;


  FT_Init_FreeType( &library );

  FT_Property_Set( library, "cff",
                            "no-stem-darkening", &no_stem_darkening );
```

<h4>note</h4>

This property can be used with <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a> also.

This property can be set via the &lsquo;FREETYPE_PROPERTIES&rsquo; environment variable (using values 1 and 0 for &lsquo;on&rsquo; and &lsquo;off&rsquo;, respectively). It can also be set per face using <a href="../ft2-base_interface/#ft_face_properties">FT_Face_Properties</a> with <a href="../ft2-parameter_tags/#ft_param_tag_stem_darkening">FT_PARAM_TAG_STEM_DARKENING</a>.

<h4>since</h4>

2.4.12 (for &lsquo;cff&rsquo; module)

2.6.2 (for &lsquo;autofitter&rsquo; module)

2.9 (for &lsquo;type1&rsquo; and &lsquo;t1cid&rsquo; modules)

<hr>

## darkening-parameters



By default, the Adobe hinting engine, as used by the CFF, Type&nbsp;1, and CID font drivers, darkens stems as follows (if the &lsquo;no-stem-darkening&rsquo; property isn't set):
```
  stem width <= 0.5px:   darkening amount = 0.4px
  stem width  = 1px:     darkening amount = 0.275px
  stem width  = 1.667px: darkening amount = 0.275px
  stem width >= 2.333px: darkening amount = 0px
```

and piecewise linear in-between. At configuration time, these four control points can be set with the macro &lsquo;CFF_CONFIG_OPTION_DARKENING_PARAMETERS&rsquo;; the CFF, Type&nbsp;1, and CID drivers share these values. At runtime, the control points can be changed using the &lsquo;darkening-parameters&rsquo; property, as the following example demonstrates for the Type&nbsp;1 driver.
```
  FT_Library  library;
  FT_Int      darken_params[8] = {  500, 300,   // x1, y1
                                   1000, 200,   // x2, y2
                                   1500, 100,   // x3, y3
                                   2000,   0 }; // x4, y4


  FT_Init_FreeType( &library );

  FT_Property_Set( library, "type1",
                            "darkening-parameters", darken_params );
```

The x&nbsp;values give the stem width, and the y&nbsp;values the darkening amount. The unit is 1000th of pixels. All coordinate values must be positive; the x&nbsp;values must be monotonically increasing; the y&nbsp;values must be monotonically decreasing and smaller than or equal to 500 (corresponding to half a pixel); the slope of each linear piece must be shallower than -1 (e.g., -.4).

The auto-hinter provides this property, too, as an experimental feature. See <a href="../ft2-properties/#no-stem-darkening">no-stem-darkening</a> for more.

<h4>note</h4>

This property can be used with <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a> also.

This property can be set via the &lsquo;FREETYPE_PROPERTIES&rsquo; environment variable, using eight comma-separated integers without spaces. Here the above example, using &lsquo;\&rsquo; to break the line for readability.
```
  FREETYPE_PROPERTIES=\
  type1:darkening-parameters=500,300,1000,200,1500,100,2000,0
```

<h4>since</h4>

2.5.1 (for &lsquo;cff&rsquo; module)

2.6.2 (for &lsquo;autofitter&rsquo; module)

2.9 (for &lsquo;type1&rsquo; and &lsquo;t1cid&rsquo; modules)

<hr>

## random-seed



By default, the seed value for the CFF &lsquo;random&rsquo; operator and the similar &lsquo;0 28 callothersubr pop&rsquo; command for the Type&nbsp;1 and CID drivers is set to a random value. However, mainly for debugging purposes, it is often necessary to use a known value as a seed so that the pseudo-random number sequences generated by &lsquo;random&rsquo; are repeatable.

The &lsquo;random-seed&rsquo; property does that. Its argument is a signed 32bit integer; if the value is zero or negative, the seed given by the &lsquo;intitialRandomSeed&rsquo; private DICT operator in a CFF file gets used (or a default value if there is no such operator). If the value is positive, use it instead of &lsquo;initialRandomSeed&rsquo;, which is consequently ignored.

<h4>note</h4>

This property can be set via the &lsquo;FREETYPE_PROPERTIES&rsquo; environment variable. It can also be set per face using <a href="../ft2-base_interface/#ft_face_properties">FT_Face_Properties</a> with <a href="../ft2-parameter_tags/#ft_param_tag_random_seed">FT_PARAM_TAG_RANDOM_SEED</a>.

<h4>since</h4>

2.8 (for &lsquo;cff&rsquo; module)

2.9 (for &lsquo;type1&rsquo; and &lsquo;t1cid&rsquo; modules)

<hr>

## no-long-family-names



If PCF_CONFIG_OPTION_LONG_FAMILY_NAMES is active while compiling FreeType, the PCF driver constructs long family names.

There are many PCF fonts just called &lsquo;Fixed&rsquo; which look completely different, and which have nothing to do with each other. When selecting &lsquo;Fixed&rsquo; in KDE or Gnome one gets results that appear rather random, the style changes often if one changes the size and one cannot select some fonts at all. The improve this situation, the PCF module prepends the foundry name (plus a space) to the family name. It also checks whether there are &lsquo;wide&rsquo; characters; all put together, family names like &lsquo;Sony Fixed&rsquo; or &lsquo;Misc Fixed Wide&rsquo; are constructed.

If &lsquo;no-long-family-names&rsquo; is set, this feature gets switched off.
```
  FT_Library  library;
  FT_Bool     no_long_family_names = TRUE;


  FT_Init_FreeType( &library );

  FT_Property_Set( library, "pcf",
                            "no-long-family-names",
                            &no_long_family_names );
```

<h4>note</h4>

This property can be used with <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a> also.

This property can be set via the &lsquo;FREETYPE_PROPERTIES&rsquo; environment variable (using values 1 and 0 for &lsquo;on&rsquo; and &lsquo;off&rsquo;, respectively).

<h4>since</h4>

2.8

<hr>

## TT_INTERPRETER_VERSION_XXX

Defined in FT_DRIVER_H (freetype/ftdriver.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <a href="../ft2-properties/#tt_interpreter_version_35">TT_INTERPRETER_VERSION_35</a>  35
#<span class="keyword">define</span> <a href="../ft2-properties/#tt_interpreter_version_38">TT_INTERPRETER_VERSION_38</a>  38
#<span class="keyword">define</span> <a href="../ft2-properties/#tt_interpreter_version_40">TT_INTERPRETER_VERSION_40</a>  40
</pre>
</div>


A list of constants used for the <a href="../ft2-properties/#interpreter-version">interpreter-version</a> property to select the hinting engine for Truetype fonts.

The numeric value in the constant names represents the version number as returned by the &lsquo;GETINFO&rsquo; bytecode instruction.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="tt_interpreter_version_35">TT_INTERPRETER_VERSION_35</td><td class="desc">
<p>Version&nbsp;35 corresponds to MS rasterizer v.1.7 as used e.g. in Windows&nbsp;98; only grayscale and B/W rasterizing is supported.</p>
</td></tr>
<tr><td class="val" id="tt_interpreter_version_38">TT_INTERPRETER_VERSION_38</td><td class="desc">
<p>Version&nbsp;38 corresponds to MS rasterizer v.1.9; it is roughly equivalent to the hinting provided by DirectWrite ClearType (as can be found, for example, in the Internet Explorer&nbsp;9 running on Windows&nbsp;7). It is used in FreeType to select the &lsquo;Infinality&rsquo; subpixel hinting code. The code may be removed in a future version.</p>
</td></tr>
<tr><td class="val" id="tt_interpreter_version_40">TT_INTERPRETER_VERSION_40</td><td class="desc">
<p>Version&nbsp;40 corresponds to MS rasterizer v.2.1; it is roughly equivalent to the hinting provided by DirectWrite ClearType (as can be found, for example, in Microsoft's Edge Browser on Windows&nbsp;10). It is used in FreeType to select the &lsquo;minimal&rsquo; subpixel hinting code, a stripped-down and higher performance version of the &lsquo;Infinality&rsquo; code.</p>
</td></tr>
</table>

<h4>note</h4>

This property controls the behaviour of the bytecode interpreter and thus how outlines get hinted. It does **not** control how glyph get rasterized! In particular, it does not control subpixel color filtering.

If FreeType has not been compiled with the configuration option TT_CONFIG_OPTION_SUBPIXEL_HINTING, selecting version&nbsp;38 or&nbsp;40 causes an &lsquo;FT_Err_Unimplemented_Feature&rsquo; error.

Depending on the graphics framework, Microsoft uses different bytecode and rendering engines. As a consequence, the version numbers returned by a call to the &lsquo;GETINFO&rsquo; bytecode instruction are more convoluted than desired.

Here are two tables that try to shed some light on the possible values for the MS rasterizer engine, together with the additional features introduced by it.
```
  GETINFO framework               version feature
  -------------------------------------------------------------------
      3   GDI (Win 3.1),            v1.0  16-bit, first version
          TrueImage
     33   GDI (Win NT 3.1),         v1.5  32-bit
          HP Laserjet
     34   GDI (Win 95)              v1.6  font smoothing,
                                          new SCANTYPE opcode
     35   GDI (Win 98/2000)         v1.7  (UN)SCALED_COMPONENT_OFFSET
                                            bits in composite glyphs
     36   MGDI (Win CE 2)           v1.6+ classic ClearType
     37   GDI (XP and later),       v1.8  ClearType
          GDI+ old (before Vista)
     38   GDI+ old (Vista, Win 7),  v1.9  subpixel ClearType,
          WPF                             Y-direction ClearType,
                                          additional error checking
     39   DWrite (before Win 8)     v2.0  subpixel ClearType flags
                                            in GETINFO opcode,
                                          bug fixes
     40   GDI+ (after Win 7),       v2.1  Y-direction ClearType flag
          DWrite (Win 8)                    in GETINFO opcode,
                                          Gray ClearType
```

The &lsquo;version&rsquo; field gives a rough orientation only, since some applications provided certain features much earlier (as an example, Microsoft Reader used subpixel and Y-direction ClearType already in Windows 2000). Similarly, updates to a given framework might include improved hinting support.
```
   version   sampling          rendering        comment
            x        y       x           y
  --------------------------------------------------------------
    v1.0   normal  normal  B/W           B/W    bi-level
    v1.6   high    high    gray          gray   grayscale
    v1.8   high    normal  color-filter  B/W    (GDI) ClearType
    v1.9   high    high    color-filter  gray   Color ClearType
    v2.1   high    normal  gray          B/W    Gray ClearType
    v2.1   high    high    gray          gray   Gray ClearType
```

Color and Gray ClearType are the two available variants of &lsquo;Y-direction ClearType&rsquo;, meaning grayscale rasterization along the Y-direction; the name used in the TrueType specification for this feature is &lsquo;symmetric smoothing&rsquo;. &lsquo;Classic ClearType&rsquo; is the original algorithm used before introducing a modified version in Win&nbsp;XP. Another name for v1.6's grayscale rendering is &lsquo;font smoothing&rsquo;, and &lsquo;Color ClearType&rsquo; is sometimes also called &lsquo;DWrite ClearType&rsquo;. To differentiate between today's Color ClearType and the earlier ClearType variant with B/W rendering along the vertical axis, the latter is sometimes called &lsquo;GDI ClearType&rsquo;.

&lsquo;Normal&rsquo; and &lsquo;high&rsquo; sampling describe the (virtual) resolution to access the rasterized outline after the hinting process. &lsquo;Normal&rsquo; means 1 sample per grid line (i.e., B/W). In the current Microsoft implementation, &lsquo;high&rsquo; means an extra virtual resolution of 16x16 (or 16x1) grid lines per pixel for bytecode instructions like &lsquo;MIRP&rsquo;. After hinting, these 16 grid lines are mapped to 6x5 (or 6x1) grid lines for color filtering if Color ClearType is activated.

Note that &lsquo;Gray ClearType&rsquo; is essentially the same as v1.6's grayscale rendering. However, the GETINFO instruction handles it differently: v1.6 returns bit&nbsp;12 (hinting for grayscale), while v2.1 returns bits&nbsp;13 (hinting for ClearType), 18 (symmetrical smoothing), and&nbsp;19 (Gray ClearType). Also, this mode respects bits 2 and&nbsp;3 for the version&nbsp;1 gasp table exclusively (like Color ClearType), while v1.6 only respects the values of version&nbsp;0 (bits 0 and&nbsp;1).

Keep in mind that the features of the above interpreter versions might not map exactly to FreeType features or behavior because it is a fundamentally different library with different internals.

<hr>

## interpreter-version



Currently, three versions are available, two representing the bytecode interpreter with subpixel hinting support (old &lsquo;Infinality&rsquo; code and new stripped-down and higher performance &lsquo;minimal&rsquo; code) and one without, respectively. The default is subpixel support if TT_CONFIG_OPTION_SUBPIXEL_HINTING is defined, and no subpixel support otherwise (since it isn't available then).

If subpixel hinting is on, many TrueType bytecode instructions behave differently compared to B/W or grayscale rendering (except if &lsquo;native ClearType&rsquo; is selected by the font). Microsoft's main idea is to render at a much increased horizontal resolution, then sampling down the created output to subpixel precision. However, many older fonts are not suited to this and must be specially taken care of by applying (hardcoded) tweaks in Microsoft's interpreter.

Details on subpixel hinting and some of the necessary tweaks can be found in Greg Hitchcock's whitepaper at &lsquo;<https://www.microsoft.com/typography/cleartype/truetypecleartype.aspx>&rsquo;. Note that FreeType currently doesn't really &lsquo;subpixel hint&rsquo; (6x1, 6x2, or 6x5 supersampling) like discussed in the paper. Depending on the chosen interpreter, it simply ignores instructions on vertical stems to arrive at very similar results.

The following example code demonstrates how to deactivate subpixel hinting (omitting the error handling).
```
  FT_Library  library;
  FT_Face     face;
  FT_UInt     interpreter_version = TT_INTERPRETER_VERSION_35;


  FT_Init_FreeType( &library );

  FT_Property_Set( library, "truetype",
                            "interpreter-version",
                            &interpreter_version );
```

<h4>note</h4>

This property can be used with <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a> also.

This property can be set via the &lsquo;FREETYPE_PROPERTIES&rsquo; environment variable (using values &lsquo;35&rsquo;, &lsquo;38&rsquo;, or &lsquo;40&rsquo;).

<h4>since</h4>

2.5

<hr>

## glyph-to-script-map



**Experimental only**

The auto-hinter provides various script modules to hint glyphs. Examples of supported scripts are Latin or CJK. Before a glyph is auto-hinted, the Unicode character map of the font gets examined, and the script is then determined based on Unicode character ranges, see below.

OpenType fonts, however, often provide much more glyphs than character codes (small caps, superscripts, ligatures, swashes, etc.), to be controlled by so-called &lsquo;features&rsquo;. Handling OpenType features can be quite complicated and thus needs a separate library on top of FreeType.

The mapping between glyph indices and scripts (in the auto-hinter sense, see the <a href="../ft2-properties/#ft_autohinter_script_xxx">FT_AUTOHINTER_SCRIPT_XXX</a> values) is stored as an array with &lsquo;num_glyphs&rsquo; elements, as found in the font's <a href="../ft2-base_interface/#ft_face">FT_Face</a> structure. The &lsquo;glyph-to-script-map&rsquo; property returns a pointer to this array, which can be modified as needed. Note that the modification should happen before the first glyph gets processed by the auto-hinter so that the global analysis of the font shapes actually uses the modified mapping.

The following example code demonstrates how to access it (omitting the error handling).
```
  FT_Library                library;
  FT_Face                   face;
  FT_Prop_GlyphToScriptMap  prop;


  FT_Init_FreeType( &library );
  FT_New_Face( library, "foo.ttf", 0, &face );

  prop.face = face;

  FT_Property_Get( library, "autofitter",
                            "glyph-to-script-map", &prop );

  // adjust `prop.map' as needed right here

  FT_Load_Glyph( face, ..., FT_LOAD_FORCE_AUTOHINT );
```

<h4>since</h4>

2.4.11

<hr>

## FT_AUTOHINTER_SCRIPT_XXX

Defined in FT_DRIVER_H (freetype/ftdriver.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <a href="../ft2-properties/#ft_autohinter_script_none">FT_AUTOHINTER_SCRIPT_NONE</a>   0
#<span class="keyword">define</span> <a href="../ft2-properties/#ft_autohinter_script_latin">FT_AUTOHINTER_SCRIPT_LATIN</a>  1
#<span class="keyword">define</span> <a href="../ft2-properties/#ft_autohinter_script_cjk">FT_AUTOHINTER_SCRIPT_CJK</a>    2
#<span class="keyword">define</span> <a href="../ft2-properties/#ft_autohinter_script_indic">FT_AUTOHINTER_SCRIPT_INDIC</a>  3
</pre>
</div>


**Experimental only**

A list of constants used for the <a href="../ft2-properties/#glyph-to-script-map">glyph-to-script-map</a> property to specify the script submodule the auto-hinter should use for hinting a particular glyph.

<h4>values</h4>
<table class="fields">
<tr><td class="val" id="ft_autohinter_script_none">FT_AUTOHINTER_SCRIPT_NONE</td><td class="desc">
<p>Don't auto-hint this glyph.</p>
</td></tr>
<tr><td class="val" id="ft_autohinter_script_latin">FT_AUTOHINTER_SCRIPT_LATIN</td><td class="desc">
<p>Apply the latin auto-hinter. For the auto-hinter, &lsquo;latin&rsquo; is a very broad term, including Cyrillic and Greek also since characters from those scripts share the same design constraints.</p>
<p>By default, characters from the following Unicode ranges are assigned to this submodule.</p>
```
U+0020 - U+007F  // Basic Latin (no control characters)
U+00A0 - U+00FF  // Latin-1 Supplement (no control characters)
U+0100 - U+017F  // Latin Extended-A
U+0180 - U+024F  // Latin Extended-B
U+0250 - U+02AF  // IPA Extensions
U+02B0 - U+02FF  // Spacing Modifier Letters
U+0300 - U+036F  // Combining Diacritical Marks
U+0370 - U+03FF  // Greek and Coptic
U+0400 - U+04FF  // Cyrillic
U+0500 - U+052F  // Cyrillic Supplement
U+1D00 - U+1D7F  // Phonetic Extensions
U+1D80 - U+1DBF  // Phonetic Extensions Supplement
U+1DC0 - U+1DFF  // Combining Diacritical Marks Supplement
U+1E00 - U+1EFF  // Latin Extended Additional
U+1F00 - U+1FFF  // Greek Extended
U+2000 - U+206F  // General Punctuation
U+2070 - U+209F  // Superscripts and Subscripts
U+20A0 - U+20CF  // Currency Symbols
U+2150 - U+218F  // Number Forms
U+2460 - U+24FF  // Enclosed Alphanumerics
U+2C60 - U+2C7F  // Latin Extended-C
U+2DE0 - U+2DFF  // Cyrillic Extended-A
U+2E00 - U+2E7F  // Supplemental Punctuation
U+A640 - U+A69F  // Cyrillic Extended-B
U+A720 - U+A7FF  // Latin Extended-D
U+FB00 - U+FB06  // Alphab. Present. Forms (Latin Ligatures)
U+1D400 - U+1D7FF // Mathematical Alphanumeric Symbols
U+1F100 - U+1F1FF // Enclosed Alphanumeric Supplement
```

</td></tr>
<tr><td class="val" id="ft_autohinter_script_cjk">FT_AUTOHINTER_SCRIPT_CJK</td><td class="desc">
<p>Apply the CJK auto-hinter, covering Chinese, Japanese, Korean, old Vietnamese, and some other scripts.</p>
<p>By default, characters from the following Unicode ranges are assigned to this submodule.</p>
```
U+1100 - U+11FF  // Hangul Jamo
U+2E80 - U+2EFF  // CJK Radicals Supplement
U+2F00 - U+2FDF  // Kangxi Radicals
U+2FF0 - U+2FFF  // Ideographic Description Characters
U+3000 - U+303F  // CJK Symbols and Punctuation
U+3040 - U+309F  // Hiragana
U+30A0 - U+30FF  // Katakana
U+3100 - U+312F  // Bopomofo
U+3130 - U+318F  // Hangul Compatibility Jamo
U+3190 - U+319F  // Kanbun
U+31A0 - U+31BF  // Bopomofo Extended
U+31C0 - U+31EF  // CJK Strokes
U+31F0 - U+31FF  // Katakana Phonetic Extensions
U+3200 - U+32FF  // Enclosed CJK Letters and Months
U+3300 - U+33FF  // CJK Compatibility
U+3400 - U+4DBF  // CJK Unified Ideographs Extension A
U+4DC0 - U+4DFF  // Yijing Hexagram Symbols
U+4E00 - U+9FFF  // CJK Unified Ideographs
U+A960 - U+A97F  // Hangul Jamo Extended-A
U+AC00 - U+D7AF  // Hangul Syllables
U+D7B0 - U+D7FF  // Hangul Jamo Extended-B
U+F900 - U+FAFF  // CJK Compatibility Ideographs
U+FE10 - U+FE1F  // Vertical forms
U+FE30 - U+FE4F  // CJK Compatibility Forms
U+FF00 - U+FFEF  // Halfwidth and Fullwidth Forms
U+1B000 - U+1B0FF // Kana Supplement
U+1D300 - U+1D35F // Tai Xuan Hing Symbols
U+1F200 - U+1F2FF // Enclosed Ideographic Supplement
U+20000 - U+2A6DF // CJK Unified Ideographs Extension B
U+2A700 - U+2B73F // CJK Unified Ideographs Extension C
U+2B740 - U+2B81F // CJK Unified Ideographs Extension D
U+2F800 - U+2FA1F // CJK Compatibility Ideographs Supplement
```

</td></tr>
<tr><td class="val" id="ft_autohinter_script_indic">FT_AUTOHINTER_SCRIPT_INDIC</td><td class="desc">
<p>Apply the indic auto-hinter, covering all major scripts from the Indian sub-continent and some other related scripts like Thai, Lao, or Tibetan.</p>
<p>By default, characters from the following Unicode ranges are assigned to this submodule.</p>
```
U+0900 - U+0DFF  // Indic Range
U+0F00 - U+0FFF  // Tibetan
U+1900 - U+194F  // Limbu
U+1B80 - U+1BBF  // Sundanese
U+A800 - U+A82F  // Syloti Nagri
U+ABC0 - U+ABFF  // Meetei Mayek
U+11800 - U+118DF // Sharada
```
<p>Note that currently Indic support is rudimentary only, missing blue zone support.</p>
</td></tr>
</table>

<h4>since</h4>

2.4.11

<hr>

## FT_Prop_GlyphToScriptMap

Defined in FT_DRIVER_H (freetype/ftdriver.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Prop_GlyphToScriptMap_
  {
    <a href="../ft2-base_interface/#ft_face">FT_Face</a>     face;
    <a href="../ft2-basic_types/#ft_ushort">FT_UShort</a>*  map;

  } <b>FT_Prop_GlyphToScriptMap</b>;
</pre>
</div>


**Experimental only**

The data exchange structure for the <a href="../ft2-properties/#glyph-to-script-map">glyph-to-script-map</a> property.

<h4>since</h4>

2.4.11

<hr>

## fallback-script



**Experimental only**

If no auto-hinter script module can be assigned to a glyph, a fallback script gets assigned to it (see also the <a href="../ft2-properties/#glyph-to-script-map">glyph-to-script-map</a> property). By default, this is <a href="../ft2-properties/#ft_autohinter_script_xxx">FT_AUTOHINTER_SCRIPT_CJK</a>. Using the &lsquo;fallback-script&rsquo; property, this fallback value can be changed.
```
  FT_Library  library;
  FT_UInt     fallback_script = FT_AUTOHINTER_SCRIPT_NONE;


  FT_Init_FreeType( &library );

  FT_Property_Set( library, "autofitter",
                            "fallback-script", &fallback_script );
```

<h4>note</h4>

This property can be used with <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a> also.

It's important to use the right timing for changing this value: The creation of the glyph-to-script map that eventually uses the fallback script value gets triggered either by setting or reading a face-specific property like <a href="../ft2-properties/#glyph-to-script-map">glyph-to-script-map</a>, or by auto-hinting any glyph from that face. In particular, if you have already created an <a href="../ft2-base_interface/#ft_face">FT_Face</a> structure but not loaded any glyph (using the auto-hinter), a change of the fallback script will affect this face.

<h4>since</h4>

2.4.11

<hr>

## default-script



**Experimental only**

If FreeType gets compiled with FT_CONFIG_OPTION_USE_HARFBUZZ to make the HarfBuzz library access OpenType features for getting better glyph coverages, this property sets the (auto-fitter) script to be used for the default (OpenType) script data of a font's GSUB table. Features for the default script are intended for all scripts not explicitly handled in GSUB; an example is a &lsquo;dlig&rsquo; feature, containing the combination of the characters &lsquo;T&rsquo;, &lsquo;E&rsquo;, and &lsquo;L&rsquo; to form a &lsquo;TEL&rsquo; ligature.

By default, this is <a href="../ft2-properties/#ft_autohinter_script_xxx">FT_AUTOHINTER_SCRIPT_LATIN</a>. Using the &lsquo;default-script&rsquo; property, this default value can be changed.
```
  FT_Library  library;
  FT_UInt     default_script = FT_AUTOHINTER_SCRIPT_NONE;


  FT_Init_FreeType( &library );

  FT_Property_Set( library, "autofitter",
                            "default-script", &default_script );
```

<h4>note</h4>

This property can be used with <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a> also.

It's important to use the right timing for changing this value: The creation of the glyph-to-script map that eventually uses the default script value gets triggered either by setting or reading a face-specific property like <a href="../ft2-properties/#glyph-to-script-map">glyph-to-script-map</a>, or by auto-hinting any glyph from that face. In particular, if you have already created an <a href="../ft2-base_interface/#ft_face">FT_Face</a> structure but not loaded any glyph (using the auto-hinter), a change of the default script will affect this face.

<h4>since</h4>

2.5.3

<hr>

## increase-x-height



For ppem values in the range 6&nbsp;&lt;= ppem &lt;= &lsquo;increase-x-height&rsquo;, round up the font's x&nbsp;height much more often than normally. If the value is set to&nbsp;0, which is the default, this feature is switched off. Use this property to improve the legibility of small font sizes if necessary.
```
  FT_Library               library;
  FT_Face                  face;
  FT_Prop_IncreaseXHeight  prop;


  FT_Init_FreeType( &library );
  FT_New_Face( library, "foo.ttf", 0, &face );
  FT_Set_Char_Size( face, 10 * 64, 0, 72, 0 );

  prop.face  = face;
  prop.limit = 14;

  FT_Property_Set( library, "autofitter",
                            "increase-x-height", &prop );
```

<h4>note</h4>

This property can be used with <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a> also.

Set this value right after calling <a href="../ft2-base_interface/#ft_set_char_size">FT_Set_Char_Size</a>, but before loading any glyph (using the auto-hinter).

<h4>since</h4>

2.4.11

<hr>

## FT_Prop_IncreaseXHeight

Defined in FT_DRIVER_H (freetype/ftdriver.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_Prop_IncreaseXHeight_
  {
    <a href="../ft2-base_interface/#ft_face">FT_Face</a>  face;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>  limit;

  } <b>FT_Prop_IncreaseXHeight</b>;
</pre>
</div>


The data exchange structure for the <a href="../ft2-properties/#increase-x-height">increase-x-height</a> property.

<hr>

## warping



**Experimental only**

If FreeType gets compiled with option AF_CONFIG_OPTION_USE_WARPER to activate the warp hinting code in the auto-hinter, this property switches warping on and off.

Warping only works in &lsquo;normal&rsquo; auto-hinting mode replacing it. The idea of the code is to slightly scale and shift a glyph along the non-hinted dimension (which is usually the horizontal axis) so that as much of its segments are aligned (more or less) to the grid. To find out a glyph's optimal scaling and shifting value, various parameter combinations are tried and scored.

By default, warping is off. The example below shows how to switch on warping (omitting the error handling).
```
  FT_Library  library;
  FT_Bool     warping = 1;


  FT_Init_FreeType( &library );

  FT_Property_Set( library, "autofitter",
                            "warping", &warping );
```

<h4>note</h4>

This property can be used with <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a> also.

This property can be set via the &lsquo;FREETYPE_PROPERTIES&rsquo; environment variable (using values 1 and 0 for &lsquo;on&rsquo; and &lsquo;off&rsquo;, respectively).

The warping code can also change advance widths. Have a look at the &lsquo;lsb_delta&rsquo; and &lsquo;rsb_delta&rsquo; fields in the <a href="../ft2-base_interface/#ft_glyphslotrec">FT_GlyphSlotRec</a> structure for details on improving inter-glyph distances while rendering.

Since warping is a global property of the auto-hinter it is best to change its value before rendering any face. Otherwise, you should reload all faces that get auto-hinted in &lsquo;normal&rsquo; hinting mode.

<h4>since</h4>

2.6

<hr>

