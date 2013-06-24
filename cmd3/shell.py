#! /usr/bin/env python
"""
This project is about developing a dynamic CMD class based on cmd.CMD. 
We assume the following directory structure::

  ./shell.py
  ./dynamic_cmd.py
  ./plugins/foo.py 
  ./plugins/bar.py 
  ./plugins/activate.py 

We have provided examples of the classes in this document

foo and bar contain some classes that include he usual do_ methods. It
also includes an activate method that is called wih the acivation
module, so you can control its behavior upon startup.

To specify the plugins please use::

  plugins = ["foo", "bar","activate"]

Now you can set a name for your class::

  name = "CmCLI"

The rest is pretty simple::

  (cmd, plugin_objects) = DynamicCmd(name, plugins)
  cmd.activate(plugin_objects)
  cmd.cmdloop()

The activate method is not called automatically as to give more
flexibility during startup.

Here are the sample classes::

   class bar:

       def activate_bar(self):
           print "... activate bar"

       def do_that(self, arg):
           print "THAT", arg


   class foo:

       def do_this(self, arg):
           print "THIS", arg
           self.activate_status()  

       def activate_foo(self):
           print "... activate foo"

   class activate:

       active = False

       def do_on(self, arg):
           self.active = True
           self.activate_status()

       def do_off(self, arg):
           self.active = False
           self.activate_status()

       def activate_status(self):
           print "Active:", self.active

       def activate(self, plugins):
           d = dir(self)
           result = []
           for key in d:
               if key.startswith("activate_"):
                   result.append(key)
           print result
           for key in result:
               print "> %s" % key.replace("_"," ")
               exec("self.%s()" % key)
"""

import sys
import cmd
import readline
import glob
import os
import getopt

from cmd3.dynamic_cmd import load_plugins
from cmd3.dynamic_cmd import make_cmd_class
from cmd3.dynamic_cmd import DynamicCmd
from cmd3.dynamic_cmd import get_plugins

def main():
  """
  
  """

  try:
    opts, args = getopt.getopt(sys.argv[1:],
                                "hif:",
                                ["help", "interactive", "file="])
  except getopt.GetoptError:
    usage()
    sys.exit(2)
  script_file = None
  interactive = False
  for option, argument in opts:
    if option in ("-h", "--help"):
      usage()
      sys.exit()
    if option in ("-f", "--file"):
      script_file = argument
    if option in ("-i", "--interactive"):
      interactive = True

  plugin_path = os.path.join(os.path.dirname(__file__),'plugins')

  plugins = get_plugins(plugin_path)

  name    = "CmCli"
  
  (cmd, plugin_objects) = DynamicCmd(name, plugins)
  cmd.version()
  cmd.activate()
  cmd.do_exec(script_file)

  if is_subcmd(opts, args):
    try:
      user_cmd = " ".join(args)
      print ">", user_cmd
      cmd.onecmd(user_cmd)
    except:
      print "'%s' is not recognized" % user_cmd
  elif not script_file or interactive:
    cmd.cmdloop()

def is_subcmd(opts, args):
    """if sys.argv[1:] does not match any getopt options, 
    we simply assume it is a sub command to execute onecmd()"""

    if not opts and args:
      return True
    return False

def usage():
    """Usage of cmd3"""
    
    print "Usage: $ cm"
    print
    print " $ echo \"help\" | cm"
    print
    print " $ cm -f file"
    print
    print " $ cm -f file -i"
    print

if __name__ == "__main__":
  main()


"""
bash$ echo "help" | shell.py > output.txt

stupid example: shell.py metric analyze -y 2013

/trunk/cog-shell/src/cogkit/Shell/CoGCli.py?revision=3648&view=markup


386def runCLI(filename=None, silent=False, interactive=False):
387    if filename == None:
388        cli = CogShell(silent)
389        cli.cmdloop()
390    else:
391        cli = CogShell(silent=True)
392        cli.do_exec(filename)
393        if interactive:
394            cli.cmdloop()
395


example form cogkit, but use docopts for the new version 
def main():
46    try:
47        opts, args = getopt.getopt(sys.argv[1:],   #IGNORE:W0612
48                                   "hqif:",
49                                   ["help", "quiet", "interactive", "file="])
50    except getopt.GetoptError:
51        # print help information and exit:
52        usage()
53        sys.exit(2)
54
55    script_file = None
56    quiet = None
57    interactive = None
58    for option, argument in opts:
59        if option in ("-h", "--help"):
60            usage()
61            sys.exit()
62        if option in ("-f", "--file"):
63            script_file = argument
64        if option in ("-q", "--quiet"):
65            quiet = True
66        if option in ("-i", "--interactive"):
67            interactive = True
68
69    cogkit.Shell.CoGCli.runCLI(script_file, quiet, interactive)
"""
