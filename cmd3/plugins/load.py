from cmd3.shell import command


# noinspection PyUnusedLocal
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
        # try:
        #    plugins.append(dict(get_plugins_from_module(module_name)))
        # except:
        #    #print "WARNING: could not find", module_name
        #    pass
        print module

