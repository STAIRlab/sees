


\#include $<\tilde{}$/Timer/Timer.h$>$



class Timer: public MovableObject



MovableObject






A Timer object is an object which can be used to measure system
resources, i.e. cpu time and memory usage. Currently for Unix systems
only. COMPILE FLAG NEEDED.

































Does nothing.




Does nothing.




Sets the accounting variables to mark the start of accounting period
using the unix functions `times()` and *getrusage*.

Sets the accounting variables to mark the end of accounting period using
the unix functions `times()` and *getrusage*.
 Uses the difference between the starting and ending accounting
variables to determine the elapsed real time between the last calls to
`start()` and `pause()`. Returns this value in units of seconds.

Uses the difference between the starting and ending accounting variables
to determine the CPU time allocated the process between the last calls
to `start()` and `pause()`. Returns this value in units of seconds.

Uses the difference between the starting and ending accounting variables
to determine the number of page faults that required reading of pages
from disk between the last calls to `start()` and `pause()`. Returns
this value.

Uses the difference between the starting and ending accounting variables
to determine the real time, CPU time, operating system time allocate the
process, total number of page faults, number of page faults that
required reading of pages from memory, and number of page faults that
required no reading from disk between the last calls to `start()` and
`pause()`. Send these values to *s*.

Invokes `Print(s)` on the Timer object *E*.
