


\#include $<\tilde{}$/matrix/Vector.h$>$



class Vector:







The Vector class provides the vector abstraction. A vector of order
*size* is an ordered 1d array of *size* numbers. For example a vector of
order 5:


$x = [x_0$ $x_1$ $x_2$ $x_3$ $x_4]$


In the Vector class the data is stored in a 1d double array of length
equal to the order of the Vector. At present time none of the methods
are declared as being virtual. THIS MAY CHANGE FOR PARALLEL.





















































































To construct a Vector of order $0$.

To construct a Vector of order *size*. The constructor creates an array
to store the data and zeroes this array. If not enough memory is
available a warning message is printed and a Vector of order $0$ is
returned. The `Zero()` method is invoked on the new Vector before it is
returned.

To construct a Vector of order *size* whose data will be stored in the
array pointed to by *data*. The array pointed to by data is not set to
zero by the constructor. Note that delete will not be called on this
array in the destructor. It is up to the user to ensure that the array
pointed to by *data* is at least as large as *size*, if this is not the
case erroneous results or a segmentation fault may occur.

To construct a Vector using another Vector. The new Vector will be
identical to the Vector *other*. The constructor creates an array to
store the data and zeroes this array. If not enough memory is available
a warning message is printed and a Vector of order $0$ is returned. The
contents of the array are then set equal to the contents of *other*.




Will delete any space allocated in the constructors. If the array is
passed in the constructor, the space is not deallocated.




Returns the order of the Vector, *size*.

Zeros out the Vector, i.e. sets all the components of the Vector to
$0$.

Assembles into the current Vector the Vector *V*. The contents of the
current Vector at location (`loc(i)`) is set equal to the current value
plus *fact* times the value of the Vector *V* at location (*i*). returns
$0$ if successful. A warning message is printed for each invalid
location in the current Vector or *V* and a $-1$ is returned.

To add a factor *fact* times the Vector *other* to the current Vector.
returns $0$ if successful. An error message is printed and $-1$ is
returned if Vectors are not of the same size. Checks are made to see if
the number of operations can be reduced if *fact* is $0$ or $1$.

To add a factor *fact* times the Vector formed by the product of the
matrix *m* and the Vector *v* to the current Vector. No temporary Vector
is created. Returns $0$ if successful. Prints a warning message and
returns $-1$ if sizes are incompatible. Checks are made to see if the
number of operations can be reduced if *fact* is $0$ or $1$.

Returns the 2 norm of the Vector. Returns the `sqrt()` of the result of
invoking the $\hat{ }$ operator on the current Vector with the current
Vector as the argument.




Returns the data at location *x* in the Vector. Assumes (*x*) is a valid
location in the Vector, i.e. $0 <= x$ order, a segmentation fault or
erroneous results can occur if this is not the case.

Used to set the data at location(*x*) in the Vector. Assumes (*x*) is a
valid location in the Vector, i.e. $0 <= x <$ order, a segmentation
fault or erroneous results can occur if this is not the case.

To safely return the data at location *x* in the Vector. Checks to
ensure *x* is a valid location, i.e. $0 <= x$ order. If *x* is not a
valid location a warning message is printed and VECTOR_NOT_VALID_ENTRY
(a static class variable) is returned. This is a slower but safer
version of *() const*.

Used to safely set the data at location(*x*) in the Vector. Checks to
ensure *x* is a valid location, i.e. $0 <= x$ order. If *x* is not a
valid location a warning message is printed and VECTOR_NOT_VALID_ENTRY
(a static class variable) is modified. This is a slower but safer
version of `()`.

Returns a Vector of order *loc.Size()*. The contents of the new Vector
are given by the contents of the current Vector at the locations given
by the *loc*. For example the contents of the new Vector at location $i$
are equal to the contents of the current Vector at location `loc(i)`.
Creates a new Vector, copies the data from the current Vector and
returns the new Vector. For each invalid location specified in *loc* for
the current Vector, a warning message is printed.

Sets the current Vector to be equal to the Vector given by *other*. If
the Vectors are of different sizes, the current data, if allocated in a
constructor, is deallocated and more space allocated before the contents
are copied. If not enough memory is available a warning message is
printed and the order of the current Vector is set to $0$.

A method to add *fact* to each component of the current Vector.

A method to subtract *fact* from each component of the current Vector.

A method to multiply each component of the current Vector by fact.

A method which will divide each component of the current Vector by
*fact*. If *fact* is equal to zero an warning message is printed and the
components of the Vector are set to VECTOR_VERY_LARGE_VALUE (defined in
$<$Vector.h$>$).

A method to return a new Vector whose components are equal to the
components of the current Vector plus the value *fact*. A new Vector is
constructed using the current Vector as an argument to the constructor;
before the new matrix is returned, the *+=* operator is invoked on the
matrix with *fact*. If the new Vector and current Vector are of
different size, i.e. constructor fails to get enough memory, a warning
message is printed.

A method to return a new Vector whose components are equal to the
components of the current Vector minus the value *fact*. A new Vector is
constructed using the current Vector as an argument to the constructor;
before the new matrix is returned, the *-=* operator is invoked on the
matrix with *fact*. If the new Vector and current Vector are of
different size, i.e. constructor fails to get enough memory, a warning
message is printed.

A method to return a new Vector whose components are equal to the
components of the current Vector times the value *fact*. A new Vector is
constructed using the current Vector as an argument to the constructor;
before the new matrix is returned, the *=* operator is invoked on the
matrix with *fact*. If the new Vector and current Vector are of
different sizes, a warning message is printed.

A method to return a new Vector whose components are equal to the
components of the current Vector divided the value *fact*. A new Vector
is constructed using the current Vector as an argument to the
constructor; before the new matrix is returned, the */=* operator is
invoked on the matrix with *fact*. Warning messages are printed if
*fact* is equal to $0$ or if the new Vector and current Vector are of
different sizes.

A method to add the contents of the Vector *V* to the current Vector. If
Vectors are not of same order a warning message is printed and nothing
is done.

A method to subtract the contents of the Vector *V* from the current
Vector. If Vectors are not of same order a warning message is printed
and nothing is done.

A method to return a new Vector which is equal to the sum of the the
current Vector and the Vector *V*. A new Vector is constructed using the
current Vector as an argument to the constructor; before the new matrix
is returned, the *+=* operator is invoked on the matrix with *V*. If the
current Vector and *V* are not of the same size, a warning message is
printed and a copy of the current Vector is returned. A warning message
is also returned if the new Vector is not of the correct size, i.e. ran
out of memory.

A method to return a new Vector which is equal to the the current Vector
minus the Vector *V*. A new Vector is constructed using the current
Vector as an argument to the constructor; before the new matrix is
returned, the *-=* operator is invoked on the matrix with *V*. If the
current Vector and *V* are not of the same size, a warning message is
printed and a copy of the current Vector is returned. A warning message
is also returned if the new Vector is not of the correct size, i.e. ran
out of memory.

A method to return the dot product of the current Vector and the Vector
*V*. If the current Vector and *V* are not of the same size, a warning
message is printed and $0$ returned.

A method to return a new Vector, $x$, equal to the solution of the
matrix equation $Mx=$ the current Vector. A new Vector is created for
the return of size *M.noRows()*. A new Matrix is created of order
*M.noRows()* x *M.noRows()* and set equal to *M* if *M* is square, or
$M^tM$ if *M* is not square. The new Vector is then set equal to the
result of invoking `Solve(\*this)`{.cpp} on the new Matrix.

```{.cpp}
friend OPS_Stream &operator$<<$(OPS_Stream &s, const Vector &V);
```

A function to print out the contents of the Vector *V* to the output
stream *s*. prints out the contents of the Vector in the stream and then
prints the newline character.

```{.cpp}
friend istream &operator$>>$(istream &s, const Vector &V);
```

A function to read the contents of the Vector *V* from the input stream
*s*. Sets the components of *V* equal to the next *V.Size()* entries in
the stream.
