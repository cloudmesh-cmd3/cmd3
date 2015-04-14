from cmd3.shell import command
from cmd3.console import Console

# noinspection PyUnusedLocal
class info:

    def print_info(self):
        """prints some info that the user may find useful"""
        
        d = dir(self)
        self.plugins = []
        for key in d:
            if key.startswith("info_"):
                self.plugins.append(key)

        for key in self.plugins:
            if self.echo:
                Console.ok("> {0}".format(key.replace("_", " ", 1)))
            exec("self.%s()" % key)

    @command
    def do_info(self, arg, arguments):
        """
        ::

            Usage:
                   info [--all]

            Options:
                   --all  -a   more extensive information 

            Prints some internal information about the shell

        """
        if arguments["--all"]:
            Console.ok(70 * "-")
            Console.ok('DIR')
            Console.ok(70 * "-")
            for element in dir(self):
                Console.ok(str(element))
            Console.ok(70 * "-")
        self.print_info()
