# PlainNumberer 

```cpp
#include <analysis/numberer/PlainNumberer.h>

class PlainNumberer: public DOF_Numberer
MovableObject
DOF_Numberer
```

\
The PlainNumberer class is a DOF_Numberer. An object of this class
assigns the equation numbers to thee DOF_Groups based on the order in
which they are obtained from the DOF_GroupIter object obtained from the
AnalyisModel. The class is useful for situations where the SystemOfEqn
or Solver objects will impose a renumbering on the equations, which
makes performing a complex numbering of the degrees-of-freedom a waste
of computational effort.

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\

The integer *NUMBERER_TAG_PlainNumberer* is passed to the DOF_Numberer
classes constructor.

\
Does nothing.

\
The PlainNumberer will twice obtain the DOF_GroupIter from the
AnalysisModel. It iterates twice through the DOF_Groups first assigning
the dofs with eqn numbers assigned -2 a number and then on the next pass
the dofs assigned -3. The PlainNumberer then invokes `setID()` on each
FE_Element in the AnalysisModel. Finally it invokes `setEqnNum(numEqn)`
on the AnalyisModel. Returns a positive integer equal to the last
equation number set if successful, a negative number if not; the value
of which depends on the type of the PlainNumberer. A PlainNumberer will
not use the *lastDOF_Group* integer, if one is supplied a warning
message is printed.

The method is identical to that outlined above. A PlainNumberer will not
use the *lastDOF_Groups* ID, if this method is invoked a warning message
is printed.

Returns $0$.

Returns $0$.
