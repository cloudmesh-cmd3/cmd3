.. raw:: html

 <a href="https://github.com/futuregrid/flask_cm"
     class="visible-desktop"><img
    style="position: absolute; top: 40px; right: 0; border: 0;"
    src="https://s3.amazonaws.com/github/ribbons/forkme_right_gray_6d6d6d.png"
    alt="Fork me on GitHub"></a>


.. raw: html

  <div class="hero-unit">
  <h1>Hello, world!</h1>
  <p>This is a template for a simple marketing or informational website. It includes a large callout called the hero unit and three supporting pieces of content. Use it as a starting point to create something more unique.</p>
  <p><a href="#" class="btn btn-primary btn-large">Learn more &raquo;</a></p>
  </div>



Cmd3
======================================================================

.. sidebar:: Table of contents

  .. toctree::
     :maxdepth: -1

     contact
     manual
     todo
     modules/modules.rst

Python has provided for a long time a very useful framework for
creating simple command line shells via Cmd. Other projects have made
use of them and extended it in various ways such as Cmd2. Although
these tools are great, we found several features missing from them to
make them more usable for our projects. Two of the main
features we needed were a mechanism to add plugins via a plugin
directory and a better automatic option parsing while at the same time
automatically generating the help messages from them. While our
developers used optparse and argparse for this we found that the
resulting code not necessarily lead to a proper documentation based on
the complexity involved with dealing with the right syntactic layout
using the parsers. Instead we decided to use docopt for our parsing
that makes it possible to create the documentation in a single easy to
write docstring and accessing them from our methods to create a data
structure that simplifies the creation of writing programs using the
information passed to the functions. In addition we also introduced a
scope that allows us to save some typing while all commands executed
in a scope will be preceded by the scope name. We also have
introduced simple variable substitution based on variable names that
follow the syntax $variable.

Here is a list of features that we found important:

* command are loaded from plugin directories 
* usage of docopts as part of the command creation
* variable substitution
* execution of python commands
* scripts loadable from a script directory

   
Indices and tables
======================================================================

:ref:`genindex`
:ref:`modindex`
:ref:`search`

Modules
======================================================================
