UNDER CONSTRUCTION


# DomainPartitioner 

```cpp
#include <domain/partitioner/DomainPartitioner.h>
```

class DomainPartitioner\

\

A DomainPartitioner is an object used to partition and load balance a
PartitionedDomain. The DomainPartitioner uses the element graph of the
domain to partition and load balance. Derived types can use the node
graph of the domain. The partitioner uses a GraphPartitioner and a
LoadBalancingAlgo to partition and load balance the domain.

// Constructors\

\

Destructor\

\
// Public Methods\

\

\
// Public Methods Used by the LoadBalancer\

\

\

\

\

Constructs a DomainPartitioner which will use *theGraphPartitioner* to
initially partition the PartitionedDomain using the element graph and
the *theLoadBalancer* to load balance the PartitionedDomain. The max
number of subdomains that the Domain can be partitioned is currently set
at 8.

Constructs a DomainPartitioner which will use *theGraphPartitioner* to
initially partition the PartitionedDomain. The max number of subdomains
that the Domain can be partitioned is currently set at 8.

\

\
Sets the link with the PartitionedDomain that is to be partitioned.

```{.cpp}
virtual int partition(int numParts);
```

Method invoked to partition the Domain. It first checks to see that the
PartitionedDomain has at least *numParts* Subdomains, with tags 1
through *numParts*; if not prints an error message and returns -1. It
then asks the domain for the element graph. This graph is then
partitioned using the GraphPartitioner into *numParts*; if partitioning
fails an error message is printed and $-10 +$ number returned from
GraphPartitioner is returned. If successful the domain is partitioned
according to the following rules:

-   All nodes which are internal to a partition are added using the
    `addNode()` method of the Subdomain. These nodes are removed from
    the PartionedDomain using `removeNode()`.

-   External nodes (these are nodes shared across partitions as a result
    of element connectivity or MP_Constraints are added to those
    Subdomains whose elements reference them. They are added using the
    `addExternalNode()` command.

-   SP_Constraints whose node is interior to a Subdomain are removed
    from the PartitionedDomain and added to the Subdomain.

-   MP_Constraints whose two nodes are interior to a Subdomain are
    removed from the PartitionedDomain and added to the Subdomain.

-   The elements are sent to the partition whose tag is given by the
    color of the vertex in the partitioned (colored) element graph. The
    elements are removed from the PartitionedDomain using
    `removeElement()` and added to the Subdomain using `addElement()`.

-   For the loads, a check is made to ensure that each Subdomain has a
    LoadCase with a tag equal to the tags in the LoadCases that have
    been added to the PartitionedDomain; if not new LoadCases are
    created and added to the Subdomain. It then iterates through all the
    NodalLoads in the LoadCases in the PartionedDomain, if the
    corresponding node is external the NodalLoad is removed and added to
    the corresponding LoadCase in the Subdomain. ELEMENTAL LOADS are not
    yet dealt with.

The DomainPartitioner invokes `hasDomainChanged()` on each Subdomain; if
the Subdomain has changed `invokeChangeOnAnalysis()`. Finally
`hasDomainChanged()` is invoked on the PartitionedDomain; if it has
changed `invokeChangeOnAnalysis()`. *partitionFlag* is set to true.
*virtual void balance(Graph &theWeightedGraph)*\
Checks first to see that the *partitionFlag* has been set; if it hasn'nt
an error message is printed and a $-1$ is returned. If a LoadBalancer
was passed in the constructor `balance()` is invoked on this object; if
no LoadBalancer was passed nothing is done and method returns$0$. If
balancing is performed, the DomainPartitioner invokes
`hasDomainChanged()` on each Subdomain; if the Subdomain has changed
`invokeChangeOnAnalysis()`. Finally `hasDomainChanged()` is invoked on
the PartitionedDomain; if it has changed `invokeChangeOnAnalysis()`.
*partitionFlag* is set to true.
Method which invokes `setPartitioner(this)` on the LoadBalancingAlgo. It
then invokes `balance(load)` on this object, where *load* is vector of
size *numParts* containing the load of each subdomain.

\
Returns the number of partitions in the PartitionedDomain.

Method which returns the partition graph. This is a graph with a vertex
for every partition and an edge between partitions if there exists an
element in one partition which is connected to an element in the other
partition.
*virtual Graph &getColoredGraph(void);* \
A method which returns the current colored graph representing the
partitioning of the elements in the subdomains. Does this by invoking
`getElementGraph()` on the PartitionedDomain. Note that this is the same
graph that was colored by the DomainPartitioner in partitioning the
PartitionedDomain.
*virtual void swapVertex(int from, int to, int vertexTag, bool
notAdjacentOther = true);* \
Method which will take the element given by vertex reference of the
vertex whose tag is given by *vertexTag* from subdomain *from* and place
it in subdomain *to*. If *notAdjacentOther* is *true* a check is made to
ensure that the vertex to be swapped is not adjacent to a vertex in any
other partition. Returns $0$ if successful, returns an error message and
$-1$ if PartitionedDomain has not been partitioned, $-2$ if *from*
Subdomain does not exist, $-3$ if *to Subdomain* does not exist, $-4$ if
a vertex given by *tag* does not exist, returns $-5$ if
*notAdjacentOther* was true and the vertex was adjacent to a vertex in
another partition, and returns $-6$ if no Element with a tag similar to
*tag* exists (this should not happen if element graph is built
correctly).
The Element, Nodes, NodalLoads, SP_Constraints and MP_Constraints that
need to be moved between the two Subdomains, or between the
PartitionedDomain and Subdomains are also moved. NO ELEMENTAL LOADS are
moved yet.
*virtual void swapBoundary(int from, int to, bool notAdjacentOther =
true);* \
Method which when invoked will take all the boundary elements in
subdomain *from* that are connected to elements in subdomain *to* and
place them in subdomain *to*. If *adjacentVertexOther* is *true* no
Elements which are connected to elements in subdomains other than *to*
and *from* are moved. Returns $0$ if successful, returns an error
message and $-1$ if PartitionedDomain has not been partitioned, $-2$ if
*from* Subdomain does not exist, $-3$ if *to Subdomain* does not exist.
The Elements, Nodes, NodalLoads, SP_Constraints and MP_Constraints that
need to be moved between the two Subdomains, or between the
PartitionedDomain and Subdomains are also moved. NO ELEMENTAL LOADS are
moved yet. It performs the operation by creating an ID of vertices and
then using code similar to that used in `swapVertex()`; `swapVErtex()`
is not called repeatedly as this was found to be too slow.
*virtual int releaseVertex(int from,\
int vertexTag,\
Graph &theWeightedPartitionGraph,\
double factorGreater,\
bool adjacentVertexOonly);* \
Method which when invoked will take the element given by vertex
reference of the vertex whose tag is given by *vertexTag* from subdomain
*from* and place it in the subdomain to which it is most attracted (to
which it is most connected). If it is equally attracted to two
subdomains it is sent to the one with the lightest load (the loads on
the subdomains are given in the *theWeightedPartitionGraph*. If the
*mustReleaseToLighter* is *true* a check is first made to see if the
load on the intended subdomain is lighter than the load in *from* and
that the ratio in load between from and the new domain is greater than
*factorGreater*; if this is the case the element is swapped, if not the
element is not swapped. An additional requirement that the vertex that
is to be swapped is not adjacent to any other partition can also be
set.
The method determines which partition the vertex is to be sent to and
then returns the result of invoking `swapVertex()` on itself, with this
partition used as the *to* argument in the arguments.
*virtual int releaseBoundary(int from,\
Graph &theWeightedPartitionGraph,\
double factorGreater,\
bool adjacentVertexOonly);* \
Method which when invoked will release all the elements on the boundary
of subdomain *from*. It performs the operation by creating an ID of all
the vertices on the boundary of the *from* Subdomain. Then
`releaseBoundary()` is invoked on all these vertices.
