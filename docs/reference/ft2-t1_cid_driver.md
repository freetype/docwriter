[Docs](ft2-index.md) &raquo; [Controlling FreeType Modules](ft2-toc.md#controlling-freetype-modules) &raquo; The Type 1 and CID drivers

-------------------------------

# The Type 1 and CID drivers

## Synopsis

It is possible to control the behaviour of FreeType's Type&nbsp;1 and Type&nbsp;1 CID drivers with <a href="../ft2-module_management/#ft_property_set">FT_Property_Set</a> and <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a>.

Behind the scenes, both drivers use the Adobe CFF engine for hinting; however, the used properties must be specified separately.

The Type&nbsp;1 driver's module name is &lsquo;type1&rsquo;; the CID driver's module name is &lsquo;t1cid&rsquo;.

Available properties are <a href="../ft2-properties/#hinting-engine">hinting-engine</a>, <a href="../ft2-properties/#no-stem-darkening">no-stem-darkening</a>, <a href="../ft2-properties/#darkening-parameters">darkening-parameters</a>, and <a href="../ft2-properties/#random-seed">random-seed</a>, as documented in the &lsquo;<a href="../ft2-properties/#properties">Driver properties</a>&rsquo; section.

Please see the &lsquo;<a href="../ft2-cff_driver/#cff_driver">The CFF driver</a>&rsquo; section for more details on the new hinting engine.

