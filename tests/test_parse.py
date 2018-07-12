import sources
import content
import utils

# create context and processor
source_processor  = sources.SourceProcessor()
content_processor = content.ContentProcessor()

def test_parse_file():
    # retrieve the list of files to process
    file_list = utils.make_file_list( ['./tests/assets/*.c'] )
    for filename in file_list:
        source_processor.parse_file( filename )
    # get blocks
    blocks = source_processor.blocks
    count  = len( blocks )

    # there must be 12 blocks in file
    assert count == 12

def test_parse_source():
    # retrieve the list of files to process
    file_list = utils.make_file_list( ['./tests/assets/*.c'] )
    for filename in file_list:
        source_processor.parse_file( filename )
        content_processor.parse_sources( source_processor )
    # process sections
    content_processor.finish()
    # get headers
    headers = content_processor.headers
    # expected values
    expected_key = 'freetype/ftbbox.h'
    expected_val = 'FT_BBOX_H'

    assert headers[expected_key] == expected_val
