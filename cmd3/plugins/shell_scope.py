import datetime
import os

from cmd3.shell import command
from cmd3.console import Console

# noinspection PyUnusedLocal
class shell_scope:

    echo = True
    active_scope = ""
    scopes = []
    # scopeless = ['info', 'var', 'use', 'quit', 'q', 'EOF', 'eof', 'help']
    scopeless = ['info', 'var', 'use', 'quit', 'q', 'help']
    prompt = 'cm> '
    variables = {}

    #
    # init
    #

    def info_shell_scope(self):
        """prints some information about the shell scope"""
        Console.ok("{:>20} = {:}".format("ECHO", self.echo))
        Console.ok("{:>20} = {:}".format("SCOPE", self.active_scope))
        Console.ok("{:>20} = {:}".format("SCOPES", self.scopes))
        Console.ok("{:>20} = {:}".format("SCOPELESS", self.scopeless))
        Console.ok("{:>20} = {:}".format("prompt", self.prompt))
        Console.ok("{:>20} = {:}".format("scripts", self.scripts))
        Console.ok("{:>20} = {:}".format("variables", self.variables))

    def activate_shell_scope(self):
        """activates the shell scope"""
        self.variables = {}
        self.prompt = 'cm> '
        self.active_scope = ""
        self.scopes = []
        self.scopeless = ['load', 'info', 'var', 'use', 'quit', 'q', 'help']
        # self.scopeless = ['use', 'quit', 'q', 'EOF', 'eof', 'help']

    def do_EOF(self, args):
        """end of file"""
        return True

    #
    # Scope and use commands
    #

    def _add_scopeless(self, name):
        self.scopeless.append(name)

    def _delete_scopeless(self, name):
        self.scopeless.remove(name)

    def _add_scope(self, name):
        self.scopes.append(name)

    def _delete_scope(self, name):
        self.scopes.remove(name)

    def _list_scope(self):
        Console.ok(10 * "-")
        Console.ok('Scope')
        Console.ok(10 * "-")
        for s in self.scopes:
            Console.ok(str(s))

        Console.ok(10 * "-")
        Console.ok('Scopeles')
        Console.ok(10 * "-")
        for s in self.scopeless:
            Console.ok(str(s))

    def do_use(self, arg):
        """
        ::
        
            USAGE:

                use list           lists the available scopes

                use add SCOPE      adds a scope <scope>

                use delete SCOPE   removes the <scope>

                use                without parameters allows an
                                   interactive selection

            DESCRIPTION
               Often we have to type in a command multiple times. To save
               us typng the name of the command, we have defined a simple
               scope that can be activated with the use command

            ARGUMENTS:
                list         list the available scopes
                add          add a scope with a name
                delete       delete a named scope
                use          activate a scope

            """
        if arg == 'list':
            self._list_scope()
            return
        elif arg.startswith('add'):
            new_scope = arg.split(' ')[1]
            self._add_scope(new_scope)
            return
        elif arg.startswith('delete'):
            # delete does not work
            which_scope = arg.split(' ')[1]
            self._delete_scope(which_scope)
            return
        elif arg == "cm" or arg == "/":
            self.active_scope = ""
        elif arg in self.scopes:
            self.active_scope = arg
        else:
            self.active_scope = self.select(
                [""] + self.scopes, 'Which scope? ')

        if self.active_scope == "":
            Console.ok("Switched scope to: cm")
            self.prompt = self.active_scope + 'cm> '
        else:
            Console.ok("Switched scope to: {0}".format(self.active_scope))
            self.prompt = self.active_scope + '> '

    #
    # emptyline
    #
    def emptyline(self):
        return

    #
    # replace vars
    #

    def update_time(self):
        time = datetime.datetime.now().strftime("%H:%M:%S")
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        self.variables['time'] = time
        self.variables['date'] = date

    #
    # line handler
    #
    forblock = False
    block = []
    forstatement = ""

    def precmd(self, line):
        if line is None or line == "":
            return ""

        if line.startswith("#"):
            Console._print("BLUE", "", line)
            return ""

        line = self.replace_vars(line)

        #
        # handeling for loops
        #
        if self.forblock is True and line.startswith(" "):
            self.block.append(line)
            # add line to block
        elif self.forblock is True:
            print ">>>> EXECUTE LOOP"
            print self.forstatement
            print self.forblock
            print self.block
            self.forblock = False

            (loopvar, values) = self.forstatement.split('in')
            loopvar = loopvar.replace("for", "").replace(" ", "")
            values = values.replace("[", "").replace("]", "").replace(" ", "")
            values = values.split(",")
            print values
            for v in values:
                self.do_var("%s=%s" % (loopvar, v))
                for l in self.block:
                    l = self.replace_vars(l)
                    self.precmd(l)
                    self.onecmd(l)

        if line.startswith("for"):
            self.forblock = True
            self.forstatement = line
            self.block = []
        #
        # history
        #

        if line != "hist" and line:
            self._hist += [line.strip()]

        #
        # strip
        #

        line = line.strip()
        if line == "":
            print
            return line

        #
        # scopes
        #
        try:
            (start, rest) = line.split(" ")
        except:
            start = line

        if (start in self.scopeless) or (self.active_scope == ""):
            line = line
        else:
            line = self.active_scope + " " + line

        #
        # echo
        #

        if self.echo:
            Console.ok(str(line))

        return line

    #
    # Echo
    #
    def set_verbose(self, on):
        self.echo = on

    def set_banner(self, banner):
        self.banner = banner

    @command
    def do_verbose(self, args, arguments):
        """
        Usage:
            verbose (True | False)
            verbose

        If it sets to True, a command will be printed before execution.
        In the interactive mode, you may want to set it to False.
        When you use scripts, we recommend to set it to True.

        The default is set to False

        If verbose is specified without parameter the flag is
        toggled.
        
        """
        if args == '':
            self.echo = not self.echo
        else:
            self.echo = arguments['True']

    #
    # VAR
    #
    def replace_vars(self, line):

        self.update_time()

        newline = line
        for v in self.variables:
            newline = newline.replace("$" + v, self.variables[v])
        for v in os.environ:
            newline = newline.replace("$" + v, os.environ[v])
        return newline

    def _add_variable(self, name, value):
        self.variables[name] = value
        # self._list_variables()

    def _delete_variable(self, name):
        self._list_variables()
        del self.variables[name]
        # self._list_variables()

    def _list_variables(self):
        Console.ok(10 * "-")
        Console.ok('Variables')
        Console.ok(10 * "-")
        for v in self.variables:
            Console.ok("{:} = {:}".format(v, self.variables[v]))

    @command
    def do_var(self, arg, arguments):
        """
        Usage:
            var list 
            var delete NAMES
            var NAME=VALUE
            var NAME

        Arguments:
            NAME    Name of the variable
            NAMES   Names of the variable separated by spaces
            VALUE   VALUE to be assigned

        special vars date and time are defined
        """
        if arg == 'list' or arg == '' or arg is None:
            self._list_variables()
            return

        elif '=' in arg:
            (variable, value) = arg.split('=', 1)
            if value == "time":
                value = datetime.datetime.now().strftime("%H:%M:%S")
            elif value == "date":
                value = datetime.datetime.now().strftime("%Y-%m-%d")
            self._add_variable(variable, value)
            return
        elif '=' not in arg and arguments['NAME=VALUE'] is not None:
            try:
                v = arguments['NAME=VALUE']
                Console.ok(str(self.variables[v]))
            except:
                Console.error('variable {:} not defined'.format(arguments['NAME=VALUE']))
            
        elif arg.startswith('delete'):
            variable = arg.split(' ')[1]
            self._delete_variable(variable)
            return
