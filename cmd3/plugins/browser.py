import webbrowser
import os

from cmd3.shell import command
from cmd3.console import Console

# noinspection PyUnusedLocal
class browser:

    #
    # Browser
    #

    def _expand_filename(self, line):
        """expands the filename if there is a . as leading path"""
        # expand .
        newline = line
        path = os.getcwd()
        if newline.startswith("."):
            newline = newline.replace(".", path, 1)
        # expand ~
        newline = os.path.expanduser(newline)
        return newline

    @command
    def do_open(self, args, arguments):
        """
        ::

            Usage:
                    open FILENAME

            ARGUMENTS:
                FILENAME  the file to open in the cwd if . is
                          specified. If file in in cwd
                          you must specify it with ./FILENAME

            Opens the given URL in a browser window.
        """
        filename = arguments['FILENAME']
        filename = self._expand_filename(filename)
        Console.ok("open {0}".format(filename))

        if not (filename.startswith("file:") or filename.startswith("http:")):
            try:
                with open(filename):
                    pass
                filename += "file://"
            except:
                Console.error("unsupported browser format in file {0}".format(filename))
                return

        try:
            webbrowser.open("%s" % filename)
        except:
            Console.error("can not open browser with file {0}".format(filename))
