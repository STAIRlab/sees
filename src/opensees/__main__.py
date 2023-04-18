#!/usr/bin/env python3
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

  -i                          interactive

  -c <command>
"""

# PROMPT = "\033[01;31mopensees\033[0m > "
# PROMPT = "\u001b[35mopensees\u001b[0m > "
# "\N{Lower Left Triangle} "
PROMPT = "\033[33mopensees\033[0m \N{WHITE PARALLELOGRAM} "


def parse_args(args):
    opts = {
        "subproc": False,
        "preload": True,
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
                import opensees.repl.eigen
                opensees.repl.eigen.modes(*argi)
                sys.exit()

            elif arg == "-eigen":
                import opensees.repl.eigen
                opensees.repl.eigen.eigen(*argi)
                sys.exit()

            elif arg == "--subproc":
                opts["subproc"] = True

            elif arg == "--no-load":
                opts["preload"] = False

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
            file = arg if file is None else file
            break


    return file, opts, argi


if __name__ == "__main__":

    file, opts, argi = parse_args(sys.argv)

    tcl = opensees.tcl.TclRuntime(verbose=opts["verbose"], preload=opts["preload"])

    not_piped = sys.stdin.isatty()

    if len(sys.argv) == 1 and not_piped:

        if opts["subproc"]:
            OpenSeesShell().cmdloop()
            sys.exit()

        try:
            # Try full-featured REPL
            from opensees.repl.ptkshell import OpenSeesREPL
            OpenSeesREPL(interp=tcl).repl()

        except ImportError:
            from opensees.repl.cmdshell import TclShell
            TclShell().cmdloop()

    else:
        argv = list(argi)
        tcl.eval(f"set argc {len(argv)+1}")
        tcl.eval(f"set argv {{{file} {' '.join(argv)}}}")

        script = None
        run_cmds = "before"
        if (not not_piped) and (len(sys.argv) == 1 or file == "-" or (file is None)): # and len(opts["commands"]) == 0):
            script = sys.stdin.read()
            run_cmds = "after"

        elif file is not None:

            try:
                script = open(file).read()
            except FileNotFoundError as e:
                print(e, file=sys.stderr)
                sys.exit(1)

            run_cmds = "before"


        if run_cmds == "before":
            for cmd in opts["commands"]:
                tcl.eval(cmd)

        if script is not None:
            try:
                print(tcl.eval(script))

            except opensees.tcl.tkinter._tkinter.TclError as e:
                print(e, file=sys.stderr)
                if not opts["interact"]:
                    sys.exit(1)

        if run_cmds == "after":
            for cmd in opts["commands"]:
                tcl.eval(cmd)

        if opts["interact"]:
            from opensees.repl.ptkshell import OpenSeesREPL
            # TODO: do something for windows
            sys.stdin = open("/dev/tty")
            OpenSeesREPL(interp=tcl).repl()
            # TclShell(interp=tcl).cmdloop()


