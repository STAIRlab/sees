
\#include
$<\tilde{ }$/system_of_eqn/linearSOE/sparseGen/SparseGenColLinSOE.h$>$\

class SparseGenColLinSOE: public LinearSOE\

MovableObject\
SystemOfEqn\
LinearSOE\

\
SparseGenColLinSOE is class which is used to store the matrix equation
$Ax=b$ of order $size$ using a sparse column-compacted storage scheme
for $A$. The $A$ matrix is stored in a 1d double array with $nnz$
elements, where $nnz$ is the number of non-zeroes in the matrix $A$. Two
additional 1d integer arrays $rowA$ and $colStartA$ are used to store
information about the location of the coefficients, with $colStartA(i)$
storing the location in the 1d double array of the start of column $i$
and $rowA(j)$ identifying the row in $A$ to which the $j'th$ component
in the 1d double array. $colStartA$ is of dimension $size+1$ and $rowA$
of dimension $nnz$. For example

$$\left[
\begin{array}{ccccc}
a_{0,0} & 0 & a_{0,2}  & a_{0,3} & 0  \\
a_{1,0} & a_{1,1} & 0 & 0 & 0  \\
0 & a_{2,1} & a_{2,2} & 0 & 0 \\
0 & 0 & 0 & a_{3,3} & a_{3,4} \\
a_{4,0} & a_{4,1} & 0 & 0 & a_{4,4}
\end{array}
\right]$$

is stored in:

$$\left[
\begin{array}{cccccccccccccc}
a_{0,0} & a_{1,0}  & a_{4,0} & a_{1,1} & a_{2,1} & a_{4,1} &
a_{0,2} & a_{2,2} & a_{0,3} & a_{3,3} & a_{3,4} & a_{4,4}  \\
\end{array}
\right]$$

with

$$colStartA =
\left[
\begin{array}{cccccccccccccc}
0 & 3 & 6 & 8 & 10 & 12
\end{array}
\right]$$

and

$$rowA =
\left[
\begin{array}{cccccccccccccc}
0 & 1 & 4 & 1 & 2 & 4 & 0 & 2 & 0 & 3 & 3 & 4 
\end{array}
\right]$$ The $x$ and $b$ vectors are stored in 1d double arrays of
length $n$.

\

\

\

\

\

\

\

\

\

\

\

\

The *solver* and a unique class tag (defined in  `<classTags.h>`) are
passed to the LinearSOE constructor. The system size is set to $0$ and
the matrix $A$ is marked as not having been factored. Invokes
*setLinearSOE(\*this)* on the *solver*. No memory is allocated for the 3
1d arrays.
*SparseGenColLinSOE(int N, int NNZ, int \*colStartA, int \*rowA,
SparseGenColLinSolver &theSolver);* \
The *solver* and a unique class tag (defined in  `<classTags.h>`) are
passed to the LinearSOE constructor. The system size is set to $N$, the
number of non-zeros is set to $NNZ$ and the matrix $A$ is marked as not
having been factored. Obtains memory from the heap for the 1d arrays
storing the data for $A$, $x$ and $b$ and stores the size of these
arrays. If not enough memory is available for these arrays a warning
message is printed and the system size is set to $0$. Invokes
*setLinearSOE(\*this)* and `setSize()` on *solver*, printing a warning
message if `setSize()` returns a negative number. Also creates Vector
objects for $x$ and $b$ using the `(double \*,int)`{.cpp} Vector constructor.
It is up to the user to ensure that *colStartA* and *rowA* are of the
correct size and contain the correct data.

\
Calls delete on any arrays created.

\
Invokes `setLinearSOE(\*this)`{.cpp} on *newSolver*. If the system size is not
equal to $0$, it also invokes `setSize()` on *newSolver*, printing a
warning and returning $-1$ if this method returns a number less than
$0$. Finally it returns the result of invoking the LinearSOE classes
`setSolver()` method.

A method which returns the current size of the system.

The size of the system is determined from the Graph object *theGraph*,
which must contain *size* vertices labelled $0$ through $size-1$, the
adjacency list for each vertex containing the associated vertices in a
column of the matrix $A$. The size is determined by invoking
`getNumVertex()` on *theGraph* and the number of non-zeros is determined
by looking at the size of the adjacenecy list of each vertex in the
graph, allowing space for the diagonal term. If the old space allocated
for the 1d arrays is not big enough, it the old space is returned to the
heap and new space is allocated from the heap. Prints a warning message,
sets size to $0$ and returns a $-1$, if not enough memory is available
on the heap for the 1d arrays. If memory is available, the components of
the arrays are zeroed and $A$ is marked as being unfactored. If the
system size has increased, new Vector objects for $x$ and $b$ using the
*(double \*,int)* Vector constructor are created. The $colStartA$ and
$rowA$ are then determined by looping through the vertices, setting
$colStartA(i)
= colStartA(i-1) + 1 +$the size of Vertices $i$ adjacency list and
placing the contents of $i$ and the adjacency list into $rowA$ in
ascending order. Finally, the result of invoking `setSize()` on the
associated Solver object is returned.

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
