import importlib
import inspect
import logging

log = logging.getLogger('pymdgen')

def doc_func(name, func, section_level=4):

    """
    output.append markdown formatted documentation for a function

    Arguments:
        - name(str): function name #FIXME: why is this manual?
        - func(function)
        - section_level(int): markdown section level
    """

    is_property = False

    if isinstance(func, property):
        func = func.fget
        is_property = True

    output = []
    docstr = inspect.getdoc(func)
    # skip functions without a docstr
    if not docstr:
        return output

    spec = inspect.getargspec(func)
    display = []
    end_args = []

    # *args and **kwargs
    if spec[1]:
        end_args.append('*' + spec[1])
    if spec[2]:
        end_args.append('**' + spec[2])

    # check for args with defaults
    if spec[3]:
        args = spec[0][-len(spec[3]):]
        default_args = list(zip(args, spec[3]))

        # set args to rest
        args = spec[0][:-len(spec[3])]
    else:
        args = spec[0]
        default_args = []

    if args:
        display.append(', '.join(args))
    if default_args:
        display.append(', '.join('%s=%s' % x for x in default_args))
    if end_args:
        display.append(', '.join(end_args))

    if name.find("__") == 0:
        title = "\{}".format(name)
    else:
        title = name

    output.append("{} {}".format('#' * section_level, title))
    output.append("")
    output.append('```')
    if is_property:
        output.append("@property")
    output.append(name + '(' + ', '.join(display) + ')')
    output.append('```')
    output.append("")
    output.append(docstr)
    output.append("")

    return output


def doc_class(name, cls, section_level=3):
    """
    output.append markdown formatted documentation for a class

    Arguments:
        - name(str): function name #FIXME: why is this manual?
        - cls(class)
        - section_level(int): markdown section level
    """

    output = []
    docstr = inspect.getdoc(cls)
    # skip functions without a docstr
    if not docstr:
        return output

    # full mro is probably overkill?
    # base_classes = inspect.getmro(cls)
    base_classes = cls.__bases__
    base_classes = (c.__module__ + '.' + c.__name__ for c in base_classes)

    output.append("{} {}".format('#' * section_level, name))
    output.append("")
    output.append('```')
    output.append(name + '(' + ', '.join(base_classes) + ')')
    output.append('```')
    output.append("")
    output.append(docstr)
    output.append("")

    for func_name, func in list(cls.__dict__.items()):
        if inspect.isfunction(func) or isinstance(func, property):
            output.extend(doc_func(func_name, func, section_level + 1))

    output.append("")

    return output


def doc_module(name, debug=False, section_level=3):

        if '/' in name or name.endswith('.py'):
            name = name.replace('/', '.')
            name = name.rstrip('.py')

        module = importlib.import_module(name)
        output = []

        for k, v in inspect.getmembers(module):
            if k == '__builtins__':
                continue
            log.debug("checking %s:%s" % (v, k))
            if inspect.isfunction(v):
                output.extend(doc_func(k, v, section_level))
            if inspect.isclass(v):
                output.extend(doc_class(k, v, section_level))

        return output


