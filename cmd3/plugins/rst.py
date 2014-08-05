from cStringIO import StringIO
import string
import textwrap
from docopt import docopt
import inspect
import sys
import importlib
from cmd3.shell import command


class rst:

    def activate_rst(self):
        """activates the RST command"""
        pass

    def _print_rst(self, what):
        """
        prints the rst page of the command what

        :param what: the command
        :type what: string

        """

        print
        print "Command - %s::" % what

        exec("h = self.do_%s.__doc__" % what)
        h = textwrap.dedent(h).replace("\n", "\n    ")
        print h

    @command
    def do_man(self, args, arguments):
        """
        ::
        
            Usage:
                   man COMMAND
                   man [--noheader]

            Options:
                   --norule   no rst header

            Arguments:
                   COMMAND   the command to be printed 

            Description:
                man 
                    Prints out the help pages
                man COMMAND
                    Prints out the help page for a specific command
        """
        if arguments['COMMAND'] is None:
        
            print
            print "Commands"
            print 70 * "="

            commands = [k for k in dir(self) if k.startswith("do_")]
            commands.sort()

        else:
            print arguments
            commands = [arguments['COMMAND']]


        for command in commands:
            what = command.replace("do_", "")
            try:
                if not arguments["--noheader"]:
                    print what
                    print 70 * "-"
                self._print_rst(what)
            except:
                print "\n    Command documentation %s missing, help_%s" % (what, what)
            print
