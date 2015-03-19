import os
import os.path

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
        filename = arguments['FILENAME']
        if platform.system() == 'Darwin':
            if os.path.isfile(filename):
                os.system("open -a '\''/Applications/Graphviz.app'\'' " + filename)

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
        filename = arguments['FILENAME']
        output_format = arguments['FORMAT']
        base = filename.replace(".dot", "")
        out = base + "." + output_format
        if output_format == "pdf":
            exec_command = "dot -Tps %s | epstopdf --filter --ooutput %s" % (
                file, out)
        else:
            exec_command = "dot -T%s %s -o %s 2>/tmp/err" % (output_format, file, out)
        os.system(exec_command)
