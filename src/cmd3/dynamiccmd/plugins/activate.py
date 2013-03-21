class activate:

    active = False
    
    def do_on(self, arg):
        self.active = True
        self.activate_status()

    def do_off(self, arg):
        self.active = False
        self.activate_status()

    def activate_status(self):
        print "Active:", self.active

    def activate(self, plugins):
        d = dir(self)
        result = []
        for key in d:
            if key.startswith("activate_"):
                result.append(key)
        print result
        for key in result:
            print "> %s" % key.replace("_"," ")
            exec("self.%s()" % key)


