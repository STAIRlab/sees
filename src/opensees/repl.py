# Claudio Perez

# https://stackoverflow.com/questions/11457931/running-an-interactive-command-from-within-python

from cmd import Cmd
import subprocess, queue, time, random
from threading import Thread

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

class OpenSeesShell(Cmd):
    def __init__(self, opensees_path=None):
        super().__init__()
        self.process = subprocess.Popen(
            opensees_path or "OpenSees",
            shell = True,
            text  = True,
            universal_newlines = True,
            stdin  = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        
        self.out_queue  = queue.Queue()
        self.err_queue  = queue.Queue()
        self.out_thread = Thread(target=enqueue_output, args=(self.process.stdout, self.out_queue))
        self.err_thread = Thread(target=enqueue_output, args=(self.process.stderr, self.err_queue))
        self.out_thread.daemon = True
        self.err_thread.daemon = True
        self.out_thread.start()
        self.err_thread.start()
        
    def default(self,line):
        self.write(line)
        return self.read2()
    
    def read(self):
        return self.process.stderr.read()#.decode("utf-8").strip()
    
    def read2(self):
        outStr = ''
        for i in range(2):
            try:
                while True: # Add output from the Queue until it is empty
                    outStr += self.err_queue.get_nowait()
                    # outStr += self.err_queue.get(timeout=.1)
            except queue.Empty:
                return outStr

    def write(self, message):
        self.process.stdin.write(f"{message.strip()}\n")#.encode("utf-8"))
        self.process.stdin.flush()
        time.sleep(random.uniform(0.5, 1.0))

    def terminate(self):
        self.process.stdin.close()
        self.process.terminate()
        self.process.wait(timeout=0.2)

o = OpenSeesShell()
print(o.read2())
o.write('puts "hello world"')
print(o.read2())
