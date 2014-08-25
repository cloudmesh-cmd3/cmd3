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

    def __init__(self):
        pass

    @staticmethod
    def _msg(message, width=90):
        return textwrap.fill(message, width=width)

    @staticmethod
    def msg(message):
        print (message)

    @staticmethod
    def error(message):
        print FAIL + Console._msg("ERROR: " + message) + ENDC

    @staticmethod
    def info(message):
        print OKBLUE + Console._msg("INFO: " + message) + ENDC

    @staticmethod
    def warning(message):
        print WARNING + Console._msg("WARNING: " + message) + ENDC

    @staticmethod
    def ok(message):
        print OKGREEN + Console._msg(message) + ENDC

#
# Example
#
# from cmd3.console import Console

# console = Console()

# console.warning("Warning")
# console.error("Error")
# console.info("Info")
# console.msg("msg")
