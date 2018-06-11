[Docs](ft2-index.md) &raquo; [Core API](ft2-toc.md#core-api) &raquo; Mac Specific Interface

-------------------------------

# Mac Specific Interface

## Synopsis

The following definitions are only available if FreeType is compiled on a Macintosh.

## FT_New_Face_From_FOND

Defined in FT_MAC_H (freetype/ftmac.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_New_Face_From_FOND</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>  library,
                         Handle      fond,
                         <a href="../ft2-basic_types/#ft_long">FT_Long</a>     face_index,
                         <a href="../ft2-base_interface/#ft_face">FT_Face</a>    *aface )
                       FT_DEPRECATED_ATTRIBUTE;
</pre>
</div>


Create a new face object from a FOND resource.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the library resource.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="fond">fond</td><td class="desc">
<p>A FOND resource.</p>
</td></tr>
<tr><td class="val" id="face_index">face_index</td><td class="desc">
<p>Only supported for the -1 &lsquo;sanity check&rsquo; special case.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aface">aface</td><td class="desc">
<p>A handle to a new face object.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>notes</h4>

This function can be used to create <a href="../ft2-base_interface/#ft_face">FT_Face</a> objects from fonts that are installed in the system as follows.
```
  fond = GetResource( 'FOND', fontName );
  error = FT_New_Face_From_FOND( library, fond, 0, &face );
```

<hr>

## FT_GetFile_From_Mac_Name

Defined in FT_MAC_H (freetype/ftmac.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_GetFile_From_Mac_Name</b>( <span class="keyword">const</span> <span class="keyword">char</span>*  fontName,
                            FSSpec*      pathSpec,
                            <a href="../ft2-basic_types/#ft_long">FT_Long</a>*     face_index )
                          FT_DEPRECATED_ATTRIBUTE;
</pre>
</div>


Return an FSSpec for the disk file containing the named font.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="fontname">fontName</td><td class="desc">
<p>Mac OS name of the font (e.g., Times New Roman Bold).</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="pathspec">pathSpec</td><td class="desc">
<p>FSSpec to the file. For passing to <a href="../ft2-mac_specific/#ft_new_face_from_fsspec">FT_New_Face_From_FSSpec</a>.</p>
</td></tr>
<tr><td class="val" id="face_index">face_index</td><td class="desc">
<p>Index of the face. For passing to <a href="../ft2-mac_specific/#ft_new_face_from_fsspec">FT_New_Face_From_FSSpec</a>.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FT_GetFile_From_Mac_ATS_Name

Defined in FT_MAC_H (freetype/ftmac.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_GetFile_From_Mac_ATS_Name</b>( <span class="keyword">const</span> <span class="keyword">char</span>*  fontName,
                                FSSpec*      pathSpec,
                                <a href="../ft2-basic_types/#ft_long">FT_Long</a>*     face_index )
                              FT_DEPRECATED_ATTRIBUTE;
</pre>
</div>


Return an FSSpec for the disk file containing the named font.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="fontname">fontName</td><td class="desc">
<p>Mac OS name of the font in ATS framework.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="pathspec">pathSpec</td><td class="desc">
<p>FSSpec to the file. For passing to <a href="../ft2-mac_specific/#ft_new_face_from_fsspec">FT_New_Face_From_FSSpec</a>.</p>
</td></tr>
<tr><td class="val" id="face_index">face_index</td><td class="desc">
<p>Index of the face. For passing to <a href="../ft2-mac_specific/#ft_new_face_from_fsspec">FT_New_Face_From_FSSpec</a>.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FT_GetFilePath_From_Mac_ATS_Name

Defined in FT_MAC_H (freetype/ftmac.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_GetFilePath_From_Mac_ATS_Name</b>( <span class="keyword">const</span> <span class="keyword">char</span>*  fontName,
                                    UInt8*       path,
                                    UInt32       maxPathSize,
                                    <a href="../ft2-basic_types/#ft_long">FT_Long</a>*     face_index )
                                  FT_DEPRECATED_ATTRIBUTE;
</pre>
</div>


Return a pathname of the disk file and face index for given font name that is handled by ATS framework.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="fontname">fontName</td><td class="desc">
<p>Mac OS name of the font in ATS framework.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="path">path</td><td class="desc">
<p>Buffer to store pathname of the file. For passing to <a href="../ft2-base_interface/#ft_new_face">FT_New_Face</a>. The client must allocate this buffer before calling this function.</p>
</td></tr>
<tr><td class="val" id="maxpathsize">maxPathSize</td><td class="desc">
<p>Lengths of the buffer &lsquo;path&rsquo; that client allocated.</p>
</td></tr>
<tr><td class="val" id="face_index">face_index</td><td class="desc">
<p>Index of the face. For passing to <a href="../ft2-base_interface/#ft_new_face">FT_New_Face</a>.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FT_New_Face_From_FSSpec

Defined in FT_MAC_H (freetype/ftmac.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_New_Face_From_FSSpec</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>     library,
                           <span class="keyword">const</span> FSSpec  *spec,
                           <a href="../ft2-basic_types/#ft_long">FT_Long</a>        face_index,
                           <a href="../ft2-base_interface/#ft_face">FT_Face</a>       *aface )
                         FT_DEPRECATED_ATTRIBUTE;
</pre>
</div>


Create a new face object from a given resource and typeface index using an FSSpec to the font file.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the library resource.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="spec">spec</td><td class="desc">
<p>FSSpec to the font file.</p>
</td></tr>
<tr><td class="val" id="face_index">face_index</td><td class="desc">
<p>The index of the face within the resource. The first face has index&nbsp;0.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aface">aface</td><td class="desc">
<p>A handle to a new face object.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

<a href="../ft2-mac_specific/#ft_new_face_from_fsspec">FT_New_Face_From_FSSpec</a> is identical to <a href="../ft2-base_interface/#ft_new_face">FT_New_Face</a> except it accepts an FSSpec instead of a path.

<hr>

## FT_New_Face_From_FSRef

Defined in FT_MAC_H (freetype/ftmac.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_New_Face_From_FSRef</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>    library,
                          <span class="keyword">const</span> FSRef  *ref,
                          <a href="../ft2-basic_types/#ft_long">FT_Long</a>       face_index,
                          <a href="../ft2-base_interface/#ft_face">FT_Face</a>      *aface )
                        FT_DEPRECATED_ATTRIBUTE;
</pre>
</div>


Create a new face object from a given resource and typeface index using an FSRef to the font file.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to the library resource.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="spec">spec</td><td class="desc">
<p>FSRef to the font file.</p>
</td></tr>
<tr><td class="val" id="face_index">face_index</td><td class="desc">
<p>The index of the face within the resource. The first face has index&nbsp;0.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aface">aface</td><td class="desc">
<p>A handle to a new face object.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

<a href="../ft2-mac_specific/#ft_new_face_from_fsref">FT_New_Face_From_FSRef</a> is identical to <a href="../ft2-base_interface/#ft_new_face">FT_New_Face</a> except it accepts an FSRef instead of a path.

<hr>

