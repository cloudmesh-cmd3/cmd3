from cmd3.cyberaide.decorators import command

import os
import sys

class clear:

    ########################################
    # CLEAR
    ########################################

    def activate_clear(self):
        pass
    

    @command
    def do_clear(self, arg, arguments):
        """
        Ussage:
            clear

        Clears the screen."""

        sys.stdout.write(os.popen('clear').read())
