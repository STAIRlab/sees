# AnalysisModel

MODIFY INTERFACE TO OFFER USER DEFINED STORAGE TYPE.

```cpp
#include  "analysis/model/AnalysisModel.h"

class AnalysisModel : public MovableObject
```

AnalysisModel is a container class. This class is responsible for
holding and providing access to the `FE_Element` and `DOF_Group` objects
that the `ConstraintHandler` creates. It is also responsible for updating
the response quantities at the `DOF_Groups` and for triggering methods in
the associated Domain. It provides operations for the following:

-   **Population**: methods so that the `ConstraintHandler` can add the
    `FE_Element` and `DOF_Group` objects to the analysis model.

-   **Access**: methods so that other classes in the analysis aggregation
    can access the components of the AnalysisModel.

-   **Connectivity**: methods such that the `SysOfEqn` can determine the
    connectivity of the DOF, which is needed for storage, sparsity, etc.

-   **Update**: methods for updating the individual DOFs with the response
    quantities given by the AnalysisMethod.

-   **Trigger**: methods which trigger events in the domain.

Each subclass of `AnalysisModel` must have its own subclasses of
`FE_ELEIter` and `DOF_GrpIter`. NOTE at the moment FE_Element and DOF_Group
objects are not TaggedObjects and for this reason TaggedObjectStorage
classes cannot be used for storage. This may change to allow efficient
storage classes to be used.

### Constructors



### Destructor

\
// Public Methods - Population/Depopulation\

\

\
// Public Member Functions - Access\

\

\

// Public Member Functions - Connectivity\

\

\

// Public Member Functions - Update\

\

\

\

\
// Public Member Functions - Trigger\

\

\

\

\

\

// Public Methods for Output\

\

// Protected Member Functions\

\

Constructs an empty AnalysisModel. The constructor allocates space for
two arrays of 256 pointers to FE_Elements and DOF_Groups. If not enough
memory is available for these arrays, an error message is printed and
the program is terminated. Note these arrays grow automatically if the
problem needs it.

Provided for subclasses to be used. The storage of the FE_Elements and
DOF_Groups and iters to access them must be provided by the subclass.

\
Is responsible for returning to memory the arrays used for storing
pointers to the FE_Element and DOF_Groups which have been added to the
AnalysisModel. It is not responsible for deleting the individual
DOF_Group and FE_Element objects, that is the responsibility of the
ConstraintHandler. If the Graphs have been requested their destructor is
invoked.

\
Adds the FE_Element pointed to by *theElement* to the domain and invokes
*setAnalysisModel(\*this)* on the FE_Element. If the array for the
FE_Elements is large enough, it adds this pointer to the array and
increments the number of FE_Elements in the array. If the array is not
large enough, a new one double in size is constructed, all the old
pointers are copied to this new array and the new pointer is then added.
If not enough room is available for this array, an error message is
printed and the program is terminated. Returns *true*, otherwise *false*
if *theElement* is $0$ or derived class used which does not implement
the method.

```{.cpp}
virtual bool addDOF_Group(DOF_Group \*theGroup);
```

Adds the DOF_Group pointed to by *theGroup* to the domain. If the array
for the DOF_Groups is large enough, it adds this pointer to the array
and increments the number of DOF_Groups in the array. If the array is
not large enough, a new one double in size is constructed, all the old
pointers are copied to this new array and the new pointer is then added.
If not enough room is available for this array, an error message is
printed and the program is terminated. Returns *true*, otherwise *false*
if *theGroup* is $0$ or derived class used which does not implement the
method.

```{.cpp}
virtual void clearAll(void);
```

Clears from the model all FE_Element and DOF_Group objects that have
been added to the analysis model using the above two methods. It does
this by setting the components in the two arrays of pointers equal to
$0$ and setting the number of components to $0$. If the Graphs have been
created their destructor is invoked. Also sets *numEqn* to $0$.

\
Returns the number of DOF_Group objects that have been added to the
model.

Returns a pointer to the DOF_Group object whose tag is given by *tag*.
It first checks to see if the DOF_Group object is at the location in the
array given by *tag*; if not it searches through the array to find the
DOF_Group object. Returns a pointer to the object if found, otherwise
$0$ is returned.

Returns an *FE_EleIter* for the FE_Elements of the model.

```{.cpp}
virtual DOF_Group getDOFs(void)=0;
```

Returns a *DOF_GrpIter* for the DOF_Groups of the model.

\
Sets the value of the number of equations in the model. Invoked by the
DOF_Numberer when it is numbering the dofs.

Returns the number of DOFs in the model which have been assigned an
equation number. Returns the value passed in `setNumEqn()`, if
`setNumEqn()` was not invoked $0$ is returned.

```{.cpp}
virtual const Graph &getDOFGraph(void);
```

Returns the DOF connectivity graph for the individual dofs in the model.
This graph is used by the system of equation object to determine its
size. If no graph has yet been constructed it creates a new DOF_Graph
object using itself as the argument, otherwise it returns a pointer to
this graph. THIS WILL CHANGE WHEN I REMOVE DOF_Graph CLASS - will go
through and construct the Graph.

```{.cpp}
virtual const Graph &getDOFGroupGraph(void);
```

Returns the connectivity of the DOF_Group objects in the model. This
graph is used by the DOF_Numberer to assign equation numbers to the
dofs. If no graph has yet been constructed it creates a new
DOF_GroupGraph object using itself as the argument, otherwise it returns
a pointer to this graph. AGAIN WILL CHANGE.

\
The model is responsible for invoking `setDisp(disp)`, `setVel(vel)` and
`setAccel(accel)` on each DOF_Group in the model. It does this by
iterating over the DOF_Group objects using the iter.

```{.cpp}
virtual void setDisp(const const Vector &disp);
```

The model is responsible for invoking `setDisp(disp)` on each DOF_Group
in the model. It does this by getting an iter to the DOF_Group objects
and iterating through them invoking `setNodeDisp(disp)` on each
DOF_Group.

```{.cpp}
virtual void setVel(const const Vector &vel);
```

The model is responsible for invoking `setVel(vel)` on each DOF_Group in
the model. It does this by getting an iter to the DOF_Group objects and
iterating through them invoking `setNodeVel(vel)` on each DOF_Group.

```{.cpp}
virtual void setAccel(const const Vector &accel);
```

The model is responsible for invoking `setAccel(accel)` on each
DOF_Group in the model. It does this by getting an iter to the DOF_Group
objects and iterating through them invoking `setNodeAccel(accel)` on
each DOF_Group.

```{.cpp}
virtual void incrDisp(const const Vector &disp);
```

The model is responsible for invoking `incrNodeDisp(disp)` on each
DOF_Group in the model. It does this by getting an iter to the DOF_Group
objects and iterating through them invoking `incrNodeDisp(disp)` on each
DOF_Group.

```{.cpp}
virtual void incrVel(const const Vector &vel);
```

The model is responsible for invoking `incrNodeVel(vel)` on each
DOF_Group in the model. It does this by getting an iter to the DOF_Group
objects and iterating through them invoking `incrNodeVel(vel)` on each
DOF_Group.

```{.cpp}
virtual void incrAccel(const const Vector &accel);
```

The model is responsible for invoking `incrNodeAccel(accel)` on each
DOF_Group in the model. It does this by getting an iter to the DOF_Group
objects and iterating through them invoking `incrNodeAccel(accel)` on
each DOF_Group.

\
Method to set the link to the associated Domain. Invoked by during the
construction of the *Analysis* object.
*virtual void applyLoadDomain(double timeStep = 0.0, double loadFactor =
1.0);*\
Method which invokes `applyLoad(timeStep, loadFactor)`{.cpp} on the domain.
This method causes the domain ask the loads in the currently set to
apply themselves. If no Domain has been set nothing is done and an error
message is printed.

```{.cpp}
virtual int commitDomain(void);
```

Method which invokes `commit()` on the domain: this is an operation
which causes all nodes in the domain to take the current values of
response quantities and copy them into the accepted values. Returns $0$
if successful , a negative number if not: $-1$ if no Domain has been set
and $-2$ if `commit()` fails on the Domain.

```{.cpp}
virtual int revertDomainToLastCommit(void);
```

Method which invokes `revertToLastCommit()` on the domain: this is an
operation which causes all nodes in the domain to set the trial response
quantities equal to the last committed response quantities. Returns $0$
if successful , a negative number if not: $-1$ if no Domain has been set
and $-2$ if *revertToLastCommit*() fails on the Domain.

```{.cpp}
virtual void updateDomain(void);
```

Method which invokes `update()` on the domain. If no Domain has been set
nothing is done and an error message is printed.

To get the current time in the Domain. If no Domain has been set a
warning message is printed and $0.0$ is returned, otherwise the result
of invoking `getCurrentTime()` on the Domain is returned.

To set the current time in the Domain to be *newTime*. If no Domain has
been set a warning message is printed, otherwise
`setCurrentTime(newTime)` is invoked on the Domain.

To get the current load factor in the Domain. If no Domain has been set
a warning message is printed and $0.0$ is returned, otherwise the result
of invoking `getCurrentLoadFactor()` on the Domain is returned.
;\
To set the current load factor in the Domain to be *newFactor*. If no
Domain has been set a warning message is printed, otherwise
`setCurrentLoadFactor(newFactor)` is invoked on the Domain.

Returns $0$. Note the FE_Elements and DOF_Group objects are not sent as
they are not MovableObjects. AnalysisModel objects are only sent when
setting up a DomainDecompAnalysis on a remote process; only type info
and whatever subclasses might need need to be sent.
;\
Returns $0$.

\
Returns a pointer to the associated Domain, that is the Domain set when
`setLinks()` was last invoked.
