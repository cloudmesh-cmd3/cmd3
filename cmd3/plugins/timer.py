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
        ::
        
            Usage:
                timer on
                timer off            
                timer list
                timer start NAME
                timer stop NAME
                timer resume NAME
                timer reset [NAME]

            Description (NOT IMPLEMENTED YET):

                 timer on | off
                     switches timers on and off not yet implemented.
                     If the timer is on each command will be timed and its
                     time is printed after the command. Please note that
                     background command times are not added.

                timer list
                    list all timers

                timer start NAME
                    starts the timer with the name. A start resets the timer to 0.

                timer stop NAME
                    stops the timer

                timer resume NAME
                    resumes the timer

                timer reset NAME
                    resets the named timer to 0. If no name is specified all
                    timers are reset

                Implementation note: we have a stopwatch in cloudmesh,
                                     that we could copy into cmd3
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
