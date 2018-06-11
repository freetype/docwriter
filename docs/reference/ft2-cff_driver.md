[Docs](ft2-index.md) &raquo; [Controlling FreeType Modules](ft2-toc.md#controlling-freetype-modules) &raquo; The CFF driver

-------------------------------

# The CFF driver

## Synopsis

While FreeType's CFF driver doesn't expose API functions by itself, it is possible to control its behaviour with <a href="../ft2-module_management/#ft_property_set">FT_Property_Set</a> and <a href="../ft2-module_management/#ft_property_get">FT_Property_Get</a>.

The CFF driver's module name is &lsquo;cff&rsquo;.

Available properties are <a href="../ft2-properties/#hinting-engine">hinting-engine</a>, <a href="../ft2-properties/#no-stem-darkening">no-stem-darkening</a>, <a href="../ft2-properties/#darkening-parameters">darkening-parameters</a>, and <a href="../ft2-properties/#random-seed">random-seed</a>, as documented in the &lsquo;<a href="../ft2-properties/#properties">Driver properties</a>&rsquo; section.

**Hinting and antialiasing principles of the new engine**

The rasterizer is positioning horizontal features (e.g., ascender height &amp; x-height, or crossbars) on the pixel grid and minimizing the amount of antialiasing applied to them, while placing vertical features (vertical stems) on the pixel grid without hinting, thus representing the stem position and weight accurately. Sometimes the vertical stems may be only partially black. In this context, &lsquo;antialiasing&rsquo; means that stems are not positioned exactly on pixel borders, causing a fuzzy appearance.

There are two principles behind this approach.

1) No hinting in the horizontal direction: Unlike &lsquo;superhinted&rsquo; TrueType, which changes glyph widths to accommodate regular inter-glyph spacing, Adobe's approach is &lsquo;faithful to the design&rsquo; in representing both the glyph width and the inter-glyph spacing designed for the font. This makes the screen display as close as it can be to the result one would get with infinite resolution, while preserving what is considered the key characteristics of each glyph. Note that the distances between unhinted and grid-fitted positions at small sizes are comparable to kerning values and thus would be noticeable (and distracting) while reading if hinting were applied.

One of the reasons to not hint horizontally is antialiasing for LCD screens: The pixel geometry of modern displays supplies three vertical subpixels as the eye moves horizontally across each visible pixel. On devices where we can be certain this characteristic is present a rasterizer can take advantage of the subpixels to add increments of weight. In Western writing systems this turns out to be the more critical direction anyway; the weights and spacing of vertical stems (see above) are central to Armenian, Cyrillic, Greek, and Latin type designs. Even when the rasterizer uses greyscale antialiasing instead of color (a necessary compromise when one doesn't know the screen characteristics), the unhinted vertical features preserve the design's weight and spacing much better than aliased type would.

2) Alignment in the vertical direction: Weights and spacing along the y&nbsp;axis are less critical; what is much more important is the visual alignment of related features (like cap-height and x-height). The sense of alignment for these is enhanced by the sharpness of grid-fit edges, while the cruder vertical resolution (full pixels instead of 1/3 pixels) is less of a problem.

On the technical side, horizontal alignment zones for ascender, x-height, and other important height values (traditionally called &lsquo;blue zones&rsquo;) as defined in the font are positioned independently, each being rounded to the nearest pixel edge, taking care of overshoot suppression at small sizes, stem darkening, and scaling.

Hstems (this is, hint values defined in the font to help align horizontal features) that fall within a blue zone are said to be &lsquo;captured&rsquo; and are aligned to that zone. Uncaptured stems are moved in one of four ways, top edge up or down, bottom edge up or down. Unless there are conflicting hstems, the smallest movement is taken to minimize distortion.

