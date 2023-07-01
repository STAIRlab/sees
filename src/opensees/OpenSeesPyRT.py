import os

# if "OPENSEESRT_LIB" in os.environ:
#     import sys
#     import importlib.util
#     spec = importlib.util.spec_from_file_location("libOpenSeesRT", os.environ.get("OPENSEESRT_LIB"))
#     libOpenSeesRT = importlib.util.module_from_spec(spec)
#     sys.modules["libOpenSeesRT"] = libOpenSeesRT
#     spec.loader.exec_module(libOpenSeesRT)
if "OPENSEESPYRT_LIB" in os.environ:
    import sys
    import importlib.util
    spec = importlib.util.spec_from_file_location("OpenSeesPyRT", os.environ.get("OPENSEESPYRT_LIB"))
    libOpenSeesPyRT = importlib.util.module_from_spec(spec)
    sys.modules["libOpenSeesPyRT"] = libOpenSeesPyRT
    spec.loader.exec_module(libOpenSeesPyRT)


else:
    print("from . import libOpenSeesRT")
    from . import libOpenSeesRT

def __getattr__(name):
    return getattr(libOpenSeesPyRT, name)

