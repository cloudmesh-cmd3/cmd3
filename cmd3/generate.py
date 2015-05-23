#! /usr/bin/env python
import os
from docopt import docopt
import sys
from cloudmesh_base.util import banner
from cloudmesh_base.util import path_expand
from cmd3.console import Console

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

def old_generate():
    # os.system("cm generate help")
    # Console.error("Please do not forget to use the cm in front of "
    #              "generate command. when executing it from the terminal.")
    Console.error("This command has been replicated with\n")
    Console.ok("   cm generate command COMMAND")
    Console.error("Please use this command instead.")




def generate_command(command=None,
                     package=None,
                     path="~",
                     topic="mycommands"
                     ):
    """
    the command will generate the package and code for a sample cmd3 module.

    :param command: the name of the command
    :param package: name of the new package. Often this will be cloudmesh_COMMAND
                    which will be used if not specified.
    :param path:    path where to place the directory
    :param topic:   the topic listed in cm
    :return:
    """

    if command is None:
        Console.error("command not specified")
        return

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

    data["destination"] = "{path}/{package}".format(**data)

    print (data)
    if os.path.exists("".format(**data)):
        Console.error("The directory {destination} already exists.".format(**data))
        return


    banner("Generating Cloudmesh Command")
    print "Command:", data['command']
    print "Package:", data['package']

    banner("Setup Directory with Package and Command")
    # mv {path}/{package}/shell_plugins.py.in {path}/{package}/shell_plugins.py
    script = """
        rm -rf {destination}
        cp -rf {dir}/etc/cmd3_template {destination}
        mv {destination}/cmd3_template {destination}/{package}
        mv {destination}/setup.py.in {destination}/setup.py
        mv {destination}/{package}/command_command.py.in {destination}/{package}/command_{command}.py
        mv {destination}/{package}/plugins/cm_shell_command.py.in {destination}/{package}/plugins/cm_shell_{command}.py
        rm -rf {destination}/command_command.py.in
        rm -rf {destination}/plugins
        """.format(**data)

    for line in script.split("\n"):
        line = line.strip()
        if line != "":
            print line
            os.system(line)

    banner("replacing command and package name in template files")
    #{path}/{package}/shell_plugins.py
    files = """
       {path}/{package}/Makefile
       {path}/{package}/{package}/plugins/cm_shell_{command}.py
       {path}/{package}/{package}/command_{command}.py
       {path}/{package}/setup.py
       """.format(**data)

    for filename in files.split("\n"):
        filename = filename.strip()
        if filename != "":
            replace_string(filename, data)

    banner("Command code created.")

