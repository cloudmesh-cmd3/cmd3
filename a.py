import os
import importlib

def load_cmd3_from_module(name):
    
    cmd3_module = __import__(name)
    location = cmd3_module.plugins.__file__
    print location
    print os.path.basename(location)
    print os.path.dirname(location)


load_cmd3_from_module('cloudmesh_cmd3.plugins')
