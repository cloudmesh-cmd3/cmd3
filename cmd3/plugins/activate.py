import sys
import string

class activate:

    command_topics = {}
    plugins = []

    def register_command_topic(self, topic, topic_command):
        try:
            a = self.command_topics[topic]
        except:
            self.command_topics[topic] = []
        self.command_topics[topic].append(topic_command)
    
    def activate_activate(self):
        """activate the activation method"""
        plugins = []

    def do_plugins(self, args):
        """
        Usage:
            plugins

        activates the plugins."""
        self.activate()

    def activate(self):
        """method to activate all activation methods in the shell and
        its plugins.
        """
        d = dir(self)
        self.plugins = []
        for key in d:
            if key.startswith("shell_activate_"):
                if self.echo:
                    print "Shell Activate:", key
                self.plugins.append(key)
        for key in d:
            if key.startswith("activate_"):
                if self.echo:
                    print "Activate:", key            
                self.plugins.append(key)

        for key in self.plugins:
            if self.echo:
               print "> %s" % key.replace("_", " ", 1)
            exec("self.%s()" % key)

    def do_help(self, arg):
        'List available commands with "help" or detailed help with "help cmd".'

        if arg:
            # XXX check arg syntax
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc=getattr(self, 'do_' + arg).__doc__
                    if doc:
                        self.stdout.write("%s\n"%str(doc))
                        return
                except AttributeError:
                    pass
                self.stdout.write("%s\n"%str(self.nohelp % (arg,)))
                return
            func()
        else:
            names = self.get_names()
            cmds_doc = []
            cmds_undoc = []
            help = {}
            for name in names:
                if name[:5] == 'help_':
                    help[name[5:]]=1
            names.sort()
            # There can be duplicates if routines overridden
            prevname = ''
            for name in names:
                if name[:3] == 'do_':
                    if name == prevname:
                        continue
                    prevname = name
                    cmd=name[3:]
                    if cmd in help:
                        cmds_doc.append(cmd)
                        del help[cmd]
                    elif getattr(self, name).__doc__:
                        cmds_doc.append(cmd)
                    else:
                        cmds_undoc.append(cmd)


            self.stdout.write("%s\n"%str(self.doc_leader))
            self.print_topics(self.doc_header,   cmds_doc,   15,80)
            self.print_topics(self.misc_header,  list(help.keys()),15,80)
            self.print_topics(self.undoc_header, cmds_undoc, 15,80)
            
            for topic in self.command_topics:
                topic_cmds =  self.command_topics[topic]
                self.print_topics(string.capwords(topic + " commands"), topic_cmds, 15,80)
            
