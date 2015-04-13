import os
import pkg_resources
from cloudmesh_base.ConfigDict import ConfigDict
from cloudmesh_base.util import banner
from cloudmesh_base.util import path_expand
from cloudmesh_base.Shell import Shell
from cmd3.console import Console



def create_cmd3_yaml_file(force=False):

    import cmd3

    banner("create cmd3.yaml")
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


    banner("create cmd3_template")
    # # # copy tree
    filename = '~/.cloudmesh/etc/cmd3_template'
    if os.path.isdir(path_expand(filename)):
        Console.error("the directory {0} already exists".format(filename))
        Console.error("")
        Console.error("If you like to reinstall it, please remove the file first")
        Console.error("")            
    else:
        import glob
        import shutil
        import cmd3.etc.cmd3_template

        f1 = cmd3.etc.cmd3_template.__file__
        cmd3_etc_path = os.path.dirname(f1)
        pattern = os.path.join(cmd3_etc_path, '*')

        for src in glob.glob(pattern):
            if os.path.isfile(src): continue
            shutil.copytree(src, path_expand(filename))
    
if __name__ == "__main__":
    create_cmd3_yaml_file()
