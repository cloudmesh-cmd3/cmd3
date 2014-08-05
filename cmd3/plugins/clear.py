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
        ::

            Usage:
                banner [-c CHAR] [-n WIDTH] [-i INDENT] TEXT

            Arguments:
                TEXT   The text message from which to create the banner
                CHAR   The character for the frame. 
                WIDTH  Width of the banner
                INDENT indentation of the banner

            Options:
                -c CHAR   The character for the frame. [default: #]
                -n WIDTH  The width of the banner. [default: 70]
                -i INDENT  The width of the banner. [default: 0]            

            Prints a banner form a one line text message.
        """

        n = int(arguments['-n'])
        c = arguments['-c']
        i = int(arguments['-i'])        
        
        print i * " " + (n-i) * c
        print i * " " + c, arguments['TEXT']
        print i * " " + (n-i) * c

