[Docs](ft2-index.md) &raquo; [Controlling FreeType Modules](ft2-toc.md#controlling-freetype-modules) &raquo; The auto-hinter

-------------------------------

# The auto-hinter

## Synopsis

While FreeType's auto-hinter doesn't expose API functions by itself, it is possible to control its behaviour with <a href="../ft2-module_management/#ft_property_set">FT_Property_Set</a> and <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a>. The following lists the available properties together with the necessary macros and structures.

Note that the auto-hinter's module name is &lsquo;autofitter&rsquo; for historical reasons.

Available properties are <a href="../ft2-properties/#increase-x-height">increase-x-height</a>, <a href="../ft2-properties/#no-stem-darkening">no-stem-darkening</a> (experimental), <a href="../ft2-properties/#darkening-parameters">darkening-parameters</a> (experimental), <a href="../ft2-properties/#warping">warping</a> (experimental), <a href="../ft2-properties/#glyph-to-script-map">glyph-to-script-map</a> (experimental), <a href="../ft2-properties/#fallback-script">fallback-script</a> (experimental), and <a href="../ft2-properties/#default-script">default-script</a> (experimental), as documented in the &lsquo;<a href="../ft2-properties/#properties">Driver properties</a>&rsquo; section.

