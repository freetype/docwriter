[Docs](ft2-index.md) &raquo; [Cache Sub-System](ft2-toc.md#cache-sub-system) &raquo; Cache Sub-System

-------------------------------

# Cache Sub-System

## Synopsis

This section describes the FreeType&nbsp;2 cache sub-system, which is used to limit the number of concurrently opened <a href="../ft2-base_interface/#ft_face">FT_Face</a> and <a href="../ft2-base_interface/#ft_size">FT_Size</a> objects, as well as caching information like character maps and glyph images while limiting their maximum memory usage.

Note that all types and functions begin with the &lsquo;FTC_&rsquo; prefix.

The cache is highly portable and thus doesn't know anything about the fonts installed on your system, or how to access them. This implies the following scheme:

First, available or installed font faces are uniquely identified by <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a> values, provided to the cache by the client. Note that the cache only stores and compares these values, and doesn't try to interpret them in any way.

Second, the cache calls, only when needed, a client-provided function to convert an <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a> into a new <a href="../ft2-base_interface/#ft_face">FT_Face</a> object. The latter is then completely managed by the cache, including its termination through <a href="../ft2-base_interface/#ft_done_face">FT_Done_Face</a>. To monitor termination of face objects, the finalizer callback in the &lsquo;generic&rsquo; field of the <a href="../ft2-base_interface/#ft_face">FT_Face</a> object can be used, which might also be used to store the <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a> of the face.

Clients are free to map face IDs to anything else. The most simple usage is to associate them to a (pathname,face_index) pair that is used to call <a href="../ft2-base_interface/#ft_new_face">FT_New_Face</a>. However, more complex schemes are also possible.

Note that for the cache to work correctly, the face ID values must be **persistent**, which means that the contents they point to should not change at runtime, or that their value should not become invalid.

If this is unavoidable (e.g., when a font is uninstalled at runtime), you should call <a href="../ft2-cache_subsystem/#ftc_manager_removefaceid">FTC_Manager_RemoveFaceID</a> as soon as possible, to let the cache get rid of any references to the old <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a> it may keep internally. Failure to do so will lead to incorrect behaviour or even crashes.

To use the cache, start with calling <a href="../ft2-cache_subsystem/#ftc_manager_new">FTC_Manager_New</a> to create a new <a href="../ft2-cache_subsystem/#ftc_manager">FTC_Manager</a> object, which models a single cache instance. You can then look up <a href="../ft2-base_interface/#ft_face">FT_Face</a> and <a href="../ft2-base_interface/#ft_size">FT_Size</a> objects with <a href="../ft2-cache_subsystem/#ftc_manager_lookupface">FTC_Manager_LookupFace</a> and <a href="../ft2-cache_subsystem/#ftc_manager_lookupsize">FTC_Manager_LookupSize</a>, respectively.

If you want to use the charmap caching, call <a href="../ft2-cache_subsystem/#ftc_cmapcache_new">FTC_CMapCache_New</a>, then later use <a href="../ft2-cache_subsystem/#ftc_cmapcache_lookup">FTC_CMapCache_Lookup</a> to perform the equivalent of <a href="../ft2-base_interface/#ft_get_char_index">FT_Get_Char_Index</a>, only much faster.

If you want to use the <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a> caching, call <a href="../ft2-cache_subsystem/#ftc_imagecache">FTC_ImageCache</a>, then later use <a href="../ft2-cache_subsystem/#ftc_imagecache_lookup">FTC_ImageCache_Lookup</a> to retrieve the corresponding <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a> objects from the cache.

If you need lots of small bitmaps, it is much more memory efficient to call <a href="../ft2-cache_subsystem/#ftc_sbitcache_new">FTC_SBitCache_New</a> followed by <a href="../ft2-cache_subsystem/#ftc_sbitcache_lookup">FTC_SBitCache_Lookup</a>. This returns <a href="../ft2-cache_subsystem/#ftc_sbitrec">FTC_SBitRec</a> structures, which are used to store small bitmaps directly. (A small bitmap is one whose metrics and dimensions all fit into 8-bit integers).

We hope to also provide a kerning cache in the near future.

## FTC_Manager

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FTC_ManagerRec_*  <b>FTC_Manager</b>;
</pre>
</div>


This object corresponds to one instance of the cache-subsystem. It is used to cache one or more <a href="../ft2-base_interface/#ft_face">FT_Face</a> objects, along with corresponding <a href="../ft2-base_interface/#ft_size">FT_Size</a> objects.

The manager intentionally limits the total number of opened <a href="../ft2-base_interface/#ft_face">FT_Face</a> and <a href="../ft2-base_interface/#ft_size">FT_Size</a> objects to control memory usage. See the &lsquo;max_faces&rsquo; and &lsquo;max_sizes&rsquo; parameters of <a href="../ft2-cache_subsystem/#ftc_manager_new">FTC_Manager_New</a>.

The manager is also used to cache &lsquo;nodes&rsquo; of various types while limiting their total memory usage.

All limitations are enforced by keeping lists of managed objects in most-recently-used order, and flushing old nodes to make room for new ones.

<hr>

## FTC_FaceID

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-basic_types/#ft_pointer">FT_Pointer</a>  <b>FTC_FaceID</b>;
</pre>
</div>


An opaque pointer type that is used to identity face objects. The contents of such objects is application-dependent.

These pointers are typically used to point to a user-defined structure containing a font file path, and face index.

<h4>note</h4>

Never use NULL as a valid <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a>.

Face IDs are passed by the client to the cache manager that calls, when needed, the <a href="../ft2-cache_subsystem/#ftc_face_requester">FTC_Face_Requester</a> to translate them into new <a href="../ft2-base_interface/#ft_face">FT_Face</a> objects.

If the content of a given face ID changes at runtime, or if the value becomes invalid (e.g., when uninstalling a font), you should immediately call <a href="../ft2-cache_subsystem/#ftc_manager_removefaceid">FTC_Manager_RemoveFaceID</a> before any other cache function.

Failure to do so will result in incorrect behaviour or even memory leaks and crashes.

<hr>

## FTC_Face_Requester

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-basic_types/#ft_error">FT_Error</a>
  (*<b>FTC_Face_Requester</b>)( <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a>  face_id,
                         <a href="../ft2-base_interface/#ft_library">FT_Library</a>  library,
                         <a href="../ft2-basic_types/#ft_pointer">FT_Pointer</a>  req_data,
                         <a href="../ft2-base_interface/#ft_face">FT_Face</a>*    aface );
</pre>
</div>


A callback function provided by client applications. It is used by the cache manager to translate a given <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a> into a new valid <a href="../ft2-base_interface/#ft_face">FT_Face</a> object, on demand.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="face_id">face_id</td><td class="desc">
<p>The face ID to resolve.</p>
</td></tr>
<tr><td class="val" id="library">library</td><td class="desc">
<p>A handle to a FreeType library object.</p>
</td></tr>
<tr><td class="val" id="req_data">req_data</td><td class="desc">
<p>Application-provided request data (see note below).</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aface">aface</td><td class="desc">
<p>A new <a href="../ft2-base_interface/#ft_face">FT_Face</a> handle.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The third parameter &lsquo;req_data&rsquo; is the same as the one passed by the client when <a href="../ft2-cache_subsystem/#ftc_manager_new">FTC_Manager_New</a> is called.

The face requester should not perform funny things on the returned face object, like creating a new <a href="../ft2-base_interface/#ft_size">FT_Size</a> for it, or setting a transformation through <a href="../ft2-base_interface/#ft_set_transform">FT_Set_Transform</a>!

<hr>

## FTC_Manager_New

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FTC_Manager_New</b>( <a href="../ft2-base_interface/#ft_library">FT_Library</a>          library,
                   <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>             max_faces,
                   <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>             max_sizes,
                   <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>            max_bytes,
                   <a href="../ft2-cache_subsystem/#ftc_face_requester">FTC_Face_Requester</a>  requester,
                   <a href="../ft2-basic_types/#ft_pointer">FT_Pointer</a>          req_data,
                   <a href="../ft2-cache_subsystem/#ftc_manager">FTC_Manager</a>        *amanager );
</pre>
</div>


Create a new cache manager.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="library">library</td><td class="desc">
<p>The parent FreeType library handle to use.</p>
</td></tr>
<tr><td class="val" id="max_faces">max_faces</td><td class="desc">
<p>Maximum number of opened <a href="../ft2-base_interface/#ft_face">FT_Face</a> objects managed by this cache instance. Use&nbsp;0 for defaults.</p>
</td></tr>
<tr><td class="val" id="max_sizes">max_sizes</td><td class="desc">
<p>Maximum number of opened <a href="../ft2-base_interface/#ft_size">FT_Size</a> objects managed by this cache instance. Use&nbsp;0 for defaults.</p>
</td></tr>
<tr><td class="val" id="max_bytes">max_bytes</td><td class="desc">
<p>Maximum number of bytes to use for cached data nodes. Use&nbsp;0 for defaults. Note that this value does not account for managed <a href="../ft2-base_interface/#ft_face">FT_Face</a> and <a href="../ft2-base_interface/#ft_size">FT_Size</a> objects.</p>
</td></tr>
<tr><td class="val" id="requester">requester</td><td class="desc">
<p>An application-provided callback used to translate face IDs into real <a href="../ft2-base_interface/#ft_face">FT_Face</a> objects.</p>
</td></tr>
<tr><td class="val" id="req_data">req_data</td><td class="desc">
<p>A generic pointer that is passed to the requester each time it is called (see <a href="../ft2-cache_subsystem/#ftc_face_requester">FTC_Face_Requester</a>).</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="amanager">amanager</td><td class="desc">
<p>A handle to a new manager object. 0&nbsp;in case of failure.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FTC_Manager_Reset

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FTC_Manager_Reset</b>( <a href="../ft2-cache_subsystem/#ftc_manager">FTC_Manager</a>  manager );
</pre>
</div>


Empty a given cache manager. This simply gets rid of all the currently cached <a href="../ft2-base_interface/#ft_face">FT_Face</a> and <a href="../ft2-base_interface/#ft_size">FT_Size</a> objects within the manager.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="manager">manager</td><td class="desc">
<p>A handle to the manager.</p>
</td></tr>
</table>

<hr>

## FTC_Manager_Done

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FTC_Manager_Done</b>( <a href="../ft2-cache_subsystem/#ftc_manager">FTC_Manager</a>  manager );
</pre>
</div>


Destroy a given manager after emptying it.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="manager">manager</td><td class="desc">
<p>A handle to the target cache manager object.</p>
</td></tr>
</table>

<hr>

## FTC_Manager_LookupFace

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FTC_Manager_LookupFace</b>( <a href="../ft2-cache_subsystem/#ftc_manager">FTC_Manager</a>  manager,
                          <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a>   face_id,
                          <a href="../ft2-base_interface/#ft_face">FT_Face</a>     *aface );
</pre>
</div>


Retrieve the <a href="../ft2-base_interface/#ft_face">FT_Face</a> object that corresponds to a given face ID through a cache manager.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="manager">manager</td><td class="desc">
<p>A handle to the cache manager.</p>
</td></tr>
<tr><td class="val" id="face_id">face_id</td><td class="desc">
<p>The ID of the face object.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aface">aface</td><td class="desc">
<p>A handle to the face object.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The returned <a href="../ft2-base_interface/#ft_face">FT_Face</a> object is always owned by the manager. You should never try to discard it yourself.

The <a href="../ft2-base_interface/#ft_face">FT_Face</a> object doesn't necessarily have a current size object (i.e., face-&gt;size can be&nbsp;0). If you need a specific &lsquo;font size&rsquo;, use <a href="../ft2-cache_subsystem/#ftc_manager_lookupsize">FTC_Manager_LookupSize</a> instead.

Never change the face's transformation matrix (i.e., never call the <a href="../ft2-base_interface/#ft_set_transform">FT_Set_Transform</a> function) on a returned face! If you need to transform glyphs, do it yourself after glyph loading.

When you perform a lookup, out-of-memory errors are detected _within_ the lookup and force incremental flushes of the cache until enough memory is released for the lookup to succeed.

If a lookup fails with &lsquo;FT_Err_Out_Of_Memory&rsquo; the cache has already been completely flushed, and still no memory was available for the operation.

<hr>

## FTC_Manager_LookupSize

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FTC_Manager_LookupSize</b>( <a href="../ft2-cache_subsystem/#ftc_manager">FTC_Manager</a>  manager,
                          <a href="../ft2-cache_subsystem/#ftc_scaler">FTC_Scaler</a>   scaler,
                          <a href="../ft2-base_interface/#ft_size">FT_Size</a>     *asize );
</pre>
</div>


Retrieve the <a href="../ft2-base_interface/#ft_size">FT_Size</a> object that corresponds to a given <a href="../ft2-cache_subsystem/#ftc_scalerrec">FTC_ScalerRec</a> pointer through a cache manager.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="manager">manager</td><td class="desc">
<p>A handle to the cache manager.</p>
</td></tr>
<tr><td class="val" id="scaler">scaler</td><td class="desc">
<p>A scaler handle.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="asize">asize</td><td class="desc">
<p>A handle to the size object.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The returned <a href="../ft2-base_interface/#ft_size">FT_Size</a> object is always owned by the manager. You should never try to discard it by yourself.

You can access the parent <a href="../ft2-base_interface/#ft_face">FT_Face</a> object simply as &lsquo;size-&gt;face&rsquo; if you need it. Note that this object is also owned by the manager.

<h4>note</h4>

When you perform a lookup, out-of-memory errors are detected _within_ the lookup and force incremental flushes of the cache until enough memory is released for the lookup to succeed.

If a lookup fails with &lsquo;FT_Err_Out_Of_Memory&rsquo; the cache has already been completely flushed, and still no memory is available for the operation.

<hr>

## FTC_Manager_RemoveFaceID

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FTC_Manager_RemoveFaceID</b>( <a href="../ft2-cache_subsystem/#ftc_manager">FTC_Manager</a>  manager,
                            <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a>   face_id );
</pre>
</div>


A special function used to indicate to the cache manager that a given <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a> is no longer valid, either because its content changed, or because it was deallocated or uninstalled.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="manager">manager</td><td class="desc">
<p>The cache manager handle.</p>
</td></tr>
<tr><td class="val" id="face_id">face_id</td><td class="desc">
<p>The <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a> to be removed.</p>
</td></tr>
</table>

<h4>note</h4>

This function flushes all nodes from the cache corresponding to this &lsquo;face_id&rsquo;, with the exception of nodes with a non-null reference count.

Such nodes are however modified internally so as to never appear in later lookups with the same &lsquo;face_id&rsquo; value, and to be immediately destroyed when released by all their users.

<hr>

## FTC_Node

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FTC_NodeRec_*  <b>FTC_Node</b>;
</pre>
</div>


An opaque handle to a cache node object. Each cache node is reference-counted. A node with a count of&nbsp;0 might be flushed out of a full cache whenever a lookup request is performed.

If you look up nodes, you have the ability to &lsquo;acquire&rsquo; them, i.e., to increment their reference count. This will prevent the node from being flushed out of the cache until you explicitly &lsquo;release&rsquo; it (see <a href="../ft2-cache_subsystem/#ftc_node_unref">FTC_Node_Unref</a>).

See also <a href="../ft2-cache_subsystem/#ftc_sbitcache_lookup">FTC_SBitCache_Lookup</a> and <a href="../ft2-cache_subsystem/#ftc_imagecache_lookup">FTC_ImageCache_Lookup</a>.

<hr>

## FTC_Node_Unref

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FTC_Node_Unref</b>( <a href="../ft2-cache_subsystem/#ftc_node">FTC_Node</a>     node,
                  <a href="../ft2-cache_subsystem/#ftc_manager">FTC_Manager</a>  manager );
</pre>
</div>


Decrement a cache node's internal reference count. When the count reaches 0, it is not destroyed but becomes eligible for subsequent cache flushes.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="node">node</td><td class="desc">
<p>The cache node handle.</p>
</td></tr>
<tr><td class="val" id="manager">manager</td><td class="desc">
<p>The cache manager handle.</p>
</td></tr>
</table>

<hr>

## FTC_ImageCache

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FTC_ImageCacheRec_*  <b>FTC_ImageCache</b>;
</pre>
</div>


A handle to a glyph image cache object. They are designed to hold many distinct glyph images while not exceeding a certain memory threshold.

<hr>

## FTC_ImageCache_New

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FTC_ImageCache_New</b>( <a href="../ft2-cache_subsystem/#ftc_manager">FTC_Manager</a>      manager,
                      <a href="../ft2-cache_subsystem/#ftc_imagecache">FTC_ImageCache</a>  *acache );
</pre>
</div>


Create a new glyph image cache.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="manager">manager</td><td class="desc">
<p>The parent manager for the image cache.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="acache">acache</td><td class="desc">
<p>A handle to the new glyph image cache object.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FTC_ImageCache_Lookup

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FTC_ImageCache_Lookup</b>( <a href="../ft2-cache_subsystem/#ftc_imagecache">FTC_ImageCache</a>  cache,
                         <a href="../ft2-cache_subsystem/#ftc_imagetype">FTC_ImageType</a>   type,
                         <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>         gindex,
                         <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a>       *aglyph,
                         <a href="../ft2-cache_subsystem/#ftc_node">FTC_Node</a>       *anode );
</pre>
</div>


Retrieve a given glyph image from a glyph image cache.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="cache">cache</td><td class="desc">
<p>A handle to the source glyph image cache.</p>
</td></tr>
<tr><td class="val" id="type">type</td><td class="desc">
<p>A pointer to a glyph image type descriptor.</p>
</td></tr>
<tr><td class="val" id="gindex">gindex</td><td class="desc">
<p>The glyph index to retrieve.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aglyph">aglyph</td><td class="desc">
<p>The corresponding <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a> object. 0&nbsp;in case of failure.</p>
</td></tr>
<tr><td class="val" id="anode">anode</td><td class="desc">
<p>Used to return the address of the corresponding cache node after incrementing its reference count (see note below).</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The returned glyph is owned and managed by the glyph image cache. Never try to transform or discard it manually! You can however create a copy with <a href="../ft2-glyph_management/#ft_glyph_copy">FT_Glyph_Copy</a> and modify the new one.

If &lsquo;anode&rsquo; is _not_ NULL, it receives the address of the cache node containing the glyph image, after increasing its reference count. This ensures that the node (as well as the <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a>) will always be kept in the cache until you call <a href="../ft2-cache_subsystem/#ftc_node_unref">FTC_Node_Unref</a> to &lsquo;release&rsquo; it.

If &lsquo;anode&rsquo; is NULL, the cache node is left unchanged, which means that the <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a> could be flushed out of the cache on the next call to one of the caching sub-system APIs. Don't assume that it is persistent!

<hr>

## FTC_SBit

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FTC_SBitRec_*  <b>FTC_SBit</b>;
</pre>
</div>


A handle to a small bitmap descriptor. See the <a href="../ft2-cache_subsystem/#ftc_sbitrec">FTC_SBitRec</a> structure for details.

<hr>

## FTC_SBitCache

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FTC_SBitCacheRec_*  <b>FTC_SBitCache</b>;
</pre>
</div>


A handle to a small bitmap cache. These are special cache objects used to store small glyph bitmaps (and anti-aliased pixmaps) in a much more efficient way than the traditional glyph image cache implemented by <a href="../ft2-cache_subsystem/#ftc_imagecache">FTC_ImageCache</a>.

<hr>

## FTC_SBitCache_New

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FTC_SBitCache_New</b>( <a href="../ft2-cache_subsystem/#ftc_manager">FTC_Manager</a>     manager,
                     <a href="../ft2-cache_subsystem/#ftc_sbitcache">FTC_SBitCache</a>  *acache );
</pre>
</div>


Create a new cache to store small glyph bitmaps.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="manager">manager</td><td class="desc">
<p>A handle to the source cache manager.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="acache">acache</td><td class="desc">
<p>A handle to the new sbit cache. NULL in case of error.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FTC_SBitCache_Lookup

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FTC_SBitCache_Lookup</b>( <a href="../ft2-cache_subsystem/#ftc_sbitcache">FTC_SBitCache</a>    cache,
                        <a href="../ft2-cache_subsystem/#ftc_imagetype">FTC_ImageType</a>    type,
                        <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>          gindex,
                        <a href="../ft2-cache_subsystem/#ftc_sbit">FTC_SBit</a>        *sbit,
                        <a href="../ft2-cache_subsystem/#ftc_node">FTC_Node</a>        *anode );
</pre>
</div>


Look up a given small glyph bitmap in a given sbit cache and &lsquo;lock&rsquo; it to prevent its flushing from the cache until needed.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="cache">cache</td><td class="desc">
<p>A handle to the source sbit cache.</p>
</td></tr>
<tr><td class="val" id="type">type</td><td class="desc">
<p>A pointer to the glyph image type descriptor.</p>
</td></tr>
<tr><td class="val" id="gindex">gindex</td><td class="desc">
<p>The glyph index.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="sbit">sbit</td><td class="desc">
<p>A handle to a small bitmap descriptor.</p>
</td></tr>
<tr><td class="val" id="anode">anode</td><td class="desc">
<p>Used to return the address of the corresponding cache node after incrementing its reference count (see note below).</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The small bitmap descriptor and its bit buffer are owned by the cache and should never be freed by the application. They might as well disappear from memory on the next cache lookup, so don't treat them as persistent data.

The descriptor's &lsquo;buffer&rsquo; field is set to&nbsp;0 to indicate a missing glyph bitmap.

If &lsquo;anode&rsquo; is _not_ NULL, it receives the address of the cache node containing the bitmap, after increasing its reference count. This ensures that the node (as well as the image) will always be kept in the cache until you call <a href="../ft2-cache_subsystem/#ftc_node_unref">FTC_Node_Unref</a> to &lsquo;release&rsquo; it.

If &lsquo;anode&rsquo; is NULL, the cache node is left unchanged, which means that the bitmap could be flushed out of the cache on the next call to one of the caching sub-system APIs. Don't assume that it is persistent!

<hr>

## FTC_CMapCache

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FTC_CMapCacheRec_*  <b>FTC_CMapCache</b>;
</pre>
</div>


An opaque handle used to model a charmap cache. This cache is to hold character codes -&gt; glyph indices mappings.

<hr>

## FTC_CMapCache_New

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FTC_CMapCache_New</b>( <a href="../ft2-cache_subsystem/#ftc_manager">FTC_Manager</a>     manager,
                     <a href="../ft2-cache_subsystem/#ftc_cmapcache">FTC_CMapCache</a>  *acache );
</pre>
</div>


Create a new charmap cache.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="manager">manager</td><td class="desc">
<p>A handle to the cache manager.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="acache">acache</td><td class="desc">
<p>A new cache handle. NULL in case of error.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

Like all other caches, this one will be destroyed with the cache manager.

<hr>

## FTC_CMapCache_Lookup

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_uint">FT_UInt</a> )
  <b>FTC_CMapCache_Lookup</b>( <a href="../ft2-cache_subsystem/#ftc_cmapcache">FTC_CMapCache</a>  cache,
                        <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a>     face_id,
                        <a href="../ft2-basic_types/#ft_int">FT_Int</a>         cmap_index,
                        <a href="../ft2-basic_types/#ft_uint32">FT_UInt32</a>      char_code );
</pre>
</div>


Translate a character code into a glyph index, using the charmap cache.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="cache">cache</td><td class="desc">
<p>A charmap cache handle.</p>
</td></tr>
<tr><td class="val" id="face_id">face_id</td><td class="desc">
<p>The source face ID.</p>
</td></tr>
<tr><td class="val" id="cmap_index">cmap_index</td><td class="desc">
<p>The index of the charmap in the source face. Any negative value means to use the cache <a href="../ft2-base_interface/#ft_face">FT_Face</a>'s default charmap.</p>
</td></tr>
<tr><td class="val" id="char_code">char_code</td><td class="desc">
<p>The character code (in the corresponding charmap).</p>
</td></tr>
</table>

<h4>return</h4>

Glyph index. 0&nbsp;means &lsquo;no glyph&rsquo;.

<hr>

## FTC_ScalerRec

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FTC_ScalerRec_
  {
    <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a>  face_id;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     width;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     height;
    <a href="../ft2-basic_types/#ft_int">FT_Int</a>      pixel;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     x_res;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     y_res;

  } <b>FTC_ScalerRec</b>;
</pre>
</div>


A structure used to describe a given character size in either pixels or points to the cache manager. See <a href="../ft2-cache_subsystem/#ftc_manager_lookupsize">FTC_Manager_LookupSize</a>.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="face_id">face_id</td><td class="desc">
<p>The source face ID.</p>
</td></tr>
<tr><td class="val" id="width">width</td><td class="desc">
<p>The character width.</p>
</td></tr>
<tr><td class="val" id="height">height</td><td class="desc">
<p>The character height.</p>
</td></tr>
<tr><td class="val" id="pixel">pixel</td><td class="desc">
<p>A Boolean. If 1, the &lsquo;width&rsquo; and &lsquo;height&rsquo; fields are interpreted as integer pixel character sizes. Otherwise, they are expressed as 1/64th of points.</p>
</td></tr>
<tr><td class="val" id="x_res">x_res</td><td class="desc">
<p>Only used when &lsquo;pixel&rsquo; is value&nbsp;0 to indicate the horizontal resolution in dpi.</p>
</td></tr>
<tr><td class="val" id="y_res">y_res</td><td class="desc">
<p>Only used when &lsquo;pixel&rsquo; is value&nbsp;0 to indicate the vertical resolution in dpi.</p>
</td></tr>
</table>

<h4>note</h4>

This type is mainly used to retrieve <a href="../ft2-base_interface/#ft_size">FT_Size</a> objects through the cache manager.

<hr>

## FTC_Scaler

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FTC_ScalerRec_*  <b>FTC_Scaler</b>;
</pre>
</div>


A handle to an <a href="../ft2-cache_subsystem/#ftc_scalerrec">FTC_ScalerRec</a> structure.

<hr>

## FTC_ImageTypeRec

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FTC_ImageTypeRec_
  {
    <a href="../ft2-cache_subsystem/#ftc_faceid">FTC_FaceID</a>  face_id;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     width;
    <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>     height;
    <a href="../ft2-basic_types/#ft_int32">FT_Int32</a>    flags;

  } <b>FTC_ImageTypeRec</b>;
</pre>
</div>


A structure used to model the type of images in a glyph cache.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="face_id">face_id</td><td class="desc">
<p>The face ID.</p>
</td></tr>
<tr><td class="val" id="width">width</td><td class="desc">
<p>The width in pixels.</p>
</td></tr>
<tr><td class="val" id="height">height</td><td class="desc">
<p>The height in pixels.</p>
</td></tr>
<tr><td class="val" id="flags">flags</td><td class="desc">
<p>The load flags, as in <a href="../ft2-base_interface/#ft_load_glyph">FT_Load_Glyph</a>.</p>
</td></tr>
</table>

<hr>

## FTC_ImageType

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FTC_ImageTypeRec_*  <b>FTC_ImageType</b>;
</pre>
</div>


A handle to an <a href="../ft2-cache_subsystem/#ftc_imagetyperec">FTC_ImageTypeRec</a> structure.

<hr>

## FTC_ImageCache_LookupScaler

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FTC_ImageCache_LookupScaler</b>( <a href="../ft2-cache_subsystem/#ftc_imagecache">FTC_ImageCache</a>  cache,
                               <a href="../ft2-cache_subsystem/#ftc_scaler">FTC_Scaler</a>      scaler,
                               <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>        load_flags,
                               <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>         gindex,
                               <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a>       *aglyph,
                               <a href="../ft2-cache_subsystem/#ftc_node">FTC_Node</a>       *anode );
</pre>
</div>


A variant of <a href="../ft2-cache_subsystem/#ftc_imagecache_lookup">FTC_ImageCache_Lookup</a> that uses an <a href="../ft2-cache_subsystem/#ftc_scalerrec">FTC_ScalerRec</a> to specify the face ID and its size.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="cache">cache</td><td class="desc">
<p>A handle to the source glyph image cache.</p>
</td></tr>
<tr><td class="val" id="scaler">scaler</td><td class="desc">
<p>A pointer to a scaler descriptor.</p>
</td></tr>
<tr><td class="val" id="load_flags">load_flags</td><td class="desc">
<p>The corresponding load flags.</p>
</td></tr>
<tr><td class="val" id="gindex">gindex</td><td class="desc">
<p>The glyph index to retrieve.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="aglyph">aglyph</td><td class="desc">
<p>The corresponding <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a> object. 0&nbsp;in case of failure.</p>
</td></tr>
<tr><td class="val" id="anode">anode</td><td class="desc">
<p>Used to return the address of the corresponding cache node after incrementing its reference count (see note below).</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The returned glyph is owned and managed by the glyph image cache. Never try to transform or discard it manually! You can however create a copy with <a href="../ft2-glyph_management/#ft_glyph_copy">FT_Glyph_Copy</a> and modify the new one.

If &lsquo;anode&rsquo; is _not_ NULL, it receives the address of the cache node containing the glyph image, after increasing its reference count. This ensures that the node (as well as the <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a>) will always be kept in the cache until you call <a href="../ft2-cache_subsystem/#ftc_node_unref">FTC_Node_Unref</a> to &lsquo;release&rsquo; it.

If &lsquo;anode&rsquo; is NULL, the cache node is left unchanged, which means that the <a href="../ft2-glyph_management/#ft_glyph">FT_Glyph</a> could be flushed out of the cache on the next call to one of the caching sub-system APIs. Don't assume that it is persistent!

Calls to <a href="../ft2-base_interface/#ft_set_char_size">FT_Set_Char_Size</a> and friends have no effect on cached glyphs; you should always use the FreeType cache API instead.

<hr>

## FTC_SBitRec

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FTC_SBitRec_
  {
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>   width;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>   height;
    <a href="../ft2-basic_types/#ft_char">FT_Char</a>   left;
    <a href="../ft2-basic_types/#ft_char">FT_Char</a>   top;

    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>   format;
    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>   max_grays;
    <a href="../ft2-basic_types/#ft_short">FT_Short</a>  pitch;
    <a href="../ft2-basic_types/#ft_char">FT_Char</a>   xadvance;
    <a href="../ft2-basic_types/#ft_char">FT_Char</a>   yadvance;

    <a href="../ft2-basic_types/#ft_byte">FT_Byte</a>*  buffer;

  } <b>FTC_SBitRec</b>;
</pre>
</div>


A very compact structure used to describe a small glyph bitmap.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="width">width</td><td class="desc">
<p>The bitmap width in pixels.</p>
</td></tr>
<tr><td class="val" id="height">height</td><td class="desc">
<p>The bitmap height in pixels.</p>
</td></tr>
<tr><td class="val" id="left">left</td><td class="desc">
<p>The horizontal distance from the pen position to the left bitmap border (a.k.a. &lsquo;left side bearing&rsquo;, or &lsquo;lsb&rsquo;).</p>
</td></tr>
<tr><td class="val" id="top">top</td><td class="desc">
<p>The vertical distance from the pen position (on the baseline) to the upper bitmap border (a.k.a. &lsquo;top side bearing&rsquo;). The distance is positive for upwards y&nbsp;coordinates.</p>
</td></tr>
<tr><td class="val" id="format">format</td><td class="desc">
<p>The format of the glyph bitmap (monochrome or gray).</p>
</td></tr>
<tr><td class="val" id="max_grays">max_grays</td><td class="desc">
<p>Maximum gray level value (in the range 1 to&nbsp;255).</p>
</td></tr>
<tr><td class="val" id="pitch">pitch</td><td class="desc">
<p>The number of bytes per bitmap line. May be positive or negative.</p>
</td></tr>
<tr><td class="val" id="xadvance">xadvance</td><td class="desc">
<p>The horizontal advance width in pixels.</p>
</td></tr>
<tr><td class="val" id="yadvance">yadvance</td><td class="desc">
<p>The vertical advance height in pixels.</p>
</td></tr>
<tr><td class="val" id="buffer">buffer</td><td class="desc">
<p>A pointer to the bitmap pixels.</p>
</td></tr>
</table>

<hr>

## FTC_SBitCache_LookupScaler

Defined in FT_CACHE_H (freetype/ftcache.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FTC_SBitCache_LookupScaler</b>( <a href="../ft2-cache_subsystem/#ftc_sbitcache">FTC_SBitCache</a>  cache,
                              <a href="../ft2-cache_subsystem/#ftc_scaler">FTC_Scaler</a>     scaler,
                              <a href="../ft2-basic_types/#ft_ulong">FT_ULong</a>       load_flags,
                              <a href="../ft2-basic_types/#ft_uint">FT_UInt</a>        gindex,
                              <a href="../ft2-cache_subsystem/#ftc_sbit">FTC_SBit</a>      *sbit,
                              <a href="../ft2-cache_subsystem/#ftc_node">FTC_Node</a>      *anode );
</pre>
</div>


A variant of <a href="../ft2-cache_subsystem/#ftc_sbitcache_lookup">FTC_SBitCache_Lookup</a> that uses an <a href="../ft2-cache_subsystem/#ftc_scalerrec">FTC_ScalerRec</a> to specify the face ID and its size.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="cache">cache</td><td class="desc">
<p>A handle to the source sbit cache.</p>
</td></tr>
<tr><td class="val" id="scaler">scaler</td><td class="desc">
<p>A pointer to the scaler descriptor.</p>
</td></tr>
<tr><td class="val" id="load_flags">load_flags</td><td class="desc">
<p>The corresponding load flags.</p>
</td></tr>
<tr><td class="val" id="gindex">gindex</td><td class="desc">
<p>The glyph index.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="sbit">sbit</td><td class="desc">
<p>A handle to a small bitmap descriptor.</p>
</td></tr>
<tr><td class="val" id="anode">anode</td><td class="desc">
<p>Used to return the address of the corresponding cache node after incrementing its reference count (see note below).</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<h4>note</h4>

The small bitmap descriptor and its bit buffer are owned by the cache and should never be freed by the application. They might as well disappear from memory on the next cache lookup, so don't treat them as persistent data.

The descriptor's &lsquo;buffer&rsquo; field is set to&nbsp;0 to indicate a missing glyph bitmap.

If &lsquo;anode&rsquo; is _not_ NULL, it receives the address of the cache node containing the bitmap, after increasing its reference count. This ensures that the node (as well as the image) will always be kept in the cache until you call <a href="../ft2-cache_subsystem/#ftc_node_unref">FTC_Node_Unref</a> to &lsquo;release&rsquo; it.

If &lsquo;anode&rsquo; is NULL, the cache node is left unchanged, which means that the bitmap could be flushed out of the cache on the next call to one of the caching sub-system APIs. Don't assume that it is persistent!

<hr>

