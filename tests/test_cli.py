import subprocess
import sys

from pymdgen.cli import run

from helpers import py2

def test_cli():

    output = subprocess.check_output(["pymdgen", "pymdgen.test_module"])

    if sys.version_info[0] == 3:
        assert output == b'### dummy\n\n```\ndummy(builtins.object)\n```\n\nthis is a dummy class \n\n#### dummy_method\n\n```\ndummy_method(self)\n```\n\nthis is a dummy func \n\n---\n\n### dummy_func\n\n```\ndummy_func()\n```\n\nthis is a dummy func \n\n---\n'
    else:
        assert output == b'### dummy\n\n```\ndummy(__builtin__.object)\n```\n\nthis is a dummy class \n\n#### dummy_method\n\n```\ndummy_method(self)\n```\n\nthis is a dummy func \n\n---\n\n### dummy_func\n\n```\ndummy_func()\n```\n\nthis is a dummy func \n\n---\n'

def test_run():
    output = run(["pymdgen.test_module"], False, 3)
    assert py2(output) == ['### dummy', '', '```', 'dummy(builtins.object)', '```', '', 'this is a dummy class ', '', '#### dummy_method', '', '```', 'dummy_method(self)', '```', '', 'this is a dummy func ', '', '---', '', '### dummy_func', '', '```', 'dummy_func()', '```', '', 'this is a dummy func ', '', '---']
