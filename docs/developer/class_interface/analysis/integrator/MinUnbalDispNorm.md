\
# MinUnbalDispNorm 

```cpp
#include <analysis/integrator/MinUnbalDispNorm.h>
```
UNDER CONSTRUCTION.

class MinUnbalDispNorm: public StaticIntegrator\

MovableObject\
Integrator\
IncrementalIntegrator\
StaticIntegrator\

\
MinUnbalDispNorm is a subclass of StaticIntegrator, it is used to when
performing a static analysis on the FE_Model using the minimum
unbalanced displacement norm method. In this method WHAT

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

The integer `INTEGRATOR_TAGS_MinUnbalDispNorm` (defined in
 `<classTags.h>`) is passed to the StaticIntegrator classes
constructor.


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
