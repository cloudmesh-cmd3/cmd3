from cmd3.shell import command


class pause:

    def activate_pause(self):
        """activates the pause command"""
        pass

    @command
    def do_pause(self, arg, arguments):
        """
        ::

            Usage:
                pause [MESSAGE]

            Displays the specified text then waits for the user to press RETURN.

            Arguments:
               MESSAGE  message to be displayed
        """
        raw_input(arg + '\n')
