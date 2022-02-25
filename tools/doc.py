import re
import sys
import inspect
import textwrap
import importlib


from opensees import ast, obj


write = lambda *args, **kwds: print(*args, **kwds)

if __name__=="__main__":
    import opensees.lib

    #for lib in [opensees.section, opensees.lib, opensees.patch]:
    for lib_name in sys.argv[1:]:
        lib = importlib.import_module(lib_name)
        for k,v in lib.__dict__.items():
            if isinstance(v, type):
                if issubclass(v, obj.Component):
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

                    # write(">| | | |\n|--|--|--|")
                    # write("<table>")
                    write(textwrap.dedent("""
                    <table>
                    <colgroup>
                      <col style="width: 15%" ><col style="width: 15%" ><col style="width: 70%" >
                    </colgroup>
                    <tbody>
                    """))
                    # write("<tbody>")
                    try:
                        for a in v._args:
                            typ = a.__class__.__name__
                            #about = a.about.replace('\n',' ').strip()
                            name = a.name
                            default = " = "+a.default if a.default else ""
                            about = re.sub('[\s+]', ' ', a.about.replace('\n',' '))
                            # write(f">| {a.name} | `{typ}` |  {about} |")
                            write(f"<tr><td>{name+default}</td><td>`{typ}`</td><td>{about}</td>")
                    except:
                        pass
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
