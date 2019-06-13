import re
import subprocess

from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension as BaseExtension

from pymdgen import doc_module

class GenCodeDocs(Preprocessor):
    """
    output code docs for specified python module
    """

    regex = re.compile("^\{pymdgen:(.+)\}$")

    def run(self, lines):
        new_lines = []
        for line in lines:
            m = self.regex.match(line)
            if m:
                new_lines.extend(self.generate(m.group(1)))
            else:
                new_lines.append(line)
        return new_lines


    def generate(self, module_name):
        return doc_module(module_name)


class GenCommandOutput(Preprocessor):
    """
    render command output
    """

    regex = re.compile("^\{pymdgen-cmd:(.+)\}$")

    def run(self, lines):
        new_lines = []
        for line in lines:
            m = self.regex.match(line)
            if m:
                new_lines.extend(self.generate(m.group(1)))
            else:
                new_lines.append(line)
        return new_lines


    def generate(self, command):
        output = subprocess.check_output(command.split(" "))
        lines = ['```']
        for line in output.split(b"\n"):
            lines.append(u"{}".format(line)[1:].strip("'"))
        lines.append('```')
        return lines


class Extension(BaseExtension):
    def extendMarkdown(self, md):
        md.preprocessors.register(GenCodeDocs(md), 'pymdgencode', 175)
        md.preprocessors.register(GenCommandOutput(md), 'pymdgencmd', 175)
