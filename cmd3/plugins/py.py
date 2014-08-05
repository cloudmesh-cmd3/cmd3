from cmd3.shell import command
from code import InteractiveConsole, InteractiveInterpreter
import sys
""" This code has been copied and modified from cmd2 to work with cmd3"""


class EmbeddedConsoleExit(SystemExit):
    pass


class Statekeeper(object):

    def __init__(self, obj, attribs):
        self.obj = obj
        self.attribs = attribs
        if self.obj:
            self.save()

    def save(self):
        for attrib in self.attribs:
            setattr(self, attrib, getattr(self.obj, attrib))

    def restore(self):
        if self.obj:
            for attrib in self.attribs:
                setattr(self.obj, attrib, getattr(self, attrib))


class py:

    pystate = {}
    locals_in_py = True

    def activate_py(self):
        self.locals_in_py = True
        self.pystate['self'] = self
        pass

    def do_py(self, arg):
        '''
        ::

            Usage:
                py
                py COMMAND

            Arguments:
                COMMAND   the command to be executed

            Description:

                The command without a parameter will be extecuted and the
                interactive python mode is entered. The python mode can be
                ended with ``Ctrl-D`` (Unix) / ``Ctrl-Z`` (Windows),
                ``quit()``,'`exit()``. Non-python commands can be issued with
                ``cmd("your command")``.  If the python code is located in an
                external file it can be run with ``run("filename.py")``.

                In case a COMMAND is provided it will be executed and the
                python interpreter will return to the commandshell.

                This code is copied from Cmd2.
        '''
        self.pystate['self'] = self
        arg = arg.strip()
        localvars = (self.locals_in_py and self.pystate) or {}
        interp = InteractiveConsole(locals=localvars)
        interp.runcode('import sys, os;sys.path.insert(0, os.getcwd())')
        if arg:
            interp.runcode(arg)
        else:
            def quit():
                raise EmbeddedConsoleExit

            def onecmd(arg):
                return self.onecmd(arg + '\n')

            def run(arg):
                try:
                    file = open(arg)
                    interp.runcode(file.read())
                    file.close()
                except IOError, e:
                    self.perror(e)
            self.pystate['quit'] = quit
            self.pystate['exit'] = quit
            self.pystate['cmd'] = onecmd
            self.pystate['run'] = run
            try:
                cprt = 'Type "help", "copyright", "credits" or "license" for more information.'
                keepstate = Statekeeper(sys, ('stdin', 'stdout'))
                sys.stdout = self.stdout
                sys.stdin = self.stdin
                interp.interact(banner="Python %s on %s\n%s\n(%s)\n%s" %
                               (sys.version, sys.platform, cprt, self.__class__.__name__, self.do_py.__doc__))
            except EmbeddedConsoleExit:
                pass
            keepstate.restore()
