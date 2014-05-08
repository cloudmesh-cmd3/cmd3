import sys


class activate:

    plugins = []

    def activate_activate(self):
        """activate the activation method"""
        plugins = []

    def do_plugins(self, args):
        """
        Usage:
            plugins

        activates the plugins."""
        self.activate()

    def activate(self):
        """method to activate all activation methods in the shell and
        its plugins.
        """
        d = dir(self)
        self.plugins = []
        for key in d:
            if key.startswith("shell_activate_"):
                if self.echo:
                    print "Shell Activate:", key
                self.plugins.append(key)
        for key in d:
            if key.startswith("activate_"):
                if self.echo:
                    print "Activate:", key            
                self.plugins.append(key)

        for key in self.plugins:
            if self.echo:
               print "> %s" % key.replace("_", " ", 1)
            exec("self.%s()" % key)
