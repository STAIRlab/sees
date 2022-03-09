
```cpp
#include <analysis/algorithm/equiSolnAlgo/NewtonRaphson.h>
```


class NewtonRaphson: public EquiSolnAlg;\

MovableObject\
SolutionAlgorithm\
EquiSolnAlgo\

\
The NewtonRaphson class is an algorithmic class which obtains a solution
to a non-linear system using the Newton-Raphson iteration scheme. The
iteration scheme is based on a Taylor expansion of the non-linear system
of equations $\R(\U) = \zero$ about an approximate solution $\U^{(i)}$:
$$\R(\U) = 
\R(\U^{(i)}) +
\left[ {\frac{\partial \R}{\partial \U} \vert}_{\U^{(i)}}\right]
\left( \U - \U^{(i)} \right)$$

which can be expressed as: $$\
\K^{(i)}  \Delta \U^{(i)} = \R(\U^{(i)})$$ which is solved for
$\Delta \U^{(i)}$ to give approximation for
$\U^{(i+1)} = \U^{(i)} + \Delta \U^{(i)}$. To start the iteration
$\U^{(1)} = \U_{trial}$, i.e. the current trial response quantities are
chosen as initial response quantities. To stop the iteration, a test
must be performed to see if convergence has been achieved at each
iteration. Each NewtonRaphson object is associated with a
ConvergenceTest object. It is this object which determines if
convergence has been achieved.

// Constructors\

\

// Destructor\

\
// Public Member Functions\

\

// Public Methods for Output\

\

\

The constructor takes as an argument the ConvergenceTest object
*theTest*, the object which is used at the end of each iteration to
determine if convergence has been obtained. The integer
*EquiALGORITHM_TAGS_NewtonRaphson* (defined in  `<classTags.h>`) is
passed to the EquiSolnAlgo classes constructor.

Provided for FEM_ObjectBroker to instantiate a blank object with a class
tag of EquiALGORITHM_TAGS_NewtonRaphson is passed. `recvSelf()` must be
invoked on this object.

\
Does nothing.

\
When invoked the object first sets itself as the EquiSolnAlgo object
that the ConvergenceTest is testing and then it performs the
Newton-Raphson iteration algorithm:

::: {.tabbing}
while ̄ while ̄ theTest-$>$start()\
theIntegrator-$>$formUnbalance();\
do {\
theIntegrator-$>$formTangent();\
theSOE-$>$solveX();\
theIntegrator-$>$update(theSOE-$>$getX());\
theIntegrator-$>$formUnbalance();\
} while (theTest-$>$test() $==$ false)
:::

The method returns a 0 if successful, otherwise a negative number is
returned; a $-1$ if error during `formTangent()`, a $-2$ if error during
`formUnbalance()`, a $-3$ if error during `solve()`, and a $-4$ if error
during `update()`. If an error occurs in any of the above operations the
method stops at that routine, none of the subsequent operations are
invoked. A $-5$ is returned if any one of the links has not been setup.
NOTE it is up to ConvergenceTest to ensure an infinite loop situation is
not encountered.

```{.cpp}
void setTest(ConvergenceTest &theTest);
```

A method to set the ConvergenceTest object associated with the Algorithm
to be *theTest*.

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

Sends the string 'NewtonRaphson' to the stream if *flag* equals $0$.
