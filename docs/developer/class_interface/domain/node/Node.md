NEW METHOD POSSIBLY NEEDED TO SPECIFY THE NUMBER OF PREVIOUSLY COMMITTED
RESPONSES TO KEEP .. NEEDED FOR EXPLICIT DYNAMIC INTEGRATORS\

\#include $<$/domain/node/Node.h$>$\

class Node: public DomainComponent\

TaggedObject\
MovableObject\
DomainComponent\

\
Nodes are points in space connected by the elements. Nodes have original
position, trial displacement, velocity and acceleration, and committed
displacement, velocity and acceleration (the last committed trial
quantities). Nodes also store information about any load acting on the
node, nodal mass and the nodal participation matrix. In addition, each
Node object keeps track of it's associated DOF_Group object. The Node
interface provides methods to set and retrieve these quantities.

// Constructors\

\

\

\

// Destructor\

\
// Public Methods dealing with DOF at the Node\

\

\
// Public Method for obtaining nodal coordinates\

\
// Public Method for obtaining committed and trial responses\

\

\

\

\
// Public Method for updating trial responses\

\

\

\

// Public Method for setting and obtaining unbalanced load\

\

\

\
// Public Method for setting state\

\

\
// Public Method for dynamic and modal analysis\

\

\

\
// Public Method for Output\

\

\

\
To construct a node which has no data, other than the *classTag*
identifier; $0$ and *classTag* are passed to the DomainComponent
constructor. This is the constructor called by an FEM_ObjectBroker. The
data must be filled in subsequently by a call to `recvSelf()`.

To construct a node whose unique integer among nodes in the domain is
given by *tag* and whose classTag is given by *classTag*. This
constructor can be used by subclasses who wish to handle their own data
management.

To construct a node for 1d problems whose unique integer among nodes in
the domain is given by *tag* and whose original position in 1d space is
given by (Crd1). With the node is associated *ndof* number of degrees of
freedom. The class tag is NOD_TAG_Node (defined in classTags.h). A
Vector object is created to hold the coordinates. No storage objects are
created to hold the trial and committed response quantities, mass, load
quantities; these are created as needed to reduce the memory demands on
the system in certain situations.

To construct a node for 2d problems whose unique integer among nodes in
the domain is given by *tag* and whose original position in 2d space is
given by (Crd1,Crd2). With the node is associated *ndof* number of
degrees of freedom. The class tag is NOD_TAG_Node. A Vector object is
created to hold the coordinates. No storage objects are created to hold
the trial and committed response quantities, mass, load quantities;
these are created as needed to reduce the memory demands on the system
in certain situations.

To construct a node for 3d problems whose unique integer among nodes in
the domain is given by *tag* and whose original position in 3d space is
given by (Crd1,Crd2,Crd3). With the node is associated *ndof* number of
degrees of freedom. The class tag is NOD_TAG_Node. A Vector object is
created to hold the coordinates. No storage objects are created to hold
the trial and committed response quantities, mass, load quantities;
these are created as needed to reduce the memory demands on the system
in certain situations.

To construct a node which is an exact copy of *theCopy*.

\
Invokes the destructor on all the storage objects created to hold the
coordinates, response quantities, mass and load quantities.

\
Returns the number of degrees-of-freedom, *ndof*, associated with the
node.

Each node, when involved with an analysis, will be associated with a
DOF_Group object. It is the DOF_Group that contains the ID of equation
numbers. When invoked this method sets the pointer to that DOF_Group
object.

```{.cpp}
virtual DOF_Group \*getDOF_GroupPtr(void);
```

Method which returns a pointer to the DOF_Group object that was set
using *setDOF_GroupPtr*. If no pointer has been set a $0$ is returned.

```{.cpp}
virtual const Vector &getCrds(void) const;
```

Returns the original coordinates in a Vector. The size of the vector is
2 if node object was created for a 2d problem and the size is 3 if
created for a 3d problem.

```{.cpp}
virtual const Vector &getDisp(void) ;
```

Returns the last committed displacement as a Vector, the vector of size
*ndof*. If no Vector has yet been allocated, two Vector objects are
created to store the committed and trial response quantities created; if
not enough space is available an error message is printed and program
terminated.

```{.cpp}
virtual const Vector &getVel(void) ;
```

Returns the last committed velocity as a Vector, the vector of size
*ndof*. If no Vector has yet been allocated, two Vector objects are
created to store the committed and trial response quantities created; if
not enough space is available an error message is printed and program
terminated.

```{.cpp}
virtual const Vector &getAccel(void) ;
```

Returns the last committed acceleration as a Vector, the vector of size
*ndof*. If no Vector has yet been allocated, two Vector objects are
created to store the committed and trial response quantities created; if
not enough space is available an error message is printed and program
terminated.

```{.cpp}
virtual const Vector &getTrialDisp(void) ;
```

Returns the current trial displacements as a Vector, the vector of size
*ndof*. If no Vector has yet been allocated, a new Vector is created and
returned; if not enough space is available an error message is printed
and the program is terminated.

```{.cpp}
virtual const Vector &getTrialVel(void) ;
```

Returns the current trial velocities as a Vector, the vector of size
*ndof*. If no Vector has yet been allocated, a new Vector is created and
returned; if not enough space is available an error message is printed
and the program is terminated.

```{.cpp}
virtual const Vector &getTrialAccel(void) ;
```

Returns the current trial accelerations as a Vector, the vector of size
*ndof*. If no Vector has yet been allocated, a new Vector is created and
returned; if not enough space is available an error message is printed
and the program is terminated.

```{.cpp}
virtual const Vector &getIncrDisp(void) ;
```

Returns the incremental displacement as a Vector. The incremental
displacement is equal to the difference between the current trial
displacement and committed displacement (trial - committed). If no
Vector has yet been allocated, three Vector objects are created to store
the committed, trial and incremental response quantities; if not enough
space is available an error message is printed and program terminated.

```{.cpp}
virtual int setTrialDisp(const Vector &newTrialDisp);
```

Sets the current trial displacement to be that given by *newTrialDisp*.
Sets th incremental displacement to be trial $-$ committtd. If no space
has yet been allocated for the trial displacements, two Vector objects
are now created to store the trial and committed response quantities; if
not enough memory is available on the heap to create these new Vectors
an error message is printed and the program is terminated. Returns $0$
if successful, an error message is printed and a $-2$ is returned if
*newTrialDisp* is not of size *ndof*.

```{.cpp}
virtual int setTrialVel(const Vector &newTrialVel);
```

Sets the current trial velocity to be that given by *newTrialVel*. If no
space has yet been allocated for the trial velocities, two Vector
objects are now created to store the trial and committed response
quantities; if not enough memory is available on the heap to create
these new Vectors an error message is printed and the program is
terminated. Returns $0$ if successful, an error message is printed and a
$-2$ is returned if *newTrialVel* is not of size *ndof*.

```{.cpp}
virtual int setTrialAccel(const Vector &newTrialAccel);
```

Sets the current trial acceleration to be that given by *newTrialAccel*.
If no space has yet been allocated for the trial accelerations, two
Vector objects are now created to store the trial and committed response
quantities; if not enough memory is available on the heap to create
these new Vectors an error message is printed and the program is
terminated. Returns $0$ if successful, an error message is printed and a
$-2$ is returned if *newTrialAccel* is not of size *ndof*.

```{.cpp}
virtual int incrTrialDisp(const Vector &trialIncrDisp);
```

Sets the current trial displacement to be that given by the addition of
the last trial displacement, assumed $0$ if not yet set, and
*trialIncrDisp*. Increments the incremental displacement by
*trialIncrDisp*. If no space has yet been allocated for the
displacements, three Vector objects are now created to store the trial,
committed and incremental response quantities; if not enough memory is
available on the heap to create these new Vectors an error message is
printed and the program is terminated. Returns $0$ if successful, an
error message is printed and a $-2$ is returned if *trialIncrDisp* is
not of size *ndof*.

```{.cpp}
virtual int incrTrialVel(const Vector &trialIncrVel);
```

Sets the current trial velocity to be that given by the addition of the
last trial velocity, assumed $0$ if not yet set, and *trialIncrVel*. If
no space has yet been allocated for the trial velocities, two Vector
objects are now created to store the trial and committed response
quantities; if not enough memory is available on the heap to create
these new Vectors an error message is printed and the program is
terminated. Returns $0$ if successful, an error message is printed and a
$-2$ is returned if *trialIncrVel* is not of size *ndof*.

```{.cpp}
virtual int incrTrialAccel(const Vector &trialIncrAccel);
```

Sets the current trial Acceleration to be that given by the addition of
the last trial Acceleration, assumed $0$ if not yet set, and
*trialIncrAccel*. If no space has yet been allocated for the trial
accelerations, two Vector objects are now created to store the trial and
committed response quantities; if not enough memory is available on the
heap to create these new Vectors an error message is printed and the
program is terminated. Returns $0$ if successful, an error message is
printed and a $-2$ is returned if *trialIncrAccel* is not of size
*ndof*.

```{.cpp}
virtual void zeroUnbalancedLoad(void);
```

Causes the node to zero out its unbalanced load vector.
*virtual int addUnbalancedLoad(const Vector &additionalLoad, double
fact);*\
The Node is responsible for adding *fact* times *additionalLoad* to the
current unbalanced load at the Node. If *additionalLoad* is not of size
*ndof* no load is added, an error message is printed and a $-1$ is
returned. If no space has yet been allocated for the unbalanced load a
new Vector is now created; if not enough space is available for this
Vector an error message is printed and the program is terminated.
Returns $0$ if successful.

To add **minus** *fact* times the product $M * R * accel$ to the current
unbalanced load. Nothing is done if no mass or R matrix have been set.
Prints a warning and returns a $-1$ if the size of accel and the number
of columns in $R$ are not the same. If no space has yet been allocated
for the unbalanced load a new Vector is now created; if not enough space
is available for this Vector an error message is printed and the program
is terminated. Returns $0$ if successful.

```{.cpp}
virtual const Vector &getUnbalancedLoad(void);
```

Returns the current unbalanced load. If no space has yet been allocated
for the unbalanced load a new Vector of size *numDOF* is now created; if
not enough space is available for this Vector an error message is
printed and the program is terminated.

```{.cpp}
virtual const Vector &getUnbalancedLoadIncInertia(void);
```

Returns the current unbalanced load Vector, as defined above, MINUS the
product of the nodes mass matrix and the trial nodal accelerations. The
result is saved in another vector which is returned. If no space has yet
been allocated for this new Vector, a Vector of size *numDOF* is now
created; if not enough space is available for this Vector an error
message is printed and the program is terminated.

```{.cpp}
virtual int commitState(void);
```

Causes the node to set the committed model displacements, velocities and
accelerations to be equal to the current trial displacements, velocities
and accelerations. The incremental displacement is set to $0$. No
assignment is done for any of the quantities for which no memory has
been allocated. Returns $0$.

```{.cpp}
virtual int revertToLastCommit(void);
```

Causes the node to set the trial nodal displacements, velocities and
accelerations to be equal to the current committed displacements,
velocities and accelerations. The incremental displacement is set to
$0$. No assignment is done for any of the trial quantities for which no
memory has been allocated. Returns $0$.

```{.cpp}
virtual int revertToStart(void);
```

Causes the node to set the trial and committed nodal displacements,
velocities and accelerations to zero. No assignment is done for any of
the trial quantities for which no memory has been allocated. Returns
$0$.

```{.cpp}
virtual const Matrix &getMass(void) ;
```

Returns the mass matrix set for the node, which is a matrix of size
*ndof,ndof*. This matrix is equal to that set in `setMass()` or zero if
`setMass()` has not been called. If no storage space has been allocated
for the mass, a matrix is now created. An error message is printed and
the program terminated if no space is available on the heap for this
matrix.

```{.cpp}
virtual int setMass(const Matrix &mass);
```

Sets the value of the mass at the node. A check is made to ensure that
the *mass* has the same dimensions of the mass matrix associated with
the Node; if incompatible size an error message is printed and -1
returned. If no mass matrix yet allocated, one is created; if no space
is available an error message is printed and the program terminated.
Returns 0 if successful.

Creates a Matrix to store the R matrix. The matrix is of dimension
*ndof* and *numCol*. If not enough space is available for this matrix an
error message is printed and the program is terminated. Zeros the matrix
R and returns $0$ if successful.

Sets the *$row,col$* entry of R to be equal to *Value*. If no matrix R
has been specified or the position in R is out of range a warning
message is printed and a $-1$ is returned. Returns $0$ if successful.

This is a method provided for Element objects, the Node object returns
the product of the matrix $R$ and the vector $V$. If the matrix and
vector are of inappropriate size a warning message is printed and a zero
vector is returned.

```{.cpp}
virtual int sendSelf(int commitTag, Channel &theChannel);
```

Causes the Node object to send the data needed to init itself on a
remote machine to the Channel object *theChannel*. The data sent
includes the tag, number of dof, coordinates, committed response
quantities, unbalanced load, mass and participation matrix. To do this
the Node creates an ID object into which it stores its tag, the *ndof*
and a flag indicating whether any additional information, i.e. mass,
response quantities also need to be sent. In addition four database tags
are also included in this ID object. The database tags, if not already
obtained, are requested from the Channel object (these are needed as
each object can only store a single object of a particular size using
it's own database tags -- additional tags are needed when multiple
objects of the same size are needed. The objects that have been created
are then sent.
*virtual int recvSelf(int commitTag, Channel &theChannel,
FEM_ObjectBroker &theBroker);*\
Invoked on a remote machine to read its data that was sent by a node
object in another actor when `sendSelf()` was invoked. As in
`sendSelf()`, the Node object creates an ID object. It asks the Channel
object to fill this object with data. Based on the data it creates
Matrix and Vector objects to store the Nodes data and asks the Channel
object to fill these with data. The data placed here by the Channel
object correspond to the data put there by the sending Node object.

```{.cpp}
void Print(OPS_Stream &s, int flag = 0);
```

Causes the Node to print out its tag, mass matrix, and committed
response quantities.

Causes the Node to display itself. If *flag* is $1$ the Node will cause
its tag to be printed to the display.
