# BandGenLinLapackSolver
## User Interface

## Class Interface

```cpp
#include <system_of_eqn/linearSOE/bandGEN/BandGenLinLapackSolver.h>

class BandGenLinLapackSolver:
public BandGenLinSolver
       MovableObject
       Solver
       LinearSOESolver
```


A `BandGenLinLapackSolver` object can be constructed to solve a
`BandGenLinSOE` object. It obtains the solution by making calls on the the
LAPACK library. The class is defined to be a friend of the BandGenLinSOE
class (see  `<BandGenLinSOE.h>`).

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\
A unique class tag (defined in  `<classTags.h>`) is passed to the
BandGenLinSolver constructor. Sets the size of *iPiv* to $0$, *iPiv*
being an integer array needed by the LAPACK routines.

\
Invokes delete on *iPiv* to free the memory allocated to store the
array.

\
The solver first copies the B vector into X and then solves the
BandGenLinSOE system by calling the LAPACK routines `dgbsv()`, if the
system is marked as not having been factored, and `dgbtrs()` if system
is marked as having been factored. If the solution is successfully
obtained, i.e. the LAPACK routines return $0$ in the INFO argument, it
marks the system has having been factored and returns $0$, otherwise it
prints a warning message and returns INFO. The solve process changes $A$
and $X$.

Is used to construct a 1d integer array, *iPiv* that is needed by the
LAPACK solvers. It checks to see if current size of *iPiv* is large
enough, if not it deletes the cold and creates a larger array. Returns
$0$ if successful, prints a warning message and returns a $-1$ if not
enough memory is available for this new array.

Does nothing but return $0$.

Does nothing but return $0$.
