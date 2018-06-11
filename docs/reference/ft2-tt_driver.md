[Docs](ft2-index.md) &raquo; [Controlling FreeType Modules](ft2-toc.md#controlling-freetype-modules) &raquo; The TrueType driver

-------------------------------

# The TrueType driver

## Synopsis

While FreeType's TrueType driver doesn't expose API functions by itself, it is possible to control its behaviour with <a href="../ft2-module_management/#ft_property_set">FT_Property_Set</a> and <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a>. The following lists the available properties together with the necessary macros and structures.

The TrueType driver's module name is &lsquo;truetype&rsquo;.

A single property <a href="../ft2-properties/#interpreter-version">interpreter-version</a> is available, as documented in the &lsquo;<a href="../ft2-properties/#properties">Driver properties</a>&rsquo; section.

We start with a list of definitions, kindly provided by Greg Hitchcock.

_Bi-Level Rendering_

Monochromatic rendering, exclusively used in the early days of TrueType by both Apple and Microsoft. Microsoft's GDI interface supported hinting of the right-side bearing point, such that the advance width could be non-linear. Most often this was done to achieve some level of glyph symmetry. To enable reasonable performance (e.g., not having to run hinting on all glyphs just to get the widths) there was a bit in the head table indicating if the side bearing was hinted, and additional tables, &lsquo;hdmx&rsquo; and &lsquo;LTSH&rsquo;, to cache hinting widths across multiple sizes and device aspect ratios.

_Font Smoothing_

Microsoft's GDI implementation of anti-aliasing. Not traditional anti-aliasing as the outlines were hinted before the sampling. The widths matched the bi-level rendering.

_ClearType Rendering_

Technique that uses physical subpixels to improve rendering on LCD (and other) displays. Because of the higher resolution, many methods of improving symmetry in glyphs through hinting the right-side bearing were no longer necessary. This lead to what GDI calls &lsquo;natural widths&rsquo; ClearType, see <http://www.beatstamm.com/typography/RTRCh4.htm#Sec21>. Since hinting has extra resolution, most non-linearity went away, but it is still possible for hints to change the advance widths in this mode.

_ClearType Compatible Widths_

One of the earliest challenges with ClearType was allowing the implementation in GDI to be selected without requiring all UI and documents to reflow. To address this, a compatible method of rendering ClearType was added where the font hints are executed once to determine the width in bi-level rendering, and then re-run in ClearType, with the difference in widths being absorbed in the font hints for ClearType (mostly in the white space of hints); see <http://www.beatstamm.com/typography/RTRCh4.htm#Sec20>. Somewhat by definition, compatible width ClearType allows for non-linear widths, but only when the bi-level version has non-linear widths.

_ClearType Subpixel Positioning_

One of the nice benefits of ClearType is the ability to more crisply display fractional widths; unfortunately, the GDI model of integer bitmaps did not support this. However, the WPF and Direct Write frameworks do support fractional widths. DWrite calls this &lsquo;natural mode&rsquo;, not to be confused with GDI's &lsquo;natural widths&rsquo;. Subpixel positioning, in the current implementation of Direct Write, unfortunately does not support hinted advance widths, see <http://www.beatstamm.com/typography/RTRCh4.htm#Sec22>. Note that the TrueType interpreter fully allows the advance width to be adjusted in this mode, just the DWrite client will ignore those changes.

_ClearType Backward Compatibility_

This is a set of exceptions made in the TrueType interpreter to minimize hinting techniques that were problematic with the extra resolution of ClearType; see <http://www.beatstamm.com/typography/RTRCh4.htm#Sec1> and <https://www.microsoft.com/typography/cleartype/truetypecleartype.aspx>. This technique is not to be confused with ClearType compatible widths. ClearType backward compatibility has no direct impact on changing advance widths, but there might be an indirect impact on disabling some deltas. This could be worked around in backward compatibility mode.

_Native ClearType Mode_

(Not to be confused with &lsquo;natural widths&rsquo;.) This mode removes all the exceptions in the TrueType interpreter when running with ClearType. Any issues on widths would still apply, though.

