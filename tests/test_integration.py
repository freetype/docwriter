"""
# Docwriter Integration tests

This is a simple integration test that builds Docwriter
documentation against a test file.

From the root of the Docwriter git repo, use:
    python -m pytest tests/test_integration.py
"""

import logging
import os
import subprocess

log = logging.getLogger('mkdocs')

def test_integration( capfd ):

    log.propagate = False
    stream = logging.StreamHandler()
    formatter = logging.Formatter(
        "\033[1m\033[1;32m *** %(message)s *** \033[0m")
    stream.setFormatter(formatter)
    log.addHandler(stream)
    log.setLevel(logging.DEBUG)

    base_cmd = ['python', 'docwriter.py', '--prefix=test',
                '--title=Docwriter Test', '--output=./tests/output',
                '--verbose' ]
    folders  = ['./tests/assets/*.c']

    log.debug("Building markdown docs.")
    command = base_cmd + folders
    # run the command
    subprocess.check_call( command )
    # capture output to check for warnings
    out, err = capfd.readouterr()
    # print the logs on failure
    print( err )
    # fail if there are warnings
    assert not "WARNING" in err
