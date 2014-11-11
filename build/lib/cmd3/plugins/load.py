from cmd3.shell import command


class load:

    def activate_load(self):
        """activates the load command"""
        pass

    @command
    def do_load(self, arg, arguments):
        """
        ::

            Usage:
                load MODULE

            Loads the plugin given a specific module name. The plugin must be ina plugin directory.

            Arguments:
               MODULE  The name of the module.
        """
        module = arguments["MODULE"]
        print module

