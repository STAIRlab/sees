# Matrix

```cpp
#include <matrix/Matrix.h>

class Matrix:
```


The Matrix class provides the matrix abstraction. A matrix of order
numRows X numCols is an ordered 2d array of numbers arranged in numRows
rows and numCols columns. For example, a matrix $A$ of order 2 X 3:

$$A =
\left[
\begin{array}{ccc}
a_{0,0} & a_{0,1}  & a_{0,2}  \


a_{1,0} & a_{1,1} & a_{1,2}  \


\end{array}
\right]$$

The Matrix class provides the implementation of a general unsymmetric
matrix. The data for the matrix is stored in a 1d double array of size
numRows\*numCols with the data for $a_{i,j}$ located at j\*numRows + i
in the 1d array. This is similar to the ordering of a Fortran 2d array
and will permit calls to numerical Fortran libraries, e.g. BLAS, for
certain method calls at a future stage. At present no subclassing is
permitted (THIS MAY CHANGE), the reason for this is that the Matrix
objects are envisioned to be small scale matrices primarily used for the
passing of data between objects in the system. To allow subclassing
could reduce the efficiency of the program due to the manner in which
virtual functions are implemented.




To construct a Matrix with numRows = $0$, and numCols = $0$. No memory
is allocated to store the data.

To construct a Matrix with numRows = *nrows*, and numCols = *ncols* and
all coefficients equal to $0$. Allocates memory for the storage of the
data. If numRows $<$ $0$, numCols $<$ $0$ or not enough memory is
available available, an error message is printed and a Matrix with
numRows = $0$ and numCols = $0$ is returned. Before the Matrix is
returned, `Zero()` is called on the Matrix.

To construct a Matrix with numRows = *nrows*, and numCols = *ncols* and
all coefficients equal to $0$. The memory for storage of the data is
found at the location pointed to by *data*. Note that this memory must
have been previously allocated and it must be of appropriate size,
erroneous results and segmentation faults can occur otherwise. No
additional memory is allocated for the storage of the data.

To construct a Matrix using another Matrix. The new Matrix will be a
general matrix that is identical to the Matrix *M*, i.e. same size and
identical components. If not enough memory is available, an error
message is printed and a Matrix with numRows = $0$ and numCols = $0$ is
returned. The constructor tests for the type of $M$ to see whether the
performance can be improved, by avoiding having to call $M$'s overloaded
(i,j) operators if $M$ is of type genMatrix.




Free's up any memory allocated in the constructor. Note that if the
third constructor had been invoked, the memory passed is not released
back to the system (this must be done later by the user of this
constructor).




Returns the number of rows, numRows, of the Matrix. The method is
declared inline for the compiler to produce faster code which does not
require a method call.

Returns the number of columns, numCols, of the Matrix.

Zero's out the Matrix, i.e. sets all the components of the matrix to
$0$. The method tests for the type of Matrix, to see whether the
performance can be improved by avoiding having to call the overloaded
(i,j) operators if the Matrix is of type genMatrix.

Assembles into the current Matrix the Matrix *M*. The contents of the
current matrix at location (*rows(i),cols(j)*) is set equal to the
current value plus *fact* times the value of the matrix *M* at location
(*i,j* ). A warning is printed for every `rows(i), cols(j)`{.cpp} specified
which is outside the bounds of the matrix.

Will solve the equation *$Ax=V$* for the Vector *x*, which is returned.
At the moment the current matrix is assumed to be symmetric positive
definite. THIS IS TO CHANGE. A Vector is created using *V*. If this
Vector is not of the correct size or if an error occurs during
factorization a warning message is printed and the Vector *x* is
returned.

To add a factor *fact* times the Matrix *other* to the current Matrix.
The size of the other Matrix is first checked to see sizes are
compatible; if size are not compatible nothing is done and a warning
message is printed. The method tests for the type of *other*, to see
whether the performance can be improved by avoiding having to call
*other*'s overloaded (i,j) operators, if *other* is of type genMatrix.




Returns the data at location(*row,col*) in the Matrix. Assumes
(*row,col*) is a valid location in the Matrix, a segmentation fault or
erroneous results can occur if this is not the case.

Used to set the data at location(*row,col*) in the Matrix. Assumes
(*row,col*) is a valid location in the Matrix, a segmentation fault or
erroneous results can occur if this is not the case.

Returns a new Matrix of dimension (*rows.Size()*, *cols.Size()*). The
contents of the new matrix are given by the contents of the current
matrix at the locations given by the *rows* and *cols* objects. For
example the contents of the new matrix at location (*i,j*) are equal to
the contents of the current matrix at location (*rows(i),cols(j)*).
Assumes ( *row,col*) is a valid location in the Matrix, a segmentation
fault or erroneous results can occur if this is not the case.

Sets the current Matrix to be equal to the Matrix given by *M*. If the
Matrices are of different sizes, the current data is deallocated and
additional space allocated before the contents are copied. If not enough
space can be allocated for the new data, an error message is printed and
a Matrix of size $0$ x $0$ is returned. The method tests for the type of
*M*, to see whether the performance can be improved by avoiding having
to call $M$'s overloaded (i,j) operators, if $M$ is of type genMatrix.
This method must be implemented by each subclass.

A method to add *fact* to each component of the current Matrix. The
method tests for the type of the current Matrix, to see whether the
performance can be improved by avoiding having to call the overloaded
(i,j) operators, if the current Matrix is of type genMatrix.

A method to subtract *fact* from each component of the current Matrix.
The method tests for the type of the current Matrix, to see whether the
performance can be improved by avoiding having to call the overloaded
(i,j) operators, if the current Matrix is of type genMatrix.

A method to multiply each component of the current Matrix by *fact*. The
method tests for the type of the current Matrix, to see whether the
performance can be improved by avoiding having to call the overloaded
(i,j) operators, if the current Matrix is of type genMatrix.

A method which will divide each component of the current Matrix by
*fact*. If *fact* is equal to zero, an error message is printed and the
contents of the Matrix are set to MATRIX_VERY_LARGE_VALUE (defined in
 `<Matrix.h>`). The method tests for the type of the current Matrix, to
see whether the performance can be improved by avoiding having to call
the overloaded (i,j) operators, if the current Matrix is of type
genMatrix.

A method to return a new Matrix, whose components are equal to the
components of the current Matrix plus the value *fact*. A new Matrix
object is constructed, using the current Matrix as the argument to the
constructor. The *+=* operator is then invoked on this Matrix with
*fact* as the argument, and the new Matrix is then returned.

A method to return a new Matrix, whose components are equal to the
components of the current Matrix minus the value *fact*. A new Matrix
object is constructed, using the current Matrix as the argument to the
constructor. The *-=* operator is then invoked on this Matrix with
*fact* as the argument, and this new Matrix is then returned.

A method to return a new Matrix, whose components are equal to the
components of the current Matrix times the value *fact*. A new Matrix
object is constructed, using the current Matrix as the argument to the
constructor. The *=* operator is then invoked on this Matrix with *fact*
as the argument, and this new Matrix is then returned.

A method to return a new Matrix whose components are equal to the
components of the current Matrix divided the value *fact*. A new Matrix
object is constructed by using the current Matrix as the argument to the
constructor. The */=* operator is then invoked on this Matrix with
*fact* as the argument, and this new Matrix is then returned.

A method to return a new Vector, of size numRows, whose components are
equal to the product of the current Matrix times the Vector *V*. If the
current Matrix and Vector *V* are not compatible, i.e. V.Size() is not
equal to numCols, an error message is printed and a zero Vector of size
equal to the number of rows in the current Matrix is returned. The
method tests for the type of the current Matrix, to see whether the
performance can be improved by avoiding having to call the overloaded
(i,j) operators, if the current Matrix is of type genMatrix.

A method to return a new Vector, of size numCols, whose components are
equal to the product of the transpose of the current Matrix times the
Vector *V*. If the current Matrix and Vector *V* are not compatible,
i.e. V.Size() is not equal to numRows, an error message is printed and a
zero Vector of size equal to the number of columns in the current Matrix
is returned. The method tests for the type of the current Matrix, to see
whether the performance can be improved by avoiding having to call the
overloaded (i,j) operators, if the current Matrix is of type genMatrix.

A method to return a new Matrix equal to the sum of the current Matrix
and the Matrix *M*. It does this by creating a new matrix passing itself
as an argument to the constructor. The `addMatrix()` method is then
invoked on this new Matrix with $M$ and $-1$ as the arguments. The new
Matrix is then returned.

A method to return a new Matrix equal to the the current Matrix minus
the Matrix *M*. It does this by creating a new matrix passing itself as
an argument to the constructor. The `addMatrix()` method is then invoked
on this new Matrix with $M$ and $-1$ as the arguments. The new Matrix is
then returned.

A method to return a new Matrix equal to the product of the current
Matrix and the Matrix *M*. It does this by first creating a new Matrix
of size numRows and M.numCols. The contents of this new Matrix are then
determined and the resulting Matrix is returned. If the two matrices are
of incompatible sizes, a warning message is printed and a zeroed Matrix
is returned. The method tests for the type of the current Matrix, to see
whether the performance can be improved by avoiding having to call the
overloaded (i,j) operators, if *M* is of type genMatrix.

A method to return a new Matrix equal to the product of the transpose of
the current Matrix and the Matrix *M*. It does this by first creating a
new Matrix of size numRows and M.numRows. The contents of this new
Matrix are then determined and the resulting Matrix is returned. If the
two matrices are of incompatible sizes, a warning message is printed and
a zeroed Matrix is returned. The method tests for the type of the
current Matrix, to see whether the performance can be improved by
avoiding having to call the overloaded (i,j) operators, if *M* is of
type genMatrix.

To print the contents of the Matrix to the output stream *s*. The method
will print the contents one row at a time.

To read the contents of the Matrix from the input stream *s*. The method
expects the components one row at a time.

```{.cpp}
friend OPS_Stream &operator$<<$(OPS_Stream &s, const Matrix &M);
```

A function to print out the contents of the Matrix *M* to the output
stream *s*. Does this by invoking `Output()` on the Matrix *M*.

```{.cpp}
friend OPS_Stream &operator$>>$(istream &s, const Matrix &M);
```

A function to print out the contents of the Matrix *M* to the output
stream *s*. Does this by invoking `Output()` on the Matrix *M*.
