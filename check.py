#
#  check.py
#
#    Check if all external modules are present.
#
#  Copyright 2018 by
#  Nikhil Ramakrishnan.
#
#  This file is part of the FreeType project, and may only be used,
#  modified, and distributed under the terms of the FreeType project
#  license, LICENSE.TXT.  By continuing to use, modify, or distribute
#  this file you indicate that you have read the license and
#  understand and accept it fully.
'''
Module to check if all required modules are available.

Usage:
    import check
    status = check.check()
'''
import sys

#
# Required imports
# Note that this is not the package name, but the module name as would be
# used in an import statement.
#
import_list = ["mistune", "yaml"]

def check( ):
    '''Check if all required modules are present.
    
    Return 0 on success, non-zero on error.'''
    flag = 0
    for package in import_list:
        try:
            exec( "import " + package )
        except:
            sys.stderr.write( "[ERROR] Missing module: " + package )
            flag = True
    if flag:
        return 1
    return 0
