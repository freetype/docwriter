[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; List Processing

-------------------------------

# List Processing

## Synopsis

This section contains various definitions related to list processing using doubly-linked nodes.

## FT_List

Defined in FT_TYPES_H (freetype/fttypes.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_ListRec_*  <b>FT_List</b>;
</pre>
</div>


A handle to a list record (see <a href="../ft2-list_processing/#ft_listrec">FT_ListRec</a>).

<hr>

## FT_ListNode

Defined in FT_TYPES_H (freetype/fttypes.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span> FT_ListNodeRec_*  <b>FT_ListNode</b>;
</pre>
</div>


Many elements and objects in FreeType are listed through an <a href="../ft2-list_processing/#ft_list">FT_List</a> record (see <a href="../ft2-list_processing/#ft_listrec">FT_ListRec</a>). As its name suggests, an FT_ListNode is a handle to a single list element.

<hr>

## FT_ListRec

Defined in FT_TYPES_H (freetype/fttypes.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_ListRec_
  {
    <a href="../ft2-list_processing/#ft_listnode">FT_ListNode</a>  head;
    <a href="../ft2-list_processing/#ft_listnode">FT_ListNode</a>  tail;

  } <b>FT_ListRec</b>;
</pre>
</div>


A structure used to hold a simple doubly-linked list. These are used in many parts of FreeType.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="head">head</td><td class="desc">
<p>The head (first element) of doubly-linked list.</p>
</td></tr>
<tr><td class="val" id="tail">tail</td><td class="desc">
<p>The tail (last element) of doubly-linked list.</p>
</td></tr>
</table>

<hr>

## FT_ListNodeRec

Defined in FT_TYPES_H (freetype/fttypes.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">struct</span>  FT_ListNodeRec_
  {
    <a href="../ft2-list_processing/#ft_listnode">FT_ListNode</a>  prev;
    <a href="../ft2-list_processing/#ft_listnode">FT_ListNode</a>  next;
    <span class="keyword">void</span>*        data;

  } <b>FT_ListNodeRec</b>;
</pre>
</div>


A structure used to hold a single list element.

<h4>fields</h4>
<table class="fields">
<tr><td class="val" id="prev">prev</td><td class="desc">
<p>The previous element in the list. NULL if first.</p>
</td></tr>
<tr><td class="val" id="next">next</td><td class="desc">
<p>The next element in the list. NULL if last.</p>
</td></tr>
<tr><td class="val" id="data">data</td><td class="desc">
<p>A typeless pointer to the listed object.</p>
</td></tr>
</table>

<hr>

## FT_List_Add

Defined in FT_LIST_H (freetype/ftlist.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_List_Add</b>( <a href="../ft2-list_processing/#ft_list">FT_List</a>      list,
               <a href="../ft2-list_processing/#ft_listnode">FT_ListNode</a>  node );
</pre>
</div>


Append an element to the end of a list.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="list">list</td><td class="desc">
<p>A pointer to the parent list.</p>
</td></tr>
<tr><td class="val" id="node">node</td><td class="desc">
<p>The node to append.</p>
</td></tr>
</table>

<hr>

## FT_List_Insert

Defined in FT_LIST_H (freetype/ftlist.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_List_Insert</b>( <a href="../ft2-list_processing/#ft_list">FT_List</a>      list,
                  <a href="../ft2-list_processing/#ft_listnode">FT_ListNode</a>  node );
</pre>
</div>


Insert an element at the head of a list.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="list">list</td><td class="desc">
<p>A pointer to parent list.</p>
</td></tr>
<tr><td class="val" id="node">node</td><td class="desc">
<p>The node to insert.</p>
</td></tr>
</table>

<hr>

## FT_List_Find

Defined in FT_LIST_H (freetype/ftlist.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-list_processing/#ft_listnode">FT_ListNode</a> )
  <b>FT_List_Find</b>( <a href="../ft2-list_processing/#ft_list">FT_List</a>  list,
                <span class="keyword">void</span>*    data );
</pre>
</div>


Find the list node for a given listed object.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="list">list</td><td class="desc">
<p>A pointer to the parent list.</p>
</td></tr>
<tr><td class="val" id="data">data</td><td class="desc">
<p>The address of the listed object.</p>
</td></tr>
</table>

<h4>return</h4>

List node. NULL if it wasn't found.

<hr>

## FT_List_Remove

Defined in FT_LIST_H (freetype/ftlist.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_List_Remove</b>( <a href="../ft2-list_processing/#ft_list">FT_List</a>      list,
                  <a href="../ft2-list_processing/#ft_listnode">FT_ListNode</a>  node );
</pre>
</div>


Remove a node from a list. This function doesn't check whether the node is in the list!

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="node">node</td><td class="desc">
<p>The node to remove.</p>
</td></tr>
</table>

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="list">list</td><td class="desc">
<p>A pointer to the parent list.</p>
</td></tr>
</table>

<hr>

## FT_List_Up

Defined in FT_LIST_H (freetype/ftlist.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_List_Up</b>( <a href="../ft2-list_processing/#ft_list">FT_List</a>      list,
              <a href="../ft2-list_processing/#ft_listnode">FT_ListNode</a>  node );
</pre>
</div>


Move a node to the head/top of a list. Used to maintain LRU lists.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="list">list</td><td class="desc">
<p>A pointer to the parent list.</p>
</td></tr>
<tr><td class="val" id="node">node</td><td class="desc">
<p>The node to move.</p>
</td></tr>
</table>

<hr>

## FT_List_Iterate

Defined in FT_LIST_H (freetype/ftlist.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_List_Iterate</b>( <a href="../ft2-list_processing/#ft_list">FT_List</a>           list,
                   <a href="../ft2-list_processing/#ft_list_iterator">FT_List_Iterator</a>  iterator,
                   <span class="keyword">void</span>*             user );
</pre>
</div>


Parse a list and calls a given iterator function on each element. Note that parsing is stopped as soon as one of the iterator calls returns a non-zero value.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="list">list</td><td class="desc">
<p>A handle to the list.</p>
</td></tr>
<tr><td class="val" id="iterator">iterator</td><td class="desc">
<p>An iterator function, called on each node of the list.</p>
</td></tr>
<tr><td class="val" id="user">user</td><td class="desc">
<p>A user-supplied field that is passed as the second argument to the iterator.</p>
</td></tr>
</table>

<h4>return</h4>

The result (a FreeType error code) of the last iterator call.

<hr>

## FT_List_Iterator

Defined in FT_LIST_H (freetype/ftlist.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-basic_types/#ft_error">FT_Error</a>
  (*<b>FT_List_Iterator</b>)( <a href="../ft2-list_processing/#ft_listnode">FT_ListNode</a>  node,
                       <span class="keyword">void</span>*        user );
</pre>
</div>


An FT_List iterator function that is called during a list parse by <a href="../ft2-list_processing/#ft_list_iterate">FT_List_Iterate</a>.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="node">node</td><td class="desc">
<p>The current iteration list node.</p>
</td></tr>
<tr><td class="val" id="user">user</td><td class="desc">
<p>A typeless pointer passed to <a href="../ft2-list_processing/#ft_list_iterate">FT_List_Iterate</a>. Can be used to point to the iteration's state.</p>
</td></tr>
</table>

<hr>

## FT_List_Finalize

Defined in FT_LIST_H (freetype/ftlist.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_List_Finalize</b>( <a href="../ft2-list_processing/#ft_list">FT_List</a>             list,
                    <a href="../ft2-list_processing/#ft_list_destructor">FT_List_Destructor</a>  destroy,
                    <a href="../ft2-system_interface/#ft_memory">FT_Memory</a>           memory,
                    <span class="keyword">void</span>*               user );
</pre>
</div>


Destroy all elements in the list as well as the list itself.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="list">list</td><td class="desc">
<p>A handle to the list.</p>
</td></tr>
<tr><td class="val" id="destroy">destroy</td><td class="desc">
<p>A list destructor that will be applied to each element of the list. Set this to NULL if not needed.</p>
</td></tr>
<tr><td class="val" id="memory">memory</td><td class="desc">
<p>The current memory object that handles deallocation.</p>
</td></tr>
<tr><td class="val" id="user">user</td><td class="desc">
<p>A user-supplied field that is passed as the last argument to the destructor.</p>
</td></tr>
</table>

<h4>note</h4>

This function expects that all nodes added by <a href="../ft2-list_processing/#ft_list_add">FT_List_Add</a> or <a href="../ft2-list_processing/#ft_list_insert">FT_List_Insert</a> have been dynamically allocated.

<hr>

## FT_List_Destructor

Defined in FT_LIST_H (freetype/ftlist.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <span class="keyword">void</span>
  (*<b>FT_List_Destructor</b>)( <a href="../ft2-system_interface/#ft_memory">FT_Memory</a>  memory,
                         <span class="keyword">void</span>*      data,
                         <span class="keyword">void</span>*      user );
</pre>
</div>


An <a href="../ft2-list_processing/#ft_list">FT_List</a> iterator function that is called during a list finalization by <a href="../ft2-list_processing/#ft_list_finalize">FT_List_Finalize</a> to destroy all elements in a given list.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="system">system</td><td class="desc">
<p>The current system object.</p>
</td></tr>
<tr><td class="val" id="data">data</td><td class="desc">
<p>The current object to destroy.</p>
</td></tr>
<tr><td class="val" id="user">user</td><td class="desc">
<p>A typeless pointer passed to <a href="../ft2-list_processing/#ft_list_iterate">FT_List_Iterate</a>. It can be used to point to the iteration's state.</p>
</td></tr>
</table>

<hr>

