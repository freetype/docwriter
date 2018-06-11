[Docs](ft2-index.md) &raquo; [General Remarks](ft2-toc.md#general-remarks) &raquo; FreeType's header inclusion scheme

-------------------------------

# FreeType's header inclusion scheme

## Synopsis

To be as flexible as possible (and for historical reasons), FreeType uses a very special inclusion scheme to load header files, for example
```
  #include <ft2build.h>

  #include FT_FREETYPE_H
  #include FT_OUTLINE_H
```

A compiler and its preprocessor only needs an include path to find the file &lsquo;ft2build.h&rsquo;; the exact locations and names of the other FreeType header files are hidden by preprocessor macro names, loaded by &lsquo;ft2build.h&rsquo;. The API documentation always gives the header macro name needed for a particular function.

