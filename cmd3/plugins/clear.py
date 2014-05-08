from cmd3.shell import command

import os
import sys


class clear:

    #
    # CLEAR
    #

    def activate_clear(self):
        """activates the clear command"""
        pass

    @command
    def do_clear(self, arg, arguments):
        """
        Usage:
            clear

        Clears the screen."""

        sys.stdout.write(os.popen('clear').read())

    @command
    def do_banner(self, arg, arguments):
        """
        Usage:
            banner [--c=CHAR] TEXT

        Arguments:
            TEXT   The text message from which to create the banner
            CHAR   The character for the frame. [default='=']
            
        Prints a banner form a one line text message."""

        print 70 * arguments['CHAR']
        print arguments['TEXT']
        print 70 * arguments['CHAR']         

