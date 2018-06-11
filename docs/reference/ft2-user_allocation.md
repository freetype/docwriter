[Docs](ft2-index.md) &raquo; [General Remarks](ft2-toc.md#general-remarks) &raquo; User allocation

-------------------------------

# User allocation

## Synopsis

FreeType assumes that structures allocated by the user and passed as arguments are zeroed out except for the actual data. In other words, it is recommended to use &lsquo;calloc&rsquo; (or variants of it) instead of &lsquo;malloc&rsquo; for allocation.

