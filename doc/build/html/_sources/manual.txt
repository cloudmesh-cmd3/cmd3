.. raw:: html

 <a href="https://github.com/futuregrid/flask_cm"
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

Instalation
----------------------------------------------------------------------

Install form Pypi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: pypi installation

::

   pip install cmd3

Install form Source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend that you use virtual env for installing this package, but
you can naturally also install it in other ways. To use virtual env
you may consult with its manaula. We assume we create a virtual env
called CMD3::

   virtualenv ~/CMD3
   ~/CMD3/bin/activate

Next you need to get the source code from git as follows and conduct
the instalation

::

   git clone git@github.com:futuregrid/cmd3.git
   cd cmd3
   python setup.py install


Running the installed version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now you are ready to run the shell with the command::

  cm

Which will give you something like this::

  > activate activate
  > activate bar
  > activate clear
  > activate edit
  > activate foo
  > activate metric
  > activate opt_example
  > activate pause
  > activate rst
  > activate template

		FutureGrid - Cloud Mesh Shell
  ------------------------------------------------------
     ____ _                 _   __  __           _     
    / ___| | ___  _   _  __| | |  \/  | ___  ___| |__  
   | |   | |/ _ \| | | |/ _` | | |\/| |/ _ \/ __| '_ \ 
   | |___| | (_) | |_| | (_| | | |  | |  __/\__ \ | | |
    \____|_|\___/ \__,_|\__,_| |_|  |_|\___||___/_| |_|
  ======================================================

  cm> 

It first prints the plugin that it found and loads the, and than gets
into the shell. As we use the shell to develop a much larger shell for
clouds, we called it cloud mesh. However cloudmesh is not yet
available for distribution.

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

Extending the Shell
----------------------------------------------------------------------

.. todo:: using the shell

This project is about developing a dynamic CMD class based on cmd.CMD. 
We assume the following directory structure::

  ./shell.py
  ./plugins/foo.py 
  ./plugins/bar.py 
  ./plugins/activate.py 
 
   ... other dirs and file ...

We have provides examples of the classes in this document

foo and bar contain some classes that include he usual do_ methods. It
also includes an activate method that is called with the activation
module, so you can control its behavior upon startup.

To specify the plugins please use::

  plugins = ["foo", "bar","activate"]

Now you can set a name for your class::

  name = "CmCLI"

The rest is pretty simple::

  (cmd, plugin_objects) = DynamicCmd(name, plugins)
  cmd.activate(plugin_objects)
  cmd.cmdloop()


Many times you may want to provide some better location for your
plugins such as system wide installed blugins, or plugins maintained
in your user environment rather than the current path. For this reason we provide the following examples.

Reading plugins from your local instalation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We assume you have placed a plugin directory at
"~/.futuregrid/cmd3/". Than you simply can read the plugins by ::

  plugin_path = os.path.expanduser("~/.futuregrid/cmd3/")

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
aware of several facts. First, if you design a method within two
different plugins, the last loaded plugin will overwrite the previous
method. This is the intended behavior as to allow for easy extensions
to be put in place. However, you need to be careful as not to confuse
yourself by minding the order in which the plugins are loaded.  In
addition we have on purpose not used an __init__ method in the class
but instead used an activate method to indicate that we like in future
to activate and deactivate certain plugins.  

A Basic Plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is the sample classes form the file plugins/foo.py::

   class foo:

       def activate_bar(self):
           print "... activate foo"

       def do_foo(self, arg):
           print "I am Foo", arg

Now place this module in your plugins directory and you are all
set. when you start the shell and say::

  foo bar

It will print::

  I am Foo bar
   
THis does not seem much different from the original cmd, an in fact it
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
the method.

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

            """
            print arguments

Please not the differences to our previous class. We have introduced a
decorator that transforms the do_bar method into a method that returns
an additional parameter called arguments. This is the arguments dict
that is created by docopt. And allows for some very convenient
introduction of handeling the parameters, arguments, and options.  If
you like to find more out about docopts please visit the `website`_ ,
which also includes some nice `examples`_ to show the use of docopt in
python.

.. _website: https://github.com/docopt
.. _examples: https://github.com/docopt/docopt/tree/master/examples

Help
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One other good feature the above declaration has is that it
automatically registers a help string so you can say::

   help bar

and you will get presented with the manual page

