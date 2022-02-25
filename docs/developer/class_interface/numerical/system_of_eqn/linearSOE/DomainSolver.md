\
# DomainSolver 

```cpp
#include <system_of_eqn/linearSOE/DomainSolver.h>
```

class DomainSolver: public LinearSOESolver\

MovableObject\
Solver\
LinearSOESolver\

\
DomainSolver is an abstract class. DomainSolver objects are responsible
for performing the numerical operations required for the domain
decomposition methods.

// Constructor\

\
// Destructor\

\
// Public Methods\

\

\

\

\

\
*classTag* is needed by the LinearSOESolver objects constructor.

\

\
Causes the condenser to form
$A_{ee}^* = A_{ee} -A_{ei} A_{ii}^{-1} A_{ie}$, where $A_{ii}$ is the
first *numInt* rows of the $A$ matrix. The original $A$ is changed as a
result. $A_{ee}^*$ is to be stored in $A_{ee}$.

```{.cpp}
virtual int condenseRHS(int numInt) =0;
```

Causes the condenser to form $B_e^* = B_e - A_{ei} A_{ii}^{-1} B_i$,
where $A_{ii}$ is the first *numInt* rows of $A$. The original $B$ is
changed as a result. $B_e^*$ is to be stored in $B_e$.

```{.cpp}
virtual int computeCondensedMatVect(Vector &u, int numInt) =0;
```

Causes the condenser to form $A_{ee} u$.

```{.cpp}
virtual Matrix &getCondensedA(void) =0;
```

Returns the contents of $A_{ee}$ as a matrix.

```{.cpp}
virtual Vector &getCondensedRHS(void) =0;
```

Returns the contents of $B_e$ as a Vector.

```{.cpp}
virtual Vector &getCondensedMatVect(void) =0;
```

Returns the contents of the last call to `computeCondensedMatVect()`.
`virtual int setComputedXext(const Vector &u) =0;`{.cpp}
Sets the computed value of the unknowns in $X_e$ corresponding to the
external equations to *u*. The number of external equations is given by
the size of vector $u$.

```{.cpp}
virtual int solveXint(void) =0;
```

To compute the internal equation numbers $X_i$ given the value set for
the external equations in the last call to `setComputedXext()`.
