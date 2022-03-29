# SolutionAlgorithm 

```cpp
#include <analysis/algorithm/SolutionAlgorithm.h>

class SolutionAlgorithm: public MovableObject
```

The `SolutionAlgorithm` class is an abstract base class. Its purpose is to
define the interface common among all its subclasses. A
`SolutionAlgorithm` object performs the steps in the analysis by
specifying the sequence of operations to be performed by members in the
analysis aggregation.

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\
The integer *classTag* is passed to the MovableObject classes
constructor.

\
Invokes the destructor on any recorder object added to the
SolutionAlgorithm and releases memory used to hold pointers to the
recorder objects.

\
Is called by the Analysis if the domain changes. It is called after
`domainChange()` has been called on the `ConstraintHandler`, `DOF_Numberer`
and the Integrator and after `setSize()` has been called on the
SystemOfEqn object. For base class nothing is done and $0$ is returned.
The subclasses can provide their own implementation of this method if
anything needs to be done, e.g. memory allocation, To return $0$ if
successful, a negative number if not.

To add a recorder object *theRecorder* to the SolutionAlgorithm. returns
$0$ if successful, a warning message and a $-1$ is returned if not
enough memory is available.

To invoke `record(track)` on any Recorder objects which have been added
to the SolutionAlgorithm.

To invoke `playback(track)` on any Recorder objects which have been
added to the SolutionAlgorithm.

