
```cpp
#include <system_of_eqn/linearSOE/fullGEN/SuperLU.h>
```


class SuperLU: public SparseGenColLinSolver\

MovableObject\
Solver\
LinearSOESolver\
SparseGenColLinSolver\

\
A SuperLU object can be constructed to solve a SparseGenColLinSOE
object. It obtains the solution by making calls on the the SuperLU
library developed at UC Berkeley by Prof. James Demmel, Xiaoye S. Li and
John R. Gilbert. The SuperLU library contains a set of subroutines to
solve a sparse linear system $AX=B$. It uses Gaussian elimination with
partial pivoting (GEPP). The columns of A may be preordered before
factorization; the preordering for sparsity is completely separate from
the factorization and a number of ordering schemes are provided.

// Constructor\

\
// Destructor\

\
// Public Methods\

\

\

\
A unique class tag (defined in  `<classTags.h>`) is passed to the
SparseGenColLinSolver constructor. Saves the values for the arguments
*permSpec*, *panelSize*, *relax* and *thresh* that will be used when
calling the SuperLU routines in `solve()` and `setSize()`.

*permSpec* defines the ordering routine used in defining the column
permutations *permC*: $0$ uses the original ordering supplied, $1$
defines a min-degree ordering based on $A^TA$ and $2$ a min-degree
ordering based on $A^T + A$. *relax* defines the min number of columns
in a subtree for the subtree to be considered a single supernode.
*thresh* defines the pivoting threshold: at step j of the Gaussian
elimination if (abs$(A_{jj}) \ge$ *thresh* (max$i \ge j$ abs($A_{ij}$)).
A value for *thresh* of $0.0$ definines no pivoting, a value of $1.0$
classical partial pivoting. *panelSize* defines the number of
consecutive columns used as a panel in the elimination. For more
information on these values see the SuperLU manual.

\
Invokes delete on *permR*, *permC* and *etree* arrays.

\
First copies $B$ into $X$ and then solves the FullGenLinSOE system it is
associated with (pointer kept by parent class) by calling the SeuperLU
routine `dgstrf()`, if the system is marked as not having been factored,
or `dgstrs()`, if system is marked as having been factored. If the
solution is successfully obtained, i.e. the SuperLU routines return $0$
in the INFO argument, it marks the system has having been factored and
returns $0$, otherwise it prints a warning message and returns INFO. The
solve process changes $A$ and $X$ and sets the char *rafact* to *Y*.

Obtains the size of the system from it's associaed SparseGenColLinSOE
object. With this information it creates space for the integer arrays
*permR*, *permC* and *etree*. It then creates the a SuperMatrix for A by
calling the SuperLU routine `dCreate_CompCol_Matrix()`, sets the column
permutation *permR* by calling the SuperLU routine *get_perm_c(permSpec,
A, permC)*, applies this permutation and determines the elimination tree
*etree* by calling the SuperLU routine `sp_preorder()`. It then creates
a SuperMatrix for X by calling the SuperLU routine
`dCreate_Dense_Matrix()`. Returns $0$ if successful, prints a warning
message and returns a $-1$ if not enough memory is available for the
arrays.

Does nothing but return $0$.

Does nothing but return $0$.
