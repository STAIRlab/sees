\
# Newmark 

```cpp
#include <analysis/integrator/Newmark.h>
```

class Newmark: public TransientIntegrator\

MovableObject\
Integrator\
IncrementalIntegrator\
TransientIntegrator\

\
Newmark is a subclass of TransientIntegrator which implements the
Newmark method. In the Newmark method, to determine the velocities,
accelerations and displacements at time $t + \Delta t$, the equilibrium
equation (expressed for the TransientIntegrator) is typically solved at
time $t + \Delta t$ for ${\bf U}_{t+\Delta t}$, i.e. solve:

$${\bf R} ({\bf U}_{t + \Delta t}) = {\bf P}(t + \Delta t) - {\bf F}_I(\ddot{\bf U}_{t+\Delta t})
- {\bf F}_R(\dot{\bf U}_{t + \Delta t},{\bf U}_{t + \Delta t})$$

for ${\bf U}_{t+\Delta t}$. The following difference relations are used to
relate $\dot{\bf U}_{t + \Delta t}$ and $\ddot{\bf U}_{t + \Delta t}$ to
${\bf U}_{t + \Delta t}$ and the response quantities at time $t$:

$$\dot {\bf U}_{t + \Delta t} = \frac{\gamma}{\beta \Delta t}
\left( {\bf U}_{t + \Delta t} - {\bf U}_t \right)
 + \left( 1 - \frac{\gamma}{\beta}\right) \dot {\bf U}_t + \Delta t \left(1
- \frac{\gamma}{2 \beta}\right) \ddot {\bf U}_t$$

$$\ddot {\bf U}_{t + \Delta t} = \frac{1}{\beta {\Delta t}^2}
\left( {\bf U}_{t+\Delta t} - {\bf U}_t \right)
 - \frac{1}{\beta \Delta t} \dot {\bf U}_t + \left( 1 - \frac{1}{2
\beta} \right) \ddot {\bf U}_t$$

which results in the following

$$\left[ \frac{1}{\beta \Delta t^2} {\bf M} + \frac{\gamma}{\beta \Delta t}
{\bf C} + {\bf K} \right] \Delta {\bf U}_{t + \Delta t}^{(i)} = {\bf P}(t + \Delta t) -
{\bf F}_I\left(\ddot{\bf U}_{t+\Delta  t}^{(i-1)}\right)
- {\bf F}_R\left(\dot{\bf U}_{t + \Delta t}^{(i-1)},{\bf U}_{t + \Delta t}^{(i-1)}\right)$$

An alternative approach, which does not involve $\Delta t$ in the
denumerator (useful for impulse problems), is to solve for the
accelerations at time $t + \Delta t$

$${\bf R} (\ddot{\bf U}_{t + \Delta t}) = {\bf P}(t + \Delta t) - {\bf F}_I(\ddot{\bf U}_{t+\Delta t})
- {\bf F}_R(\dot{\bf U}_{t + \Delta t},{\bf U}_{t + \Delta t})$$

where we use following functions to relate ${\bf U}_{t + \Delta
t}$ and $\dot{\bf U}_{t + \Delta t}$ to $\ddot{\bf U}_{t + \Delta t}$ and the response
quantities at time $t$:

$${\bf U}_{t + \Delta t} = {\bf U}_t + \Delta t \dot{\bf U}_t + \left[
\left(\frac{1}{2} - \beta\right)\ddot{\bf U}_t + \beta \ddot{\bf U}_{t + \Delta
t}\right] \Delta t^2$$

$$\dot{\bf U}_{t + \Delta t} = \dot{\bf U}_t + \left[ \left(1 - \gamma\right)\ddot{\bf U}_t +
\gamma\ddot{\bf U}_{t + \Delta t}\right] \Delta t$$

which results in the following

$$\left[ {\bf M} + \gamma \Delta t {\bf C} + \beta \Delta t^2 {\bf K} \right] \Delta
\ddot{\bf U}_{t + \Delta t}^{(i)} = {\bf P}(t + \Delta t) - {\bf F}_I\left(\ddot{\bf U}_{t+\Delta 
t}^{(i-1)}\right)
- {\bf F}_R\left(\dot{\bf U}_{t + \Delta t}^{(i-1)},{\bf U}_{t + \Delta
t}^{(i-1)}\right)$$


### Constructors

\

\
### Destructor

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
$\Delta \ddot \U$, if *dispFlag* is *false*. In addition, a flag is set
indicating that Rayleigh damping will not be used.

Sets $\gamma$ to *gamma* and $\beta$ to *beta*. Sets a flag indicating
whether the incremental solution is done in terms of displacement or
acceleration to *dispFlag* and a flag indicating that Rayleigh damping
will not be used.

This constructor is invoked if Rayleigh damping is to be used, i.e.
$\D = \alpha_M M + \beta_K K$. Sets $\gamma$ to *gamma*, $\beta$ to
*beta*, $\alpha_M$ to *alphaM* and $\beta_K$ to *betaK*. Sets a flag
indicating whether the incremental solution is done in terms of
displacement or acceleration to *dispFlag* and a flag indicating that
Rayleigh damping will be used.

\
Invokes the destructor on the Vector objects created.

\
This tangent for each FE_Element is defined to be ${\bf K}_e = c1 {\bf K} + c2
\D + c3 \M$, where c1,c2 and c3 were determined in the last invocation
of the `newStep()` method. The method returns $0$ after performing the
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

The method returns $0$ after performing the following operations:

::: {.tabbing}
while ̄ while w̄hile ̄ theDof-$>$zeroUnbalance()\
if (RayleighDamping == false)\
theDof-$>$addMtoTang(c3)\
else\
theDof-$>$addMtoTang(c3 + c2 \* $\alpha_M$)\
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
    $\gamma / (\beta \Delta t)$ and *c3* to $1/ (\beta \Delta t^2)$. If
    the flag is *false* *c1* is set to $\beta \Delta t^2$, *c2* to
    $\gamma \Delta t$ and *c3* to $1.0$.

2.  Then the Vectors for response quantities at time $t$ are set equal
    to those at time $t + \Delta t$.

    ::: {.tabbing}
    while w̄hile w̄hile w̄hile ̄ ${\bf U}_t = {\bf U}_{t + \Delta t}$\
    $\dot{\bf U}_t = \dot{\bf U}_{t + \Delta t}$\
    $\ddot{\bf U}_t = \ddot{\bf U}_{t + \Delta t}$
    :::

3.  Then the velocity and accelerations approximations at time $t +
    \Delta t$ are set using the difference approximations if *dispFlag*
    was *true*. (displacement and velocity if *false*).

    ::: {.tabbing}
    while w̄hile w̄hile w̄hile ̄ if (displIncr == true) {\
    $\dot {\bf U}_{t + \Delta t} = 
     \left( 1 - \frac{\gamma}{\beta}\right) \dot {\bf U}_t + \Delta t \left(1
    - \frac{\gamma}{2 \beta}\right) \ddot {\bf U}_t$\
    $\ddot {\bf U}_{t + \Delta t} = 
     - \frac{1}{\beta \Delta t} \dot {\bf U}_t + \left( 1 - \frac{1}{2
    \beta} \right) \ddot {\bf U}_t$\
    } else {\
    ${\bf U}_{t + \Delta t} = {\bf U}_t + \Delta t \dot{\bf U}_t + \frac{\Delta
    t^2}{2}\ddot{\bf U}_t$\
    $\dot{\bf U}_{t + \Delta t} = \dot{\bf U}_t +  \Delta t \ddot{\bf U}_t$\
    }
    :::

4.  The response quantities at the DOF_Group objects are updated with
    the new approximations by invoking `setResponse()` on the
    AnalysisModel with new quantities for time $t + \Delta t$.

    ::: {.tabbing}
    while w̄hile w̄hile w̄hile ̄
    theModel-$>$setResponse$({\bf U}_{t + \Delta t}, \dot{\bf U}_{t+\Delta t},
    \ddot{\bf U}_{t+\Delta t})$
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

Invoked this causes the object to increment the DOF_Group response
quantities at time $t + \Delta t$. The displacement Vector is
incremented by $c1 * \Delta U$, the velocity Vector by $c2 * \Delta U$,
and the acceleration Vector by $c3 * \Delta U$. The response at the
DOF_Group objects are then updated by invoking `setResponse()` on the
AnalysisModel with quantities at time $t +
\Delta t$. Finally `updateDomain()` is invoked on the AnalysisModel.

::: {.tabbing}
while w̄hile w̄hile w̄hile ̄ if (displIncr == true) {\
${\bf U}_{t + \Delta t} += \Delta \U$\
$\dot {\bf U}_{t + \Delta t} += \frac{\gamma}{\beta \Delta t} \Delta \U$\
$\ddot {\bf U}_{t + \Delta t} += \frac{1}{\beta {\Delta t}^2} \Delta
\U$\
} else {\
$\ddot{\bf U}_{t + \Delta t} += \Delta \Udd$\
${\bf U}_{t + \Delta t} += \beta \Delta t^2 \Delta \Udd$\
$\dot{\bf U}_{t + \Delta t} += \gamma \Delta t \Delta \Udd$\
}\
theModel-$>$setResponse$({\bf U}_{t + \Delta t}, \dot{\bf U}_{t+\Delta t},
\ddot{\bf U}_{t+\Delta t})$\
theModel-$>$setUpdateDomain()
:::

Returns $0$ if successful. A warning message is printed and a negative
number returned if an error occurs: $-1$ if no associated AnalysisModel,
$-2$ if the Vector objects have not been created, $-3$ if the Vector
objects and $\delta U$ are of different sizes.
*int sendSelf(int commitTag, Channel &theChannel);* \
Places in a Vector of size 6 the values of $\beta$, $\gamma$,
*dispFlag*, RayleighDampingFlag, $\alpha_M$ and $\beta_K$. Then invokes
`sendVector()` on the Channel with this Vector. Returns $0$ if
successful, a warning message is printed and a $-1$ is returned if
*theChannel* fails to send the Vector.
*int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker
&theBroker);* \
Receives in a Vector of size 6 the values of $\beta$, $\gamma$,
*dispFlag*, RayleighDampingFlag, $\alpha_M$ and $\beta_K$. Returns $0$
if successful. A warning message is printed, $\gamma$ is set to 0.5,
$\beta$ to 0.25 and the Rayleigh damping flag set to *false*, and a $-1$
is returned, if *theChannel* fails to receive the Vector.

```{.cpp}
int Print(OPS_Stream &s, int flag = 0);
```

The object sends to $s$ its type, the current time, $\gamma$ and
$\beta$. If Rayleigh damping is specified, the constants $\alpha_M$ and
$\beta_K$ are also printed.
