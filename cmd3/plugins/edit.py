import os
import platform

from cmd3.shell import command
from sh import open as open_editor
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

        filename = arg

        if platform.system() == 'Darwin':

            # touch filename
            if not os.path.exists(filename):
                file(filename, 'w+').close()

            editors = ["/Applications/Aquamacs.app",
                       "/Applications/Emacs.app",
                       "/usr/bin/emacs"]

            for editor in editors:
                if os.path.exists(editor):
                    open_editor("-a", editor, filename)
                    return

            Console.error("Could not find working editor in {0}".format(str(editors)))
