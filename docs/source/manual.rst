.. raw:: html

 <a href="https://github.com/cloudmesh/cmd3"
     class="visible-desktop"><img
    style="position: absolute; top: 40px; right: 0; border: 0;"
    src="https://s3.amazonaws.com/github/ribbons/forkme_right_gray_6d6d6d.png"
    alt="Fork me on GitHub"></a>


.. raw: html


Manual
======================================================================

Gregor von Laszewski, laszewski@gmail.com

.. sidebar:: 
   . 

  .. contents:: Table of Contents
     :depth: 5

..

Documentation
----------------------------------------------------------------------

The documentation of cmd3 is maintained at 

* http://cloudmesh.github.com/cmd3/

Installation
----------------------------------------------------------------------

Install from Pypi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   
   pip install cmd3


.. note:: dut to some current issues in pip, you will need to do the
	  following steps::
   
	    pip --trusted-host pypi.python.org install cloudmesh_base	
	    pip --trusted-host pypi.python.org install cmd3

	  Make sure cm is installed and works with::

	    cm help

	  If you have not yet set up a cmd3.yaml file in ~/.cloudmesh
	  you can do this with::

	     cm setup-yaml

   
Install from Source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend that you use virtual env for installing this package, but
you can naturally also install it in other ways. To use virtual env
you may consult with its manual. We assume we create a virtual env
called CMD3::

   virtualenv ~/CMD3
   ~/CMD3/bin/activate

Next you need to get the source code from git as follows and conduct
the installation

::

   git clone git@github.com:cloudmesh/cmd3.git
   cd cmd3
   python setup.py install

Install the cmd3 Configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cloudmesh is configured with a configuration file in the yaml
format. Please place this file in::

  ~/.cloudmesh/cmd3.yaml

This file specifies which modules are imported in addition to the
default locations for the plugins.

An example file is located at:

* https://github.com/cloudmesh/cmd3/blob/master/etc/cmd3.yaml

and looks as follows::

    meta:
	yaml_version: 2.1
	kind: cmd3
	filename: ${HOME}/.cloudmesh/cmd3.yaml
	location: ${HOME}/.cloudmesh/cmd3.yaml
	prefix: null
    cmd3:
	modules:
	- cloudmesh_cmd3.plugins
	- cloudmesh_docker.plugins
	- cloudmesh_slurm.plugins
	- cloudmesh_deploy.plugins

In the modules attribute you can add new plugin modules following the
cmd3 specification. This has the advantage that you do not have to
worry about the path as it is taken from a local deployed version.
	  
Running the installed version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now you are ready to run the shell with the command::

  cm

Which will give you something like this::
  
  ======================================================
     ____ _                 _                     _     
    / ___| | ___  _   _  __| |_ __ ___   ___  ___| |__  
   | |   | |/ _ \| | | |/ _` | '_ ` _ \ / _ \/ __| '_ \ 
   | |___| | (_) | |_| | (_| | | | | | |  __/\__ \ | | |
    \____|_|\___/ \__,_|\__,_|_| |_| |_|\___||___/_| |_|
  ======================================================
		       Cloudmesh Shell

  cm> 

It first prints the plugins that it found, loads them and than starts
the shell. As we use the shell to develop a much larger shell for
clouds (which we call cloudmesh) you will see a welcome
message. Cloudmesh is available on github at
https://github.com/cloudmesh/cmd3. Please note that cloudmesh is under
development and you can actively help us while joining the cloudmesh
project.

Running from the Source Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This will install you code in to the site-packages directory. If you
do not want to install the package, you can also go into src/cmd3
where you can find the shell.py program. Now you can alternatively
start it with::

  python shell.py



Using the Shell
----------------------------------------------------------------------

.. todo:: using the shell

The shell is easy to use and you can get started by exploring the
available commands simply by saying::

  help

It will list you a number of commands that are available to you. some
of them will be located in your plugin directories where you can place
additional plugins. Upon start of cmd3 the plugins will be reread and
all of them, including new once, will be available to you.

Extending the Shell
----------------------------------------------------------------------

CMD3 allows you to extend the commands provided in via plugin directories. 
We assume the following directory structure::

  ./shell.py
  ./plugins/foo.py 
  ./plugins/bar.py 
  ./plugins/activate.py 
 
   ... other dirs and file ...

We provide a simple example of how to write and add new classes via
the plugin directory in this manual.

Let us assume that `foo` and `bar` contain some classes that include
the usual do_ methods yo may know from cmd. However in addition to the
do_ method it also includes an activate method that is called with the
activation module, so you can control its behavior upon startup. This
is similar to an __init__ method, but we decided not to name them
__init__ in order to highlight that they are called only at the
activation of the plugin.

To specify the plugins please use in the shell.py code::

  plugins = ["foo", "bar","activate"]

Now you can set a name for your class::

  name = "CmCLI"

The rest is pretty simple::

  (cmd, plugin_objects) = DynamicCmd(name, plugins)
  cmd.activate(plugin_objects)
  cmd.cmdloop()


Many times you may want to provide some better location for your
plugins such as system wide installed plugins, or plugins maintained
in your user environment rather than the current path. For this reason
we provide the following examples.

Reading plugins from your local instalation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We assume you have placed a plugin directory at
"~/.cloudmesh/cmd3local/". Than you simply can read the plugins by ::

  plugin_path = os.path.expanduser("~/.cloudmesh/cmd3local/")

  plugins = get_plugins(plugin_path)

Naturally you can have other plugin directories. In fact we will be
expanding our plugin module called plugin so users could add their own
plugin directories on demand.


Reading plugins from the deploy directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assume you like to load the plugins from the deployed cmd3, this can
be done easily while looking at the code for shell.py::

  plugin_path = os.path.join(os.path.dirname(__file__),'plugins')

  plugins = get_plugins(plugin_path)

Writing Plugins
----------------------------------------------------------------------

Plugins are very simple to design and write. However we have to be
aware of several facts. First, if you design a method with the same
name within two different plugins, the method from the last loaded
plugin will overwrite the previous method. This is the intended
behavior as to allow for easy extensions to be put in place and
overwrite default behavior. However, you need to be careful as not to
confuse yourself by properly ordering the plugins upon load loaded.
In addition we have on purpose not used an __init__ method in the
class but instead used an activate method to indicate that we like in
future to activate and deactivate certain plugins.

A Basic Plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is the sample class from the file plugins/foo.py::

   class foo:

       def activate_foo(self):
           print "... activate foo"

       def do_foo(self, arg):
           print "I am Foo", arg

Now place this module in your plugins directory and you are all
set. when you start the shell and say::

  foo bar

It will print::

  I am Foo bar
   
This does not seem much different from the original cmd, an in fact it
is not. The only difference so far is the introduction of the plugins
directory. Thus instead of changing my shell.py program, adding
inheritance or other mechanisms and making sure I invoke the right
__init__ methods, all this is not needed here.

This has advantages and disadvantages and you may judge for yourself,
if you like to use a plugin or an inheritance mode.

Argument parsing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of the important differentiation to the original cmd is how we are
handeling documentation. Although it is possible to use just the same
mechanism as in cmd, Cmd3 also allows the use of docopts. This has the
advantage that we can very quickly design prototypes of commands with
nice option parsing based on the documentation that is provided with
the method as documented at http://docopt.org.

So let us create a new plugin called bar::

   from cmd3.cyberaide.decorators import command

   class bar:

       def activate_bar(self):
           print "... activate bar"

       @command
       def do_bar(self, arg, arguments):
           """Usage:
                   bar -f FILE
                   bar FILE
                   bar list

            This command does some useful things.

            Arguments:
                  FILE   a file name

            Options:
                  -f      specify the file

            Example:
	        bar filename

		     executes the bar command with the given filename
		     
            print arguments

Please note the differences to our previous class. We have introduced a
decorator that transforms the do_bar method into a method that returns
an additional parameter called arguments. This is the arguments dict
that is created by `docopt` and allows for some very convenient
introduction of handling the parameters, arguments, and options.  If
you like to find more out about docopts please visit the `website`_ ,
which also includes some nice `examples`_ to show the use of docopt in
python.



Generating Information  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Often it is good to provide some summary information about a module
that you have installed. As each package may have such information we
have implemented the `info` command that prints out all information from
all modules if available

So let us enhance the previous plugin while adding an information::

   from cmd3.cyberaide.decorators import command

   class bar:

       def activate_bar(self):
           print "... activate bar"

       def info_bar(self):
           print "information for the class bar"

       @command
       def do_bar(self, arg, arguments):
           """Usage:
                   bar -f FILE
                   bar FILE
                   bar list

            This command does some useful things.

            Arguments:
                  FILE   a file name

            Options:
                  -f      specify the file

            Example:

	            bar filename

		        executes the bar command with the given filename

            """
            print arguments

When you call the command::

     cm> info 

from the cm command it will execute the info method fo the class bar.

.. _website: https://github.com/docopt
.. _examples: https://github.com/docopt/docopt/tree/master/examples


Function Registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes you have already developed a function with docopts and
instead of redeveloping it you may just want to add it. Although we
could just register the function it is beneficial for us to use our
plugin and class concept to organize such a command.  Hence we have
developed a very convenient function_command decorator, that accepts
an external function so you can integrate it trivially into the
shell. After these many words, we demonstrate this through
the following program.  In this example the command fbar will inherit
the documentation form the function main_func and will also execute
it.

.. include:: ../../cmd3/examples/fbar.py
   :literal: 

This has also the advantage that you could make the main_func
available through a python main section so you could also run it directly
on the commandline. This will simplify debugging of the main_func as
certain debug checks are switched of when it is run through the command
shell. Just make sure that you parse the arguments in docpots before
you call the main_func::

  def main():
      arguments = docopt(main_func.__doc__)
      main_func(arguments)

  if __name__ == '__main__':
      main()

Generating independent packages
----------------------------

Often you may want to generate your own extensions, but like to
maintain them in a separate module. We have provided a command with
cmd3 that creates from a template a new module including a directory
structure and setup.py files. Thus once you create such a module, ypu
can cd into it and install it just as any other python package.

Let us walk through how to do this in more detail. The command to
create such a module is called `cm-generate-command`. It uses a
template that is installed in the directory::

  ~/.cloudmesh/cmd3_template

You can obtain the manual page by just typing::

  $ cm-generate-command

Let us assume you like to create a command called `uebercool` to be
included in cmd3. This can be achieved with a very small number of steps.

First, call the command::

  cm-generate-command uebercool --path=~

This will generate a a cloudmesh command module in your home
directory. be careful that there is no such module already as the
current version deletes the existing directory. 

You will now have created a python module at::

    ~/cloudmesh_uebercool

You can install it simply with::

    cd ~/cloudmesh_uebercool
    python setup.py install

Now you have installed the example into your environment. However you
need to still register this new package with cmd3. This is easy as you
can place the following filr into the directory::

    ~/.cloudmesh/cmd3.yaml

  ::
    meta:
	yaml_version: 2.1
	kind: cmd3
	filename: ${HOME}/.cloudmesh/cmd3.yaml
	location: ${HOME}/.cloudmesh/cmd3.yaml
	prefix: cmd3
    cmd3:
	modules:
	- cloudmesh_cmd3.plugins
	- cloudmesh_uebercool.plugins

Make sure the yaml file does not have any tabs in it.

Now you can start cmd3 with::

  cm

and issue the command::

  help

You should be able to see the new command. 

To start it you simply say::

 cm>  uebercool iu.edu
 
to run it directly from commandline you can use::

  cm uebercool iu.edu

The template simply executes a ping that is defined in the source
`command_uebercool.py`. If youlike to modify the command just change
the code in the plugins and the command files.

Yes its that simple!

If you have written extensions with cmd3 let us know we could discuss
the creation of user contributed space in the cmd3 git reporsitory. We
like to host your extensions.





Build In Commands
----------------------------------------------------------------------

Help
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One other good feature the above declaration has is that it
automatically registers a help string so you can say::

   help bar

and you will get presented with the manual page

Manual Pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Often you will run in the situation where you may have to create a
list of manual pages for your commands for your users. To simplify
that we have not provided this in Unix Man format, but simply in RST
format. You can type in the command::

  man

and it will print you in RST format a list of all commands available
to you for your cmd3 shell. This naturally you could put into a sphinx
documentation to create a nice user manual for your users.


Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CMD3 contains the ability to use variables within the shell. To see a
list of all variables, use the command::

  var list

or simply::

  var

To use the content of the variable, simple use it on the shell with a
dollar sign such as::

  $date

Note that the variables $dat and $time are predefined and give the
current date and time.

Scope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Often we have to type in a command multiple times. To save us typing
the name of the command, we have defined a simple scope that can be
activated with the use command.

You can list the scopes by typing::

  use list

To use a scope simply type::

  use

Scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multiple commands can be stored in scripts. To find out more about
scripts, please execute::

  help script

You can use a script that is stored in a file simply by saying::

  script load filename

where filename is the name of the file containing the script.

Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can execute a python command as follows::

  py COMMAND

where command is the command you like to execute

Quitting the shell
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To quit the shell you can use either the commands::

  q
  quit
  EOF




