import sys
# import _pyg3
# from _pyg3 import domain, builders, analysis, Vector

# from anabel.builders import SkeletalModel as SafeBuilder

__version__ = "0.0.0"

class ScriptBuilder:
    TAB = object()
    RET = object()
    def __init__(self, obj=None):
        from io import StringIO
        self.obj = obj
        self.out = StringIO()
        self.w = self.writer()
        next(self.w)
        self.send(obj.get_cmd())
        self.w.close()
        self.script = self.out.getvalue()


    def writer(self):
        idnt = ""
        asep = " "
        while True:
            arg = (yield)
            if arg is self.TAB:
                idnt += "\t"
                print("{", file=self.out)
            elif arg is self.RET:
                idnt = idnt[:-1]
                print("\n}", file=self.out)
            else:
                print(f"{arg}", end=asep, file=self.out)

    def send(self, args, idnt=None):
        w = self.w
        idnt = idnt or ""
        print(idnt,end="", file=self.out)
        for arg in args:
            if isinstance(arg,list) and isinstance(arg[0],list):
                w.send(self.TAB)
                [self.send(a,idnt+"\t") for a in arg]
                w.send(self.RET)
            else:
                w.send(arg)
        print("", file=self.out)

def TclInterpreter():
    import tkinter, pathlib
    #install_dir = pathlib.Path("/home/claudio/sees/pyg3/src/")
    #install_dir = pathlib.Path("/home/claudio/sees/cmake-src/build/SRC/api/tclCommandPackage/")
    install_dir = pathlib.Path("/home/claudio/opensees/pyg3/libg3/build/SRC/api/tclCommandPackage/")
    interp = tkinter.Tcl()
    interp.eval(f"load {install_dir/'libOpenSeesCommandPackage.so'}")
    return interp

class TclBuilder:
    def __init__(self,  domain=None):
        from functools import partial
        self._partial = partial
        #self._domain = domain
        self._c_domain = None
        self._interp = TclInterpreter()

    @property
    def _domain(self):
        if self._c_domain:
            return self._c_domain
        else:
            self._c_domain = _pyg3.get_domain(self._interp.tk.interpaddr())
            return self._c_domain

    @classmethod
    def _as_tcl_arg(cls, arg):
        if isinstance(arg, list):
            return f"{{{''.join(TclBuilder._as_tcl_arg(a) for a in arg)}}}"
        elif isinstance(arg, dict):
            return "{\n" + "\n".join([
              f"{cmd} " + " ".join(TclBuilder._as_tcl_arg(a) for a in val)
                  for cmd, val in kwds
        ]) + "}"
        else:
            return str(arg)


    def _tcl_call(self, arg, *args, **kwds):
        tcl_args = [TclBuilder._as_tcl_arg(arg) for arg in args]
        tcl_args += [
          f"-{key} " + TclBuilder._as_tcl_arg(val)
              for key, val in kwds.items()
        ]
        ret = self._interp.tk.eval(
            f"{arg} " + " ".join(tcl_args))
        return ret if ret != "" else None

    def eval(self, string):
        return self._interp.tk.eval(string)

    def __getattr__(self, attr):
        return self._partial(self._tcl_call, attr)

    def fix(self, nodes, *dofs):
        if not isinstance(nodes,list):
            nodes = [nodes]
        for node in nodes:
            self.eval(f"fix {node} {' '.join(map(str,dofs))}")

    def pattern(self, *args):
        pass

    def add_tagged(self, objs):
        for k,v in objs.items():
            if isinstance(k, int):
                self.eval(v.cmd)
            

class BasicBuilder(TclBuilder):
    def __init__(self, ndm=None, ndf=None):
        super().__init__()
        self.model("basic", "-ndm", ndm, "-ndf", ndf)

class SafeBuilder(TclBuilder):
    def __init__(self, ndm=None, ndf=None):
        super().__init__()
        self.model("safe", "-ndm", ndm, "-ndf", ndf)

def model(typ, *args, **kwds):
    builder = TclBuilder()
    builder.model(typ, *args, **kwds)
    return builder

def read_tcl_domain(script: str):
    interp = TclInterpreter()
    interp.eval(f"""

    {script}

    """)

    builder = builders.TclModelBuilder(interp.tk.interpaddr())
    domain = builder.getDomain()
    return domain

def dumps(model, format="tcl")->str:
    """
    Return a string representation of a model.
    Formats:
    - JSON
    - Tcl
    - pyg3 | python
    """
    import anabel.writers
    writer = dict(
        json = None,
        tcl  = anabel.writers.OpenSeesWriter,
    )[format.lower()](model)

    return writer.dump()

