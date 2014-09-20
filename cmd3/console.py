import textwrap

    
class Console(object):

    def __init__(self, _color_on = True):
        self._color_on = True
        self.theme = {
            'HEADER': '\033[95m',
            'OKBLUE': '\033[34m',
            'OKGREEN': '\033[32m',
            'FAIL': '\033[31m',
            'WARNING': '\033[31m',
            'ENDC': '\033[m',
            'BOLD': "\033[1m",
        }


    def theme(self, theme):
        self.theme = theme
        
    def color(self, on):
        self._color_on = on
                
    def _msg(self, message, width=90):
        return textwrap.fill(message, width=width)

    def msg(self, message):
        print (message)

    def error(self, message):
        if self._color_on:
            print self.theme['FAIL'] + self._msg("ERROR: " + message) + self.theme['ENDC']
        else:
            print self._msg("ERROR: " + message)

    def info(self, message):
        if self._color_on:
            print self.theme['OKBLUE'] + self._msg("INFO: " + message) + self.theme['ENDC']
        else:
            print self._msg("INFO: " + message)

    def warning(self, message):
        if self._color_on:
            print self.theme['WARNING'] + self._msg("WARNING: " + message) + self.theme['ENDC']
        else:
            print self._msg("WARNING: " + message)

    def ok(self, message):
        if self._color_on:
            print self.theme['OKGREEN'] + self._msg(message) + self.theme['ENDC']
        else:
            print self._msg(message)

#
# Example
#

"""
from cmd3.console import Console

console = Console()

console.warning("Warning")
console.error("Error")
console.info("Info")
console.msg("msg")
"""
