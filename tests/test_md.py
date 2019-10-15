import sys
import os.path

import markdown

from helpers import write_expected


EXT = ["pymdgen"]
VERSION = "{}".format(sys.version_info[0])


def test_gencodedocs(expected_docs_html):
    html = markdown.markdown("{pymdgen:pymdgen.test_module}", extensions=EXT)
    #write_expected("html", html)
    assert html == expected_docs_html


def test_gencommandoutput():

    expected_path = os.path.join(
        os.path.dirname(__file__), "data", VERSION, "gencommandoutput.expected.html"
    )

    with open(expected_path, "r") as fh:
        expected = fh.read().strip("\n")

    md = markdown.markdown("{pymdgen-cmd:pymdgen --help}", extensions=EXT)
    assert md == expected
