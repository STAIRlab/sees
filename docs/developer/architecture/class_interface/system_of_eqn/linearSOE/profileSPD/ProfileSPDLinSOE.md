# ProfileSPDLinSOE

```cpp
#include "ProfileSPDLinSOE.h"

class ProfileSPDLinSOE: public LinearSOE
```

    MovableObject
    SystemOfEqn
    LinearSOE


`ProfileSPDLinSOE` is class which is used to store a symmetric system of
equations using a profile storage scheme. The upper triangular part of
$A$ is stored in a 1d double array with the diagonals of $A$ located at
positions given by an integer array $iLoc$. For example when $n=5$ and
$A$ as shown below:

$$\left[
\begin{array}{ccccc}
a_{0,0} & a_{0,1}  & 0 & 0 & a_{0,4} \\
a_{1,0} & a_{1,1} & a_{1,2} & a_{1,3} & 0 \\
a_{2,0} & a_{2,1} & a_{2,2} & a_{2,3} & a_{2,4}  \\
0 & a_{3,1} & a_{3,2} & a_{3,3} & a_{3,4} \\
0 & 0 & a_{4,2} & a_{4,3} & a_{4,4} \\
\end{array}
\right]$$

this is stored using:

$$A =
\left[
\begin{array}{cccccccccccccccccccc}
a_{0,0} & a_{0,1}  & a_{1,1} & a_{1,2} & a_{2,2} & a_{1,3} &
a_{2,3} & a_{3,3} & a_{0,4} & 0 & a_{2,4} & a_{3,4} & a_{4,4}\\
\end{array}
\right]$$

and

$$iLoc =
\left[
\begin{array}{cccccccccccccccccccc}
1 & 3 & 5 & 8 & 13 \\
\end{array}
\right]$$ 

Note $iLoc$ stores the diagonal locations using Fortran
indexing. This is to facilitate calls to Fortran libraries, e.g.
Digital's DXML. The $x$ and $b$ vectors are stored in 1d double arrays
of length $N$.


The *solver* and a unique class tag (defined in  `<classTags.h>`) are
passed to the LinearSOE constructor. The system size is set to $0$ and
the matrix $A$ is marked as not having been factored. Invokes
*setLinearSOE(\*this)* on the *solver*. No memory is allocated for the
1d arrays.
*ProfileSPDLinSOE(int N, int \*newIloc, ProfileSPDLinSolver
&theSolver);* \
The *solver* and a unique class tag (defined in  `<classTags.h>`) are
passed to the LinearSOE constructor. The system size is set to $N$ and
the matrix $A$ is marked as not having been factored or condensed.
Obtains memory from the heap for the 1d arrays storing the data for $A$,
$x$, $b$ and $iLoc$ and stores the size of these arrays. If not enough
memory is available for these arrays a warning message is printed and
the system size is set to $0$. The size of $A$ is given by
$newIloc(N-1)$, if this is not a valid address in *newIloc* a
segmentation fault or erronious results will result. The contents of
$iLoc$ are set equal to those of *newIloc*. Invokes
*setLinearSOE(\*this)* and `setSize()` on *solver*, printing a warning
message if `setSize()` returns a negative number. Also creates Vector
objects for $x$ and $b$ using the `(double \*,int)`{.cpp} Vector constructor.

\
Calls delete on any arrays created.

\
Invokes `setLinearSOE(\*this)`{.cpp} on *newSolver*. If the system size is not
equal to $0$, it also invokes `setSize()` on *newSolver*, printing a
warning and returning the returned value if this method returns a number
less than $0$. Finally it returns the result of invoking the LinearSOE
classes `setSolver()` method.

A method which returns the current size of the system.

The size of the system is determined by looking at the adjacency ID of
each Vertex in the Graph object *G*. This is done by first determining
the column height for each Vertex $i$ in *G*, done by setting $iLoc(i)$
equal to $0$ and then checking for each Vertex in *G*, whether any of
the vertex tags in the Vertices adjacency ID results in $iLoc(i)$ being
increased. Knowing the col height of each column, the values of *iLoc*
can be determined. Knowing *iLoc* and the size of the system (the number
of Vertices in *G*, a check to see if the previously allocated 1d arrays
for $A$, $x$ and $b$ are large enough. If the memory portions allocated
for the 1d arrays are not big enough, the old space is returned to the
heap and new space is allocated from the heap. Printins a warning
message if not enough memory is available on the heap for the 1d arrays
and returns a $-1$. If memory is available, the components of the arrays
are zeroed and $A$ is marked as being unfactored. If the system size has
increased, new Vector objects for $x$ and $b$ using the *(double
\*,int)* Vector constructor are created. Finally, the result of invoking
`setSize()` on the associated Solver object is returned.

First tests that *loc* and *M* are of compatible sizes; if not a warning
message is printed and a $-1$ is returned. The LinearSOE object then
assembles *fact* times the Matrix *M* into the matrix $A$. The Matrix is
assembled into $A$ at the locations given by the ID object *loc*, i.e.
$a_{loc(i),loc(j)} +=
fact * M(i,j)$. If the location specified is outside the range, i.e.
$(-1,-1)$ the corrseponding entry in *M* is not added to $A$. If *fact*
is equal to $0.0$ or $1.0$, more efficient steps are performed. Returns
$0$.

```{.cpp}
int addB(const Vector & V, const ID & loc, double fact = 1.0) =0;
```

First tests that *loc* and *V* are of compatible sizes; if not a warning
message is printed and a $-1$ is returned. The LinearSOE object then
assembles *fact* times the Vector *V* into the vector $b$. The Vector is
assembled into $b$ at the locations given by the ID object *loc*, i.e.
$b_{loc(i)} += fact * V(i)$. If a location specified is outside the
range, e.g. $-1$, the corresponding entry in *V* is not added to $b$. If
*fact* is equal to $0.0$, $1.0$ or $-1.0$, more efficient steps are
performed. Returns $0$.

```{.cpp}
int setB(const Vector & V, double fact = 1.0) =0;
```

First tests that *V* and the size of the system are of compatible sizes;
if not a warning message is printed and a $-1$ is returned. The
LinearSOE object then sets the vector *b* to be *fact* times the Vector
*V*. If *fact* is equal to $0.0$, $1.0$ or $-1.0$, more efficient steps
are performed. Returns $0$.

```{.cpp}
void zeroA(void) =0;
```

Zeros the entries in the 1d array for $A$ and marks the system as not
having been factored.

```{.cpp}
void zeroB(void) =0;
```

Zeros the entries in the 1d array for $b$.

```{.cpp}
const Vector &getX(void) = 0;
```

Returns the Vector object created for $x$.

```{.cpp}
const Vector &getB(void) = 0;
```

Returns the Vector object created for $b$.

```{.cpp}
double normRHS(void) =0;
```

Returns the 2-norm of the vector $x$.

```{.cpp}
void setX(int loc, double value) =0;
```

If *loc* is within the range of $x$, sets $x(loc) = value$.

Returns $0$. The object does not send any data or connectivity
information as this is not needed in the finite element design.

Returns $0$. The object does not receive any data or connectivity
information as this is not needed in the finite element design.
