


# PartitionedModelBuilder 

```cpp
#include <modelbuilder/PartitionedModelBuilder.h>
```



class PartitionedModelBuilder: public ModelBuilder, public
MovableObject



PartitionedModelBuilder


MovableObject






The PartitionedModelBuilder class is an abstract class. A subclass of
PartitionedModelBuilder is a class which creates a partitioned finite
element discretization of a structure: that is it discretizes the
structure to be modeled into Elements, Nodes, Constraints, etc. and adds
these components to the Subdomains of a PartitionedDomain.
PartitionedModelBuilders can be used for creating models for analysis
involving domain decomposition methods where there exist natural
partitions or where a model has previously been partitioned and this
information has been saved.

// Constructors











// Destructor






// Public Methods










// Protected Methods







Typically, a PartitionedModelBuilder is associated with a
PartitionedDomain, this constructor sets up a link for the
PartitionedModelBuilder and the domain, setting its link to the Domain
object *domain*. The Domain *domain* is passed to the constructor for
ModelBuilder, and the integer *classTag* is passed to the MovableObject
classes constructor.

This is the constructor that is called when a PartitionedModelBuilder is
to be created by an FE_ObjectBroker. The only method that can be invoked
on such an object is `buildSubdomain()`.




Does nothing.




The PartitionedModelBuilder will first check that the
PartitionedModelBuilder was constructed with a PartitioneDomain, if not
a warning message is printed and a $-1$ is returned. If o.k. the object
then determines the number of Subdomains, *numSub* in the
PartitionedDomain. It then invokes `buildInterface(numSub)` on itself.
Then for each Subdomain in the PartitionedDomain it invokes
*buildSubdomain(numSub, \*this)*. If building the interface or any of
the subdomains fails, a warning message is printed and a negative number
is returned. Returns $0$ if sucessfull.

This method must be provided by the subclasses. It is used to add any
boundary nodes, nodal loads and constraints to the PartitionedDomain
object. The integer *numSubdomains* is passed to provide information
about the number of subdomains in the PartitionedDomain. To return $0$
if successfull, a negative number if not.

This method must be provided by the subclasses. It is used to add nodes,
elements, loads and constraints to the subdomain *theSubdomain*. The
integers *partition* and *numPartitions* are used to identify which
partition is being built and the total number of partitions. To return
$0$ if succesfull, a negative number if not.




Returns a pointer to the PartitionedDomain object passed in the
constructor.
