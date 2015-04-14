import os
import pkg_resources
from cloudmesh_base.ConfigDict import ConfigDict
from cloudmesh_base.util import banner
from cloudmesh_base.util import path_expand
from cloudmesh_base.Shell import Shell
from cmd3.console import Console


def create_cmd3_yaml_file(force=False):

    def print_error(kind, path):
        Console.error("the {0} {1} already exists".format(kind, path))
        Console.error("")
        Console.error("If you like to reinstall it, "
                      "please remove the file first")
        Console.error("")

    import cmd3

    banner("create cmd3.yaml")
    pkg_cmd3_yaml = pkg_resources.resource_string(cmd3.__name__,
                                                  "etc/cmd3.yaml")

    cmd3_yaml = path_expand("~/.cloudmesh/cmd3.yaml")

    if os.path.isfile(cmd3_yaml) and not force:
        print_error('file', cmd3_yaml)
    else:
        Shell.mkdir(path_expand("~/.cloudmesh"))
        with open(path_expand("~/.cloudmesh/cmd3.yaml"), "w") as cmd3_file:
            cmd3_file.write(pkg_cmd3_yaml)


    banner("create cmd3_template")
    # # # copy tree
    filename='~/.cloudmesh/etc/cmd3_template'
    if os.path.isdir(path_expand(filename)):
        print_error('directory', filename)
    else:
        import glob
        import shutil
        import cmd3.etc.cmd3_template

        f1=cmd3.etc.cmd3_template.__file__
        cmd3_etc_path=os.path.dirname(f1)
        pattern=os.path.join(cmd3_etc_path, '*')

        for src in glob.glob(pattern):
            if os.path.isfile(src): continue
            shutil.copytree(src, path_expand(filename))

if __name__ == "__main__":
    create_cmd3_yaml_file()
