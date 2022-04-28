# Linear 

```cpp
#include <analysis/algorithm/equiSolnAlgo/Linear.h>

class Linear: 
public EquiSolnAlg;
       MovableObject
       SolutionAlgorithm
       EquiSolnAlgo
```


The Linear class is an algorithmic class which uses the linear solution
algorithm to solve the equations. This is based on a Taylor expansion of
the linear system $\R(\U) = \zero$ about an approximate solution
${\bf U}_{a}$.

$$\R(\U) = 
\R({\bf U}_{a}) +
\left[ {\frac{\partial \R}{\partial \U} \vert}_{{\bf U}_{a}}\right]
\left( {\bf U} - {\bf U}_{a} \right)$$ 

which can be expressed as: 

$${\bf K}_{a} \Delta {\bf U} = {\bf R}({\bf U}_{a})$$ 

which is solved for $\Delta \U$ to give
the approximation ${\bf U} = {\bf U}_{a} + \Delta \U$.
To start the iteration ${\bf U}_a = {\bf U}_\text{trial}$, i.e. the current trial
response quantities are chosen as approximate solution quantities.

### Constructor


### Destructor


### Public Methods


// Public Methods for Output


The integer `EquiALGORITHM_TAGS_Linear` (defined in  `<classTags.h>`)
is passed to the EquiSolnAlgo classes constructor.



This method performs the linear solution algorithm:

<!--// while ̄ whilewhilewhilewhilewhilewhilewhilewhilewhile ̄
-->

>```cpp
>// form {\bf K}_{a}
>theIntegrator->formTangent() 
>// form \R({\bf U}_{a})
>theIntegrator->formUnbalance() 
>// solve for \Delta \U
>theSOE->solveX() 
>// set U = Ua + DU
>theIntegrator->update(theSOE->getX()) 
>```
>
>The method returns a 0 if successful, otherwise warning message is
printed and a negative number is returned; a $-1$ if error during
`formTangent()`, a $-2$ if error during `formUnbalance()`, a $-3$ if
error during `solve()`, a $-4$ if error during `update()`. If an error
occurs in any of the above operations the method stops at that routine,
none of the subsequent operations are invoked. A $-5$ is returned if any
one of the links has not been setup.

>```{.cpp}
>int sendSelf(int commitTag, Channel &theChannel);
>```
>
>Does nothing. Returns 0.


>```{.cpp}
>int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker &theBroker);
>```
>Does nothing. Returns 0.

>```{.cpp}
>int Print(OPS_Stream &s, int flag =0);
>```
>Sends the string `'Linear Algorithm'` to the stream.

