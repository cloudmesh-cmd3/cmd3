from __future__ import print_function
import os
from cmd3.console import Console
from cmd3.shell import command

from {package}.command_{command} import command_{command}


class cm_shell_{command}:

    def activate_cm_shell_{command}(self):
        self.register_command_topic('{topic}', '{command}')

    @command
    def do_{command}(self, args, arguments):
        """
        ::

          Usage:
              {command} NAME 

          tests via ping if the host ith the give NAME is reachable

          Arguments:

            NAME      Name of the machine to test

          Options:

             -v       verbose mode

        """
        # pprint(arguments)

        if arguments["NAME"] is None:
            Console.error("Please specify a host name")
        else:
            host = arguments["NAME"]
            Console.info("trying to reach {0}".format(host))
            status = command_{command}.status(host)
            if status:
                Console.info("machine " + host + " has been found. ok.")
            else:
                Console.error("machine " + host + " not reachable. error.")
        pass

if __name__ == '__main__':
    command = cm_shell_{command}()
    command.do_{command}("iu.edu")
    command.do_{command}("iu.edu-wrong")
