
```cpp
#include <domain/loadBalancer/ReleaseHeavierToLighterNeighbours.h>
```


clas ReleaseHeavierToLighterNeighbours: public LoadBalancer\

LoadBalancer\

\
A ReleaseHeavierToLighterNeighbours is an object used to balance a
PartitionedDomain. It does this by shedding the boundary vertices on the
heaviest loaded partition (subdomain).

// Constructors\

\

// Destructor\

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
For *numRelease* times the Vertices of *theWeightedGraph* are iterated
through. For each Vertex, $i$, *releaseBoundary(i, theWeightedGraph,
true, factorGreater)* is invoked on the DomainPartitioner. Returns $0$
if successful, otherwise a negative number and a warning message are
returned if either no link has been set to the DomainPartitioner or
`releaseBoundary()` returns a negative number.
