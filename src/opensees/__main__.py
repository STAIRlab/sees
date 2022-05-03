#!/usr/bin/env python3

import sys
import cmd
import _tkinter

__version__="0.0.0"

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
"""

#PROMPT = "\033\\[01;32mopensees\033\\[0m > "
PROMPT = "\u001b[35mopensees\u001b[0m > "

# Path to Tcl script which loads commands
INIT_TCL = ""

def parse_args(args):
    opts = {"subproc": False}
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
            elif arg == "--version":
                print(__version__)
                sys.exit()
        else:
            files.append(arg)
            break
    return files, opts, argi


from cmd import Cmd
import subprocess, queue, time, random
from threading import Thread

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

class OpenSeesShell(Cmd):
    def __init__(self):
        super().__init__()
        self.process = subprocess.Popen(
            "OpenSees",
            shell=True,
            text=True,
            universal_newlines=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        
        self.out_queue = queue.Queue()
        self.err_queue = queue.Queue()
        self.out_thread = Thread(target=enqueue_output, args=(self.process.stdout, self.out_queue))
        self.err_thread = Thread(target=enqueue_output, args=(self.process.stderr, self.err_queue))
        self.out_thread.daemon = True
        self.err_thread.daemon = True
        self.out_thread.start()
        self.err_thread.start()
        
    def default(self,line):
        self.write(line)
        time.sleep(random.uniform(0.1, 1.0))
        return self.read2()
    
    def read(self):
        return self.process.stderr.read()#.decode("utf-8").strip()
    
    def read2(self):
        outStr = ''
        try:
            while True: # Adds output from the Queue until it is empty
                outStr += self.err_queue.get_nowait()
        except queue.Empty:
            return outStr

    def write(self, message):
        self.process.stdin.write(f"{message.strip()}\n")#.encode("utf-8"))
        self.process.stdin.flush()

    def terminate(self):
        self.process.stdin.close()
        self.process.terminate()
        self.process.wait(timeout=0.2)


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

    files, opts, argi = parse_args(sys.argv)
    if len(sys.argv) == 1:
        if opts["subproc"]:
            OpenSeesShell().cmdloop()
        else:
            TclShell().cmdloop()
    else:
        import time
        tcl = opensees.tcl.TclRuntime()
        tcl.eval(f"set argc {len(sys.argv) - 2}")
        tcl.eval(f"set argv {{{' '.join(argi)}}}")
        for filename in files:
            if filename == "-":
                tcl.eval(sys.stdin.read())
            else:
                tcl.eval(open(filename).read())
                time.sleep(3)


