from cmd3.shell import command

import os
import sys


class clear:

    #
    # CLEAR
    #

    def activate_clear(self):
        pass

    @command
    def do_clear(self, arg, arguments):
        """
        Usage:
            clear

        Clears the screen."""

        sys.stdout.write(os.popen('clear').read())
