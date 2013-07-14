import types
import textwrap
from docopt import docopt
import inspect
import sys
import importlib
from cmd3.shell import command


class opt_example:

    """opt_example class"""

    def activate_opt_example(self):
        pass

    @command
    def do_opt_example(self, args, arguments):
        """
        Usage:
               opt_example [-vr] [FILE] ...

        Process FILE and optionally apply some options

        Arguments:
          FILE        optional input file

        Options:
          -v       verbose mode
          -r       make report

        """
        print(arguments)

    @command
    def do_neu(self, args, arguments):
        """
        Usage:
               opt_example [-vr] [FILE] ...

        Process FILE and optionally apply some options

        Arguments:
          FILE        optional input file

        Options:
          -v       verbose mode
          -r       make report

        """
        #arguments = _get_doc_args(self.do_neu,args)

        print(arguments)
        return ""

    @command
    def do_old(self, args, arguments):
        """
        Usage:
               old [-ab] [FILE] ...

        Process FILE and optionally apply some options

        Arguments:
          FILE        optional input file

        Options:
          -a       verbose mode
          -b       make report

        """
        #arguments = _get_doc_args(self.do_neu,args)

        print(arguments)
        return ""
