\
# FEM_ObjectBroker 

```cpp
#include <actor/objectBroker/FEM_ObjectBroker.h>
```

class FEM_ObjectBroker\

\

FEM_ObjectBrokers is an object used to create a new blank of a certain
type in a process. The explicit type of object created depends on the
method invoked and the integer *classTag* passed as an argument to the
method. Once the object has been created, `recvSelf()` can be invoked on
the object to instantiate the object with it's data.

### Constructor

\
### Destructor

\
// Public Methods to get new Domain objects\

\

\

\

\
// Public Methods to get New Matrix,Vector and ID objects - NOT USED\

\

\
// Public Methods to get new Analysis objects - NOT NEEDED SEQUENTIAL\

\

\

\

\

\

\

\

// Public Methods for Parallel Model Generation\

\

\
Does nothing.

\
Does nothing.

