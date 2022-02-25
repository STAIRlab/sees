import re
import sys
import inspect
import textwrap
import importlib


from opensees import ast, obj


write = lambda *args, **kwds: print(*args, **kwds)

def write_grp(a):
    args = (write_grp(i) if isinstance(i, ast.Grp) else (i.name if i.name else "") for i in a.args)
    return "["+",".join(args)+"]"
    #write(f"<td>`{name}`</td><td>`typ`</td><td>{about}", end="")

def write_arg(a):
    write("<tr>",end="")
    typ = f"<code>{a.__class__.__name__}</code>"
#about = a.about.replace('\n',' ').strip()
    name = a.name or ""
    default = " = "+str(a.default) if a.default else ""
    about = re.sub('[\s+]', ' ', a.about.replace('\n',' '))
    # write(f">| {a.name} | `{typ}` |  {about} |")

    if isinstance(a, ast.Grp):
        if name == "":
            name = f"<code>{write_grp(a)}</code>"
            #grp = ""
        else:
            typ = f"<code>{write_grp(a)}</code>"
        write(f"<td>{name+default}</td><td>{typ}</td><td>{about}", end="")
        #write(grp)
        write("<table>")
        [write_arg(i) for i in a.args]
        write("</table>")
    else:
        write(f"<td>{name+default}</td><td>{typ}</td><td>{about}", end="")

    write("</tr>")


if __name__=="__main__":
    import opensees.lib

    #for lib in [opensees.section, opensees.lib, opensees.patch]:
    for lib_name in sys.argv[1:]:
        lib = importlib.import_module(lib_name)
        write(textwrap.dedent(f"""
        ---
        title: {lib_name}
        ...

        # `{lib_name}`

        """))
        for k,v in lib.__dict__.items():
            if isinstance(v, type):
                if issubclass(v, obj.Component) and hasattr(v, "_args"):
                    #print(k)
                    s = str(inspect.signature(v))
                    #write("::: admonition\n\n``` python")
                    write(textwrap.dedent(f"""
                    <blockquote>
                    <pre><!-- <code class="python"> -->
                        <span style="color:#900">{k}</span>{s.replace('=None','')}
                    <!-- </code> --> </pre>
                    """))
                    try:
                        write(v.about)
                    except:
                        pass
                    if hasattr(v, "_img"):
                        write(f"![](/figures/{v._img})")

                    # write(">| | | |\n|--|--|--|")
                    # write("<table>")
                    write(textwrap.dedent("""
                    <table>
                    <colgroup>
                      <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
                    </colgroup>
                    <tbody>
                    """))
                    # write("<tbody>")
                    try:
                        pass
                    except Exception as e:
                        print(e, file=sys.stderr)
                    if True:
                        for a in v._args:
                            write_arg(a)

                    write(textwrap.dedent("""
                    </tbody>
                    </table>
                    </blockquote>
                    """))
                    #write(":::\n")
            else:
                pass
                #print(type(v))
                #print(k)
