from .writer import ModelWriter
from opensees.ast import Arg
from collections import defaultdict

class Identifier: 
    def __init__(self, tag_space, space_name):
        self.nm = (tag_space, space_name)

    def __hash__(self):
        return hash(self.nm)

    def tclstr(self):
        return f"{self.nm[0]}({self.nm[1]})"

class TagSpace:
    def __init__(self):
        self.current_tag = 1
        self.obj_by_tag = {}
        self.tag_by_obj = {}
        self.forced_tags = set()
        self.forced_names = set()
    
    def __getitem__(self, name):
        return self.tag_by_obj[name]

    def new_tag(self):
        t = self.current_tag
        while t in self.forced_tags: t += 1
        self.current_tag = t + 1
        return t

    def add(self, name, force_tag=None)->bool:
        if force_tag is not None:
            tag = force_tag
            if force_tag in self.forced_tags:
                raise ValueError("Duplicate forced tag:" + 
                        f"{name} and {self.obj_by_tag[force_tag]}"
                )
            elif tag in self.obj_by_tag:
                new_tag = self.new_tag()
                old_obj = self.obj_by_tag[tag]
                self.tag_by_obj[old_obj] = new_tag
                self.obj_by_tag[new_tag] = old_obj
            self.forced_tags.add(force_tag)
        else:
            tag = self.new_tag()

        self.tag_by_obj[name] = tag
        self.obj_by_tag[tag] = name
        return True

class Registry:
    def __init__(self):
        self.tag_spaces = defaultdict(TagSpace)
        self.identifiers = {}
        self.objects = {}
        self.anonid = 1

    def __getitem__(self, tag_space: str)->TagSpace:
        return self.tag_spaces[tag_space]

    def registered(self, obj):
        return id(obj) in self.objects

    def register(self, obj, name=None, tag_space=None, force_tag=None) -> Identifier:
        ts = tag_space or obj.tag_space

        if force_tag is not None:
            id2 = str(force_tag)
        elif name is None:
            # Anonymous
            assert obj is not None
            id2 = f"<{self.anonid}>"
            self.anonid += 1
        else:
            id2 = str(name)

        self.tag_spaces[ts].add(id2, force_tag=force_tag)

        ident = Identifier(ts, id2)
        self.objects[id(obj)] = ident
        self.identifiers[ident] = id(obj)
        return ident

    def index(self)->dict:
        return {
            i: self.tag_spaces[i.nm[0]][i.nm[1]]
            for i in self.identifiers if i.nm[0] is not None
        }

    def ident(self, obj)->Identifier:
        return self.objects[id(obj)]


class TclWriter:
    def Arg(this, self, value=None)->list:
        if self.__class__.__name__ in dir(this):
            getattr(this, self.__class__.__name__)(self, value=value)
            return

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
        this.write(self.flag, str(value))

    def Lst(this, self, value=None):
        this.write(self.flag)
        this.write("{")
        for v in map(self.type, value):
            this.write(v)
        this.write("}")

    def Tag(this, self, value=None):
        value = self.value if value is None else value

        if isinstance(value, int):
            force_tag = value
        else:
            force_tag = None

        ident = this.registry.register(this.current_obj, name=value, force_tag=force_tag)

        this.write("$"+ident.tclstr())

    def Flg(this, self, value=None): 
        value = self.value if value is None else value
        if value: this.write(self.flag)

    def Grp(this, self, value=None):
        val = self._get_value(None,value)
        if value is None:
            if self.reqd:
                value = [None]*self.num
            else:
                return []        
        if "reverse" in self.kwds and self.kwds["reverse"]:
            value = reversed(value)

        this.write(self.flag)
        if not hasattr(value,"__len__") or len(self.args) == len(value):
            for a,v in zip(self.args, value):
                this.Arg(a, value=v)
        else:
            assert "min" in self.kwds
            assert len(self.args) == 1
            for v in value:
                this.Arg(self.args[0], value=v)


        # this.write(self.flag, " ".join(map(str,(
        #     a for arg,v in zip(self.args,value) for a in arg.as_tcl_list(v)
        # ))))
        # [this.parent.send(v) for v in value]
    
    def Ref(this, self, value=None): 
        val = self._get_value(None, value=value)
        #value = value.name if val is None else val
        if val is None:
            value = "$"+this.registry.ident(value).tclstr()
        else:
            value = val
        return this.write(self.flag,value)

    def Blk(this, self, value=None):
        value = self.get_value(value=value)
        if value is None:
            value = [None]
        this.write(self.flag, "{")
        this.endln()
        this.rshift()
        for v in value:
            this.parent.send(v)
        this.lshift()
        this.write("}")

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

        return this.write(self.flag, *vals)

from io import StringIO 

class ObjectSerializationError(Exception): pass

class ScriptBuilder:
    TAB = object()
    RET = object()
    class Writer(TclWriter):
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

    def __init__(self):
        self.sent = set()
        self.streams = [ScriptBuilder.Writer(StringIO(), self)]
        self.python_objects = {}

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

        if not hasattr(obj,"_args"):
            raise ObjectSerializationError()
        
        if self.registry.registered(obj):
            return self

        for ref in obj.get_refs():
            try: self.send(ref)

            except ObjectSerializationError:
                ident = self.registry.register(ref)
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


class OpenSeesWriter(ModelWriter):
    def __init__(self, model=None):
        if hasattr(model,"apply"):
            model = model.apply(model.prototypes)
        self.model = model
        self.comment_char = "#"

    def dump_initialize(self, definitions={}):
        cmds = "# Parameters\n" + "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n\n"
        ndm, ndf = self.model.ndm, self.model.ndf
        dof_keys = "dx dy dz rx ry rz"
        dofs = " ".join( str(i) for i in range(1, ndf + 1))
        cmds += f"# Create ModelBuilder (with {ndm} dimensions and {ndf} DOF/node)\n"
        cmds += f"model BasicBuilder -ndm {ndm} -ndf {ndf}\n"
        cmds += f"lassign {{{dofs}}} {dof_keys}"
        return cmds

    def dump_elements(self, *elems, definitions={}):
        transforms = set()
        cmds = "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n"
        for i, el in enumerate(elems):
            #el.init()
            if el.name is None:
                el.name = i+1
            try:
                cmds += "\nelement " + " ".join(str(p) for p in el.ops_elem.serialize(tag=i))
            except:
                cmds += "\n" + " ".join(el.get_cmd_str()) + "\n"

            if hasattr(el, "_transform") and el._transform:
                transforms.update({el._transform})

        return "".join(" ".join(t.get_cmd_str()) + "\n" for t in transforms) + cmds

    @classmethod 
    def dump_sections(self, *sections, definitions={}):
        cmds = "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n"
        for sect in sections:
            cmds += " ".join(sect.get_cmd_str()) + "\n"
        return cmds
    
    def dump_materials(self, *materials, definitions={}):
        builder = ScriptBuilder()
        writer = builder.streams[0]
        cmds = "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n"
        writer.write(
            "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n"
        )
        all_materials = self.model.materials
        for i,mat in enumerate(all_materials):
            if mat.name is None:
                mat.name = i+1
            cmds += " ".join(mat.get_cmd_str()) + "\n"
            writer.parent.send(mat)
        return builder.getScript()

    def dump_constraints(self, definitions={}):
        cmds = "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n"
        for n in self.model.nodes:
            if 'boun' in n.kwds and any(n.kwds["boun"]):
                cmds += f"fix {n.name} {' '.join(str(i) for i in n.kwds['boun'])}\n"

        return cmds

    def dump_connectivity(self, definitions={}):
        cmds = "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n"
        for i,nd in enumerate(self.model.nodes):
            nd.name = i + 1
            cmds +=  " ".join(nd.get_cmd_str()) + "\n"
        cmds += self.dump_elements(*self.model.elems)
        return cmds


