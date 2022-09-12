import os

if "OPENSEESRT_LIB" in os.environ:
    print(os.environ)
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("libOpenSeesRT", os.environ.get("OPENSEESRT_LIB"))
    libOpenSeesRT = importlib.util.module_from_spec(spec)
    sys.modules["libOpenSeesRT"] = libOpenSeesRT
    spec.loader.exec_module(libOpenSeesRT)
    # libOpenSeesRT.MyClass()

else:
    # from .libOpenSeesRT import *

    from . import libOpenSeesRT

def __getattr__(name):
    return getattr(libOpenSeesRT, name)

