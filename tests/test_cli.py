import subprocess

def test_cli():

    output = subprocess.check_output(["pymdgen", "pymdgen.test_module"])
    assert output == b'### dummy\n\n```\ndummy(builtins.object)\n```\n\nthis is a dummy class \n\n#### dummy_method\n\n```\ndummy_method(self)\n```\n\nthis is a dummy func \n\n---\n\n### dummy_func\n\n```\ndummy_func()\n```\n\nthis is a dummy func \n\n---\n'
