from cloudmesh_base.Shell import Shell

from cloudmesh_base.locations import config_file
from cloudmesh_base.ConfigDict import ConfigDict
from cmd3.console import Console


class setup_management(object):

    def __init__(self, quiet=False):
        self.quiet = quiet
        try:
            self.filename = config_file("/cmd3.yaml")
            if not self.quiet:
                Console.ok("Reading " + self.filename + ". ok.")
        except:
            Console.error("problem loading cmd3.yaml file")
        try:
            self.config = ConfigDict(filename=self.filename)
            # print(self.config)
        except Exception, e:
            Console.error("problem with ConfigDict")
            print(e)

    def add(self, plugin, dryrun=False):

        if not plugin.endswith(".plugins"):
            plugin = plugin + ".plugins"

        modules = self.config["cmd3"]["modules"]
        if plugin in modules:
            if not self.quiet:
                Console.error("plugin {:} is already activated.".format(plugin))
        else:
            self.config["cmd3"]["modules"].append(plugin)
            if not self.quiet:
                Console.ok("Adding plugin " + plugin)

        if not dryrun:
            self.config.write(self.filename, output="yaml")
        else:
            print(self.config.yaml())

    def delete(self, plugin, dryrun=False):

        if not plugin.endswith(".plugins"):
            plugin = plugin + ".plugins"

        modules = self.config["cmd3"]["modules"]
        if plugin not in modules:
            Console.error("plugin {:} is already deactivated.".format(plugin))
        else:
            self.config["cmd3"]["modules"].remove(plugin)
            if not self.quiet:
                Console.ok("Deleting plugin " + plugin)

        if not dryrun:
            self.config.write(self.filename, output="yaml")
        else:
            print(self.config.yaml())


    def __str__(self):
        with open(self.filename, 'r') as f:
            r = f.read()
        return r

