import os
import sys
import tkinter
import pathlib
from opensees.obj import Component
from .runtime import AbstractRuntime

def TclInterpreter():
    if "OPENSEESRT_LIB" in os.environ:
        libOpenSeesRT_path = os.environ["OPENSEESRT_LIB"]
    else:
        # install_dir = pathlib.Path("/home/claudio/opensees/pyg3/libg3/build/SRC/api/tclCommandPackage/")
        # install_dir = pathlib.Path("/home/claudio/opensees/pyg3/libg3/build/SRC/api/tclCommandPackage/")
        install_dir = pathlib.Path(__file__).parents[0]
        libOpenSeesRT_path = install_dir/'libOpenSeesRT.so'
    interp = tkinter.Tcl()
    #from . import libOpenSeesRT
    interp.eval(f"load {libOpenSeesRT_path}")
    return interp

def eval(script: str):
    interp = TclInterpreter()
    interp.eval(f"""

    {script}

    """)
    return interp


def dumps(model):
    if not isinstance(model, Component):
        from opensees.emit import OpenSeesWriter
        return OpenSeesWriter(model).dump()
    else:
        from opensees.emit.opensees import ScriptBuilder
        writer = ScriptBuilder()
        refs = {r for r in model.get_refs()}
        for ref in refs:
            writer.send(ref)

        return writer.send(model).getstr()


class TclRuntime(AbstractRuntime):
    def __init__(self,  model=None):
        from functools import partial
        self._partial = partial
        self._c_domain = None
        self._c_rt = None
        self._interp = TclInterpreter()
        if model is not None:
            self.model(model)
    
    def model(self, *args, **kwds):
        """
        model(model: opensees.model)
        model(ndm:int, ndf:int)
        """
        for arg in args:
            if isinstance(arg, int):
                pass
            else:
                self.eval("model basic 2 3")
                self.eval(dumps(arg))

    @property
    def _rt(self):
        if self._c_rt is None:
            from . import libOpenSeesRT
            self._c_rt = libOpenSeesRT.getRuntime(self._interp.tk.interpaddr())
        return self._c_rt

    @property
    def _domain(self):
        if self._c_domain is None:
            from . import libOpenSeesRT
            self._c_domain = libOpenSeesRT.get_domain(self._rt)
        return self._c_domain

    @classmethod
    def _as_tcl_arg(cls, arg):
        if isinstance(arg, list):
            return f"{{{''.join(TclRuntime._as_tcl_arg(a) for a in arg)}}}"
        elif isinstance(arg, dict):
            return "{\n" + "\n".join([
              f"{cmd} " + " ".join(TclRuntime._as_tcl_arg(a) for a in val)
                  for cmd, val in kwds
        ]) + "}"
        else:
            return str(arg)

    def _tcl_call(self, arg, *args, **kwds):
        tcl_args = [TclRuntime._as_tcl_arg(arg) for arg in args]
        tcl_args += [
          f"-{key} " + TclRuntime._as_tcl_arg(val)
              for key, val in kwds.items()
        ]
        ret = self._interp.tk.eval(
            f"{arg} " + " ".join(tcl_args))
        return ret if ret != "" else None

    def eval(self, string):
        try:
            return self._interp.tk.eval(string)
        except tkinter._tkinter.TclError as e:
            print("ERROR:", e, file=sys.stderr)

    def __getattr__(self, attr):
        return self._partial(self._tcl_call, attr)

    def fix(self, nodes, *dofs):
        if not isinstance(nodes,list):
            nodes = [nodes]
        for node in nodes:
            self.eval(f"fix {node} {' '.join(map(str,dofs))}")

    def add_tagged(self, objs):
        for k,v in objs.items():
            if isinstance(k, int):
                self.eval(v.cmd)            

# class BasicBuilder(TclRuntime):
#     def __init__(self, ndm=None, ndf=None):
#         super().__init__()
#         self.model("basic", "-ndm", ndm, "-ndf", ndf)
# 
# class SafeBuilder(TclRuntime):
#     def __init__(self, ndm=None, ndf=None):
#         super().__init__()
#         self.model("safe", "-ndm", ndm, "-ndf", ndf)

# def model(typ, *args, **kwds):
#     builder = TclRuntime()
#     builder.model(typ, *args, **kwds)
#     return builder

# def read_tcl_domain(script: str):
#     interp = TclInterpreter()
#     interp.eval(f"""
# 
#     {script}
# 
#     """)
#     builder = builders.TclModelBuilder(interp.tk.interpaddr())
#     domain = builder.getDomain()
#     return domain

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

