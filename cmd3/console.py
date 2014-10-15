import textwrap


class Console(object):

    color = True

    theme = {
        'HEADER': '\033[95m',
        'BLACK': '\033[30m',
        'PURPLE': '\033[35m',
        'CYAN': '\033[36m',
        'WHITE': '\033[37m',
        'OKBLUE': '\033[34m',
        'OKGREEN': '\033[32m',
        'FAIL': '\033[31m',
        'WARNING': '\033[31m',
        'RED': '\033[31m',
        'ENDC': '\033[0m',
        'BOLD': "\033[1m",
    }

    @staticmethod
    def get(name):
        if name in Console.theme:
            Console.theme[name]
        else:
            Console.theme['BLACK']

    @staticmethod
    def _msg(message, width=90):
        return textwrap.fill(message, width=width)

    @staticmethod
    def msg(message):
        print (message)

    @staticmethod
    def error(message):
        if Console.color:
            Console._print('FAIL', "ERROR: ", message)
        else:
            print Console._msg("ERROR: " + message)

    @staticmethod
    def info(message):
        if Console.color:
            Console._print('OKBLUE', "INFO: ", message)
        else:
            print Console._msg("INFO: " + message)

    @staticmethod
    def warning(message):
        if Console.color:
            Console._print('WARNING', "WARNING: ", message)
        else:
            print Console._msg("WARNING: " + message)

    @staticmethod
    def ok(message):
        if Console.color:
            Console._print('OKGREEN', "", message)
        else:
            print Console._msg(message)

    @staticmethod
    def _print(color, prefix, message):
        print (Console.theme[color] +
               prefix +
               Console._msg(message) +
               Console.theme['ENDC'])

#
# Example
#

"""
from cmd3.console import Console


print Console.color

print Console.theme

Console.warning("Warning")
Console.error("Error")
Console.info("Info")
Console.msg("msg")
Console.ok("Success")

print Console.color = False
Console.error("Error")

"""
