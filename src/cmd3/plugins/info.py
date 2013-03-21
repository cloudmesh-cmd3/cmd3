from cmd3.cyberaide.decorators import command


class info:


    @command
    def do_info(self, arg, arguments):
        """
        Usage:
               info

        Prints some internal information about the shell

        """

        for element in dir(self):
            print element


