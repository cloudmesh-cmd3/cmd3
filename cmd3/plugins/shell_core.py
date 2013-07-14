import traceback
from cmd3.shell import command

import os
import sys


class shell_core:

    def info_shell_core(self):
        self.get_version()
        print "%20s = " % "VERSION", self.__version__

    def version(self):
        self.get_version()
        return self.__version__

    def get_version(self):
        import pkg_resources  # part of setuptools
        self.__version__ = pkg_resources.require("cmd3")[0].version

    def do_version(self, args):
        """
        Usage:
           version

        Prints out the version number
        """
        self.get_version()
        print self.__version__

    def activate_shell_core(self):
        self._hist = []

    def do_EOF(self, args):
        """
        Usage:
            EOF

        Action to be performed at the` end of a file. If true it terminates reating the file.
        """
        return True

    def do_quit(self, args):
        """
        Usage:
            quit

        Action to be performed whne quit is typed
        """
        sys.exit()

    do_q = do_quit

    def emptyline(self):
        return

    def cmdloop(self, intro=None):
        """Repeatedly issue a prompt, accept input, parse an initial prefix
        off the received input, and dispatch to action methods, passing them
        the remainder of the line as argument.
        """
        self.preloop()
        if self.use_rawinput and self.completekey:
            try:
                import readline
                self.old_completer = readline.get_completer()
                readline.set_completer(self.complete)
                readline.parse_and_bind(self.completekey + ": complete")
            except ImportError:
                pass
        try:
            if intro is not None:
                self.intro = intro
            if self.intro:
                self.stdout.write(str(self.intro) + "\n")
            stop = None
            while not stop:
                if self.cmdqueue:
                    line = self.cmdqueue.pop(0)
                else:
                    if self.use_rawinput:
                        try:
                            line = raw_input(self.prompt)
                        except EOFError:
                            line = 'EOF'
                    else:
                        self.stdout.write(self.prompt)
                        self.stdout.flush()
                        line = self.stdin.readline()
                        if not len(line):
                            line = 'EOF'
                        else:
                            line = line.rstrip('\r\n')
                line = self.precmd(line)
                stop = self.onecmd(line)
                stop = self.postcmd(stop, line)
            self.postloop()
        finally:
            if self.use_rawinput and self.completekey:
                try:
                    import readline
                    readline.set_completer(self.old_completer)
                except ImportError:
                    pass

    def do_exec(self, filename):
        """Execute script file"""
        if not filename:
            return

        if os.path.exists(filename):
            with open(filename, "r") as f:
                for line in f:
                    print ">", line
                    self.onecmd(line)
        else:
            print '"%s" file does not exist.' % filename
            sys.exit()
