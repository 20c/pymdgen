import os.path

import markdown


EXT = ["pymdgen"]

def test_gencodedocs():
    expected_path = os.path.join(
        os.path.dirname(__file__), "data", "gencodedocs.expected.html")

    with open(expected_path, "r") as fh:
        expected = fh.read().strip("\n")

    md = markdown.markdown("{pymdgen:pymdgen.test_module}", extensions=EXT)
    assert md == expected


def test_gencommandoutput():

    expected_path = os.path.join(
        os.path.dirname(__file__), "data", "gencommandoutput.expected.html")

    with open(expected_path, "r") as fh:
        expected = fh.read().strip("\n")

    md = markdown.markdown("{pymdgen-cmd:pymdgen --help}", extensions=EXT)
    assert md == expected
