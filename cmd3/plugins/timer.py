from cmd3.shell import command


class timer:

    """
    needs to be integrated in pre post command
    """
    #
    # TIMER
    #

    @command
    def do_timer(self, args, arguments):
        """
        Ussage:
            timer (on|off)

        switches timers on and off not yet implemented
        """
        args = args.lower()

        if args in ("on", "off"):
            self.with_timers = (line == "on")
            print "Timers are now:", self.with_timers
        if args == 'list':
            self.list_timers()
        else:
            self.help_timer()

    def list_tmers(self):
        print "TODO"
        pass
