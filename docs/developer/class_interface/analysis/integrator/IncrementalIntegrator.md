\
# IncrementalIntegrator 

```cpp
#include <analysis/integrator/IncrementalIntegrator.h>
```

class IncrementalIntegrator: public Integrator\

MovableObject\
Integrator\

\
IncrementalIntegrator is an abstract class. A subclass of it is used
when performing a static or transient analysis using an incremental
displacement approach. Subclasses of IncrementalIntegrators provide
methods informing the FE_Element and DOF_Group objects how to build the
tangent and residual matrices and vectors. They also provide the method
for updating the response quantities at the DOFs with appropriate
values; these values being some function of the solution to the linear
system of equations.

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\

\

\
// Public Method added for Domain Decomposition\

\
// Protected Methods\

\

\

\
The integer *classTag* is passed to the Integrator classes constructor.
Pointers to the AnalysisModel and LinearSOE are set to $0$.

\
Does nothing.

\
Invoked by the Analysis object to set up the links the
IncrementalIntegrator objects needs to perform its operations. Sets the
pointers to the AnalysisModel and LinearSOE objects to point to
*theAnalaysisModel* and *theSOE*.

```{.cpp}
virtual int formTangent(void);
```

Invoked to form the structure tangent matrix. The method first loops
over all the FE_Elements in the AnalysisModel telling them to form their
tangent and then it loops over the FE_Elements again adding the tangent
to the LinearSOE objects A matrix. It performs the following:

::: {.tabbing}
while ̄ while w̄hile ̄ FE_EleIter &theEles = theAnalysisModel.getFEs();\
theSOE.zeroA();\
while((elePtr = theEles1()) $\neq$ 0)\
if (theSOE.addA(elePtr-$>$getTangent(this), elePtr-$>$getID(), $1.0$)
$<$ 0)\
return $-1$;
:::

Returns $0$ if successful, otherwise an error message is printed an a
$-1$ is returned if `setLinks()` has not been called, or $-2$ if failure
to add an FE_Elements tangent to the LinearSOE. The two loops are
introduced to allow for efficient parallel programming. THIS MAY CHANGE
TO REDUCE MEMORY DEMANDS.

```{.cpp}
virtual int formUnbalance(void);
```

Invoked to form the unbalance. The method fist zeros out the $B$ vector
of the LinearSOE object and then invokes formElementResidual() and
formNodalUnbalance() on itself.

::: {.tabbing}
while ̄ while w̄hile ̄ theSOE.zeroB();\
this-$>$fromElementResidual();\
this-$>$formNodalUnbalance()\
:::

If an error occurs in either of these two methods or if `setLinks()` has
not been called, an error message is printed and a negative number is
returned. Returns $0$ if successful.

To inform the FE_Element how to build its tangent matrix for addition to
the system of equations. The subclasses must provide the implementation
of this method.

```{.cpp}
virtual int formEleResidual(FE_Element \*theEle) =0;
```

To inform the FE_Element how to build its residual vector for addition
to the system of equations. The subclasses must provide the
implementation of this method.

```{.cpp}
virtual int formNodTangent(DOF_Group \*theDof) =0;
```

To inform the DOF_Group how to build its tangent matrix for addition to
the system of equations. The subclasses must provide the implementation
of this method. This is required in transient analysis as th Node
objects have mass. THIS MAY CHANGE.

```{.cpp}
virtual int formNodUnbalance(DOF_Group \*theDof) =0;
```

To inform the DOF_Group how to build its residual vector for addition to
the system of equations. The subclasses must provide the implementation
of this method.

```{.cpp}
virtual int update(const Vector &$\Delta U$) =0;
```

When invoked causes the integrator object to update the DOF_Group
responses with the appropriate values based on the computed solution to
the system of equation object. The subclasses must provide an
implementation of this method.

```{.cpp}
virtual int commit(void) =0;
```

Invoked by the SolutionAlgorithm to inform the Integrator that current
state of domain is on solution path. Returns the result of invoking
`commitDomain()` on the AnalysisModel object associated with the
Integrator.

\
Returns in *result* values for the last solution to the system of
equation object whose location in the solution vector is given by *id*.
For a location specified by a negative integer in *id* 0.0 will be
returned in *result*. Returns a $0$ if successful, a warning message and
a negative number is returned if an error occurs. $-1$ if `setSize()`
has not been called and a $-2$ if location in *id* is greater than
$order-1$ of $b$ vector.

\
A const member function which returns a pointer to the LinearSOE
associated with the IncrementalIntegrator object, i.e. *theSOE* passed
in `setLinks()`.

```{.cpp}
AnalysisModel \*getAnalysisModelPtr(void) const;
```

A const member function which returns a pointer to the AnalysisModel
associated with the IncrementalIntegrator object, i.e. *theModel* passed
in `setLinks()`.

```{.cpp}
virtual int formNodalUnbalance(void);
```

The method first loops over all the DOF_Group objects telling them to
form their unbalance and then adds this Vector to the $b$ vector of the
LinearSOE object, i.e. it performs the following:\

::: {.tabbing}
while ̄ while w̄hile ̄ DOF_EleIter &theDofs =
theAnalysisModel.getDOFs();\
theSOE.zeroB();\
while((dofPtr = theDofs()) $\neq$ 0)\
theSOE.addB(dofPtr-$>$getUnbalance(theIntegrator), dofPtr-$>$getID())\
:::

Returns $0$ if successful, otherwise a negative number is returned and a
warning message is printed if an error occurred. Note, no test is made
to ensure `setLinks()` has been invoked.

```{.cpp}
virtual int formElementResidual(void);
```

Invoked to form residual vector (the C vector in theSOE). The method
iterates twice over the FE_elements in the AnalysisModel, the first time
telling the FE_Elements top form their residual and the second time to
add this residual to the LinearSOE objects $b$ vector, i.e. it performs
the following:

::: {.tabbing}
while ̄ while w̄hile ̄ FE_EleIter &theEles = theAnalysisModel.getFEs();\
while((elePtr = theEles()) $\neq$ 0) {\
theSOE.addA(elePtr-$>$getResidual(this), elePtr-$>$getID())\
:::

Returns $0$ if successful, otherwise a warning message is printed and a
negative number is returned if an error occurs. Note, no test is made to
ensure `setLinks()` has been invoked.
