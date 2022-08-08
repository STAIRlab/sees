from .libOpenSeesRT import *

from . import libOpenSeesRT

def __getattr__(name):
    return getattr(libOpenSeesRT, name)

