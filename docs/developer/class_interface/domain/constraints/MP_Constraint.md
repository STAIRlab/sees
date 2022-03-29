\
# MP_Constraint 

```cpp
#include <domain/constraints/MP_Constraint.h>
```

class MP_Constraint: public DomainComponent\

TaggedObject\
MovableObject\
DomainComponent\

\
An `MP_Constraint` represents a multiple point constraint in the domain. A
multiple point constraint imposes a relationship between the
displacement for certain dof at two nodes in the model, typically called
the *retained* node and the *constrained* node: $U_c = C_{cr} U_r$

An `MP_Constraint` is responsible for providing information on the
relationship between the dof, this is in the form of a constraint
Matrix, $C_{cr}$, and two ID objects, *retainedID* and *constrainedID*
indicating the dof's at the nodes represented by $C_{cr}$. For example,
for the following constraint imposing a relationship between the
displacements at node $1$, the constrained node, with the displacements
at node $2$, the retained node in a problem where the x,y,z components
are identified as the 0,1,2 degrees-of-freedom:

$$u_{1,x} = 2 u_{2,x} + u_{2,z}$$ $$u_{1,y} = 3 u_{2,z}$$

the constraint matrix is: $$C_{cr} =
\left[
\begin{array}{cc}
2 & 1  \\
0 & 3  \\
\end{array}
\right]$$

*constrainedID* = $[0$ $1]$ and *retainedID* $= [0$ $2]$.

### Constructors

\

\
### Destructor

\
// Public Methods\

\

\

\

\
// Public Methods for Output\

\

\

To construct a multiple point constraint where the constrained node is
given by *nodeConstr*, the retained node by *nodeRetain*, the
*constrainedID* by *constrainedDOF*, the *retainedID* by *retainedDOF*
and $C_{cr}$ by *constraint*. The integers *tag* and
CNSTRNT_TAG_MP_Constraint are passed to the DomainComponent classes
constructor. New Matrix and ID objects are created to hold the
information.

For the subclasses to use. The subclasses can vary the contents of the
Matrix returned when `getConstraint()` is invoked. The integers *tag*
*classTag* are passed to the DomainComponent classes constructor. New ID
objects are created to hold the information.

Provided for the FEM_ObjectBroker to construct a blank object. The data
for the object is filled in when `recvSelf()` is invoked on the object.
$0$ and *classTag* are passed to the DomainComponent constructor.

\
Invokes the destructor on both the ID and the Matrix object, if a Matrix
object is passed in the constructor.

\
Returns the value of *nodeRetain* passed in the constructor, i.e. the
tag of the retained node.
*virtual int getNodeConstrained(void) const;* \
Returns the value of *nodeConstr* passed in the constructor, i.e. the
tag of the constrained node.
*virtual const ID &getConstrainedDOFs(void) const;* \
Returns, as a const, the *constrainedID* formed in the constructor.
*virtual const ID &getRetainedDOFs(void) const;* \
Returns, as a const, the *retainedID* formed in the constructor.
*virtual int applyConstraint(double timeStamp)*\
A method to invoked to inform the `MP_Constraint` to determine $C_{cr}$,
for the time *timeStamp*. **The base class will do nothing, as Matrix is
assumed to be constant.**\

```{.cpp}
virtual const Matrix &getConstraint(void) const;
```

Returns the current constraint Matrix, that determined in the last call
to `applyConstraint()`. For the `MP_Constraint` class, $C_{cr}$ determined
in the constructor is returned.

```{.cpp}
virtual int sendSelf(int commitTag, Channel &theChannel);
```

Creates a Vector, stores the MP_Constraints tag, nodeRetain,
nodeConstrained and value in the Vector, and sends the Vector to the
Channel using the objects own database tag and *commitTag*. It then
sends the *participatingDOF* ID and the *constraint* Matrix, again using
the objects database tag and *commitTag*. Returns $0$ if successful, a
negative number if the Channel object, *theChannel*, failed to send the
data.
*virtual int recvSelf(int commitTag, Channel &theChannel,
FEM_ObjectBroker &theBroker);*\
Creates a Vector, receives the Vector from the Channel using *commitTag*
and the objects database tag, and sets theMP_Constraints tag,
nodeRetain, nodeConstrained from the the Vector. Creates a Vector and a
Matrix, and then receives the *participatingDOF* ID and the *constraint*
Matrix into these objects. Returns $0$ if successful, a negative number
if the Channel object, *theChannel*, failed to receive the data.

```{.cpp}
virtual void Print(OPS_Stream &s, int flag = 0);
```

Prints out the MP_Constraints tag, then the tags of the constrained and
retained nodes, then the two ID's and finally the constraint Matrix.
