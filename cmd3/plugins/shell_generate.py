from cmd3.shell import command
from cmd3.generate import generate_command

class shell_generate:

    # Not needed as we moved this to cmd3
    #
    # def activate_shell_generate(self):
    #    self.register_command_topic('cmd3', 'command')

    @command
    def do_generate(self, args, arguments):
        """
        ::

            Usage:
                generate command COMMAND [--path=PATH] [--topic=TOPIC]

            the command will generate the package and code for a sample cmd3 module.

            Arguments:

                COMMAND   the name of the command.

                PATH      path where to place the directory [default: ~]

                TOPIC     the topic listed in cm [default: mycommands]

            Options:
                 -v       verbose mode

            Example:

                The command

                    generate command example

                would create in the home directory  the following files

                    ├── LICENSE
                    ├── Makefile
                    ├── __init__.py
                    ├── __init__.pyc
                    ├── cloudmesh_example
                    │   ├── __init__.py
                    │   ├── command_example.py
                    │   └── plugins
                    │       ├── __init__.py
                    │       └── cm_shell_example.py
                    ├── requirements.txt
                    ├── setup.cfg
                    └── setup.py

                To install the plugin go to the directory and say

                    python setup.py install

                Next register it in cm with

                    cm plugins add cloudmesh_example

                Now say

                    cm help

                and you see the command example in cm.
                To modify the command, yous change the docopts and the logic in
                cm_shell_example.py and command_example.py


        """
        if arguments["command"]:
            generate_command(
                command=arguments["COMMAND"],
                path=arguments["--path"],
                topic=arguments["--topic"],
                )
        pass