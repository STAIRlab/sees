\
# DOF_Numberer 

```cpp
#include <analysis/numberer/DOF_Numberer.h>
```

class DOF_Numberer: public MovableObject\

MovableObject\

\
The DOF_Numberer class is a base class. Its purpose is to define the
interface common among all subclasses. A DOF_Numberer object is
responsible for assigning the equation numbers to the individual dofs in
each of the DOF_Groups in the AnalysisModel. The base DOF_Numberer uses
a GraphNumberer object to first number the DOF_Groups, based on the
ordering of the DOF_Group objects, it assigns the equation numbers to
the individual degrees-of-freedom. Subtypes may wish to implement the
numbering in a more efficient manner by using the FE_Element and
DOF_Group objects directly.

// Constructors\

\

\
// Destructor\

\
// Public Methods\

\

\

\
// Protected Methods\

\

\
The integer *NUMBERER_TAG_DOF_Numberer* (defined in  `<classtags.h>`)
is passed to the MovableObject classes constructor. Sets the
GraphNumberer to be used in the numbering to `theGraphNumberer()`.

Provided for subclasses. The integer *classTag* is passed to the
MovableObject classes constructor.

Provided for FEM_ObjectBroker. The integer *NUMBERER_TAG_DOF_Numberer*
(defined in  `<classtags.h>`) is passed to the MovableObject classes
constructor. Sets the GraphNumberer to be used in the numbering to be
$0$, the GraphNumberer object is created and linked in a `recvSelf()`
method invocation.

\
Does nothing.

\
Invoked to set a link to the AnalysisModel from which the DOF_Numberer
will number (provide the equation number in the SystemOfEqn object) the
degrees-of-freedoms in each DOF_Group objects.

Invoked to assign the equation numbers to the dofs in the DOF_Groups and
the FE_Elements, ensuring that the dof's in the DOF_Group whose tag is
given by *lastDOF_Group* are numbered last in a $-2$ or $-3$ group. The
initial values of these equation numbers have been set by the
ConstraintHandler object to be $-1$, $-2$ or $-3$, all dofs with a $-3$
are to be assigned higher equation numbers than those assigned a $-2$.
To set the *numEqn* in the AnalysisModel and to return the number of
equations *numEqn* if successful, a negative number if not.

This base class performs the ordering by getting an ID containing the
ordered DOF_Group tags, obtained by invoking
*number(theModel-$>$getDOFGroupGraph(), lastDOF_Group)* on the
GraphNumberer, *theGraphNumberer*, passed in the constructor. The base
class then makes two passes through the DOF_Group objects in the
AnalysisModel by looping through this ID; in the first pass assigning
the equation numbers incrementally to any degree-of-freedom marked with
a $-2$ and in the second pass assigning the equation numbers
incrementally to any degree-of-freedom marked with a $-3$. It then
iterates through the FE_Elements in the AnalsisModel invoking `setID()`
on each object. Finally `setNumEqn(numEqn)` is invoked on the
AnalysisModel. Return *numEqn* if successful, a warning message and a
negative number is returned if an error occurs; $-1$ is returned if
`setLinks()` has not yet been invoked, $-2$ if no GraphNumberer was
passed in the constructor, $-3$ if the number of *DOF_Groups* in
AnalysisModel and size of ID returned are not the same, and a $-4$ if
there is no DOF_Group corresponding to one of the tags given in the ID.

Invoked to assign the equation numbers to the dofs in the DOF_Groups and
the FE_Elements, ensuring that the dof's in the DOF_Groups whose tag is
given in *lastDOF_Groups* are numbered last in a $-2$ or $-3$ group. The
initial values of these equation numbers have been set by the
ConstraintHandler object to be $-1$, $-2$ or $-3$, all dofs with a $-3$
are to be assigned higher equation numbers than those assigned a $-2$.
To set the *numEqn* in the AnalysisModel and to return the number of
equations *numEqn* if successful, a negative number if not.

This method in the base class is almost identical to the one just
described. The only difference is that the ID identifying the order of
the DOF_Groups is obtained by invoking
*number(theModel-$>$getDOFGroupGraph(), lastDOF_Groups)* on the
GraphNumberer.

The DOF_Numberer sends the class identifier and database tag of the
GraphNumberer in a ID to the channel, if no GraphNumberer is associated
a $-1$ is sent as the class tag. The object then invokes `sendSelf()` on
the GraphNumberer.

The DOF_Numberer receives the class identifier and database tag of the
GraphNumberer in an ID from the channel, if no GraphNumberer is
associated a $-1$ is received. The DOF_Numberer will then ask
*theBroker* for a GraphNumberer with that class identifier, it sets the
database tag for the GraphNumberer and it then invokes `recvSelf()` on
that GraphNumberer.

\
A const member function to return the AnalysisModel object associated
with the DOF_Numberer, *theModel*.

A const member function to return the GraphNumberer object associated
with the DOF_Numberer, *theGraphNumberer*.
