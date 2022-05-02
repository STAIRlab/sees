
# ShedHeaviest 

```cpp
#include <domain/loadBalancer/ShedHeaviest.h>
```

class ShedHeaviest: public LoadBalancer\

LoadBalancer\

\
A ShedHeaviest is an object used to balance a PartitionedDomain. It does
this by shedding the boundary vertices on the heaviest loaded partition
(subdomain).

### Constructors

\

### Destructor

\
// Public Methods\

\

\
Sets *numRealeases* to $1$ and *factorGreater* to $1.0$. These are the
paramemeters used in the `balance()` method.

Sets the parameters used in the `balance()` method.

\
Does nothing.

\
The heaviest loaded partition, *max*, is first determined by iterating
through the Graph *theWeightedGraph* looking at the vertex weights. Then
*releaseBoundary(max, theWieightedGraph, true, factorGreater)* is
invoked on the DomainPartitioner *numRelease* times. Returns $0$ if
successful, otherwise a negative number and a warning message are
returned if either no link has been set to the DomainPartitioner or
`releaseBoundary()` returns a negative number.
