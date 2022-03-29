\
# MachineBroker 

```cpp
#include <actor/machineBroker/MachineBroker.h>
```

class MachineBroker\

\

MachineBrokers are objects that are used to start remote processes
running on the parallel machine.

### Constructor

\
### Destructor

\
// Public Member Functions\

\

\

Does nothing.

\
Invoked to start the program, *actorProgram*, on the parallel machine.
The remote actor process uses information supplied by *theChannel* to
allow the remote process to connect to the local process. The integer
*compDemand* provides an indication of the computational demands of the
remote process in a heterogeneous environment.

