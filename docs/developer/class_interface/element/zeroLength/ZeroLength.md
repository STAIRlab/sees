\
# ZeroLength 

```cpp
#include <element/ZeroLength.h>
```

class ZeroLength: public Element\

TaggedObject\
MovableObject\
DomainComponent\
Element\

\
The ZeroLength class represents an element defined by two nodes at the
same geometric location, hence it has zero length. The nodes are
connected by of uniaxial materials to represent the force-deformation
relationship for the element.

ZeroLength elements are constructed with a *tag* in a domain of
*dimension* 1, 2, or 3, connected by nodes *Nd1* and *Nd2*. The vector
*x* defines the local x-axis for the element and the vector *yprime*
lies in the local x-y plane for the element. The local z-axis is the
cross product between *x* and *yprime*, and the local y-axis is the
cross product between the local z-axis and *x*.

// Constructors\

\

\
// Destructor\

\
// public methods to obtain information about dof & connectivity\

\

\
// public methods to set the state of the element\

\

// public methods to obtain stiffness, mass, damping and residual
information\

\

\

\

\

// public methods for element output\

\

\

\

\
Construct a ZeroLength element with *tag* . The force-deformation
relationship for the element is given by a pointer *theMaterial* to a
**UniaxialMaterial** model acting in local *direction*. The local
*direction* is 1, 2, 3, for translation in the local x, y, z axes or 4,
5, 6 for rotation about the local x, y, z axes.

Construct a ZeroLength element with *tag* . The force-deformation
relationship is given by the *n1dMat* pointers *theMaterial* to
**UniaxialMaterial** models. *direction* is an **ID** of length *n1dMat*
that gives the local direction for each corresponding entry in the array
*theMaterial* The local *direction* is 1, 2, 3, for translation in the
local x, y, z axes or 4, 5, 6 for rotation about the local x, y, z
axes.

This is the constructor invoked by an **FEM_ObjectBroker** object. It
constructs an empty ZeroLength element with two nodes. The `recvSelf()`
method is invoked on the object for it to set the internal data.

\
Element destructor deletes memory for storing material model pointers.

\
Returns 2.

Return **ID** of size $2$ with the node tags defining the element.

Return the number of DOF for the element, which depends on the dimension
of the problem and the number of DOF associated with each node.

Initialize element and define data structures.

Commit state of element by committing state of materials. Return 0 if
successful, !0 otherwise.

Revert state of element to last commit by reverting to last committed
state of materials. Return 0 if successful, !0 otherwise.

Revert state of element to initial state by reverting to initial state
of materials. Return 0 if successful, !0 otherwise.

Return tangent stiffness matrix for element.

Return secant stiffness matrix of element. The secant stiffness is
defined by the secant for the materials.

Return a zero damping matrix.

Return a zero mass matrix.

The element has no loads, so this operation has no effect.

The element has no loads, so this operation has no effect and returns
0.

The element has no mass, so this operation has no effect and returns 0.

Return resisting force vector.

Return resisting force vector with inertia included.

Send information about element over a channel.

Receive information about element over a channel.

Display element.

Print information about element.

Set response quantities as \"force\", \"deformation\", \"material\", or
\"stiff\". Return response ID or -1 if error. Currently, only the one
uniaxial material can be set.

Get response information for *responseID*. Return 0 if successful, -1
otherwise.
