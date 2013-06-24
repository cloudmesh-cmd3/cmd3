from cmd3.cyberaide.decorators import command

class pause:
    
    def activate_pause(self):
        pass

    @command
    def do_pause(self, arg, arguments):
        """
        Ussage:
            pause

        Displays the specified text then waits for the user to press RETURN.
        """
        raw_input(arg + '\n')
