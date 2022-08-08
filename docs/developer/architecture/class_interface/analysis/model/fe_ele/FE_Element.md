# FE_Element

```cpp
#include <analysis/fe_ele/FE_Element.h>

class FE_Element;
```

`FE_Element` is a base class, subtypes of which are used to enforce the
constraints on the domain. An object of type `FE_Element` represents an
element of the domain in the analysis. It enforces no constraints other
than single point homogeneous boundary conditions, imposed on any of the
elements nodes. It provides a similar interface to that of an Element
but modified to provide features useful to an Analysis class. The
`FE_Element` is responsible for:

1.  Holding information about the mapping between equation numbers and
    the degrees-of-freedom at the element ends, this mapping is
    determined from the `DOF_Group` objects associated with the elements
    Node objects.

2.  Providing methods to allow the integrator to combine the elements
    stiffness, mass and damping matrices into the elements contribution
    to the structure tangent matrix and the elements resisting force to
    the structure unbalance. Obtaining the stiffness, damping and mass
    matrices from the elements.

3.  Providing methods so other forces can be determined.

While the `FE_Element` class is associated with an element in the domain,
subclasses do not have to be. It is the subclasses that are used to
implement the constraints imposed on the nodal displacements in the
domain.

// Constructors



// Destructor


// Public Methods - Mapping



// Public Methods to form and obtain Tangent & Residual



// Public Methods to allow Integrator to Build Tangent



// Public Methods to allow Integrator to Build Residual




// Public Methods to allow Element-by-Element strategies



// Public Methods added for Domain Decomposition


```cpp
FE_Element(int tag, Element *theElement)
```

Constructs an empty `FE_Element` with an associated element given by
`theElement`. During construction it determines the number of unknown
dofs from the element. Constructs an ID for the mapping between dof's of
the element and equation numbers in the system of equation and an ID to
hold the tag of the `DOF_Group` objects associated with each Node of the
element. If the result of invoking `theElementPtr->isSubdomain()` is
`true` invokes `setFE_Element(this)` on the Subdomain; if false creates
a Matrix for the tangent and a Vector for the residual to be stored. An
error message is printed and the program is terminated if no Domain
object is associated with the Element, a Node of the Element does not
exist in the Domain, each Node has not yet been associated with a
DOF_Group object, or there is not enough memory for the Vectors and
Matrices required.

```{.cpp}
FE_Element(int numDOFGroup, int numDOF);
```

Provided for subclasses. Constructs an empty `FE_Element` with the number
of unknown dofs given by `numDOF` and the number of associated DOF_Group
objects given by `numDOFGroup`, two empty IDs are constructed to hold
the mapping and the tags of the DOF_Groups. The subclass must fill in
the ID for the tags of the DOF_Groups in order that `setID()` will work.
No element is associated with this FE_Element. No space is allocated for
the tangent and residual matrix and vector, this is the responsibility
of the subclass.

```{.cpp}
~FE_Element();
```
Deletes the IDs, Vectors and Matrices created by the constructor.

```cpp
const ID &FE_Element::getDOFtags(void) const 
```

Returns a const ID containing the unique tag number of the `DOF_Group`
objects associated with that FE_Element. For this base class, these are
obtained from the DOF_Groups associated with the Node objects that are
associated with the Element object passed in the constructor. This `ID` is
computed only once, during the creation of the object.

```{.cpp}
virtual const ID &getID(void) const;
```

Returns a const ID containing the equation numbers associated with its
matrices and vectors. This ID will contain $0$'s unless the `setID()`
method has been called.

```{.cpp}
void setAnalysisModel(AnalysisModel &theModel);
```

To set a link to the AnalysisModel in which the `FE_Element` resides; this
link is needed in `setID()`. Is invoked by the AnalysisModel when the
`FE_element` is added to the AnalysisModel.

```{.cpp}
virtual void setID(void);
```

Causes the `FE_Element` to determine the mapping between it's equation
numbers and the degrees-of-freedom. The $i-1$ component of the ID
contains the equation number that is associated with $i$'th
degree-of-freedom (a consequence of C indexing for IDs). The method is
to be invoked by the DOF_Numberer after the DOF_Groups have been
assigned their equation numbers. The base class uses the ID containing
the tags of the `DOF_Group` objects to determine this by looping over the
`DOF_Group` objects (identified in the `DOF_Group` ID and obtained from the
AnalysisModel) and getting their mapping by invoking `getID()`. Returns
$0$ if successful, a warning message and a negative number is returned
if an error occurs: $-1$ returned if no AnalysisModel link has been set,
$-2$ if a `DOF_Group` object does not exist in the AnalysisModel and a
$-3$ if there are more dof's in the DOF_Groups than dof's identified for
the `FE_Element`.


```cpp
const Matrix &FE_Element::getTangent(Integrator *theNewIntegrator)
```
Causes the `FE_Element` to determine it's contribution to the tangent
matrix and to return this matrix. If the Element is a Subdomain it
invokes `computeTangent()` and `getTang()` on the Subdomain. Otherwise
`formEleTangent(this)` is invoked on `theIntegrator` and the new tangent
matrix is returned. Subclasses must provide their own implementation. If
no Element is passed in the constructor, a warning message is printed
and an error Matrix of size $1\times1$ is returned.


```cpp
const Vector &getResidual(Integrator *theNewIntegrator)
```
Causes the `FE_Element` to determine it's contribution to the residual
vector and to return this vector. If the Element is a Subdomain it
invokes `computeResidual()` and `getResistingForce()` on the Subdomain.
Otherwise `formEleResidual(this)` is invoked on *theIntegrator* and the
resuting residual vector is returned. Subclasses must provide their own
implementation. If no Element is passed in the constructor, a warning
message and an error vector is returned.

```cpp
void FE_Element::zeroTangent(void)
```
Zeros the tangent matrix. If the Element is not a Subdomain invokes
`Zero()` on the tangent matrix. Subclasses must provide their own
implementation. Nothing is done and a warning message is printed if no
Element was passed in the constructor or the Element passed was a
Subdomain.

```cpp
virtual void addKtToTang(double fact = 1.0);
```

Adds the product of *fact* times the element's tangent stiffness matrix
to the tangent. If no element is associated with the `FE_Element` nothing
is added, if the element is not a Subdomain
`addMatrix(theEle->getTangentStiff(),fact)` is invoked on the tangent
matrix. Nothing is done and a warning message is printed if no `Element`
was passed in the constructor or the Element passed was a Subdomain.

```cpp
virtual void addKsToTang(double fact = 1.0);
```
Adds the product of `fact` times the element's secant stiffness matrix
to the tangent. If no element is associated with the `FE_Element` nothing
is added, if the element is not a Subdomain
`addMatrix(theEle->getSecantStiff(),fact)` is invoked on the tangent
matrix. Nothing is done and a warning message is printed if no Element
was passed in the constructor or the Element passed was a Subdomain.

```cpp
virtual void addCtoTang(double fact = 1.0);
```
Adds the product of *fact* times the element's damping matrix to the
tangent. If no element is associated with the `FE_Element` nothing is
added, if the element is not a Subdomain
`addMatrix(theEle->getDamp(),fact)` is invoked on the tangent matrix.
Nothing is done and a warning message is printed if no Element was
passed in the constructor or the Element passed was a Subdomain.

```cpp
virtual void addMtoTang(double fact = 1.0);
```
Adds the product of `fact` times the element's mass matrix to the
tangent. If no element is associated with the `FE_Element` nothing is
added, if the element is not a Subdomain
*addMatrix(theEle-$>$getMass(),fact* is invoked on the tangent matrix.
Nothing is done and a warning message is printed if no Element was
passed in the constructor or the Element passed was a Subdomain.

```cpp
void FE_Element::zeroResidual(void)
```
Zeros the residual vector. If the Element is not a Subdomain invokes
`Zero()` on the residual vector. Subclasses must provide their own
implementation. Nothing is done and a warning message is printed if no
Element was passed in the constructor or the Element passed was a
Subdomain.

```cpp
virtual void addRtoResidual(double fact = 1.0);
```
Adds to the residual vector the product of the elements residual load
vector and `fact`. If no element is associated with the `FE_Element`
nothing is added, if the associated element is not a Subdomain
`addVector(myEle->getResistingForce(),fact)` is invoked on the
residual. Nothing is done and a warning message is printed if no Element
was passed in the constructor or the Element passed was a Subdomain.

```cpp
virtual void addRIncInertiaToResidual(double fact = 1.0);
```
Adds to the residual vector the product of the elements residual load
vector with inertia forces included and `fact`. If no element is
associated with the `FE_Element` nothing is added, if the associated
element is not a Subdomain
`addVector(myEle->getResistingForceIncInertia(),fact)` is invoked on
the residual. Nothing is done and a warning message is printed if no
Element was passed in the constructor or the Element passed was a
Subdomain.

*virtual void addKtForce(const Vector &disp, double fact = 1.0);*
Adds to the residual the product of elements current tangent stiffness
matrix and a Vector whose values are obtained by taking the product of
*fact* and those elements of the Vector *disp* associated with the
FE_Elements equation numbers. If no element is associated with the
FE_Element or the Element is a Subdomain nothing is added and an warning
message is printed. An error message is also printed if invoking
`addMatrixVector()` on the residual vector returns $< 0$.

*virtual void addKsForce(const Vector &disp, double fact = 1.0);*
Adds to the residual the product of elements current tangent stiffness
matrix and a Vector whose values are obtained by taking the product of
*fact* and those elements of the Vector *disp* associated with the
FE_Elements equation numbers. If no element is associated with the
FE_Element or the Element is a Subdomain nothing is added and an warning
message is printed. An error message is also printed if invoking
`addMatrixVector()` on the residual vector returns $< 0$.

*virtual void addD_Force(const Vector &vel, double fcat = 1.0);*
Adds to the residual the product of elements current damping matrix and
a Vector whose values are obtained by taking the product of *fact* and
those elements of the Vector *vel* associated with the FE_Elements
equation numbers. If no element is associated with the `FE_Element` or the
Element is a Subdomain nothing is added and an warning message is
printed. An error message is also printed if invoking
`addMatrixVector()` on the residual vector returns $< 0$.

*virtual void addM_Force(const Vector &accel, double fact = 1.0);*
Adds to the residual the product of elements current mass matrix and a
Vector whose values are obtained by taking the product of *fact* and
those elements of the Vector *accel* associated with the FE_Elements
equation numbers. If no element is associated with the `FE_Element` or the
Element is a Subdomain nothing is added and an warning message is
printed. An error message is also printed if invoking
`addMatrixVector()` on the residual vector returns $< 0$.

```cpp
virtual const Vector &getTangForce(const Vector &disp, double fact=1.0);
```
Returns the product of FE_Elements current tangent matrix and a Vector
whose values are obtained by taking the product of *fact* and those
elements of the Vector *disp* associated with the FE_Elements equation
numbers. If the element associated with the `FE_Element` is a subdomain,
the tangent is obtained by invoking `getTang()` on the subdomain,
otherwise the tangent is formed by invoking `formEleTang(this)` on the
integrator object last used in a `getTangent()` or `getResidual()`. If
no element is associated with the `FE_Element` a zero vector is returned
and an error message is printed. An error message is also printed if
invoking `addMatrixVector()` on the force vector returns $< 0$.

```cpp
virtual const Vector &getKtForce(const Vector &disp, double fact=1.0);
```
Returns the product of elements current tangent stiffness matrix and a
Vector whose values are obtained by taking the product of *fact* and
those elements of the Vector *disp* associated with the `FE_Elements`
equation numbers. If no element is associated with the `FE_Element` or the
associated element is a Subdomain an error vector is returned and a
warning message printed.

*virtual const Vector &getKsForce(const Vector &disp, double fact = 1.0);*
Returns the product of elements current secant stiffness matrix and a
Vector whose values are obtained by taking the product of *fact* and
those elements of the Vector *disp* associated with the FE_Elements
equation numbers. If no element is associated with the `FE_Element` or the
associated element is a Subdomain an error vector is returned and a
warning message printed.

```cpp
virtual const Vector &getD_Force(const Vector &vel, double fact = 1.0);
```

Returns the product of elements current damping matrix and a Vector
whose values are obtained by taking the product of *fact* and those
elements of the Vector *vel* associated with the FE_Elements equation
numbers. If no element is associated with the `FE_Element` or the
associated element is a Subdomain a warning message is printed and an
error Vector is returned.

```cpp
virtual const Vector &getM_Force(const Vector &accel, double fcat = 1.0);
```

Returns the product of elements current mass matrix and a Vector whose
values are obtained by taking the product of `fact` and those elements
of the Vector `accel` associated with the FE_Elements equation numbers.
If no element is associated with the `FE_Element` or the associated
element is a Subdomain a warning message is printed and an error Vector
is returned.

```{.cpp}
Integrator *getLastIntegrator(void);
```

Method which returns the last integrator supplied in a `formTangent()`
or a `formResidual()` invocation.

```{.cpp}
const Vector &getLastResponse(void);
```

A method which invokes `getLastResponse()` on the Integrator object that
was last passed as an argument to any of the routines. The `FE_Element`s
ID and the force Vector object is passed as arguments. Returns the force
Vector object if successful. If no element is associated with the
`FE_Element` or no integrator has yet to be passed, a warning message is
printed and an error Vector is returned.

