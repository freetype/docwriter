[Docs](ft2-index.md) &raquo; [Controlling FreeType Modules](ft2-toc.md#controlling-freetype-modules) &raquo; The PCF driver

-------------------------------

# The PCF driver

## Synopsis

While FreeType's PCF driver doesn't expose API functions by itself, it is possible to control its behaviour with <a href="../ft2-module_management/#ft_property_set">FT_Property_Set</a> and <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a>. Right now, there is a single property <a href="../ft2-properties/#no-long-family-names">no-long-family-names</a> available if FreeType is compiled with PCF_CONFIG_OPTION_LONG_FAMILY_NAMES.

The PCF driver's module name is &lsquo;pcf&rsquo;.

