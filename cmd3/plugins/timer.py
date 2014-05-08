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
        Usage:
            timer on
            timer off            
            timer list 

        Description:
        
             switches timers on and off not yet implemented.
             If the timer is on each command will be timed and its
             time is printed after the command. Please note that
             background command times are not added.
        """
        print arguments
        print "args", args
        args = args.lower()

        if args in ("on", "off"):
            self.with_timers = (args == "on")
            print "Timers are now:", self.with_timers
        if args == 'list':
            self.list_timers()
        else:
            self.do_timer.__doc__

    def list_timers(self):
        """list of all timers"""
        print "TODO"
        pass
