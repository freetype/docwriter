[Docs](ft2-index.md) &raquo; [Format-Specific API](ft2-toc.md#format-specific-api) &raquo; Font Formats

-------------------------------

# Font Formats

## Synopsis

The single function in this section can be used to get the font format. Note that this information is not needed normally; however, there are special cases (like in PDF devices) where it is important to differentiate, in spite of FreeType's uniform API.

## FT_Get_Font_Format

Defined in FT_FONT_FORMATS_H (freetype/ftfntfmt.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">const</span> <span class="keyword">char</span>* )
  <b>FT_Get_Font_Format</b>( <a href="../ft2-base_interface/#ft_face">FT_Face</a>  face );


  /* deprecated */
  FT_EXPORT( <span class="keyword">const</span> <span class="keyword">char</span>* )
  FT_Get_X11_Font_Format( <a href="../ft2-base_interface/#ft_face">FT_Face</a>  face );
</pre>
</div>


Return a string describing the format of a given face. Possible values are &lsquo;TrueType&rsquo;, &lsquo;Type&nbsp;1&rsquo;, &lsquo;BDF&rsquo;, &lsquo;PCF&rsquo;, &lsquo;Type&nbsp;42&rsquo;, &lsquo;CID&nbsp;Type&nbsp;1&rsquo;, &lsquo;CFF&rsquo;, &lsquo;PFR&rsquo;, and &lsquo;Windows&nbsp;FNT&rsquo;.

The return value is suitable to be used as an X11 FONT_PROPERTY.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face">face</td><td class="desc">
<p>Input face handle.</p>
</td></tr>
</table>

<h4>return</h4>

Font format string. NULL in case of error.

<h4>note</h4>

A deprecated name for the same function is &lsquo;FT_Get_X11_Font_Format&rsquo;.

<hr>

