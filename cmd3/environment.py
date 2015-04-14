import sys
from cmd3.console import Console

version = sys.version_info[:3]

if version == (2, 7, 9):
    Console.info("You are running a supported version of python: " + str(version))
else:
    Console.error("You are running an unsupported version of python: " + str(version))
    Console.error("We recommend you update your python version: " + str(version))

if pip.__version__ == '6.1.1':
    Console.info("You are running a supported version of pip: " + str(version))
else:
    Console.error("You are running an unsupported version of pip: " + str(version))
    Console.error("We recommend you update your pip version: " + str(version))    
