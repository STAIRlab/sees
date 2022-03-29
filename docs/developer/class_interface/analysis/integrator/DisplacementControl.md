# DisplacementControl 

UNDER CONSTRUCTION.

```cpp
#include <analysis/integrator/DisplacementControl.h>

class DisplacementControl: 
public StaticIntegrator
    MovableObject
    Integrator
    IncrementalIntegrator
```


DisplacementControl is a subclass of StaticIntegrator, it is used to
when performing a static analysis on the FE_Model using the displacement
control method. In the displacement control method the displacement at a
specified degree-of-freedom Uc is specified for each iteration. The
following constraint equation is added to
equation [\[staticFormTaylor\]](#staticFormTaylor){reference-type="ref"
reference="staticFormTaylor"} of the StaticIntegrator class:

$$Uc_n^{(i)} - Uc_{n-1} = \delta Uc_n$$

where $\delta Uc_n$ depends on $\delta Uc_{n-1}$, the displacement
increment at the previous time step, $J_{n-1}$, the number of iterations
required to achieve convergence in the previous load step, and $Jd$, the
desired number of iteraions. $\delta
Uc_n$ is bounded by $\delta Uc_{min}$ and $\delta Uc_{max}$.
$$\delta Ucn = max \left( \delta Uc{min}, min \left(
\frac{Jd}{J_{n-1}} \delta Uc{n-1}, \delta Uc{max} \right) \right)$$

SOME THEORY.

### Constructors

\
### Destructor

\
// Public Methods\

\

\
// Public Methods for Output\

\

\

The integer `INTEGRATOR_TAGS_DisplacementControl` (defined in
 `<classTags.h>`) is passed to the StaticIntegrator classes
constructor. $\delta Uc_1$ is the load factor used in the first step.
The arguments $Jd$, $\delta Uc_{min}$, and $\delta
Uc_{max}$ are used in the determination of the increment in the load
factor at each step.

\
Does nothing.


```{.cpp}
int newStep(void);
```

WHAT DO I DO?\

```{.cpp}
int update(const Vector &$\Delta U$);
```

WHAT DO I DO?\
*int sendSelf(int commitTag, Channel &theChannel);* \
WHAT DO I DO?\
*int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker
&theBroker);* \
WHAT DO I DO?\

```{.cpp}
int Print(OPS_Stream &s, int flag = 0);
```

WHAT DO I DO?
