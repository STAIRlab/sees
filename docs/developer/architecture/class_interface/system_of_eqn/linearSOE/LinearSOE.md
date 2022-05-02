
# LinearSOE 

```cpp
#include <system_of_eqn/linearSOE/LinearSOE.h>

class LinearSOE: 
    public SystmOfEqn
           MovableObject
```


LinearSOE is an abstract class. A LinearSOE object provides an
abstraction of a system of linear equations. A linear system of equation
of order $n$:

$$\begin{array}{ccccccccc}
a_{0,0}x_0 & + & a_{0,1}x_1  & + & ... & + & a_{0,n-1}x_{n-1} & = & b_0  \\
a_{1,0}x_0 & + & a_{1,1}x_1  & + & ... & + & a_{1,n-1}x_{n-1} & = & b_1 \\
 ...  &  & ...  &  & & &  ... & & ... \\
a_{n-1,0}x_0 & + & a_{n-1,1}x_1  & + & ... & + & a_{n-1,n-1}x_{n-1} &
= & b_{n-1} \\ 
\end{array}$$

can be expressed by the matrix equation $Ax=b$, where $A$ is a matrix of
order $n$ X $n$ and $b$ and $x$ are vectors or order $n$. A LinearSOE
object is responsible for storing these equations and for providing
methods at the interface to set up and obtain the equations. Each
LinearSOE object will be associated with a LinearSOESolver object. It is
the LinearSOESolver objects that is responsible for solving the linear
system of equations.

\



The integer `classTag` is passed to the constructor for the `SystemOfEqn`.
The constructor sets sets the pointer for the currently associated
LinearSOESolver object to point to *theSolver*.

\
Does nothing.

\
Causes the SystemOfEqn object to invoke `solve()` on the currently
associated LinearSOESolver object. Returns a $0$ if successful, negative
number if not; the actual value depending on the LinearSOESolver. To
solve a linear system of equations means to find $x$ such that the
equation $Ax=b$ is satisfied.

A method which returns the number of equations in the system, i.e. the
number of unknowns.

Invoked to allow the LinearSOE object to determine the size and sparsity
of the matrix $A$ and vectors $x$ and $b$. This information can be
deduced from the number of vertices and the connectivity between the
vertices in the Graph object *G*. To return $0$ if successful, a
negative number if not.

The LinearSOE object assembles *fact* times the Matrix *M* into the
matrix $A$. The Matrix is assembled into $A$ at the locations given by
the ID object *loc*, i.e. $a_{loc(i),loc(j)} +=
M(i,j)$. Numbering in $A$ starts at $(0,0)$, i.e. C style. If a location
specified is outside the range, i.e. $(-1,-1)$ the corresponding entry
in *M* is not added to $A$. To return $0$ if successful, a negative
number if not.
*virtual int addB(const Vector & theVector, const ID & loc, double fact
= 1.0) =0;*\
The LinearSOE object assembles *fact* times the Vector *V* into the
vector $b$. The Vector is assembled into $b$ at the locations given by
the ID object *loc*, i.e. $b_{loc(i)} += V(i)$. If a location specified
is outside the range, e.g. $-1$, the corresponding entry in *V* is not
added to $b$. To return $0$ if successful, a negative number if not.

```{.cpp}
virtual int setB(const Vector & theVector, double fact = 1.0) =0;
```

The LinearSOE object sets the vector *b* to be *fact* times the Vector
*V*. To return $0$ if successful, a negative number if not.

```{.cpp}
virtual void zeroA(void) =0;
```

To zero the matrix $A$, i.e. set all the components of $A$ to $0$.

```{.cpp}
virtual void zeroB(void) =0;
```

To zero the vector $b$, i.e. set all the components of $b$ to $0$.

```{.cpp}
virtual const Vector &getX(void) = 0;
```

To return, as a Vector object, the vector $x$. A const reference is
returned, meaning the Vector that is returned cannot be modified, i.e.
no non-const method can be invoked on the Vector.

```{.cpp}
virtual const Vector &getB(void) = 0;
```

To return as a Vector object the vector $b$. A const reference is
returned, meaning the Vector that is returned cannot be modified, i.e.
no non-const method can be invoked on the Vector.

```{.cpp}
virtual double normRHS(void) =0;
```

To return the 2-norm of the vector $x$.

```{.cpp}
virtual void setX(int loc, double value) =0;
```

The LinearSOE object is responsible for setting $x(loc) = value$. This
is needed in domain decomposition methods and could be useful in
iterative solution strategies when an initial approximation is known.

This is invoked to set the currently associated LinearSOESolver object
to be *newSolver*. Each subclass will provide it's own variation of
`setSolver()` method (needed so subclasses can verify type of Solver
object passed). the subclasses in their variation of the `setSolver()`
method (unless they wish to implement their own `solve()` method) invoke
this method. Returns $0$.

Returns a pointer to the associated LinearSOESolver object.
