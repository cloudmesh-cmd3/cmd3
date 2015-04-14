from cmd3.shell import command


class yaml_setup:

    def activate_load(self):
        """activates the load command"""
        pass

    @command
    def do_setup_yaml(self, arg, arguments):
        """
        ::
            Usage:
              setup_yaml  [--force] 

            Copies a cmd3.yaml file into ~/.cloudmesh/cmd3.yaml
        """
        from cmd3.yaml_setup import create_cmd3_yaml_file
        force = arguments["--force"]
        create_cmd3_yaml_file(force=force)
