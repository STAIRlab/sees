\
# ZeroLengthSection 

```cpp
#include <element/zeroLength/ZeroLengthSection.h>
```

class ZeroLengthSection : public Element\

TaggedObject\
MovableObject\
DomainComponent\
Element\

\
The ZeroLengthSection class represents an element defined by two nodes
at the same geometric location, hence it has zero length. The nodes are
connected by a SectionForceDeformation object which represents the
force-deformation relationship for the element.

ZeroLengthSection elements are constructed with a *tag* in a domain of
*dimension* 2 or 3, connected by nodes *Nd1* and *Nd2*. The vector *x*
defines the local x-axis for the element and the vector *yprime* lies in
the local x-y plane for the element. The local z-axis is the cross
product between *x* and *yprime*, and the local y-axis is the cross
product between the local z-axis and *x*.

### Constructors

\

### Destructor

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
Construct a ZeroLengthSection element with *tag* . The force-deformation
relationship for the element is obtained by invoking `getCopy()` on the
**SectionForceDeformation** pointer *theSection*. The section model acts
in the local space defined by the *x* and *yprime* vectors. The section
axial force-deformation acts along the element local x-axis and the
section y-z axes directly corresponsd to the local element y-z axes.

This is the constructor invoked by an **FEM_ObjectBroker** object. It
constructs an empty ZeroLengthSection element with two nodes. The
`recvSelf()` method is invoked on the object for it to set the internal
data.

\
Element destructor deletes memory for storing the section model
pointer.

\
Returns 2.

Return **ID** of size $2$ with the node tags defining the element.

Return the number of DOF for the element, which depends on the dimension
of the problem and the number of DOF associated with each node.

Initialize element and define data structures. Sets up the element
transformation matrix, $A$, which defines the kinematic relationship
between nodal displacements and section deformations.

Commit state of element by committing state of the section. Return 0 if
successful, !0 otherwise.

Revert state of element to last commit by reverting to last committed
state of the section. Return 0 if successful, !0 otherwise.

Revert state of element to initial state by reverting to initial state
of the section. Return 0 if successful, !0 otherwise.

Return tangent stiffness matrix for element. The element tangent is
computed from the section tangent matrix, $k_b$, as $K_e = A^T k_b A$.
The section tangent is obtained by calling `getSectionTangent()`.

Returns the tangent stiffness matrix for the element as the secant
stiffness is not defined for SectionForceDeformation objects.

Return a zero damping matrix.

Return a zero mass matrix.

The element has no loads, so this operation has no effect.

The element has no loads, so this operation has no effect and returns
0.

The element has no mass, so this operation has no effect and returns 0.

Return resisting force vector for element. The element resisting force
is computed from the section stress resultants, $s$, as $P_e = A^T s$.
The section stress resulant is obtained by calling
`getStressResultant()`.

Returns the result of `getResistingForce()` as there is no element
mass.

Send information about element and the section over a channel.

Receive information about element and section from a channel.

Display element.

Prints the element node tags and section model to the stream em s.

Currently returns -1.

Currently returns -1.
