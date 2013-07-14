import sys


class activate:

    verbose = True
    plugins = []

    def activate_activate(self):
        self.verbose = True
        plugins = []

    def do_plugins(self, args):
        """
        Ussage:
            plugins

        activates the plugins."""
        self.activate()

    def activate(self):
        d = dir(self)
        self.plugins = []
        for key in d:
            if key.startswith("shell_activate_"):
                self.plugins.append(key)
        for key in d:
            if key.startswith("activate_"):
                self.plugins.append(key)

        for key in self.plugins:
            if self.verbose:
                print "> %s" % key.replace("_", " ", 1)
            exec("self.%s()" % key)
