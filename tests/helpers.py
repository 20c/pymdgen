import sys

def py2(output):

    """
    builtins.object is called __builtin__.object in py2
    so if py version is 2 we adjust the output so the tests
    pass
    """

    if sys.version_info[0] == 2:
        output = [o.replace("__builtin__", "builtins") for o in output]
    return output


