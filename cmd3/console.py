import textwrap

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
#WARNING = '\033[93m' # yellow
FAIL = '\033[91m'
WARNING = FAIL
ENDC = '\033[0m'
BOLD = "\033[1m"

class Console(object):
    
    def __init__(self, _color_on = True):
        self._color_on = _color_on

    def _msg(self, message, width=90):
        return textwrap.fill(message, width=width)

    def msg(self, message):
        print (message)

    def error(self, message):
        if self._color_on:
            print FAIL + self._msg("ERROR: " + message) + ENDC
        else:
            print self._msg("ERROR: " + message)

    def info(self, message):
        if self._color_on:
            print OKBLUE + self._msg("INFO: " + message) + ENDC
        else:
            print self._msg("INFO: " + message)

    def warning(self, message):
        if self._color_on:
            print WARNING + self._msg("WARNING: " + message) + ENDC
        else:
            print self._msg("WARNING: " + message)

    def ok(self, message):
        if self._color_on:
            print OKGREEN + self._msg(message) + ENDC
        else:
            print self._msg(message)

#
# Example
#
# from cmd3.console import Console

# console = Console()

# console.warning("Warning")
# console.error("Error")
# console.info("Info")
# console.msg("msg")
