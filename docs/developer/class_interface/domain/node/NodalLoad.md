\
# NodalLoad 

```cpp
#include <domain/node/NodalLoad.h>
```

class NodalLoad: public Load\

TaggedObject\
MovableObject\
DomainComponent\
Load\

\
NodalLoads are loads acting on Nodes. The public methods are all
declared as virtual to allow subclasses to be introduced for the
provision of time varying loads. Each NodalLoad object is associated
with a single Node object and has a Vector object corresponding to the
load acting on this Node object as a result of the NodalLoad.

### Constructors

\

\
### Destructor

\
// Public Methods\

\

\
// Public Methods for Output\

\

\

To create a NodalLoad object with tag *tag* acting on Node *node* with a
reference load given by *load*. *tag* and *LOAD_TAG_NodalLoad* (defined
in  `<classTags.h>`)are passed to the Load constructor. A new vector
object is created using the vector *load* as the argument. (THIS MAY
CHANGE - may associate the load Vector with *load*, allowing identical
loads on diff nodes to be created without the need for each to have its
own vector) If no enough memory is available an error message is printed
and the program terminates. The boolean *isLoadConstant* is used to
indicate whether the value of the load applies to the Node is
independent of the load factor.

Provided for subclasses, which may which to provide the abstraction of
time varying nodal loads. The integers *tag* and *classTag* are passed
to the Load constructor.

Provided so that a FEM_ObjectBroker can construct an object. $0$ and
*classTag* are passed to the Load classes constructor. The data for the
object is filled in when `recvSelf()` is invoked on the object.

\
If a Vector for the load was constructed, the destructor invokes delete
on this Vector object.

\
To set the associated Domain object. First checks to ensure that a Node
object with the tag exists in the Domain. It sets the pointer for it's
associated Node object to point to this object, and then invokes the
DomainComponent classes `setDomain()` method. If the Node does not exist
in the Domain a warning message and `setDomain()` is not invoked.

Returns the integer *node* passed in the constructor.

To it's associated Node it invokes `addUnbalancedLoad()` with it's copy
of the Vector object *load* and a factor of *loadFactor* if
*isLoadConstant* was specified as *false* in the constructor or $1$ if
it was specified as *true*. Warning messages are printed, if no Domain
has been associated with the NodalLoad object or no Node with a tag
*node* exists in the Domain. For efficiency reasons, the NodalLoad
object keeps a pointer to it's associated Node object. The time
*timeStep* has no influence on the load added.

Determines its database tag. The object then sends it's tag, *node* and
size of load Vector to the Channel in an ID object. Then, if *load* is
not NULL, it sends it's copy of the *load* Vector. Returns $0$ if
successful, a negative number if the Channel failed to send the data.

The object first determines its database tag. It then invokes receives
an ID object from the Channel containing it's tag, *node* and size of
load Vector. If size of *load* is not $0$ it then receives it's copy of
the *load* Vector. Returns $0$ if successful, a negative number if the
Channel failed to receive the data.

Prints it's *node* and then prints the load Vector.
