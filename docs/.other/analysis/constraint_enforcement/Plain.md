# Plain

```cpp
#include <analysis/handler/PlainHandler.h>
```

class PlainHandler: public ConstraintHandler\

MovableObject\
ConstraintHandler\

\
The PlainHandler class is a class which only deals with homogeneous
single point constraints. To do this it creates regular `FE_Element` and
DOF_Group objects and enforces the constraints by specifying that
degrees-of-freedom which are constrained are not assigned an equation
number. Pointers to the `DOF_Group` and `FE_Element` objects are kept in two
arrays.

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\

The integer *HANDLER_TAG_PlainHandler* (defined in  `<classTags.h>`) is
passed to the PlainHandler constructor.

\
Invokes the destructor on all the `FE_Element` and `DOF_Group` objects
created in *handle*. Then invokes the destructor on the two pointer
arrays.

\
Determines the number of FE_Elements and DOF_Groups needed from the
Domain (a one to one mapping between Elements and FE_Elements and Nodes
and DOF_Groups) Creates two arrays of pointers to store the FE_elements
and DOF_Groups, returning a warning message and a $-2$ or $-3$ if not
enough memory is available for these arrays. Then the object will
iterate through the Nodes of the Domain, creating a `DOF_Group` for each
node and setting the initial id for each dof to $-2$ if no SP_Constraint
exists for the dof, or $-1$ if a SP_Constraint exists or $-3$ if the
node identifier is in *nodesToBeNumberedLast*. The object then iterates
through the Elements of the Domain creating a `FE_Element` for each
Element, if the Element is a Subdomain `setFE_ElementPtr()` is invoked
on the Subdomain with the new `FE_Element` as the argument. If not enough
memory is available for any `DOF_Group` or `FE_Element` a warning message is
printed and a $-4$ or $-5$ is returned. If any `MP_Constraint` objects
exist in the Domain a warning message is printed and $-6$ is returned.
If all is successful, the method returns the number of
degrees-of-freedom associated with the DOF_Groups in
*nodesToBeNumberedLast*.

```{.cpp}
void clearAll(void) =0;
```

Currently this invokes delete on all the `FE_Element` and DOF_Group
objects created in `handle()` and the arrays used to store pointers to
these objects. FOR ANALYSIS INVOLVING DYNAMIC LOAD BALANCING, RE-MESHING
AND CONTACT THIS MUST CHANGE.
*int sendSelf(int commitTag, Channel &theChannel);* \
Returns $0$.
*int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker
&theBroker);* \
Returns $0$.
