import os
import os.path
import tempfile
from cmd3.shell import command


class graphviz:


    def activate_graphviz(self):
        """activates the graphviz command"""
        pass

    @command
    def do_graphviz(self, args, arguments):
        """
        ::
        
            Usage:
                   graphviz FILENAME

            Export the data in cvs format to a file. Former cvs command

            Arguments:
                FILENAME   The filename

        """
        file = arguments['FILENAME']
        if platform.system() == 'Darwin':
            if os.path.isfile(file):
                os.system("open -a '\''/Applications/Graphviz.app'\'' " + file)

    @command
    def do_dot2(self, args, arguments):
        """
        ::

            Usage:
                   dot2 FILENAME FORMAT

            Export the data in cvs format to a file. Former cvs command

            Arguments:
                FILENAME   The filename
                FORMAT     the export format, pdf, png, ...

        """
        file = arguments['FILENAME']
        format = arguments['FORMAT']
        base = file.replace(".dot", "")
        out = base + "." + format
        if format == "pdf":
            command = "dot -Tps %s | epstopdf --filter --ooutput %s" % (
                file, out)
        else:
            command = "dot -T%s %s -o %s 2>/tmp/err" % (format, file, out)
        os.system(command)
