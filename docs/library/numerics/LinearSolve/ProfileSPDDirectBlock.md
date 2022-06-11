# ProfileSPDDirectBlockSolver

UNDER CONSTRUCTION

```cpp
#include <system_of_eqn/linearSOE/profileSPD/ProfileSPDLinDirectBlockSolver.h>

class ProfileSPDLinDirectBlockSolver: public LinearSOESolver\
```



MovableObject\
Solver\
LinearSOESolver\
ProfileSPDLinSolver\


A ProfileSPDLinDirectBlockSolver object can be constructed to solve a
ProfileSPDLinSOE object. It does this by direct means, using the $LDL^t$
variation of the cholesky factorization. The matrx $A$ is factored one
block row at a time using a right-looking approach. No BLAS or LAPACK
routines are called for the factorization or subsequent substitution.

Constructor\

\
Destructor\

\
Public Methods\

\

\

\
A unique class tag (defined in  `<classTags.h>`) is passed to the
ProfileSPDLinSolver constructor.

\
Does nothing.

\
The solver first copies the B vector into X. FILL IN The solve process
changes $A$ and $X$.

Does nothing but return $0$.

Does nothing but return $0$.

Does nothing but return $0$.
