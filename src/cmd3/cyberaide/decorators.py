#from method_decorator import method_decorator

import textwrap
from docopt import docopt
import inspect

def command(func):
    classname = inspect.getouterframes(inspect.currentframe())[1][3]
    name = func.__name__
    help_name = name.replace("do_","help_")
    doc = textwrap.dedent(func.__doc__)
    
    def new(instance, args):
        #instance.new.__doc__ = doc
        try:
            arguments = docopt(doc, help=True, argv=args)
            func(instance, args, arguments)
        except SystemExit:
            if not args in ('-h','--help'):
                print "Error: Wrong Format"
            print doc
    new.__doc__ = doc
    return new

        

