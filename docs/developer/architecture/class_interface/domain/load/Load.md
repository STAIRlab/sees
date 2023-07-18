# Load 

```cpp
#include <domain/load/Load.h>

class Load: public DomainComponent
```


Load is an abstract base class. A Load object is used to add load to the
domain. The Load class defines one method in its interface
`applyLoad()`, a method all subclasses must implement.

### Constructor




// Public Methods\

\

\

Constructs a load with a tag given by *tag* and a class tag is given by
*classTag*. These are passed to the DomainComponent constructor.

\

\
The load object is to add *loadFactor* times the load to the
corresponding residual value at its associated element(s) or node(s).

To set the tag of the enclosing load pattern for the load to be
*loadPatternTag*.

To return the current load pattern tag associated with the load. If no
load pattern tag has been set $-1$ is returned.
