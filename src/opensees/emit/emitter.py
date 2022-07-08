
from io import StringIO 
from .registry import Registry

class ObjectSerializationError(Exception): pass

class Emitter:
    def __init__(self, strm, parent):
        self.idnt = ""
        self.strm = strm
        self.parent = parent
        self.refs = set()
        self.newline = True
        self.registry = Registry()
        # self.tags = {}

    def write(self, *args, end=" "):
        if self.newline:
            self.newline=False
            print(self.idnt, end="", file=self.strm)
        for arg in args:
            if isinstance(arg, (int,float,str)):
                print(f"{arg}", end=end, file=self.strm)
            else:
                raise ValueError()

    def endln(self):
        self.newline = True
        print("", file=self.strm)
            
    def rshift(self):
        self.idnt += "\t"

    def lshift(self):
        self.idnt = self.idnt[:-1]

class ScriptBuilder:
    # TAB = object()
    # RET = object()

    def __init__(self, emitter):
        self.sent = set()
        self.streams = [emitter(StringIO(), self)]
        self.python_objects = {}

    def __repr__(self):
        return self.getScript()

    def getIndex(self):
        return "\n".join(
            (f"set {i.tclstr()} {tag}" 
                for i,tag in self.registry.index().items())
        )

    def getScript(self, indexed=True)->str:
        index = self.getIndex() if indexed else ""
        return "\n\n".join((index, self.streams[0].strm.getvalue()))
    
    @property
    def registry(self):
        return self.streams[0].registry

    def send(self, obj, idnt=None):
        w = self.streams[0]

        if isinstance(obj, (list,tuple)):
            #import sys
            for i in obj:
                #print(i, file=sys.stderr)
                self.send(i)
            return self

        elif not hasattr(obj,"_args"):
            raise ObjectSerializationError(f"object {obj}")
        
        if self.registry.registered(obj):
            return self

        for ref,tag_space in obj.get_refs():
            try: 
                self.send(ref)

            except ObjectSerializationError:
                ident = self.registry.register(ref, tag_space=tag_space)
                self.python_objects[ident] = ref

        w.write(" ".join(obj._cmd))
        w.current_obj = obj # TODO: Clean this up

        for arg in obj._args:
            typ = arg.__class__.__name__
            value = getattr(obj, arg.field)

            try:
                getattr(w, typ)(arg, value=value)
            except AttributeError:
                w.Arg(arg, value=value)

        w.endln();

        if not self.registry.registered(obj):
            self.registry.register(obj)

        return self

