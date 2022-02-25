\
# CentralDifference 

```cpp
#include <analysis/integrator/CentralDifference.h>
```

class CentralDifference: public TransientIntegrator\

MovableObject\
Integrator\
IncrementalIntegrator\
TransientIntegrator\

\
CentralDifference is a subclass of TransientIntegrator which implements
the CentralDifference method. In the CentralDifference method, to
determine the velocities, accelerations and displacements at time
$t + \Delta t$, the equilibrium equation (expressed for the
TransientIntegrator) is typically solved at time $t$ for
$\U_{t+\Delta t}$, i.e. solve:

$$\R (\U_{t+ \Delta t}) = \P(t) - \F_I(\Udd_{t})
- \F_R(\Ud_{t},\U_{t})$$

where we use following to relate $\Ud_{t}$ and $\Udd_{t}$ to $\U_{t}$
and the displacement quantities at times $t$ and $t - \Delta
t$:

$$\dot \U_{t} = \frac{1}{2 \Delta t} \left(
\U_{t + \Delta t} -  \U_{t - \Delta t} \right)$$

$$\ddot \U_{t} = \frac{1}{\Delta t^2} \left(
\U_{t + \Delta t} - 2 \U_t + \U_{t - \Delta t}\right)$$

which results in the following

$$\left[ \frac{1}{\Delta t^2} \M + \frac{1}{2 \Delta t}
\C \right] \U_{t + \Delta t} = \P(t) - F_I \left(\Udd_t^{(i-1)}
\right)
-F_R\left( \Ud_t^{(i-1)}, \U_t)\right)$$\

// Constructors\

\

// Destructor\

\
// Public Methods\

\

\

\
// Public Methods for Output\

\

\

Sets $\gamma$ to $1/2$ and $\beta$ to $1/4$. Sets a flag indicating
whether the incremental solution is done in terms of displacement,
$\Delta \U$, if *dispFlag* is *true*, or acceleration,
$\Delta \ddot \U$, if *dispFlag* is *false*.

Sets $\gamma$ to *gamma* and $\beta$ to *beta*. Sets a flag indicating
whether the incremental solution is done in terms of displacement or
acceleration to *dispFlag*.

\
Invokes the destructor on the Vector objects created.

\
This tangent for each FE_Element is defined to be $\K_e = c1 \K + c2
\D + c3 \M$, where c1,c2 and c3 were determined in the last invocation
of the `newStep()` method. The method returns $0$ after performing the
following operations:

::: {.tabbing}
while ̄ while w̄hile ̄ theEle-$>$zeroTang()\
theEle-$>$addKtoTang(c1)\
theEle-$>$addCtoTang(c2)\
theEle-$>$addMtoTang(c3)
:::


```{.cpp}
int formNodTangent(DOF_Group \*theDof);
```

The method returns $0$ after performing the following operations:

::: {.tabbing}
while ̄ while w̄hile ̄ theDof-$>$zeroUnbalance()\
theDof-$>$addMtoTang(c3)
:::


```{.cpp}
int domainChanged(void);
```

If the size of the LinearSOE has changed, the object deletes any old
Vectors created and then creates $6$ new Vector objects of size equal to
*theLinearSOE-$>$getNumEqn()*. There is a Vector object created to store
the current displacement, velocity and accelerations at times $t$ and
$t + \Delta t$. The response quantities at time $t + \Delta t$ are then
set by iterating over the DOF_Group objects in the model and obtaining
their committed values. Returns $0$ if successful, otherwise a warning
message and a negative number is returned: $-1$ if no memory was
available for constructing the Vectors.

```{.cpp}
int newStep(double $\Delta t$);
```

The following are performed when this method is invoked:

1.  First sets the values of the three constants *c1*, *c2* and *c3*
    depending on the flag indicating whether incremental displacements
    or accelerations are being solved for at each iteration. If
    *dispFlag* was *true*, *c1* is set to $1.0$, *c2* to
    $\gamma / (\beta * deltaT)$ and *c3* to $1/ (\beta * deltaT^2)$. If
    the flag is *false* *c1* is set to $\beta * deltaT^2$, *c2* to
    $\gamma * deltaT$ and *c3* to $1.0$.

2.  Then the Vectors for response quantities at time $t$ are set equal
    to those at time $t + \Delta t$.

3.  Then the velocity and accelerations approximations at time $t +
    \delta t$ are set using the difference approximations if *dispFlag*
    was *true*. (displacement and velocity if *false*).

4.  The response quantities at the DOF_Group objects are updated with
    the new approximations by invoking `setResponse()` on the
    AnalysisModel with new quantities for time $t + \Delta t$.

5.  current time is obtained from the AnalysisModel, incremented by
    $\Delta t$, and `applyLoad(time, 1.0)`{.cpp} is invoked on the
    AnalysisModel.

6.  Finally `updateDomain()` is invoked on the AnalysisModel.

The method returns $0$ if successful, otherwise a negative number is
returned: $-1$ if $\gamma$ or $\beta$ are $0$, $-2$ if *dispFlag* was
true and $\Delta t$ is $0$, and $-3$ if `domainChanged()` failed or has
not been called.

```{.cpp}
int update(const Vector &$\Delta U$);
```

Invoked this causes the object to increment the DOF_Group response
quantities at time $t + \Delta t$. The displacement Vector is
incremented by $c1 * \Delta U$, the velocity Vector by $c2 * \Delta U$,
and the acceleration Vector by $c3 * \Delta U$. The response at the
DOF_Group objects are then updated by invoking `setResponse()` on the
AnalysisModel with quantities at time $t +
\Delta t$. Finally `updateDomain()` is invoked on the AnalysisModel.
Returns $0$ if successful. A warning message is printed and a negative
number returned if an error occurs: $-1$ if no associated AnalysisModel,
$-2$ if the Vector objects have not been created, $-3$ if the Vector
objects and $\delta U$ are of different sizes.
*int sendSelf(int commitTag, Channel &theChannel);* \
Places the $\beta$ and $\gamma$ and *dispFlag* into a vector if size 3
and invokes *sendVector* on the Channel with this Vector. Returns $0$ if
successful, a warning message is printed and a $-1$ is returned if
*theChannel* fails to send the Vector.
*int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker
&theBroker);* \
Receives in a Vector of size 3 the values of $\beta$, $\gamma$ and
*dispFlag*. Returns $0$ if successful, a warning message is printed,
$\delta \lambda$ is set to $0$, and a $-1$ is returned if *theChannel*
fails to receive the Vector.

```{.cpp}
int Print(OPS_Stream &s, int flag = 0);
```

The object sends to $s$ its type, the current time, $\gamma$ and
$\beta$.
