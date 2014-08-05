from cmd3.shell import command

import webbrowser
import platform
import os


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
        print "open %s" % filename

        if not (filename.startswith("file:") or filename.startswith("http:")):
            try:
                with open(filename):
                    pass
                filename = "file://" + filename
            except:
                print "can not open file %s" % filename
                return

        try:
            webbrowser.open("%s" % filename)
        except:
            print "can not open browser %s" % filename
