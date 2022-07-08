import re
import sys
import inspect
import textwrap
import importlib

from opensees.emit.writer import ModelWriter
from opensees.emit.emitter import Emitter, ScriptBuilder
from opensees.ast import Arg
from opensees import ast

def write_grp(a):
    args = (write_grp(i) if isinstance(i, ast.Grp) else (i.name if i.name else "") for i in a.args)
    return "["+",".join(args)+"]"
    #write(f"<td>`{name}`</td><td>`typ`</td><td>{about}", end="")


def write_obj(v, w):
    name = v.__name__
    s = str(inspect.signature(v)).replace('=None','')
    if len(s) > 65:
        s = s.replace(", ", ",<br>&emsp;&emsp;&emsp;")
    w.write(textwrap.dedent(f"""
    <span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
        <span style="color:#900">{name}</span>{s}
    </span>
    """))
    try:
        w.write(v.about)
    except:
        w.write(v.__doc__ or "")
    if hasattr(v, "_img"):
        w.write(f"![](/figures/{v._img})")


    w.write(textwrap.dedent("""
    <div>
    <table>
    <!-- <colgroup>
      <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
    </colgroup> -->
    <tbody>
    """))

    # for a in v._args:
    #     # print(a, file=sys.stderr)
    #     write_arg(a)

class ApiEmitter(Emitter):
    def Arg(this, a, value=None)->list:

        if a.__class__.__name__ in dir(this):
            getattr(this, a.__class__.__name__)(a)
            return
        name = a.name or ""
        default = " = "+str(a.default) if a.default else ""
        about = re.sub('[\s+]', ' ', a.about.replace('\n',' '))
        try:
            typ = f'<code style="white-space: nowrap;">{a.type.__name__}</code>'
        except:
            typ = f"<code>{a.__class__.__name__}</code>"
        this.write(f"<td>{name+default}</td><td>{typ}</td><td>{about}")


    def Lst(self, arg, value=None):
        self.write(f"Array[{arg.type.__name__}]")

    def Tag(this, self, value=None):
        pass


    def Flg(this, self, value=None): 
        value = self.value if value is None else value
        if value: this.write(self.flag)

    def Grp(this, a, value=None):
        name = (a and a.name) or ""
        default = " = "+str(a.default) if a.default else ""
        about = re.sub('[\s+]', ' ', a.about.replace('\n',' '))
        try:
            typ = f"<code>{a.__class__.__name__}({a.type.__name__})</code>"
        except:
            typ = f"<code>{a.__class__.__name__}</code>"

        if name == "":
            name = f"<code>{write_grp(a)}</code>"
        else:
            typ = f"<code>{write_grp(a)}</code>"
        #this.write(f"<td>{name+default}</td><td>{typ}</td><td>{about}")
        this.write(f'<td colspan="2">{name+default}</td><td>{typ}, {about}')
        this.endln()
        #this.rshift()
        this.write("<table>")
        for i in a.args:
            this.endln()
            this.write("<tr>")
            this.Arg(i)
            this.write("</tr>")
        this.write("</td></table>")
        #this.lshift()
    
    def Ref(this, a, value=None): 
        name = a.name or ""
        default = " = "+str(a.default) if a.default else ""
        about = re.sub('[\s+]', ' ', a.about.replace('\n',' '))
        typ = f"<code>{a.__class__.__name__}({a.type.__name__})</code>"
        this.write(f"<td>{name+default}</td><td>{typ}</td><td>{about}")

    # def Blk(this, self, value=None):
    #     value = self.get_value(value=value)
    #     if value is None:
    #         value = [None]
    #     this.write(self.flag, "{")
    #     this.endln()
    #     this.rshift()
    #     for v in value:
    #         this.parent.send(v)
    #     this.lshift()
    #     this.write("}")

    def Map(this, a, value=None):
        typ = f"<code>{a.__class__.__name__}</code>"
        # about = a.about.replace('\n',' ').strip()
        name = a.name or ""
        default = " = "+str(a.default) if a.default else ""
        about = re.sub('[\s+]', ' ', a.about.replace('\n',' '))
        typ = f"<code>{a.__name__}</code>"
        this.write(f"<td>{name+default}</td><td>{typ}</td><td>{about}", end="")
        this.write("<table>")
        this.Arg(a.key_type)
        this.Arg(a.val_type)
        this.write("</table>")


class ApiDocWriter(ScriptBuilder):
    def __init__(self):
        ScriptBuilder.__init__(self, ApiEmitter)

    def send(self, obj, idnt=None):
        w = self.streams[0]        

        write_obj(obj, w)
        w.endln();

        for arg in obj._args:
            w.write("<tr>")
            typ = arg.__class__.__name__
            
           # try:
           #     getattr(w, typ)(arg)
           # except AttributeError:
            w.Arg(arg)
            # try:
            #     w.Arg(arg)
            # except Exception as e:
            #     print(e, file=sys.stderr)

            w.write("</tr>")
            w.endln();

        w.write(textwrap.dedent("""
        </tbody>
        </table>
        </div>
        """))

        w.endln();

        return self


if __name__ == "__main__": 
    import opensees

    _, module, obj = sys.argv[1].split(".")

    print(ApiDocWriter().send(
        getattr(getattr(opensees, module), obj)
        ))



