# ModifiedNewton

```cpp
#include <analysis/algorithm/equiSolnAlgo/ModifiedNewton.h>


class ModifiedNewton: public EquiSolnAlg;
```

MovableObject\
SolutionAlgorithm\
EquiSolnAlgo\


The `ModifiedNewton` class is an algorithmic class which obtains a
solution to a non-linear system using the modified Newton-Raphson
iteration scheme. The Newton-Rapson iteration scheme is based on a
Taylor expansion of the non-linear system of equations $\R(\U) = \zero$
about an approximate solution $\U{(i)}$: 

$$\R(\U) = 
\R({\bf U}^{(i)}) +
\left[ {\frac{\partial \R}{\partial \U} \vert}_{{\bf U}^{(i)}}\right]
\left( {\bf U} - {\bf U}^{(i)} \right)$$

which can be expressed as: $$\
{\bf K}^{(i)}  \Delta \U{(i)} = \R({\bf U}^{(i)})$$ which is solved for
$\Delta {\bf U}^{(i)}$ to give approximation for
${\bf U}^{(i+1)} = {\bf U}^{(i)} + \Delta {\bf U}^{(i)}$. To start the iteration
${\bf U}^{(1)} = {\bf U}_{trial}$, i.e. the current trial response quantities are
chosen as initial response quantities.
in the modified version the tangent is formed only once, i.e $$\
{\bf K}^{(1)}  \Delta {\bf U}^{(i)} = \R({\bf U}^{(i)})$$

To stop the iteration, a test must be performed to see if convergence
has been achieved at each iteration. Each NewtonRaphson object is
associated with a ConvergenceTest object. It is this object which
determines if convergence has been achieved.

### Constructors and Destructors


The constructor takes as an argument the ConvregenceTest object
*theTest*, the object which is used at the end of each iteration to
determine if convergence has been obtained. The integer
`EquiALGORITHM_TAGS_ModifiedNewton` (defined in  `<classTags.h>`) is
passed to the EquiSolnAlgo classes constructor.

Provided for FEM_ObjectBroker to instantiate a blank object with a class
tag of EquiALGORITHM_TAGS_ModofiedNewton. `recvSelf()` must be invoked
on this object.

```cpp
~ModifiedNewton();
```
Does nothing.

### Public Methods

```cpp
int solveCurrentStep(void);
```
When invoked the object first sets itself as the EquiSolnAlgo object
that the ConvergenceTest is testing and then it performs the modified
Newton-Raphson iteration algorithm:

```cpp
theTest->start();
theIntegrator->formTangent();
do {
  theIntegrator->formUnbalance();
  theSOE->solveX();
  theIntegrator->update(theSOE->getX());
} while (theTest->test() == false)
```

The method returns a 0 if successful, otherwise a negative number is
returned; a $-1$ if error during `formTangent()`, a $-2$ if error during
`formUnbalance()`, a $-3$ if error during `solve()`, and a $-4$ if error
during `update()`. If an error occurs in any of the above operations the
method stops at that routine, none of the subsequent operations are
invoked. A $-5$ is returned if any one of the links has not been setup.

```{.cpp}
void setTest(ConvergenceTest &theTest);
```

A method to set the tolerance criteria of the algorithm to be equal to
the value *theTol*.

```{.cpp}
int sendSelf(int commitTag, Channel &theChannel);
```

Creates an ID object, puts the values of the *theTest* objects class and
database tags into this ID. It then invokes `sendVector()` on the
Channel object *theChannel* to send the data to the remote object. It
then invokes `sendSelf()` on *theTest*. Returns $0$ if successful, the
channel error if not.
*int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker
&theBroker);*\
Creates an ID object, invokes `recvVector()` on the Channel object. Uses
the data in the ID to create a ConvergenceTest object of appropriate
type and sets its dbTag. It then invokes `recvSelf()` on this test
object.

```{.cpp}
int Print(OPS_Stream &s, int flag =0);
```

Sends the string 'ModifiedNewton' to the stream if *flag* equals $0$.
