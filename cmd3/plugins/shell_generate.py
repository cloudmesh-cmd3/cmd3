from cmd3.shell import command
from cmd3.generate import generate

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
                generate command COMMAND [PACKAGE] [--path=PATH] [--topic=TOPIC]

            the command will generate the package and code for a sample cmd3 module.

            Arguments:
                PACKAGE   name of the new package. Often this will be cloudmesh_COMMAND
                          which will be used if not specified.

                COMMAND   the name of the command.

                PATH      path where to place the directory [default: .]

                TOPIC     the topic listed in cm [default: mycommands]

            Options:
                 -v       verbose mode

        """

        generate(arguments)
        pass