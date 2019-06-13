# Usage

```
Usage: pymdgen [OPTIONS] [MODULES]...

  inspects given python modules and prints markdown

Options:
  --section-level INTEGER  markdown section level
  --help                   Show this message and exit.
```

# Markdown extension

pymddgen also provides a markdown extension that allows you to
easily insert code and command documentation into your generated
docs.

Simply add the `pymdgen` extension to your python markdown instance

### Generate docs for a python module

```
{pymdgen:path.to.python.module}
```

### Generate output for `ls --help`

```
{pymdgen-cmd:ls --help}
```
