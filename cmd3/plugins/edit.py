import os
import platform

from cmd3.shell import command
from cmd3.console import Console

# noinspection PyUnusedLocal
class edit:

    #
    # EDIT
    #

    def activate_edit(self):
        """activates the edit command"""
        pass

    @command
    def do_edit(self, arg, arguments):
        """
        ::

            Usage:
                    edit FILENAME

            Edits the file with the given name

            Arguments:
                FILENAME  the file to edit

        """

        def _create_file(filename):
            if not os.path.exists(filename):
                file(filename, 'w+').close()

        def _edit(prefix, editors, filename):
            for editor in editors:
                if os.path.exists(editor):
                    _create_file(filename)
                    os.system("{:} {:} {:}".format(prefix, editor, filename))
                    return True
            return False


        filename = arg

        what =  platform.system().lower()
        prefix = ""

        print (what)
        if 'darwin' in what:

            editors = ["/Applications/Aquamacs.app",
                       "/Applications/Emacs.app"]
            prefix = "open -a "

        elif "linux" in what:

            editors = ["emacs",
                       "vi",
                       "vim",
                       "nano"]

        elif "windows" in what:

            editors = ["emacs",
                       "vi",
                       "vim",
                       "nano",
                       "notepad",
                       "notepad++"]

        else:
            Console.error("Please contact the developers to add an "
                          "editor for your platform")
            return

        if not _edit(prefix, editors, filename):
            Console.error("Could not find working editor in {0}"
                          .format(str(editors)))
