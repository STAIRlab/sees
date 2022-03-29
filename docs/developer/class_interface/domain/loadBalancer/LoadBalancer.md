\
# LoadBalancer 

```cpp
#include <domain/loadBalancer/LoadBalancer.h>
```

class LoadBalancer\

\

A LoadBalancer is an object used to balance a PartitionedDomain. The
LoadBalancer does this by invoking methods in the DomainPartitioner
object with which it is associated.

### Constructor

\
### Destructor

\
// Public Methods\

\

// Public Methods\

\

Sets the pointer to the associated PartitionedDomain to be $0$.

\
Does nothing. Provided so the subclasses destructor will be called.

\
Sets the pointer to the DomainPartitioner object associated with the
LoadBalancer to point to *thePartitioner*.

```{.cpp}
virtual int balance(Graph &theWeightedGraph) =0;
```

Each subclass must provide an implementation of this method. This method
is invoked to balance the PartitionedDomain. The Graph
*theWeightedGraph* is a weighted graph in which the vertices represent
the Subdomains, the edges Subdomains sharing common boundary nodes and
the weight the cost of the previous Subdomain calculations (determined
by invoking `getCost()` on the Subdomains).

\
Returns a pointer to the DomainPartitioner. If no DomainPartitioner has
been set, a warning message is printed and $0$ returned.
