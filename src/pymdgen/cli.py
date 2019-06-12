#!/bin/env python

import argparse
import importlib
import inspect
import logging

from pymdgen import (
    doc_func,
    doc_class,
    )


log = logging.getLogger('pymdgen')


def main():

    parser = argparse.ArgumentParser(
        description="Inspects given python modules and prints markdown")

    parser.add_argument("--debug", dest="debug", action="store_true",
                        help="display debug messages")
    parser.add_argument("--section-level", type=int, default=3,
                        help="markdown section lavel")
    parser.add_argument("modules", nargs="+")

    args = parser.parse_args()

    debug = args.debug
    modules = args.modules
    section_level = args.section_level

    if debug:
        logging.basicConfig(level=logging.DEBUG)

    for name in modules:
        if '/' in name or name.endswith('.py'):
            name = name.replace('/', '.')
            name = name.rstrip('.py')
            print('modules should be in python notation, trying with', name)

        module = importlib.import_module(name)

        for k, v in inspect.getmembers(module):
            if k == '__builtins__':
                continue
            log.debug("checking %s:%s" % (v, k))
            if inspect.isfunction(v):
                doc_func(k, v, section_level)
            if inspect.isclass(v):
                doc_class(k, v, section_level)

if __name__ == "__main__":
    main()

