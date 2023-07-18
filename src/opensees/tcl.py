import os
import sys
import pathlib
import platform
from contextlib import contextmanager

try:
    # On certain servers (heroku), tkinter is not
    # provided. In this case we  can fall pack
    # to the tcinter repackaging
    import tkinter
except:
    import tcinter as tkinter

from opensees.library.obj import Component


@contextmanager
def _build_extension_env():
    cookies = []

    # Windows and Python >= 3.8
    if hasattr(os, "add_dll_directory"):
        for path in os.environ.get("PATH", "").split(os.pathsep):

            if path and pathlib.Path(path).is_absolute() and pathlib.Path(path).is_dir():
                cookies.append(os.add_dll_directory(path))

    try:
        yield

    finally:
        for cookie in cookies:
            cookie.close()


def _find_openseesrt():
    if "OPENSEESRT_LIB" in os.environ:
        libOpenSeesRT_path = pathlib.Path(os.environ["OPENSEESRT_LIB"])
        return libOpenSeesRT_path.parents[0], libOpenSeesRT_path

    op_sys = platform.system()
    ext = {
        "Darwin":  ".dylib",
        "Linux":   ".so",
        "Windows": ".dll"
    }[op_sys]

    install_dir = pathlib.Path(__file__).parents[0]

    if op_sys == "Windows":
        libOpenSeesRT_path = install_dir/"bin"/f"OpenSeesRT{ext}"
    else:
        libOpenSeesRT_path = install_dir/f"libOpenSeesRT{ext}"

    return libOpenSeesRT_path.parents[0], libOpenSeesRT_path


def TclInterpreter(verbose=False, tcl_lib=None, preload=True, enable_tk=False):

    install_dir, libOpenSeesRT_path = _find_openseesrt()

    if verbose:
        print(f"OpenSeesRT: {libOpenSeesRT_path}", file=sys.stderr)

    if enable_tk:
        interp = tkinter.Tk()
    else:
        interp = tkinter.Tcl()


    if preload:
        with _build_extension_env():
            interp.eval(f"load {{{libOpenSeesRT_path}}}")

    def check():
        interp.after(50, check)

    interp.after(50, check)

    return interp

def eval(script: str):
    interp = TclInterpreter()
    interp.eval(f"""

    {script}

    """)
    return interp


def dumps(obj):
    if not isinstance(obj, (Component,list,tuple)):
        from opensees.emit import OpenSeesWriter
        return OpenSeesWriter(obj).dump()
    else:
        from opensees.emit.opensees import TclScriptBuilder
        writer = TclScriptBuilder()
        try:
            writer.send(obj)
            if not writer.python_objects:
                return writer.getScript(indexed=True)
            else:
                return writer
        except Exception as e:
            raise e
            # print(writer.getScript(indexed=True), file=sys.stderr)
            # raise ValueError("Cannot dump model with binary objects")


class TclRuntime:
    def __init__(self,  model=None, verbose=False, safe=False, preload=True, enable_tk=False):
        from functools import partial
        self._partial = partial
        self._c_domain = None
        self._c_rt = None
        self._interp = TclInterpreter(verbose=verbose,
                                      preload=preload,
                                      enable_tk=enable_tk)

        if not safe:
            self._interp.createcommand("=", self.pyexpr)

        if enable_tk:
            self._interp.createcommand("tkloop", self._interp.mainloop)

        self._interp.createcommand("export", self.export)

        # self._interp.createcommand("import", self.pyimport)

        if model is not None:
            self.send(model)

        try:
            import sees.tcl
            sees.tcl.add_commands(self)
        except ImportError:
            pass

    @property
    def registry(self):
        registry["UniaxialMaterial"][0].getStress()
        return

    def pyimport(self, *args):
        try:
            lib = __import__(args[0])
            print(lib)
        except:
            self.eval("opensees::import " + " ".join(args))
            return

    def to_dict(self):
        import json
        # TODO: use tempfile or pipe
        self.eval("print -json .abcd.json")

        with open(".abcd.json", "r") as f:
            model = json.load(f)
            model = model["StructuralAnalysisModel"]

        os.remove(".abcd.json")
        return model

    def export(self, *args):
        import io
        import os
        import sys
        import opensees.emit.mesh

        model = self.to_dict()

        if args[0] == "stdout":
            file = io.StringIO()
        else:
            file = args[0]

        if len(args) > 1:
            fmt = args[1]
        else:
            fmt = "vtk"

        mesh = opensees.emit.mesh.dump(model, args[0], fmt)

        try:
            mesh.write(file, file_format=fmt)

        except Exception as e:
            print(e, file=sys.stderr)

        return ""



    def pyexpr(self, *args):
        try:
            import numpy as math
        except:
            import math

        env = math.__dict__
        env["locals"]   = None
        env["globals"]  = None
        env["__name__"] = None
        env["__file__"] = None
        env["__builtins__"] = {}
        for k in self.eval("info globals").split():
            try:
                update = {k: float(self._interp.getvar(k))}
            except:
                continue
            env.update(update)
        try:
            return __builtins__["eval"]((" ".join(args[:])).replace("$",""), env)

        except Exception as e:
            print(e, file=sys.stderr)

    def model(self, ndm, ndf, **kwds):
        """
        model(model: opensees.model)
        model(ndm:int, ndf:int)
        """
        self.eval(f"model basic -ndm {ndm} -ndf {ndf}")


    def lift(self, type: str, tag: int=None):
        type = type.lower()
        # libOpenSeesRT must be imported by Python
        # AFTER if has been loaded by Tcl (this was done
        # when a TclRuntime() is created) so that Tcl stubs
        # are initialized. Otherwise there will be a segfault
        # when a python c-binding attempts to call a Tcl
        # C function. Users should never import OpenSeesPyRT
        # themselves
        from opensees.tcl import TclRuntime
        from opensees import OpenSeesPyRT as libOpenSeesRT

        if type == "uniaxialmaterial":
#           self.eval("model basic 1 1")
#           self.send(self, ndm=1, ndf=1)
            _builder = libOpenSeesRT.get_builder(self._interp.interpaddr())
            return _builder.getUniaxialMaterial(tag)

        elif type == "section":
            rt.send(self, ndm=2, ndf=3)
            self._builder = libOpenSeesRT.get_builder(self._interp.interpaddr())
            handle = self._builder.getSection(str(self.name))

        elif type == "backbone":
            rt.send(self)
            self._builder = libOpenSeesRT.get_builder(self._interp.interpaddr())
            handle = self._builder.getHystereticBackbone(str(self.name))

        else:
            raise TypeError("Unimplemented type")


    def send(self, obj, ndm=2, ndf=3, **kwds):
        self.model(ndm=ndm, ndf=ndf)

        m = dumps(obj)

        if isinstance(m, str):
            try:
                self.eval(m)
            except Exception as e:
                print(e, file=sys.stderr)
        else:
            self.eval(m.getIndex())
            from . import OpenSeesPyRT as libOpenSeesRT
            _builder = libOpenSeesRT.get_builder(self._interp.interpaddr())
            for ident,obj in m.python_objects.items():
                tag = self.eval(f"set {ident.tclstr()}")
                _builder.addPythonObject(tag, obj)

            self.eval(m.getScript())
        return self

    @property
    def _rt(self):
        # if self._c_rt is None:
        #     from . import OpenSeesPyRT as libOpenSeesRT
        #     self._c_rt = libOpenSeesRT.getRuntime(self._interp.tk.interpaddr())
        return self._c_rt

    @property
    def _domain(self):
        if self._c_domain is None:
            from . import OpenSeesPyRT as libOpenSeesRT
            self._c_domain = libOpenSeesRT.get_domain(self._rt)
        return self._c_domain

    def getNodeResponse(self, node, typ):
        import numpy as np
        return np.array(self._domain.getNodeResponse(node, typ))

    def getTime(self):
        return self._domain.getTime()

    time = getTime

    def eval(self, string):
        try:
            return self._interp.tk.eval(string)

        except tkinter._tkinter.TclError as e:
            print(self._interp.getvar("errorInfo"), file=sys.stderr)
            raise e

    def fix(self, nodes, *dofs):
        if not isinstance(nodes,list):
            nodes = [nodes]
        for node in nodes:
            self.eval(f"fix {node} {' '.join(map(str,dofs))}")

    def add_tagged(self, objs):
        for k,v in objs.items():
            if isinstance(k, int):
                self.eval(v.cmd)

# Used in test_lift for NV
ModelRuntime = TclRuntime

