from cmd3.cyberaide.decorators import command
import glob

class script:

    ######################################################################
    # Scripts
    ######################################################################

    
    script_files = ["scripts/*.txt"]
    scripts = {}


    def activate_script(self):
        # locationof scripts must be rethought
        # ./scripts
        # deploydir/./scripts
        # .futuregrid/scripts
        self.script_files = ["scripts/*.txt"]
        self._load_scripts(self.script_files)
        self._add_scope("script")

    # just as activate when i specify info all info_ ar being called
    def info_script (self):
        print "%20s =" % "Script Locations", str(self.script_files)
        print "%20s =" % "Scripts", str(self.scripts)

    def _load_scripts (self,script_files):
        self.scripts = {}
        for location in script_files:
            self._import_scripts(location)

    def _import_scripts (self, regex):
        scripts = glob.glob(regex)
        if scripts:
            for filename in scripts:
                (dir, script) = filename.split("/")
                (script,ext) = script.split(".")
                script = script.replace("script_", "")
                print "Import Script", script, "from", filename
                self.scripts[script] = filename

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
            line = self.postcmd(line)
        file.close()

    @command
    def do_script(self, args, arguments):
        """
        Usage:
               script load
               script load LABEL FILENAME
               script load FILENAME
               script load REGEXP
               script list
               script LABEL

        ARGUMENTS:
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
            self._load_scripts()
            self._list_scripts()
        elif args == "list":
            self._list_scripts()
        elif args in self.scripts:
            filename = self.scripts[args]
            runt_script(filename)            
        else:
            print "script execution not yet defined"

