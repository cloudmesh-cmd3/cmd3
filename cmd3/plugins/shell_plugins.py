from cmd3.shell import command
from cmd3.console import Console
from cmd3.setup_management import setup_management

class shell_plugins:

    # Not needed as we moved this to cmd3
    #
    # def activate_shell_plugins(self):
    #    self.register_command_topic('cmd3', 'plugins')
    #    self.register_command_topic('cmd3', 'setup')

    @command
    def do_setup(self, arg, arguments):
        """
        ::
            Usage:
              setup init [--force]
              setup test

            Copies a cmd3.yaml file into ~/.cloudmesh/cmd3.yaml
        """
        if arguments["test"]:
            Console.ok("test")
        elif arguments["init"]:
            Console.ok("init")

            from cmd3.yaml_setup import create_cmd3_yaml_file
            force = arguments["--force"]
            create_cmd3_yaml_file(force=force)

    @command
    def do_plugins(self, args, arguments):
        """
        ::

            Usage:
                plugins add COMMAND [--dryrun] [-q]
                plugins delete COMMAND [--dryrun] [-q]
                plugins list [--output=FORMAT] [-q]
                plugins activate

            Arguments:

                FORMAT   format is either yaml, json, or list [default=yaml]

            Options:

                -q        stands for quiet and suppresses additional messages

            Description:

                Please note that adding and deleting plugins requires restarting
                cm to activate them

                plugins list

                    lists the plugins in the yaml file

                plugins add COMMAND
                plugins delete COMMAND

                    cmd3 contains a ~/.cloudmesh/cmd3.yaml file.
                    This command will add/delete a plugin for a given command
                    that has been generated with cm-generate-command
                    To the yaml this command will add to the modules

                        - cloudmesh_COMMAND.plugins

                    where COMMAND is the name of the command. In case we add
                    a command and the command is out commented the comment
                    will be removed so the command is enabled.

                plugins activate

                    NOT YET SUPPORTED.

            Example:

                plugins add pbs
        """
        # pprint(arguments)

        quiet = arguments["-q"]

        if arguments["activate"]:

            Console.error("this method is not yet supported.")
            self.activate()

        elif arguments["list"]:

            if arguments["--output"] == "yaml":
                plugins_object = setup_management(quiet=quiet)
                print(plugins_object.config.yaml())
            elif arguments["--output"] == "json":
                plugins_object = setup_management(quiet=quiet)
                print(plugins_object.config)
            elif arguments["--output"] == "list":
                plugins_object = setup_management(quiet=quiet)
                print(plugins_object.config["cmd3"]["modules"])
            if arguments["--output"] is None:
                plugins_object = setup_management(quiet=quiet)
                print(plugins_object)

        elif arguments["add"]:

            plugins_object = setup_management()
            plugins_object.add(arguments["COMMAND"],
                               dryrun=arguments["--dryrun"])


        elif arguments["delete"]:

            plugins_object = setup_management()
            plugins_object.delete(arguments["COMMAND"],
                               dryrun=arguments["--dryrun"])

        else:
            Console.error("unknown option.")

