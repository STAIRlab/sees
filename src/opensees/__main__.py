#!/usr/bin/env python3
"""
"""

import sys

import opensees
import opensees.tcl

HELP = """\
usage: opensees <file> [args]...
                [options] <file> [args]...
                <command> ...

                -trans        Transient analysis
                -eigen        Eigenvalue analysis returning frequencies
                -modes        Eigenvalue analysis returning modes
                -displ        Displacement-controlled static analysis
                -force        Force-controled static analysis
                -modal        Modal response history

       opensees -print
       opensees -json
       opensees -emit

Options
  -v/--verbose

  -c <command>
"""

# PROMPT = "\033[01;31mopensees\033[0m > "
# PROMPT = "\u001b[35mopensees\u001b[0m > "
# "\N{Lower Left Triangle} "
PROMPT = "\033[33mopensees\033[0m \N{WHITE PARALLELOGRAM} "


def parse_args(args):
    opts = {
        "subproc": False,
        "verbose": False,
        "interact": False,
        "commands": []
    }
    files = []
    argi = iter(args[1:])
    for arg in argi:
        if arg[0] == "-":
            if arg == "-":
                files.append("-")
            if arg == "-h" or arg == "--help":
                print(HELP)
                sys.exit()
            elif arg == "-modes":
                import opensees.eigen
                opensees.eigen.modes(*argi)
                sys.exit()

            elif arg == "-eigen":
                import opensees.eigen
                opensees.eigen.eigen(*argi)
                sys.exit()

            elif arg == "--subproc":
                opts["subproc"] = True

            elif arg == "--version" or arg == "-version":
                print(opensees.__version__)
                sys.exit()

            elif arg == "-v":
                opts["verbose"] = True

            elif arg == "-c":
                opts["commands"].append(next(argi))

            elif arg == "-i":
                opts["interact"] = True


        else:
            files.append(arg)
            break

    return files, opts, argi


if __name__ == "__main__":

    files, opts, argi = parse_args(sys.argv)

    if len(sys.argv) == 1:
        if opts["subproc"]:
            OpenSeesShell().cmdloop()
            sys.exit()

        try:
            from opensees.repl import OpenSeesREPL
            OpenSeesREPL().repl()
        except:
            from opensees.repl.cmdshell import TclShell
            TclShell().cmdloop()

    else:
        tcl = opensees.tcl.TclRuntime(verbose=opts["verbose"])
        tcl.eval(f"set argc {len(sys.argv) - 2}")
        tcl.eval(f"set argv {{{' '.join(argi)}}}")

        for cmd in opts["commands"]:
            tcl.eval(cmd)

        for filename in files:
            try:
                if filename == "-":
                    tcl.eval(sys.stdin.read())
                else:
                    tcl.eval(open(filename).read())
            except:
                pass
                #tcl.eval("puts $errorInfo")

        if opts["interact"]:
            from opensees.repl import OpenSeesREPL
            OpenSeesREPL(interp=tcl).repl()
            # TclShell(interp=tcl).cmdloop()


