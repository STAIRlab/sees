import os
import sys
import tkinter
import pathlib

def TclInterpreter():
    if "OPENSEESRT_LIB" in os.environ:
        libOpenSeesRT_path = os.environ["OPENSEESRT_LIB"]
    else:
        install_dir = pathlib.Path("/home/claudio/opensees/pyg3/libg3/build/SRC/api/tclCommandPackage/")
        libOpenSeesRT_path = install_dir/'libOpenSeesRT.so'
    interp = tkinter.Tcl()
    interp.eval(f"load {libOpenSeesRT_path}")
    return interp


class TclWriter:
    def Arg(this, self, value=None)->list:
        value = self._get_value(None, value)
        if isinstance(value, (type(None), )):
            if not self.reqd:
                return []
            else:
                value = f"${self.name}"
        elif isinstance(value, (Arg,)):
            if not self.reqd:
                return []
            else:
                value = f"${value.name}"
        return self.flag + [value] 

    def Flg(this, self, value=None): 
        value = self.value if value is None else value
        return [self.flag] if value else []

    def Grp(this, self, value=None):
        value = self._get_value(None,value)
        if value is None:
            if self.reqd:
                value = [None]*self.num
            else:
                return []
        return self.flag + [a for arg,v in zip(self.args,value) for a in arg.as_tcl_list(v)]
    
    def Ref(this, self, value=None): 
        value = self._get_value(None, value)
        try:
            value = getattr(value, self.kwds["attr"])
        except:
            pass
        return self.flag + [value]

    def Blk(this, self, value=None):
        value = self.value if value is None else value
        if value is None:
            value = [None]
        return self.flag + [[v.get_cmd() for v in value]]

    def Map(this, self, value=None):
        value = self._get_value(None,value)
        if value is None:
            if self.reqd:
                value = [None]*self.num
            else:
                return []
        vals = []
        i, j = (1, 0) if self.tcl_rev_kv else (0, 1)
        for arg, kv in zip(arg,value.items()):
            kv = kv[0], arg.as_tcl_list(kv[1])
            vals = vals + [kv[i], kv[j]]
        return self.flag + vals


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

class TclRuntime:
    def __init__(self,  model=None):
        from functools import partial
        self._partial = partial
        self._c_domain = None
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
                self.eval(ScriptBuilder(arg).script)

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

class BasicBuilder(TclRuntime):
    def __init__(self, ndm=None, ndf=None):
        super().__init__()
        self.model("basic", "-ndm", ndm, "-ndf", ndf)

class SafeBuilder(TclRuntime):
    def __init__(self, ndm=None, ndf=None):
        super().__init__()
        self.model("safe", "-ndm", ndm, "-ndf", ndf)

def model(typ, *args, **kwds):
    builder = TclRuntime()
    builder.model(typ, *args, **kwds)
    return builder

def eval(script: str):
    interp = TclInterpreter()
    interp.eval(f"""

    {script}

    """)
    return interp

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
    if {$options(-verbose)} {
      # puts "Angular frequency (rad/s): $omega\n";
      # puts "Frequency (Hz):            $f\n";
      # puts "Periods (sec):             $T\n";
    }

    if {$options(-file) != 0} {
      source /home/claudio/brace/Scripts/OpenSeesScripts/brace2.tcl
      brace2::io::write_modes $options(-file) $options(-numModes)
    }

    foreach recorder $recorders {
      remove recorder $recorder
    }
    """)
    return interp

