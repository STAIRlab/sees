from .writer import ModelWriter
from opensees.ast import Arg

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
        #this.write(" ".join(map(str,self.flag + [value])))
        this.write(self.flag, str(value))

    def Lst(this, self, value=None):
        this.write(self.flag)
        this.write("{")
        for v in map(self.type, value):
            this.write(v)
        this.write("}")

    def Tag(this, self, value=None):
        value = self.value if value is None else value
        if not isinstance(value, int):
            value = this.current_tag
            this.current_tag += 1
            this.current_obj.name = value
        self.name = self.value = value
        this.write(value)

    def Flg(this, self, value=None): 
        value = self.value if value is None else value
        if value: this.write(self.flag)
        #self.write(" ".join([self.flag] if value else []))

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
        value = value.name if val is None else val
        # try:
        #     value = getattr(value, self.kwds["attr"])
        # except Exception as e:
        #     print(e)
        return this.write(self.flag,value)

    def Blk(this, self, value=None):
        value = self.get_value(value=value)
        if value is None:
            value = [None]
        #this.write(" ".join(self.flag + ["{"]))
        this.write(self.flag, "{")
        this.endln()
        this.rshift()
        for v in value:
            this.parent.send(v)
        # [this.parent.send(v) for v in value]
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
            self.current_tag = 1
            # self.tags = {}

        def write(self, *args, end=" "):
            if self.newline:
                self.newline=False
                print(self.idnt, end="", file=self.strm)
            for arg in args:
                if isinstance(arg, (int,float,str)):
                    print(f"{arg}", end=end, file=self.strm)
                else:
                    pass
                    # typ = arg.__class__.__name__
                    # if typ in dir(self):
                    #     self.write(getattr(self, typ)(arg))
                    # elif isinstance(arg, Arg):
                    #     self.write(w.Arg(arg))
                    # else:
                    #     raise ValueError()

        def endln(self):
            self.newline = True
            print("", file=self.strm)
                
        def rshift(self):
            self.idnt += "\t"

        def lshift(self):
            self.idnt = self.idnt[:-1]

    def __init__(self):
        self.streams = [ScriptBuilder.Writer(StringIO(), self)]

    def getstr(self):
        return self.streams[0].strm.getvalue()

    def send(self, obj, idnt=None):
        w = self.streams[0]
        w.write(" ".join(obj._cmd))
        w.current_obj = obj # TODO: Clean this up
        for arg in obj._args:
            typ = arg.__class__.__name__
            value = getattr(obj, arg.field)

            if typ in dir(w):
                w.write(getattr(w, typ)(arg, value=value))
            elif isinstance(arg, Arg):
                w.write(w.Arg(arg, value=value))
            else:
                raise ValueError()
        w.endln();
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
        writer = ScriptBuilder().streams[0]
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
        return writer.strm.getvalue()

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


