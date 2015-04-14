#! /usr/bin/env python
import os
from docopt import docopt
import sys
from cloudmesh_base.util import banner
from cloudmesh_base.util import path_expand


def replace_dict(filename, data):
    if filename is None or filename == "":
        return
    print "Converting:", filename
    # read content
    with open(filename, 'r') as f:
        content = str(f.readlines())
    # replace content
    content = content.format(**data)
    # write content back to file
    with open(filename, 'w') as f:
        for line in content:
            f.write(line)


def replace_string(filename, data):
    if filename is None or filename == "":
        return
    print "Converting:", filename
    # read content
    with open(filename, 'r') as f:
        content = f.readlines()
    # replace content
    # write content back to file
    with open(filename, 'w') as f:
        for line in content:
            for key in data:
                old = "{" + key +"}"
                new = data[key]
                line = line.replace(old, new).rstrip()
            f.write(line + "\n")


def generate(arguments=None):
    """
    ::

        Usage:
            cm-generate-command COMMAND [PACKAGE] [--path=PATH] [--topic=TOPIC]

        the command will generate the package and code for a sample cmd3 module.

        Arguments:
            PACKAGE   name of the new package. Often this will be cloudmesh_COMMAND
                      which will be used if not specified.
                      
            COMMAND   the name of the command.

            PATH      path where to place the directory [default: .]

            TOPIC     the topic listed in cm [default: mycommands]
            
        Options:
             -v       verbose mode

        """
    # if arguments is None:
    #     argv=sys.argv[1:]

    arguments = docopt(generate.__doc__)

    # BUG check if dir exists

    command = arguments['COMMAND']
    package = arguments['PACKAGE']
    path = arguments['--path']
    topic = arguments['--topic']

    if topic is None:
        topic = "mycommands"
        
    if path is None:
        path = "."
    path = path_expand(path)

    if package is None:
        package = "cloudmesh_" + command

    data = {'command': command,
            'package': package,
            'path': path,
            'topic': topic,
            'dir': path_expand('~/.cloudmesh')}

    banner("Generating Cloudmesh Command")
    print "Command:", data['command']
    print "Package:", data['package']

    banner("Setup Directory with Package and Command")
    script = """
        rm -rf {path}/{package}
        cp -rf {dir}/etc/cmd3_template {path}/{package}
        mv {path}/{package}/cmd3_template {path}/{package}/{package}
        mv {path}/{package}/setup.py.in {path}/{package}/setup.py       
        mv {path}/{package}/{package}/command_command.py.in {path}/{package}/{package}/command_{command}.py
        mv {path}/{package}/{package}/plugins/cm_shell_command.py.in {path}/{package}/{package}/plugins/cm_shell_{command}.py
        """.format(**data)

    for line in script.split("\n"):
        line = line.strip()
        if line != "":
            print line
            os.system(line)

    banner("replaceing comand and package name in template files")
    files = """
       {path}/{package}/setup.py
       {path}/{package}/Makefile
       {path}/{package}/{package}/plugins/cm_shell_{command}.py
       {path}/{package}/{package}/command_{command}.py
       """.format(**data)

    for filename in files.split("\n"):
        filename = filename.strip()
        if filename != "":
            replace_string(filename, data)

    banner("Comand code created.")

if __name__ == "__main__":
    generate()
