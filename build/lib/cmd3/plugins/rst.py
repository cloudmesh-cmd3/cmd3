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
        pass

    @command
    def do_rst(self, args, arguments):
        """
        Usage:
               rst COMMAND

        Prints out the comand for inclusion into rst

        Arguments:
          COMMAND    The name of the command

        """

        what = arguments['COMMAND']
        print
        print "Commnad - %s::" % what

        exec("h = self.do_%s.__doc__" % what)
        h = textwrap.dedent(h).replace("\n", "\n    ")
        print h

    @command
    def do_man(self, args, arguments):
        """
        Usage:
               man [--noheader]

        Options:
               --norule   no rst header

        Prints out the help pages
        """

        print
        print "Commands"
        print 70 * "="

        commands = [k for k in dir(self) if k.startswith("do_")]
        commands.sort()

        for command in commands:
            what = command.replace("do_", "")
            try:
                if not arguments["--noheader"]:
                    print what
                    print 70 * "-"
                self.do_rst(what)
            except:
                print "\n    Command documentation %s missing, help_%s" % (what, what)
            print
