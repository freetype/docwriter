#!/bin/bash
set -exo pipefail

#
#  freetype.sh
#
#    Clone freetype2 and make targets `refdoc' and `refdoc-venv`.
#
#  Copyright (C) 2020-2021 by
#  Nikhil Ramakrishnan.
#
#  This file is part of the FreeType project, and may only be used,
#  modified, and distributed under the terms of the FreeType project
#  license, LICENSE.TXT.  By continuing to use, modify, or distribute
#  this file you indicate that you have read the license and
#  understand and accept it fully.

check_output_dir () {
    # Count number of files in output directories
    file_count=$(find "$1" -type f | wc -l)

    echo Number of files in $1 is $file_count

    if [ "$file_count" -eq "0" ]; then
        echo ERROR: No output files found in $1 1>&2
        return 1
    fi
    return 0
}

dir="${PWD}"

script_dir=$( dirname $( readlink -f "${0}" ) ) # this is the `tests' dir
output_dir="$script_dir/output"
freetype_dir="freetype2"
path_to_freetype="$output_dir/$freetype_dir"
docs_dir="docs"
markdown_dir="$docs_dir/markdown"
reference_dir="$docs_dir/reference"
build_dir="freetype2.compile"

cd "$output_dir" # go to `tests/output'

# Clone FreeType from master
git clone --depth=50 --branch=master https://gitlab.freedesktop.org/freetype/freetype.git $freetype_dir

cd "$freetype_dir"

git clean -dfqx
git reset --hard
git rev-parse HEAD

sh autogen.sh

sh configure

#########################################################################
# Part 1 - Use the docwriter that is already installed
#########################################################################
make refdoc

# Come back to freetype2 directory
cd "$path_to_freetype"

# Check output
check_output_dir "$markdown_dir"
res1=$?
check_output_dir "$reference_dir"
res2=$?

if [ "$res1" -ne "0" ] || [ "$res2" -ne "0" ]; then
    exit 1
fi

# Clean up only the `docs' dir
cd "$docs_dir"
git clean -dfqx
git reset --hard
cd "$path_to_freetype"

#########################################################################
# Part 2 - Use a virtual environment
#########################################################################
make refdoc-venv

# Come back to freetype2 directory
cd "$path_to_freetype"

# Check output
check_output_dir "$markdown_dir"
res1=$?
check_output_dir "$reference_dir"
res2=$?

if [ "$res1" -ne "0" ] || [ "$res2" -ne "0" ]; then
    exit 1
fi

# Clean up only the `docs' dir
cd "$docs_dir"
git clean -dfqx
git reset --hard
cd "$path_to_freetype"

#########################################################################
# Part 3 - Build docs with `builddir' != `srcdir'
#########################################################################
# Configure freetype2 in another directory
cd ../
mkdir "$build_dir"
cd "$build_dir"
../$freetype_dir/configure

make refdoc

# Come back to `builddir'
cd "$output_dir/$build_dir"

# Check output
check_output_dir "$markdown_dir"
res1=$?
check_output_dir "$reference_dir"
res2=$?

if [ "$res1" -ne "0" ] || [ "$res2" -ne "0" ]; then
    exit 1
fi

# Final clean up
cd  "$output_dir"
rm -rf $freetype_dir $build_dir

cd "$dir"

# eof
