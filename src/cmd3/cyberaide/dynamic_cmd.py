#
# Gregor von Laszewski
#
# code insired from cyberaide and cogkit, while trying to develop a
# dynamic CMD that loads from plugin directory
# 


import cmd
import glob

def DynamicCmd(name,plugins):
    exec('class %s(cmd.Cmd):\n    prompt="cm> "' % name)
    plugin_objects = load_plugins(plugins)    
    cmd = make_cmd_class(name, *plugin_objects)()
    return (cmd, plugin_objects)

def make_cmd_class(name, *bases):
    return type(cmd.Cmd)(name, bases + (cmd.Cmd,), {})

def get_plugins(dir):
    # not just plugin_*.py
    plugins = []
    list=glob.glob(dir + "/*.py")
    for p in list:
        p = p.replace(dir + "/", "").replace(".py", "")
        if not p.startswith('_'):
            plugins.append(p)
    return plugins

def load_plugins(list):

    plugins = []
    object = {}
    for plugin in list:
        object[plugin] = __import__("cmd3.plugins." + plugin, globals(), locals(), [plugin], -1)
        exec("cls = object['%s'].%s" % (plugin, plugin))
        plugins.append(cls)
    return plugins
