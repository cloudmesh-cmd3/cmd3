#! /usr/bin/env python
"""
Usage: cm
       cm -h
       cm [-q] [-v] [-f] FILE
       cm [-q] [-v] -i

Description:

   The cloud mesh shell is a simple command line like shell that
   assists in running small numbers of jobs in an interactive
   or script fashion.

Arguments:
  FILE        input file

Options:
  -h --help
  -v       verbose mode
  -q       quiet mode
  -f       specify the file to run

Examples:

   > cm

     starts the cog shell in interactive mode

   > cat file | cm

     pipes the lines in the file to the cog shell and terminates

   > cm -f file

     reads the lines of the files, runs them and terminates

   > cm -f file -i

     executes all lines in file and switches to the interactive mode

"""

from docopt import docopt
import cmd
import string
import sys
import os
import glob
import textwrap

imports = []
add_bases = ()

def importer(regex):
    global imports
    plugins = glob.glob(regex)
    if plugins:
        for filename in plugins:
            filename = filename.replace(".py", "")
            (dir, plugin) = filename.split("/")
            importer_line =  "from %(dir)s.%(plugin)s import %(plugin)s as %(plugin)s" % {"plugin": plugin, "dir": dir}
            imports.append(importer_line)
            print "Loading Plugin:", plugin

importer("plugins/shell_*.py")

for import_line in imports:
    # I am just doing exec and not __import__ for now due to simplicity
    exec(import_line)


#
# no dynamic loading yet
#

class Shell(cmd.Cmd,
            shell_metric,
            shell_opt_example,
            shell_util,
            shell_banner,
            shell_scope):
            

    scopes = ['rain', 'gregor']

    def __init__ (self, silent=False):
        cmd.Cmd.__init__(self)
        self.silent = silent
        # determins if logo should be printed

        sys.exit()

    ######################################################################
    # DO NOT CAHNGE
    ######################################################################

    preloop = shell_banner.preloop

    def preloop(self):
        """Initialization before prompting user for commands.
           Despite the claims in the Cmd documentaion, Cmd.preloop() is not a stub.
        """
        shell_banner.preloop(self)
        cmd.Cmd.preloop(self)   ## sets up command completion
        self._hist    = []      ## No history yet
        self._locals  = {}      ## Initialize execution namespace for user
        self._globals = {}
    
    prompt  = shell_scope.prompt
    precmd  = shell_scope.precmd
    emptyline = shell_scope.emptyline
    
    ######################################################################
    # Info Command
    ######################################################################
    def help_info(self):
        msg = """
        DESCRIPTION

           provides information that is maintained internally in the shell
            
        """
        print textwrap.dedent(msg)

        
    def do_info(self,arg):
        print "%20s =" % "Scripts", str(self.scripts)
        print "%20s =" % "Variables", str(self.variables)
        print "%20s =" % "Echo", str(self.echo)
        print "%20s =" % "Scope", self.scope
        print "%20s =" % "With scope", self.scopes
        print "%20s =" % "No scope", self.scopeless

    ######################################################################
    # Sample Command
    ######################################################################

    def do_gregor(self,arg):
        print "GREGOR", arg

    def do_rain(self,arg):
        print "RAIN ", arg

    def default(self, line):       
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """
        if line.startswith ("for"):
            return
        try:
            exec(line) in self._locals, self._globals
        except Exception, e:
            self.do_shell(line)
            #print e.__class__, ":", e

 ## Command definitions ##
    def do_hist(self, args):
        """Print a list of commands that have been entered"""
        print self._hist

    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!'"""
        os.system(args)

def runCLI(filename=None, silent=False, interactive=False):
    if filename == None:
        cli = Shell(silent)
        cli.cmdloop()
    else:
        cli = Shell(silent=True)
        cli.do_exec(filename)
        if interactive:
            cli.cmdloop()


def main():
    arguments = docopt(__doc__)
    print(arguments)

    
    if arguments["-f"] and arguments['FILE'] != None:
        script_filename = arguments['FILE']
        try:
            with open(script_file): pass
        except IOError:
            print 'Script file "%s" does not exists.' % script_file

    quiet = arguments['-q'] or arguments['q'] != None
    interactive = arguments['-q'] or arguments['q'] != None

    run(script_file, quiet, interactive)

if __name__ == "__main__":
    main()
