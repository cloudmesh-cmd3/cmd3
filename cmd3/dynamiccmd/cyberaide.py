#
# Gregor von Laszewski
#
# code insired from cyberaide and cogkit, while trying to develop a
# dynamic CMD that loads from plugin directory
# 


import cmd

def DynamicCmd(name,plugins):
    exec('class %s(cmd.Cmd):\n    prompt="cm> "' % name)
    plugin_objects = load_plugins(plugins)    
    cmd = make_cmd_class(name, *plugin_objects)()
    return (cmd, plugin_objects)

def make_cmd_class(name, *bases):
    return type(cmd.Cmd)(name, bases + (cmd.Cmd,), {})

def load_plugins(list):

    plugins = []
    object = {}
    for plugin in list:
        object[plugin] = __import__("plugins." + plugin, globals(), locals(), [plugin], -1)
        exec("cls = object['%s'].%s" % (plugin, plugin))
        plugins.append(cls)
    return plugins
