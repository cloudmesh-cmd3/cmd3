from cmd3.shell import command
import glob
import os


class script:

    #
    # Scripts
    #

    script_files = ["scripts/*.txt"]
    scripts = {}

    def activate_script(self):
        """activates the script command"""
        
        
        # must be rethought
        # ./scripts
        # deploydir/./scripts
        self._add_scope("script")
        self.scripts = {}
        self.script_files = [
            "./scripts/script_*.txt", "~/.cloudmesh/scripts/script_*.txt"]
        self._load_scripts(self.script_files)

    def add_script_dir(self, regexp):
        self.script_files.append(regexp)

    # just as activate when i specify info all info_ ar being called
    def info_script(self):
        print "%20s =" % "Script Locations", str(self.script_files)
        print "%20s =" % "Scripts", str(self.scripts)

    def _load_scripts(self, script_files):
        for location in script_files:
            self._import_scripts(location)

    def _import_scripts(self, regex):
        # expand
        if regex.startswith("."):
            regex = regex.replace(".", os.getcwd(), 1)
        regex = os.path.expanduser(regex)

        scripts = glob.glob(regex)
        if scripts:
            for filename in scripts:
                try:
                    script = os.path.basename(filename)
                    dir = os.path.dirname(filename)

                    (script, ext) = script.split(".")
                    script = script.replace("script_", "")
                    if self.echo:
                        print "Import Script", script, "from", filename
                    self.scripts[script] = filename
                except:
                    print ">>>>> ", filename

    def _list_scripts(self):
        print 10 * "-"
        print 'Scripts'
        print 10 * "-"
        for v in self.scripts:
            print v, '=', self.scripts[v]

    # logic of load does not work
    # we want load regex and load without that just loads defaul
    # needs docopt

    def run_script(self, filename):
        print filename
        file = open(filename, "r")
        for line in file:
            line = self.precmd(line)
            line = self.onecmd(line)
            #line = self.postcmd(line)
        file.close()

    @command
    def do_script(self, args, arguments):
        """
        ::
        
            Usage:
                   script
                   script load
                   script load LABEL FILENAME
                   script load REGEXP
                   script list
                   script LABEL

            Arguments:
                   load       indicates that we try to do actions toload files.
                              Without parameters, loads scripts from default locations
                    NAME      specifies a label for a script
                    LABEL     a conveninet LABEL, it must be unique
                    FILENAME  the filename in which the script is located
                    REGEXP    Not supported yet.
                              If specified looks for files identified by the REGEXP.

            NOT SUPPORTED YET

               script load LABEL FILENAME
               script load FILENAME
               script load REGEXP

            Process FILE and optionally apply some options

            """
        if args == "load":
            self._load_scripts(self.script_files)
            self._list_scripts()
        elif args == "list" or args == "" or args is None:
            self._list_scripts()
        elif args in self.scripts:
            filename = self.scripts[args]
            self.run_script(filename)
        elif arguments['load'] and arguments['REGEXP']:
            new_files = arguments['REGEXP']
            self.add_script_dir(new_files)
            self._load_scripts(new_files)
            self._list_scripts()
        else:
            print "script execution not yet defined"
            print arguments
            print args
