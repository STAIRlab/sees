\
# HHT 

```cpp
#include <analysis/integrator/HHT.h>
```

class HHT: public TransientIntegrator\

MovableObject\
Integrator\
IncrementalIntegrator\
TransientIntegrator\

\
HHT is a subclass of TransientIntegrator which implements the
Hilber-Hughes-Taylor (HHT) method. In the HHT method, to determine the
velocities, accelerations and displacements at time $t + \Delta t$, by
solving the following equilibrium equation

$$\R (\U_{t + \Delta t}) = \P(t + \Delta t) -
\F_I(\Udd_{t+\Delta t}) - \F_R(\Ud_{t + \alpha \Delta t},\U_{t +
\alpha \Delta t})$$

where

$$\U_{t + \alpha} = \left( 1 - \alpha \right) \U_t + \alpha \U_{t +
\Delta t}$$

$$\Ud_{t + \alpha} = \left( 1 - \alpha \right) \Ud_t + \alpha \Ud_{t +
\Delta t}$$

and the velocities and accelerations at time $t + \Delta t$ are
determined using the Newmark relations. The HHT method results in the
following for determining the response at $t + \Delta t$

$$\left[ \frac{1}{\beta \Delta t^2} \M + \frac{\alpha \gamma}{\beta
\Delta t} \C + \alpha \K \right] \Delta \U_{t + \Delta t}^{(i)} = \P(t
+ \Delta t) - \F_I\left(\Udd_{t+\Delta  t}^{(i-1)}\right)
- \F_R\left(\Ud_{t + \alpha \Delta t}^{(i-1)},\U_{t + \alpha \Delta
t}^{(i-1)}\right)$$\

// Constructors\

\

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

The integer INTEGRATOR_TAGS_HHT is passed to the TransientIntegrator
constructor. $\alpha$, $\beta$ and $\gamma$ are set to 0.0. This
constructor should only be invoked by an FEM_ObjectBroker.

Sets $\alpha$ to *alpha*, $\gamma$ to $(1.5 - \alpha)$ and $\beta$ to
$0.25*\alpha^2$. In addition, a flag is set indicating that Rayleigh
damping will not be used.

This constructor is invoked if Rayleigh damping is to be used, i.e.
$\D = \alpha_M M + \beta_K K$. Sets $\alpha$ to *alpha*, $\gamma$ to
$(1.5 - \alpha)$, $\beta$ to $0.25*\alpha^2$, $\alpha_M$ to *alphaM* and
$\beta_K$ to *betaK*. Sets a flag indicating whether the incremental
solution is done in terms of displacement or acceleration to *dispFlag*
and a flag indicating that Rayleigh damping will be used.
Sets $\alpha$ to *alpha*, $\gamma$ to $(1.5 - \alpha)$ and $\beta$ to
$0.25*\alpha^2$. In addition, a flag is set indicating that Rayleigh
damping will not be used.

\
Invokes the destructor on the Vector objects created.

\
This tangent for each FE_Element is defined to be $\K_e = c1\alpha \K
+ c2\alpha \D + c3 \M$, where c1,c2 and c3 were determined in the last
invocation of the `newStep()` method. Returns $0$ after performing the
following operations:

::: {.tabbing}
while ̄ while w̄hile ̄ if (RayleighDamping == false) {\
theEle-$>$zeroTang()\
theEle-$>$addKtoTang(c1)\
theEle-$>$addCtoTang(c2)\
theEle-$>$addMtoTang(c3)\
} else {\
theEle-$>$zeroTang()\
theEle-$>$addKtoTang(c1 + c2 \* $\beta_K$)\
theEle-$>$addMtoTang(c3 + c2 \* $\alpha_M$)\
}
:::


```{.cpp}
int formNodTangent(DOF_Group \*theDof);
```

This performs the following:

::: {.tabbing}
while ̄ while w̄hile ̄ if (RayleighDamping == false)\
theDof-$>$addMtoTang(c3)\
else\
theDof-$>$addMtoTang(c3 + c2 \* $\alpha_M$)\
:::


```{.cpp}
int domainChanged(void);
```

If the size of the LinearSOE has changed, the object deletes any old
Vectors created and then creates $8$ new Vector objects of size equal to
*theLinearSOE-$>$getNumEqn()*. There is a Vector object created to store
the current displacement, velocity and accelerations at times $t$ and
$t + \Delta t$, and the displacement and velocity at time $t + \alpha
\Delta t$. The response quantities at time $t + \Delta t$ are then set
by iterating over the DOF_Group objects in the model and obtaining their
committed values. Returns $0$ if successful, otherwise a warning message
and a negative number is returned: $-1$ if no memory was available for
constructing the Vectors.

```{.cpp}
int newStep(double $\Delta t$);
```

The following are performed when this method is invoked:

1.  First sets the values of the three constants *c1*, *c2* and *c3*,
    *c1* is set to $1.0$, *c2* to $\gamma / (\beta * \Delta t)$ and *c3*
    to $1/ (\beta * \Delta t^2)$.

2.  Then the Vectors for response quantities at time $t$ are set equal
    to those at time $t + \Delta t$.

    ::: {.tabbing}
    while w̄hile w̄hile w̄hile ̄ $\U_t = \U_{t + \Delta t}$\
    $\Ud_t = \Ud_{t + \Delta t}$\
    $\Udd_t = \Udd_{t + \Delta t}$
    :::

3.  Then the velocity and accelerations approximations at time $t +
    \Delta t$ and the displacement and velocity at time
    $t + \alpha \Delta t$ are set using the difference approximations.

    ::: {.tabbing}
    while w̄hile w̄hile w̄hile ̄ $\U_{t + \alpha \Delta t} = \U_t$\
    $\dot \U_{t + \Delta t} = 
     \left( 1 - \frac{\gamma}{\beta}\right) \dot \U_t + \Delta t \left(1
    - \frac{\gamma}{2 \beta}\right) \ddot \U_t$\
    $\Ud_{t + \alpha \Delta t} = (1 - \alpha) \Ud_t + \alpha \Ud_{t +
    \Delta t}$\
    $\ddot \U_{t + \Delta t} = 
     - \frac{1}{\beta \Delta t} \dot \U_t + \left( 1 - \frac{1}{2
    \beta} \right) \ddot \U_t$\
    theModel-$>$setResponse$(\U_{t + \alpha \Delta t}, \Ud_{t+\alpha
    \Delta t}, \Udd_{t+\Delta t})$
    :::

4.  The response quantities at the DOF_Group objects are updated with
    the new approximations by invoking `setResponse()` on the
    AnalysisModel with displacements and velocities at time $t + \alpha
    \Delta t$ and the accelerations at time $t + \Delta t$.

    ::: {.tabbing}
    while w̄hile w̄hile w̄hile ̄
    theModel-$>$setResponse$(\U_{t + \alpha \Delta t}, \Ud_{t+\alpha
    \Delta t}, \Udd_{t+\Delta t})$
    :::

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

Invoked this first causes the object to increment the DOF_Group response
quantities at time $t + \Delta t$. The displacement Vector is
incremented by $c1 * \Delta U$, the velocity Vector by $c2 * \Delta U$,
and the acceleration Vector by $c3 * \Delta U$. The displacement Vector
at time $t + \alpha \Delta t$ is incremented by $c1 \alpha \Delta U$ and
the velocity Vector by $c2 \alpha \Delta U$. The response quantities at
the DOF_Group objects are then updated with the new approximations by
invoking `setResponse()` on the AnalysisModel with displacement and
velocity at time $t + \alpha
\Delta t$ and the accelerations at time $t + \Delta t$. Finally
`updateDomain()` is invoked on the AnalysisModel.

::: {.tabbing}
while ̄ while w̄hile ̄ $\U_{t + \Delta t} += \Delta \U$\
$\dot \U_{t + \Delta t} += \frac{\gamma}{\beta \Delta t} \Delta \U$\
$\ddot \U_{t + \Delta t} += \frac{1}{\beta {\Delta t}^2} \Delta \U$\
$\U_{t + \alpha \Delta t} += \alpha \Delta \U$\
$\Ud_{t + \alpha \Delta t} += \frac{\alpha \gamma}{\beta \Delta t}
\Delta \U$\
theModel-$>$setResponse$(\U_{t + \alpha \Delta t}, \Ud_{t+\alpha
\Delta t}, \Udd_{t+\Delta t})$\
theModel-$>$updateDomain()
:::

Returns $0$ if successful. A warning message is printed and a negative
number returned if an error occurs: $-1$ if no associated AnalysisModel,
$-2$ if the Vector objects have not been created, $-3$ if the Vector
objects and $\Delta U$ are of different sizes.

```{.cpp}
int commit(void);
```

First the response quantities at the DOF_Group objects are updated with
the new approximations by invoking `setResponse()` on the AnalysisModel
with displacement, velocity and accelerations at time $t +
\Delta t$. Finally `updateDomain()` and `commitDomain()` are invoked on
the AnalysisModel. Returns $0$ if successful, a warning message and a
negative number if not: $-1$ if no AnalysisModel associated with the
object and $-2$ if `commitDomain()` failed.
*int sendSelf(int commitTag, Channel &theChannel);* \
Places in a Vector of size 6 the values of $\alpha$, $\beta$, $\gamma$,
RayleighDampingFlag, $\alpha_M$ and $\beta_K$. Then invokes
`sendVector()` on the Channel with this Vector. Returns $0$ if
successful, a warning message is printed and a $-1$ is returned if
*theChannel* fails to send the Vector.
*int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker
&theBroker);* \
Receives in a Vector of size 6 the values of $\alpha$, $\beta$,
$\gamma$, RayleighDampingFlag, $\alpha_M$ and $\beta_K$. Returns $0$ if
successful. A warning message is printed, and a $-1$ is returned if
*theChannel* fails to receive the Vector.

```{.cpp}
int Print(OPS_Stream &s, int flag = 0);
```

The object sends to $s$ its type, the current time, $\alpha$, $\gamma$
and $\beta$. If Rayleigh damping is specified, the constants $\alpha_M$
and $\beta_K$ are also printed.
