import sys
import cmd
import _tkinter

__version__="0.0.0"

import opensees.tcl

HELP = """
usage: opensees <file>...

"""

#PROMPT = "\033\\[01;32mopensees\033\\[0m > "
PROMPT = "\u001b[35mopensees\u001b[0m > "

# Path to Tcl script which loads commands
INIT_TCL = ""

def parse_args(args):
    files = []
    argi = iter(args[1:])
    for arg in argi:
        if arg[0] == "-":
            if arg == "-":
                files.append("-")
            if arg == "-h" or arg == "--help":
                print(HELP)
                sys.exit()
            if arg == "--version":
                print(__version__)
                sys.exit()
        else:
            files.append(arg)
    return files, {}

class TclShell(cmd.Cmd):
    intro = """         
    OpenSees -- Open System For Earthquake Engineering Simulation
                 Pacific Earthquake Engineering Research Center
"""
    prompt = PROMPT
    file = None
    def __init__(self, *args, **kwds):
        self.tcl_interp = opensees.tcl.TclInterpreter()
        super().__init__(*args, **kwds)

    def default(self, arg):
        try:
            return self.tcl_interp.eval(arg) or None
        except _tkinter.TclError as e:
            print(e)

    def precmd(self, line):
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def completedefault(self, text, line, begidx, endidx):
        print(text,line,begidx,endidx)
        return ["hi"]

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == "__main__":

    if len(sys.argv) == 1:
        TclShell().cmdloop()
    else:
        files, opts = parse_args(sys.argv)
        tcl = opensees.tcl.TclInterpreter()
        for filename in files:
            if filename == "-":
                tcl.eval(sys.stdin.read())
            else:
                tcl.eval(open(filename).read())


