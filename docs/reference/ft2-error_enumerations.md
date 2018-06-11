[Docs](ft2-index.md) &raquo; [Error Codes](ft2-toc.md#error-codes) &raquo; Error Enumerations

-------------------------------

# Error Enumerations

## Synopsis

The header file &lsquo;fterrors.h&rsquo; (which is automatically included by &lsquo;freetype.h&rsquo; defines the handling of FreeType's enumeration constants. It can also be used to generate error message strings with a small macro trick explained below.

**Error Formats**

The configuration macro FT_CONFIG_OPTION_USE_MODULE_ERRORS can be defined in &lsquo;ftoption.h&rsquo; in order to make the higher byte indicate the module where the error has happened (this is not compatible with standard builds of FreeType&nbsp;2, however). See the file &lsquo;ftmoderr.h&rsquo; for more details.

**Error Message Strings**

Error definitions are set up with special macros that allow client applications to build a table of error message strings. The strings are not included in a normal build of FreeType&nbsp;2 to save space (most client applications do not use them).

To do so, you have to define the following macros before including this file.
```
  FT_ERROR_START_LIST
```

This macro is called before anything else to define the start of the error list. It is followed by several FT_ERROR_DEF calls.
```
  FT_ERROR_DEF( e, v, s )
```

This macro is called to define one single error. &lsquo;e&rsquo; is the error code identifier (e.g., &lsquo;Invalid_Argument&rsquo;), &lsquo;v&rsquo; is the error's numerical value, and &lsquo;s&rsquo; is the corresponding error string.
```
  FT_ERROR_END_LIST
```

This macro ends the list.

Additionally, you have to undefine &lsquo;FTERRORS_H_&rsquo; before #including this file.

Here is a simple example.
```
  #undef FTERRORS_H_
  #define FT_ERRORDEF( e, v, s )  { e, s },
  #define FT_ERROR_START_LIST     {
  #define FT_ERROR_END_LIST       { 0, NULL } };

  const struct
  {
    int          err_code;
    const char*  err_msg;
  } ft_errors[] =

  #include FT_ERRORS_H
```

Note that &lsquo;FT_Err_Ok&rsquo; is _not_ defined with &lsquo;FT_ERRORDEF&rsquo; but with &lsquo;FT_NOERRORDEF&rsquo;; it is always zero.

