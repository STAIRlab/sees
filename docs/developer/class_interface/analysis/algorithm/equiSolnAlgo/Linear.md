\
# Linear 

```cpp
#include <analysis/algorithm/equiSolnAlgo/Linear.h>
```

class Linear: public EquiSolnAlg;\

MovableObject\
SolutionAlgorithm\
EquiSolnAlgo\

\
The Linear class is an algorithmic class which uses the linear solution
algorithm to solve the equations. This is based on a Taylor expansion of
the linear system $\R(\U) = \zero$ about an approximate solution
$\U_{a}$.

$$\R(\U) = 
\R(\U_{a}) +
\left[ {\frac{\partial \R}{\partial \U} \vert}_{\U_{a}}\right]
\left( \U - \U_{a} \right)$$ which can be expressed as: $$\
\K_{a} \Delta \U = \R(\U_{a})$$ which is solved for $\Delta \U$ to give
the approximation $\U = \U_{a} + \Delta \U$.
To start the iteration $\U_a = \U_{trial}$, i.e. the current trial
response quantities are chosen as approximate solution quantities.

// Constructor\

\
// Destructor\

\
// Public Methods\

\
// Public Methods for Output\

\

\

The integer *EquiALGORITHM_TAGS_Linear* (defined in  `<classTags.h>`)
is passed to the EquiSolnAlgo classes constructor.

\

\
This method performs the linear solution algorithm:

::: {.tabbing}
while ̄ whilewhilewhilewhilewhilewhilewhilewhilewhile ̄
theIntegrator-$>$formTangent() // form $\K_{a}$\
theIntegrator-$>$formUnbalance() // form $\R(\U_{a})$\
theSOE-$>$solveX() // solve for $\Delta \U$\
theIntegrator-$>$update(theSOE-$>$getX()) // set
$\U = \U_{a} + \Delta \U$
:::

The method returns a 0 if successful, otherwise warning message is
printed and a negative number is returned; a $-1$ if error during
`formTangent()`, a $-2$ if error during `formUnbalance()`, a $-3$ if
error during `solve()`, a $-4$ if error during `update()`. If an error
occurs in any of the above operations the method stops at that routine,
none of the subsequent operations are invoked. A $-5$ is returned if any
one of the links has not been setup.

```{.cpp}
int sendSelf(int commitTag, Channel &theChannel);
```

Does nothing. Returns 0.
*int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker
&theBroker);*\
Does nothing. Returns 0.

```{.cpp}
int Print(OPS_Stream &s, int flag =0);
```

Sends the string 'Linear Algorithm' to the stream.
