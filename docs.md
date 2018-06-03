# sources.py

## Input
Single header file

## What it does
Divides file into blocks
Comments are a different block, other stuff is different blocks

Comment blocks (self.blocks) with markup tags have self.content set to lines (decoration removed)

## Final output
Same file divided into various blocks.

Comment blocks have self.content set.

# content.py

## Input
Source processor (from above)

## What it does
For every block:
    If it is a documentation comment (self.content is set), all blocks after
    it and before the next documentation comment are put in the `follow[]` list.

    A DocBlock is created with source blocks and `follow`.

### DocBlock
Receives a documentation comment block and follow list with all blocks after it.

reset processor.
`self.markups = processor.process_content( source.content )` (discussed after this)

Compute block type from first markup tag
Compute block name from first para

if type is "section", set it
if type is "chapter", set it
else add block to section

create list block

for every block in follow:
    break if block.format
    for every line in block:
        match and add header macros
        `processor.headers[m.group( 2 )] = m.group( 1 )`
        if sep found, break
        append line to source

        strip the leading and trailing empty lines from the sources

### process_content
for every line in content:
    check if code block

    if not in_code:
        find a markup tag
        if markup tag found, get name and prefix
        remove markup from line

    if markup tag found:
        add previous data to list
        append line to self.markup_lines
        
add remaining markup
return self.markups


### DocSection
Information about Sections
