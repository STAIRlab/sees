import os
import sys
import pathlib
import platform
from contextlib import contextmanager

try:
    import tkinter
except:
    import tcinter as tkinter

from opensees.library.obj import Component


@contextmanager
def _build_extension_env():
    """
    Create a context in which build extensions can be imported.

    It fixes a change of behaviour of Python >= 3.8 in Windows:
    https://docs.python.org/3/whatsnew/3.8.html#bpo-36085-whatsnew

    Other related resources:

    - https://stackoverflow.com/a/23805306
    - https://www.mail-archive.com/dev@subversion.apache.org/msg40414.html

    Example:

    .. code-block:: python

        from cmake_build_extension import build_extension_env

        with build_extension_env():
            from . import bindings
    """

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
#       print(model)
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
            mesh.write(
                file,          # str, os.PathLike, or buffer/open file
                file_format=fmt,  # optional if first argument is a path; inferred from extension
            )
        except Exception as e:
            print(e, file=sys.stderr)
            # self.eval(f'error {{{e}}}')

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
            # raise e
            print(e, file=sys.stderr)

    def model(self, ndm, ndf, **kwds):
        # TODO: refactor this function
        """
        model(model: opensees.model)
        model(ndm:int, ndf:int)
        """
        self.eval(f"model basic -ndm {ndm} -ndf {ndf}")


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

Runtime = TclRuntime

#
# Analysis
#
def eigen(script: str, modes=1, verbose=False):
    interp = TclInterpreter()
    interp.eval(f"""

    {script}

    set options(-verbose)  {int(verbose)}
    set options(-numModes) {modes}
    set options(-file) /dev/stdout

    set PI       3.1415159
    set DOFs     {{1 2 3 4 5 6}}
    set nodeList [getNodeTags]

    """ + """
    # Initialize variables `omega`, `f` and `T` to
    # empty lists.
    foreach {omega f T recorders} {{} {} {} {}} {}

    for {set k 1} {$k <= $options(-numModes)} {incr k} {
      lappend recorders [recorder Node -node {*}$nodeList -dof {*}$DOFs "eigen $k";]
    }

    set eigenvals [eigen $options(-numModes)];

    set T_scale 1.0
    foreach eig $eigenvals {
      lappend omega [expr sqrt($eig)];
      lappend f     [expr sqrt($eig)/(2.0*$PI)];
      lappend T     [expr $T_scale*(2.0*$PI)/sqrt($eig)];
    }

    # print info to `stdout`.
    #if {$options(-verbose)} {
    #  # puts "Angular frequency (rad/s): $omega\n";
    #  # puts "Frequency (Hz):            $f\n";
    #  # puts "Periods (sec):             $T\n";
    #}

    if {$options(-file) != 0} {
      source /home/claudio/brace/Scripts/OpenSeesScripts/brace2.tcl
      brace2::io::write_modes $options(-file) $options(-numModes)
    }

    foreach recorder $recorders {
      remove recorder $recorder
    }
    """)
    return interp

