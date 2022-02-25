from  .ast  import *
from typing import get_type_hints

class Component:
    @staticmethod
    def get_value(cls, arg, value):
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

    def get_refs(self):
        for arg in self._args:
            if arg.field in self._refs:
                if isinstance(arg, Ref):
                    yield (getattr(self, arg.field), arg.type)
                elif isinstance(arg, Grp):
                    typ = arg.type.type
                    for i in getattr(self, arg.field):
                        yield (i, typ)

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
    def __init__(self, cmd , subs={}, args=None, rels=None, defs=None):
        self.cmd = cmd
        self.args = [] if args is None else args
        self.rels = [] if rels is None else rels

        for sub in subs:
            setattr(self, sub, self(sub.title(), sub, args=subs[sub]))

    def __call__(self, cls, name=None, args=None, refs=[], **opts):
        if isinstance(cls,str):
            typ = []
        else:
            args = cls._args
            typ = [cls]
            cls = name = cls.__name__

        args = self.args + args
        fields = [arg.field for arg in args]
        if "alts" in opts: fields += [a.field for a in opts["alts"]]
        alts = {arg.kwds["alt"] for arg in args if "alt" in arg.kwds}
        obj = struct(cls, fields, args, alts, refs=refs, parents=typ)
        obj._cmd  = [self.cmd, name]
        obj.kwds = opts
        setattr(self, name, obj)
        return obj


def struct(name, fields, args = None, alts=None, refs=[], parents=[]):
    import textwrap
    template = textwrap.dedent("""\
    class {name}({parents}):
        __slots__ = {fields!r}
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

Mat = LibCmd("nDMaterial")
Uni = LibCmd("uniaxialMaterial")
Ele = LibCmd("element")
Trf = LibCmd("geomTransf")
Sec = LibCmd("section")
Lnk = LibCmd("rigidLink")

def walk_refs(parent):
    P, R = "", ""
    for ref in parent.get_refs():
        print(ref)
        p, r = walk_refs(ref[0])
        P = p + P
        R = r + R
    return P, R

