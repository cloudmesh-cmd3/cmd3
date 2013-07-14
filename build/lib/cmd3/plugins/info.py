from cmd3.shell import command


class info:

    def print_info(self):
        d = dir(self)
        self.plugins = []
        for key in d:
            if key.startswith("info_"):
                self.plugins.append(key)

        for key in self.plugins:
            if self.verbose:
                print "> %s" % key.replace("_", " ", 1)
            exec("self.%s()" % key)

    @command
    def do_info(self, arg, arguments):
        """
        Usage:
               info

        Prints some internal information about the shell

        """
        print 70 * "-"
        print 'DIR'
        print 70 * "-"
        for element in dir(self):
            print element
        print 70 * "-"
        self.print_info()
