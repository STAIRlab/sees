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
    file = None
    argi = iter(args[1:])
    for arg in argi:
        if arg[0] == "-":
            if arg == "-":
                file = "-"
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
            file = arg
            break

    if file is None:
        file = "-"

    return file, opts, argi


if __name__ == "__main__":

    file, opts, argi = parse_args(sys.argv)

    if file == "-" and sys.stdin.isatty():

        if opts["subproc"]:
            OpenSeesShell().cmdloop()
            sys.exit()

        try:
            # Try full-featured REPL
            from opensees.repl.ptkshell import OpenSeesREPL
            OpenSeesREPL().repl()

        except ImportError:
            from opensees.repl.cmdshell import TclShell
            TclShell().cmdloop()

    else:
        tcl = opensees.tcl.TclRuntime(verbose=opts["verbose"])
        tcl.eval(f"set argc {len(sys.argv) - 2}")
        tcl.eval(f"set argv {{{' '.join(argi)}}}")

        for cmd in opts["commands"]:
            tcl.eval(cmd)

        try:
            if file == "-":
                tcl.eval(sys.stdin.read())
            else:
                tcl.eval(open(file).read())
        except opensees.tcl.tkinter._tkinter.TclError:
            pass


        if opts["interact"]:
            from opensees.repl.ptkshell import OpenSeesREPL
            sys.stdin = open("/dev/tty")
            OpenSeesREPL(interp=tcl).repl()
            # TclShell(interp=tcl).cmdloop()


