NEED A GETTANGFORCE() LIKE FE_ELEMENT FOR ELE_BY_ELE SOLVERS. KEEP A
POINTER TO LAST INTEGRATOR.

# DOF_Group 

```cpp
#include <analysis/dof_grp/DOF_Group.h>
```

class DOF_Group;\

DOF_Group is a base class. An object of type DOF_Group represents an
unconstrained node of the domain in the model. Each node in the domain
is associated with one DOF_Group. DOF_Groups are called upon in the
analysis to provide their contributions of unbalanced load to the system
of equations. Subclasses are used by the constraint handler to to
introduce new dofs into the analysis.

The DOF_Group is responsible for providing operations to set and access
the mapping betwwen equation numbers and DOFs, allowing the Integrator
to from the tangent (if nodal masses in transient problem) and
unbalanced load information, and for setting and obtaining the nodal
trial response quantities.

// Constructors\

\

// Destructor\

\
// Public Methods - Mapping\

\

\

\

\
// Public Methods - Tangent & Residual\

\

\

\

\

// Public Methods - Node Response\

\

\

\

\

\

Constructs a DOF_Group with an associated node given by *theNode* and a
tag given by *tag*. During construction it determines the number of
unknown dofs from the node, *numDOF*, and creates an Vector object to
hold the unbalance information and an ID object to hold mapping between
degrees-of-freedom and equation numbers. All values of the ID are set to
$-2$ initially. It creates a Vector to hold the unbalance loads and an
ID to hold the mapping information, both of size equal to the number of
unknowns. If the size of the Vector or the ID is $0$, i.e. ran out of
memory, a warning message is orinted and *numDOF* set to $0$.

```{.cpp}
DOF_Group(int tag, int numDOF);
```

Provided for subclasses. Constructs a DOF_Group with the number of
unknown dofs given by *numDOF* and a tag given by *tag*. No Node is
associated with this DOF_Group. Creates a Vector of size *numDOF* to
hold the unbalance information and an ID object to hold mapping between
degrees-of-freedom and equation numbers. All values of the ID are set to
$-2$ initially. If the size of the Vector or the ID is $0$, i.e. ran out
of memory, a warning message is orinted and *numDOF* set to $0$.

\
Invokes the destructor on the Vector created to hold the unbalance.

\
Operation to set the equation number of the *dof'th* DOF in the
DOF_Group to *value*. In this base class, if *index* is a valid
location, $0 < index < numDOF-1$ the operator *(index) = value* is
invoked on the ID object created for the mapping, otherwise an error
message is printed.

```{.cpp}
virtual void setID(const ID &values);
```

An operation to set the equation numbers of all the DOFs in the
DOF_Group to be those given in the ID *values*. In this base class, the
operator *= values* is invoked on the ID object created for the
mapping.

```{.cpp}
virtual const ID &getID(void) const;
```

A const member function which returns in an ID object the equation
numbers associated with the degrees-of-freedom in the DOF_Group. The
size of the ID object is equal to the number of degrees-of-freedom
represented by the DOF_Group. This base class returns the ID created for
the mapping.

```{.cpp}
virtual int getTag(void) const;
```

A const member function which returns the integer identifier *tag*
passed in the constructor.

```{.cpp}
virtual int getNumDOF(void) const;
```

Returns the total number of DOFs in the DOF_Group. This base class
returns *numDOF*.

```{.cpp}
virtual int getNumFreeDOF(void) const;
```

Returns the total number of *free* DOFs in the DOF_Group, i.e. number of
dof in the group who have not been assigned a negative equation number.
Determines this by looping through the ID containing the mapping
information.

```{.cpp}
virtual int getNumConstrainedDOF(void) const;
```

Returns the total number of *constrained* DOFs in the DOF_Group, i.e.
number of dof in the group who have been assigned a negative equation
number. Determines this by looping through the ID containing the mapping
information.

\
Returns the current tangent matrix for the DOF_Group. If no tangent
matrix has been created, one of size(numDOF,numDOF) is constructed. If
not enough space is available for a new tangent matrix, an error message
is printed and an error Matrix is returned..

To form the DOF_Groups tangent. Invokes `formNodTangent(this)` on The
Integrator object *theIntegrator*.

To zero the tangent. If a tangent matrix has been allocated, will invoke
`Zero()` on the tangent matrix.

To add *fact* times the nodal mass matrix to the tangent matrix. In this
base class, if a Matrix to store the tangent has not yet been created,
one of size (numDOF,numDOF) is now created; if construction of this
matrix fails an error is printed and an error Matrix is returned.
Invokes `addMatrix(theNode-$>$getMass,fact)`{.cpp} on the Matrix, printing a
warining message if this method returns a $negative$ value. If no Node
is associated with the DOF_Group an error message is printed and nothing
is done.

\
To zero the unbalance vector. Invokes `Zero()` on the vector object used
to store the unbalance information.
*virtual void formUnbalance(Integrator \*theIntegrator);* \
Causes the DOF_Group to form its contribution to the residual. Invokes
`formNodUnbalance(this)` on *theIntegrator*.
*virtual const Vector &getUnbalance() const;* \
Returns the vector holding the unbalance.

```{.cpp}
virtual void addPtoUnbalance(double fact = 1.0);
```

Adds the product of the unbalanced load at the node and *fact* to the
unbalance vector. A warning message is printed and nothing is done if no
node is associated with the DOF_Group, otherwise
*addVector(theNode-$>$getUnbalancedLoad(),fact)* is invoked on the
unbalance vector and a warning message is printed if this method returns
a negative value.

```{.cpp}
virtual void addMtoTang(const Vector &$\ddot u$, double fact);
```


Adds *fact* times the product of the associated nodes mass matrix and
the Vector $\ddot u$ to the unbalance vector. A warning message is
printed and nothing is done if no node is associated with the
DOF_Group.

\
To return the committed displacement at the node. Returns the result of
invoking `getDisp()` on the Node. If there is no associated node object,
an error message is printed and an error Vector is returned.

To return the committed velocity at the node. Returns the result of
invoking `getVel()` on the Node. If there is no associated node object,
an error message is printed and an error Vector is returned.

To return the committed velocity at the node. Returns result of invoking
`getAccel()` on the Node. If there is no associated node object, an
error message is printed and an error Vector is returned.

This operation sets the value of the nodal trial displacement at the
associated node. The vector *u* is of size equal to the number of
equations in the AnalysisModel (this is not checked by the DOF_Group).
The DOF_Group object accesses the contents of the Vector *u* using its
assigned equation numbers. If a $-1$ exists for a DOF a $0$ value is set
as the corresponding nodal displacement for the node. Creates a Vector
to store the correct components of *u*, then invokes `setTrialDisp()` on
the node object; if no node object an error message is printed.
CURRENTLY THERE IS NO CHECK TO SEE IF myID(i) DOES NOT OVERFLOW
ADMISSIBLE VALUES IN U - THIS NEEDS TO CHANGE\

```{.cpp}
virtual int setNodeVel(const Vector &$u^{.}$);
```

This operation sets the value of the nodal trial velocity at the
associated node. The vector *$u^{.}$* is of size equal to the number of
equations in the AnalysisModel (this is not checked by the DOF_Group).
The DOF_Group object accesses the contents of the Vector *$u^{.}$* using
its assigned equation numbers. If a $-1$ exists for a DOF a $0$ value is
set as the corresponding nodal velocity for the node. Creates a Vector
to store the correct components of *u*, then invokes `setTrialVel()` on
the node object; if no node object an error message is printed. MUST
CHANGE AS setNodeDisp\

```{.cpp}
virtual int setNodeAccel(const Vector &$u^{..}$);
```

This operation sets the value of the nodal trial acceleration at the
associated node. The vector *$u^{..}$* is of size equal to the number of
equations in the AnalysisModel (this is not checked by the DOF_Group).
The DOF_Group object accesses the contents of the Vector *$u^{..}$*
using its assigned equation numbers. If a $-1$ exists for a DOF a $0$
value is set as the corresponding nodal acceleration for the node. The
return value is as outlined above for *setNodeAccel().* Creates a Vector
to store the correct components of *u*, then invokes `setTrialAccel()`
on the node object; if no node object an error message is printed. MUST
CHANGE AS setNodeDisp\

\

These methods are similar to those three just outlined, the only
difference being that the trial response quantities at the nodes are
incremented, not set, with the values now given; this is done by
invoking `incrTrialDisp()`, `incrTrialVel()`, and `incrTrialAccel()`
respectively on the nodes. MUST ALL CHANGE AS setNodeDisp\
