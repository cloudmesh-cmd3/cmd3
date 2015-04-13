import os
import pkg_resources
from cloudmesh_base.ConfigDict import ConfigDict
from cloudmesh_base.util import banner
from cloudmesh_base.util import path_expand
from cloudmesh_base.Shell import Shell
from cmd3.console import Console
import cmd3

def create_cmd3_yaml_file(force=False):
    banner("Setup the cmd3.yaml file")        
    pkg_cmd3_yaml = pkg_resources.resource_string(cmd3.__name__, "etc/cmd3.yaml")

    #import pdb;pdb.set_trace()
    cmd3_yaml = path_expand("~/.cloudmesh/cmd3.yaml")
        
    if os.path.isfile(cmd3_yaml) and not force:
        Console.error("the file {0} already exists".format(cmd3_yaml))
        Console.error("")
        Console.error("If you like to reinstall it, please remove the file first")
        Console.error("")            
    else:
        Shell.mkdir(path_expand("~/.cloudmesh"))
        with open(path_expand("~/.cloudmesh/cmd3.yaml"), "w") as cmd3_file:
            cmd3_file.write(pkg_cmd3_yaml)

if __name__ == "__main__":
    create_cmd3_yaml_file()
