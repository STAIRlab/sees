
from .emitter import Emitter, ScriptBuilder


class JSON_Emitter(Emitter):
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
    
    def Ref(this, self, value=None): 
        val = self._get_value(None, value=value)
        if not isinstance(val,int):
            try:
                value = "$"+this.registry.ident(value).tclstr()
            except KeyError:
                raise KeyError(f"Unable to resolve reference to {value} when writing {this.current_obj}")
        
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


def load(model):
    nodes = {

    }