\
# SP_Constraint 

```cpp
#include <domain/constraints/SP_Constraint.h>
```

class SP_Constraint: public DomainComponent\

TaggedObject\
MovableObject\
DomainComponent\

\
An SP_Constraint represents a single point constraint in the domain. A
single point constraint specifies the response of a particular
degree-of-freedom at a node. The declaration that all methods are
virtual allows for time varying constraints to be introduced.

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

To construct a single point constraint to constrain the trial
displacement of the *ndof*'th dof at node *node* to the value given by
*value*. The integer value *tag* is used to identify the SP_Constraint
among all other SP_Constraints. If *value* is equal to $0.0$ the method
`isHomogeneous()` will always return *true*, otherwise *false*.

Provided for subclasses to use. The subclasses can vary the value of the
imposed displacement when `getValue()` is invoked. If this constructor
is used the `isHomogeneous()` method will always return *false*. The
integer value *tag* is used to identify the SP_Constraint among all
other SP_Constraints.

Provided for the FEM_ObjectBroker to be able to instantiate an object;
the data for this object will be read from a Channel object when
`recvSelf()` is invoked. $0$ and *classTag* are passed to the
DomainComponent constructor.

\
Does nothing. Provided so that a subclasses destructor can be invoked.

\
Returns the value of *node* passed in the constructor, this should be
the tag of the node that is being constrained.

```{.cpp}
virtual int getDOF_Number(void) const;
```

Returns the value of *ndof* that was passed in the constructor, this
identifies the dof number corresponding to the constraint.

To set the value of the constraint for the load factor given by
*loadFactor*. The constraint is set equal to *loadFactor* \* *value* if
the constraint is not constant, or *value* if the constraint was
identified as constant in the constructor.

To return a boolean indicating whether or not the constraint is a
homogeneous constraint. A homogeneous constraint is one where the value
of the constraint, *value*, is always $0$. This information can be used
by the ConstraintHandler to reduce the number of equations in the
system.

```{.cpp}
virtual double getValue(void) const;
```

To return the value of the constraint determined in the last call to
`applyConstraint()`. This base class returns *value* passed in the
constructor.

To set the LoadPattern tag associated with the object to be
*loadPatternTag*.

To return the load pattern tag associated with the load.

```{.cpp}
virtual int sendSelf(int commitTag, Channel &theChannel);
```

Creates a Vector, and stores the SP_Constraints tag, nodeTag, ndof and
value in the Vector. It then passes the Vector as an argument to
*theChannel* objects `sendVector()` method, along with the objects
database tag and *commitTag*. Subclasses must invoke this method in
their implementation of `sendSelf()`, so that the *node* and *ndof*
values in remote object can be set. Returns $0$ if successful, a
negative number if the Channel object, *theChannel*, failed to send the
data.
*virtual int recvSelf(int commitTag, Channel &theChannel,
FEM_ObjectBroker &theBroker);*\
Creates a Vector, and receives the Vector from the channel object using
the `recvVector()` method call and the objects own database tag and
*commitTag*. Using the information contained in the Vector, the
SP_Constraints tag, nodeTag, ndof and value are set. Subclasses must
invoke this method in their implementation of `recvSelf()`, so that the
*node* and *ndof* values can be set. Returns $0$ if successful, a
negative number if the Channel object, *theChannel*, failed to receive
the data.

```{.cpp}
virtual void Print(OPS_Stream &s, int flag = 0) const;
```

Prints out the SP_Constraints tag, then *node*, *ndof* and *value*.
