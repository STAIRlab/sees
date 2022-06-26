# ProfileSPDDirectBlockSolver

UNDER CONSTRUCTION

```cpp
#include <system_of_eqn/linearSOE/profileSPD/ProfileSPDLinDirectBlockSolver.h>

class ProfileSPDLinDirectBlockSolver: public LinearSOESolver\
```



A ProfileSPDLinDirectBlockSolver object can be constructed to solve a
ProfileSPDLinSOE object. It does this by direct means, using the $LDL^t$
variation of the Cholesky factorization. The matrx $A$ is factored one
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
The solver first copies the $B$ vector into $X$. The solve process
changes $A$ and $X$.


