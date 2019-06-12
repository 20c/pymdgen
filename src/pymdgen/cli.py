#!/bin/env python

import click
import importlib
import inspect
import logging

from pymdgen import (
    doc_func,
    doc_class,
    )


log = logging.getLogger('pymdgen')


@click.command()
@click.option('--debug', help='display debug messages', is_flag=True, default=False)
@click.option('--section-level', help='markdown section level', default=3)
@click.argument('modules', nargs=-1)
def main(modules, debug, section_level):
    """ inspects given python modules and prints markdown """

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

