from cmd3.shell import command


# noinspection PyUnusedLocal
class metric:

    def activate_metric(self):
        pass

    #
    # analyze commands
    #

    @command
    def do_analyze(self, args, arguments):
        """
        Usage:
               analyze METRIC --start START --end END
               analyze METRIC --period [monthly|quaterly|daily]
               analyze METRIC --month MONTH

        Analyze the metric data

        Arguments:
            METRIC     The metric to be analyzed ... what values does it have?? ...
            START      The start time n the format YYYY-MM-DDThh:mm:ss
            ENDT       The end time n the format YYYY-MM-DDThh:mm:ss
            MONTH      The month in 01,02, ..., 12

        Options:
          --start     specifies the time when to start the analysis
          --end       specified the time when to end the analysis
          --month     the month
          --period    the period

        """
        print(arguments)

    #
    # CVS commands
    #

    @command
    def do_table(self, args, arguments):
        """
        Usage:
               table FILENAME
               table --file FILENAME

        Export the data in cvs format to a file. Former cvs command

        Arguments:
            FILENAME   The filename

        Options:
          --filet     specifies the filename

        """
        print(arguments)

    #
    # chart
    #

    @command
    def do_chart(self, args, arguments):
        """
        Usage:
               chart [--dir DIR] --type (bar|line|column|pie|motion)
                     [--api (highchart|google|jquery|sparkline)] [FILENAME]

        Creates a chart of a given type

        Arguments:
            DIR       The directory into which the chart is written
            FILENAME  The filename in which the chart is written.

        Options:
          --dir        The directory
          --type       The type of the chart
          --api        The chart api library

        """
        print(arguments)

    #
    # count images
    #
    @command
    def do_count_images(self, line, opts=None):
        """
        Usage:
               count_images [--detail | --summary] --user USER

        Count bucket images per user (development level). It is
        virtual machine image counts grouped by users or accounts
        based on euca2ools.  It shows that which user or account
        currently owns how many virtual machine images on the system.
        This metric is based on the euca2ool command.
        euca-describe-images. that a eucalyptus user can see a list
        of machine images.

        Arguments:
            USER       The user

        Options:
          --user       Show only images from the specified userid.
          --detail     Show details of the image (What would that be?)
          --summary    show summary about the image (default)

        """
        print(arguments)
