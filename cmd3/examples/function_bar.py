from cmd3.shell import command

def do_fbar(self, arguments):
    """Usage:
            bar -f FILE
            bar FILE
            bar list

    This command does some useful things.

    Arguments:
          FILE   a file name

    Options:
          -f      specify the file

    """
    print "f"
    print arguments


class fbar:

    def activate_fbar(self):
       print "... activate bar"

    def info_fbar(self):
        print "information for the class bar"

    @command_function
    def do_fbar(self, f, arg, arguments):
        print 'fbar'
        f(arguments)
