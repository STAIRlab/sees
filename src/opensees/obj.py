from  .ast  import *

class Component:
    def __enter__(self):
        from .tcl import TclRuntime
        self._rt = TclRuntime(self)

    def get_ast(self):
        pass

    def get_cmd(self):
        args = [
            a for arg in self._args
                for a in arg.as_tcl_list(value=getattr(self, arg.field))
        ]
        return self._cmd + args

    def get_cmd_str(self):
        for i in self.get_cmd():
            if isinstance(i,list):
                yield "{\n"
                for j in i:
                    yield f"{j}"
                yield "\n}\n"
            else:
                yield str(i)

    def __call__(self, **kwds):
        return self.copy(**kwds)

    def copy(self, **kwds):
        partial = self.__class__()
        for field in self.__slots__:
            if field in kwds:
                setattr(partial, field, kwds.pop(field))
            else:
                setattr(partial, field, getattr(self, field))
        partial.kwds.update(kwds)
        return partial

    def _init(self):
        self._argdict = {}
        for arg in self._args:
            field = arg.field
            if getattr(self, field) is None:
                try: setattr(self, field, self.kwds[arg.name])
                except Exception as e: pass
            if getattr(self, field) is None:
                try: setattr(self, field, arg._get_value(None))
                except Exception as e: pass
            if getattr(self, field) is None:
                try: setattr(self, field, getattr(
                     getattr(self, arg.kwds["alt"]), field))
                except Exception as e: pass

            self._argdict[field] = arg

    def get_refs(self):
        for ref in self._refs:
            if ref in self._argdict:
                arg = self._argdict[ref]
                val = getattr(self, arg.field)
                if isinstance(arg, Ref):
                    yield val
                elif isinstance(arg, Grp):
                    typ = arg.type.type
                    yield from val
                    #for i in val:
                    #    yield i
            else:
                val = getattr(self, ref)
                if hasattr(val, "get_refs"):
                    yield val
                    yield from val.get_refs()
                else:
                    yield from val

class Cmd:
    cmd = None
    def __init__(self, cmd , defs=None):
        self.cmd = cmd


def cmd(cls, cmd, args, refs=[], **ops):
    fields = [arg.field for arg in args] 
    alts = {arg.kwds["alt"] for arg in args if "alt" in arg.kwds}
    obj = struct(cls, fields, args, alts, refs=refs)
    obj._cmd  = [cmd]
    return obj


class LibCmd(Cmd):
    cmd = None
    def __init__(self, cmd , class_name=None, subs={}, args=None, rels=None, about="", defs=None):
        if class_name is None:
            class_name = cmd.title()
        self.class_name = class_name

        if not isinstance(cmd, str):
            self.typ = cmd
            cmd = cmd.__name__
        else:
            self.typ = None

        self.__name__ = self.cmd = cmd
        self.args = [] if args is None else args
        self.rels = [] if rels is None else rels
        self.about = about

        for sub in subs:
            setattr(self, sub, self(sub.title(), sub, args=subs[sub]))

    def __call__(self, cls, name=None, args=None, refs=None, inherit=None, **opts):
        if inherit is None: inherit = []
        if self.typ is not None: inherit.append(self.typ)
        if refs is None:
            refs = []
        
        if not isinstance(cls, str):
            if hasattr(cls, "_refs"):
                refs += cls._refs
            args = cls._args
            inherit.append(cls)
            cls = name = cls.__name__

        if name is None:
            name = cls
            
        args = self.args + args
        fields = [arg.field for arg in args]
        if "alts" in opts: fields += [a.field for a in opts["alts"]]
        alts = {arg.kwds["alt"] for arg in args if "alt" in arg.kwds}
        obj = struct(cls, fields, args, alts, refs=refs, parents=inherit)
        obj._cmd  = [self.cmd, name]
        obj.kwds = opts
        obj._class_name = self.class_name
        setattr(self, name, obj)
        return obj


def struct(name, fields, args = None, alts=None, refs=[], parents=[]):
    import textwrap
    template = textwrap.dedent("""\
    class {name}({parents}):
        __slots__ = ["_argdict"] + {fields!r}
        def __init__(self, {fields_none}, **kwds):
            {self_fields} = {args}
            self.kwds = kwds
            self._refs = {refs!r}
            self._init()
            if hasattr(self,"init"): self.init()

        def keys(self): return self.__slots__
        def __getitem__(self, idx):
            return getattr(self, idx)

    """).format(
        name=name,
        refs=refs,
        fields=fields,
        parents = ",".join(["Component"]+[p.__name__ for p in parents]),
        args=','.join(fields),
        fields_none=','.join(f"{f}=None" for f in fields),
        self_fields=','.join('self.' + f for f in fields)
    )
    d = {'fields': fields, "Arg": Arg, "Component": Component}
    d.update({c.__name__: c for c in parents})
    exec(template, d)
    d[name]._args = args
    return d[name]

def walk_refs(parent):
    P, R = "", ""
    for ref in parent.get_refs():
        print(ref)
        p, r = walk_refs(ref[0])
        P = p + P
        R = r + R
    return P, R

class _LineElement:
    pass

Mat = LibCmd("nDMaterial")
Uni = LibCmd("uniaxialMaterial")
Ele = LibCmd("element")
Trf = LibCmd("geomTransf")
Sec = LibCmd("section")
Lnk = LibCmd("rigidLink")

