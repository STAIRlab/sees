# Domain

```cpp
#include  <domain/domain/Domain.h>
```

class Domain



Domain is container class for storing and providing access to the
components of a domain, i.e. nodes, elements, boundary conditions, and
load patterns. A Domain is a container class which contains the all
elements, nodes, load cases, single point constraints and multiple point
constraints that the model builder uses to create the model of the
structure. It provides operations for the following:

-   Population: Methods so that the DomainComponents can be addled to
    the Domain.

-   Depopulation: Methods so that the DomainComponents can be removed
    from the Domain.

-   Access: Methods so that other classes, i.e. analysis and design, can
    access the DomainComponents.

-   Query: Methods for determining the state of the domain.

-   Update: Methods for updating the state of the Domain

-   Analysis: Methods added for the Analysis class.

-   Output: Methods added for outputting information.

The Domain class stores each type of object, i.e. Nodes, Elements,
SP_Constraints, MP_Constraints, NodalLoads and ElementalLoads, in a
container object. Currently these container objects are a subtype of
TaggedObjectStorage (templates are not used as yet due to present
difficulties in porting code which uses templates).

### Constructors

\

\

### Destructor

\
// Public Methods to Populate the Domain\

\

\

\
// Public Methods to Populate the LoadPatterns\

\

\
// Public Methods to Depopulate the Domain\

\

\

\

// Public Methods to Access the Components of the Domain\

\

\

\

\

\

// Public Methods to Query the State of the Domain\

\

\

\

\

\

// Public Methods to Update the Domain\

\

\

\

\

\

// Public Methods for Output\

\

\
// Protected Member Functions\

\

\

Constructs an empty domain. The storage for the DomainComponents uses
ArrayOfTaggedObjects objects for each type of object to be stored. The
initial sizes specified for these objects are 4096 for the Elements and
Nodes, 256 SP_Constraints and MP_Constraints, and 32 for the container
for the LoadPatterns. A check is made to ensure that memory is allocated
for these objects, if not the `fatal()` method of the global
ErrorHandler is invoked.

Constructs an empty Domain. The storage for the DomainComponents uses
ArrayOfTaggedObjects objects for each type of object to be stored. The
initial sizes specified for these objects are as given in the arguments
for this constructor, i.e. *numElements* for the Elements and *numNodes*
for the Nodes. A size of 32 is used for the LoadPatterns. A check is
made to ensure that memory is allocated for these objects, if not the
`fatal()` method of the global ErrorHandler is invoked.

Constructs a Domain where the Nodes, Elements, MP_Constraints,
SP_Constraint and LoadPattern objects will be stored in the storage
objects provided. A check is made to ensure these container objects are
empty is made; if not empty the `warning()` method of the global
ErrorHandler is invoked and the objects are cleared.

Constructs a Domain where the Nodes, Elements, MP_Constraints,
SP_Constraint and LoadPattern objects will be stored in the storage
objects obtained by invoking `getEmptyCopy()` on the *theStorageType*
object. A check is made to ensure that memory is allocated for these
objects, if not the `fatal()` method of the global ErrorHandler is
invoked.

\
Invokes delete on all the storage objects. This means that, if the two
latter constructors have been called, the container objects must have
been created using *new* and that at no other point in the program is
the destructor invoked on these objects. It should be noted, that the
objects in the Domain, i.e. the DomainComponents, are not destroyed. To
clean up these objects `clearAll()` should be invoked before the
destructor is called.

\
To add the element pointed to by theElementPtr to the domain. If
*\_DEBUG* is defined the domain checks to see that: 1) that all external
nodes for the element exists in the domain. and 2) that the sum of the
dof at all the nodes equals the num of dof at the element. In addition
the domain always checks to ensure that no other element with a similar
tag exists in the domain. If the checks are successful, the element is
added to the domain by the domain invoking `addComponent(theElePtr)` on
the container for the elements. The domain then invokes
`setDomain(this)` on the element and `domainChange()` on itself if the
element is successfully added. The call returns *true* if the element is
added, otherwise the `warning()` method of the global ErrorHandler is
invoked and *false* is returned.

```{.cpp}
virtual bool addNode(Node \*theNodePtr = false);
```

To add the node pointed to by *theNodePtr* to the domain. The domain
first checks that no other node with a similar tag, node number, has
been previously added to the domain. The domain will then add the node
to it's node container object, by invoking `addComponent(theNodePtr)`.
If successful, the Domain invokes `setDomain(this)` on the node,
`domainChange()` on itself, and checks the coordinates of the domain to
see if they effect the box encompassing the Domain. The call returns
*true* if the node was added, otherwise the `warning()` method of the
global ErrorHandler is invoked and *false* is returned.

```{.cpp}
virtual bool addSP(SP_Constraint \*theSPptr = false);
```

To add the single point constraint pointed to by theSPptr to the domain.
If *\_DEBUG* is defined the domain is responsible for checking to see
that 1) the constrained node exists in the domain and 2) that the node
has the dof that is to be constrained. In addition the domain always
checks to ensure that no other constraint with a similar tag exists in
the domain. If the checks are successful, the constraint is added to
domain by the domain invoking `addComponent(theSPptr)` on the container
for the SP_Constraints. The domain then invokes `setDomain(this)` on the
constraint and `domainChange()` on itself. The call returns *true* if
the constraint was added, otherwise the `warning()` method of the global
ErrorHandler is invoked and *false* is returned.

```{.cpp}
virtual bool addMP(MP_Constraint \*theMPptr = false);
```

To add the multiple point constraint pointed to by theMPptr, to the
domain. If *\_DEBUG* is defined the domain first checks to see that the
retained and the constrained node both exist in the model and that the
matrix is of proper dimensions (THIS LAST PART NOT YET IMPLEMENTED). In
addition the domain always checks to ensure that no other MP_Constraint
with a similar tag exists in the domain. If the checks are successful,
the constraint is added to domain by the domain invoking
`addComponent(theMPptr)` on the container for the MP_Constraints. The
domain then invokes `setDomain(this)` on the constraint and
`domainChange()` on itself. The call returns *true* if the constraint
was added, otherwise the `warning()` method of the global ErrorHandler
is invoked and *false* is returned.

```{.cpp}
virtual bool addLoadPattern(LoadPattern \*thePattern);
```

To add the LoadPattern *thePattern* to the domain. The load is added to
domain by the domain invoking `addComponent(theLd)` on the container for
the LoadPatterns. The domain is responsible for invoking
`setDomain(this)` on the load. The call returns *true* if the load was
added, otherwise the `warning()` method of the global ErrorHandler is
invoked and *false* is returned.

```{.cpp}
virtual bool addNodalLoad(NodalLoad \*theLd, int loadPatternTag);
```

To add the nodal load *theld* to the LoadPattern in the domain whose tag
is given by *loadPatternTag*. If *\_DEBUG* is defines, checks to see
that corresponding node exists in the domain. A pointer to the
LoadPattern is obtained from the LoadPattern container and the load is
added to LoadPattern by invoking `addNodalLoad(theLd)` on the
LoadPattern object. The domain is responsible for invoking
`setDomain(this)` on the load. The call returns *true* if the load was
added, otherwise the `warning()` method on the global ErrorHandler is
invoked and *false* is returned.
*virtual bool addElementalLoad(ElementalLoad \*theLd, int
loadPatternTag);*\
To add the elemental load *theld* to the LoadPattern in the domain whose
tag is given by *loadPatternTag*. If *\_DEBUG* is defines, checks to see
that corresponding element exists in the domain. A pointer to the
LoadPattern is obtained from the LoadPattern container and the load is
added to LoadPattern by invoking `addElementalLoad(theLd)` on the
LoadPattern object. The domain is responsible for invoking
`setDomain(this)` on the load. The call returns *true* if the load was
added, otherwise the `warning()` method on the global ErrorHandler is
invoked and *false* is returned.
*virtual bool addSP_Constraint(SP_Constraint \*theConstraint, int
loadPatternTag);*\
To add the elemental load *theConstraint* to the LoadPattern in the
domain whose tag is given by *loadPatternTag*. If *\_DEBUG* is defines,
checks to see that corresponding node exists in the domain. A pointer to
the LoadPattern is obtained from the LoadPattern container and the load
is added to LoadPattern by invoking `addSP_Constraint(theConstraint)` on
the LoadPattern object. The domain is responsible for invoking
`setDomain(this)` on the constraint. The call returns *true* if the load
was added, otherwise the `warning()` method on the global ErrorHandler
is invoked and *false* is returned.

\
To remove all the components from the model and invoke the destructor on
these objects. First `clearAll()` is invoked on all the LoadPattern
objects. Then the domain object invokes `clearAll()` on its container
objects. In addition the destructor for each Recorder object that has
been added to the domain is invoked. In addition the current time and
load factor are set to $0$, and the box bounding the domain is set to
the box enclosing the origin.

To remove the element whose tag is given by *tag* from the domain. The
domain achieves this by invoking `removeComponent(tag)` on the container
for the elements. Returns $0$ if no such element exists in the domain.
Otherwise the domain invokes `setDomain(0)`{.cpp} on the element (using a cast
to go from a TaggedObject to an Element, which is safe as only an
Element objects are added to this container) and `domainChange()` on
itself before a pointer to the element is returned.

```{.cpp}
virtual Node \*removeNode(int tag);
```

To remove the node whose tag is given by *tag* from the domain. The
domain achieves this by invoking `removeComponent(tag)` on the container
for the nodes. Returns $0$ if no such node exists in the domain. If the
node is to be removed the domain invokes `setDomain(0)`{.cpp} on the node and
`domainChange()` on itself before a pointer to the Node is returned.

```{.cpp}
virtual SP_Constraint \*removeSP_Constraint(int tag);
```

To remove the SP_Constraint whose tag is given by *tag* from the domain.
The domain achieves this by invoking `removeComponent(tag)` on the
container for the single point constraints. Returns $0$ if the
constraint was not in the domain, otherwise the domain invokes
*setDomain(0)* on the constraint and `domainChange()` on itself before a
pointer to the constraint is returned. Note this will only remove
SP_Constraints which have been added to the domain and not directly to
LoadPatterns.

```{.cpp}
virtual `MP_Constraint` \*removeMP_Constraint(int tag);
```

To remove the `MP_Constraint` whose tag is given by *tag* from the domain.
The domain achieves this by invoking `removeComponent(tag)` on the
container for the multi point constraints. Returns $0$ if the constraint
was not in the domain, otherwise the domain invokes `setDomain(0)`{.cpp} on
the constraint and `domainChange()` on itself before a pointer to the
constraint is returned.

```{.cpp}
virtual LoadPattern \*removeLoadPattern(int tag);
```

To remove the LoadPattern whose tag is given by *tag* from the domain.
The domain achieves this by invoking `removeComponent(tag)` on the
container for the load patterns. If the LoadPattern exists, the domain
then iterates through the loads and constraints of the LoadPattern
invoking `setDomain(0)`{.cpp} on these objects. Returns $0$ if the load was
not in the domain, otherwise returns a pointer to the load that was
removed. Invokes `setDomain(0)`{.cpp} on the load case before it is returned.

\
To return an iter for the Elements in the domain. It returns an
*ElementIter* for the elements of the domain that were added using
`addElement()`.

```{.cpp}
virtual NodeIter &getNodes(void);
```

It returns a *NodeIter* for the nodes which have been added to the
domain.

```{.cpp}
virtual SP_ConstraintIter &getSPs(void);
```

To return an *SP_ConstraintIter* for the single point constraints which
have been added to the domain.

```{.cpp}
virtual MP_ConstraintIter &getMPs(void);
```

To return an *MP_ConstraintIter* for the multiple point constraints
which have been added to the domain.

```{.cpp}
virtual LoadPatternIter &getLoadPatterns(void);
```

To return an *LoadPatternIter* for the LoadPattern objects which have
been added to the domain.

```{.cpp}
virtual Element \*getElement(int tag);
```

To return a pointer to the element *tag*. If no such element exists $0$
is returned. It does this by invoking em getComponentPtr(tag) on the
element container and performing a cast to an element if the object
exists.

```{.cpp}
virtual Node \*getNode(int tag);
```

To return a pointer to the node whose tag is given by *tag*. If no such
node exists $0$ is returned. It does this by invoking em
getComponentPtr(tag) on the node container and performing a cast to a
node if the object exists.

```{.cpp}
virtual SP_Constraint \*getSP_ConstraintPtr(int tag);
```

To return a pointer to the SP_Constraint whose tag is given by *tag*. If
no such SP_Constraint exists $0$ is returned. It does this by invoking
em getComponentPtr(tag) on the single-point constraint container and
performing a cast to an SP_Constraint if the object exists.

```{.cpp}
virtual `MP_Constraint` \*getMP_ConstraintPtr(int tag);
```

To return a pointer to the `MP_Constraint` whose tag is given by *tag*. If
no such `MP_Constraint` exists $0$ is returned. It does this by invoking
em getComponentPtr(tag) on the multi-point constraint container and
performing a cast to an `MP_Constraint` if the object exists.

```{.cpp}
virtual ElementalLoad \*getLoadPattern(int tag);
```

To return a pointer to the LoadPattern whose tag is given by *tag*. If
no such LoadPattern exists $0$ is returned. It does this by invoking em
getComponentPtr(tag) on the elemental load container and performing a
cast to a LoadPattern if the object exists.

\
To return the number of elements in the domain. It does this by invoking
`getNumComponents()` on the container for the elements.

```{.cpp}
virtual int getNumNodes(void) const;
```

To return the number of nodes in the domain. It does this by invoking
`getNumComponents()` on the container for the nodes.

```{.cpp}
virtual int getNumSPs(void) const;
```

To return the number of single point constraints in the domain. It does
this by invoking `getNumComponents()` on the container for the single
point constraints.

```{.cpp}
virtual int getNumMPs(void) const;
```

To return the number of multi point constraints in the domain. It does
this by invoking `getNumComponents()` on the container for the multi
point constraints.

```{.cpp}
virtual int getNumLoadPatterns(void) const;
```

To return the number of load patterns in the domain. It does this by
invoking `getNumComponents()` on the container for the load patterns.

```{.cpp}
virtual const Vector &getPhysicalBounds(void);
```

To return the bounding rectangle for the Domain. The information is
contained in a Vector of size 6 containing in the following order {xmin,
ymin, zmin, xmax, ymax, zmax}. This information is built up as nodes are
added to the domain, initially all are set to $0$ in the constructor.

```{.cpp}
virtual Graph &getElementGraph(void);
```

Returns the current element graph (the connectivity of the elements in
the domain). If the *eleChangeFlag* has been set to *true* the method
will invoke `buildEleGraph(theEleGraph)` on itself before returning the
graph. The vertices in the element graph are to be labeled $0$ through
$numEle-1$. The Vertices references contain the elemental tags.

```{.cpp}
virtual Graph &getNodeGraph(void);
```

Returns the current node graph (the connectivity of the nodes in the
domain). If the *nodeChangeFlag* has been set to *true* the will invoke
`buildNodeGraph(theNodeGraph)` on itself before returning the graph. The
vertices in the node graph are to be labeled $0$ through $numNode-1$.
The Vertices references contain the nodal tags.

\
To set the current commitTag to *newTag*.

To set the current time to *newTime*.

To set the committed time to *newTime*.

To apply the loads for the given time *pseudoTime*. The domain first
clears the current load at all nodes and elements, done by invoking
`zeroUnbalancedLoad()` on each node and `zeroLoad()` on each element.
The domain then invokes `applyLoad(pseudoTime)` on all LoadPatterns
which have been added to the domain. The domain will then invoke
`applyConstraint(pseudoTime)` on all the constraints in the single and
multi point constraint containers. Finally the domain sets its current
time to be *pseudoTime*.

To set the loads in the LoadPatterns to be constant. The domain achieves
this by invoking `setLoadConstant()` on all the LoadPatterns which have
been added to the domain. Note that LoadPatterns added after this method
has been invoked will not be constant until this method is invoked
again.

```{.cpp}
virtual void commit(void);
```

To commit the state of the domain , that is to accept the current state
as being ion the solution path. The domain invokes `commit()` on all
nodes in the domain and then `commit()` on all elements of the domain.
These are calls for the nodes and elements to set there committed state
as given by their current state. The domain will then set its committed
time variable to be equal to the current time and lastly increments its
commit tag by $1$.

```{.cpp}
virtual int revertToLastCommit(void);
```

To return the domain to the state it was in at the last commit. The
domain invokes `revertToLastCommit()` on all nodes and elements in the
domain. The domain sets its current loadFactor and time stamp to be
equal to the last committed values. The domain decrements the current
commitTag by $1$. Finally it invokes `applyLoad()` on itself with the
current time.

```{.cpp}
virtual void update(void);
```

Called by the AnalysisModel to update the state of the domain. Iterates
over all the elements of the Domain and invokes `update()`.

To set the domain stamp to be *newStamp*. Domain stamp is the integer
returned by `hasDomainChanged()`.


```{.cpp}
virtual int hasDomainChanged(void);
```

To return an integer stamp indicating the state of the domain. Initially
$0$, this integer is incremented by $1$ if `domainChange()` has been
invoked since the last invocation of the method. If the domain has
changed it marks the element and node graph flags as not having been
built.

\
To add a recorder object *theRecorder* to the domain.
`record(commitTag)` is invoked on each `commit()`. The pointers to the
recorders are stored in an array which is resized on each invocation of
this method.

The domain will invoke `playback(commitTag)` on all recorder objects
which have been added to the domain.

To print the state of the domain. The domain invokes `Print(s,flag)`{.cpp} on
all it's container objects.

This function allows domain objects to be printed to streams. The
function invokes $M.Print(s)$ before returning $s$.

\
Sets a flag indicating that the integer returned in the next call to
`hasDomainChanged()` must be incremented by $1$. This method is invoked
whenever a Node, Element or Constraint object is added to the domain.
*virtual int buildEleGraph(Graph &theEleGraph)*\
A method which will cause the domain to discard the current element
graph and build a new one based on the element connectivity. Returns $0$
if successful otherwise $-1$ is returned along with an error message to
opserr.
*virtual int buildNodeGraph(Graph &theNodeGraph)*\
A method which will cause the domain to discard the current node graph
and build a new one based on the node connectivity. Returns $0$ if
successful otherwise $-1$ is returned along with an error message to
opserr.
