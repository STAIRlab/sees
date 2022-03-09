\
\#include
$<\tilde{ }$/system_of_eqn/linearSOE/bandSPD/BandSPDLinLapackSolver.h$>$\

class BandSPDLinLapackSolver: public BandSPDLinSolver\

MovableObject\
Solver\
LinearSOESolver\
BandSPDLinSolver\

\
A BandSPDLinLapackSolver object can be constructed to solve a
BandSPDLinSOE object. It obtains the solution by making calls on the the
LAPACK library. The class is defined to be a friend of the BandSPDLinSOE
class (see  `<BandSPDLinSOE.h>`).

// Constructor\

\
// Destructor\

\
// Public Methods\

\

\

\
A unique class tag (defined in  `<classTags.h>`) is passed to the
BandSPDLinSolver constructor.

\
Does nothing.

\
The solver first copies the B vector into X and then solves the
BandSPDLinSOE system by calling the LAPACK routines `dpbsv()`, if the
system is marked as not having been factored, and `dpbtrs()` if system
is marked as having been factored. If the solution is successfully
obtained, i.e. the LAPACK routines return $0$ in the INFO argument, it
marks the system has having been factored and returns $0$, otherwise it
prints a warning message and returns INFO. The solve process changes $A$
and $X$.

Does nothing but return $0$.

Does nothing but return $0$.

Does nothing but return $0$.
