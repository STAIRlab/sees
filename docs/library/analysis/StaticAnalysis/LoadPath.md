
# LoadPath 

```cpp
#include <analysis/integrator/LoadPath.h>
```

class LoadPath: public StaticIntegrator\

MovableObject\
Integrator\
IncrementalIntegrator\
StaticIntegrator\

\
LoadPath is a subclass of StaticIntegrator, it is used to when
performing a static analysis on the FE_Model using a user specified load
path. The load path is specified in a Vector, *path*, to the objects
constructor and at each step in the analysis:

$$\lambda_n^{(i)} - \lambda_{n-1} = path(n) - path(n-1)$$

Knowing $\lambda_n^{(i)} = path(n)$ prior to each iteration, the $N+1$
unknowns in
equation [\[staticFormTaylor$$
](#staticFormTaylor){reference-type="ref"
reference="staticFormTaylor"}, is reduced to $N$ unknowns and results in
the following equation:

$$\R({\bf U}_{n}) = \lambda_n^{(i)} {\bf P} 
 - {\bf F}_{R}\left({\bf U}_{n}^{(i)} \right) - 
{\bf K}_n^{(i)} 
({\bf U}_{n} - {\bf U}_{n}^{(i)})  
\label{staticFormLoadPath}$$


### Constructors

\

### Destructor

\
// Public Methods\

\

// Public Methods for Output\

\

\

The integer `INTEGRATOR_TAGS_LoadPath` (defined in  `<classTags.h>`) is
passed to the StaticIntegrator classes constructor. A vector object
*path* is created which is a copy of *loadPath* and an index into this
vector is set to $0$.

The integer `INTEGRATOR_TAGS_LoadPath` (defined in  `<classTags.h>`) is
passed to the StaticIntegrator classes constructor. No vector object is
created. Provided for the FEM_ObjectBroker to create a blank object,
`recvSelf()` should be invoked on this object.

\
Invokes the destructor on the vector *path*.

\
The object obtains the current value of $\lambda$ from the *path* vector
using the current index. The index is then incremented by $1$. If the
index is greater than the size of *path*, $\lambda$ is set to $0$ and an
error message is printed. It will then invoke *applyLoadDomain(0.0,
$\lambda$)* on the AnalysisModel object. Returns $0$ if successful. A
warning message is printed and a $-1$ is returned if no AnalysisModel is
associated with the object.

```{.cpp}
int update(const Vector &$\Delta U$);
```

Invoked this causes the object to first increment the DOF_Group
displacements with $\Delta U$, by invoking *incrDisp($\Delta U)$* on the
AnalysisModel, and then to update the domain, by invoking
`updateDomain()` on the AnalysisModel. Returns $0$ if successful, a
warning message and a $-1$ is returned if no AnalysisModel is associated
with the object.
*int sendSelf(int commitTag, Channel &theChannel);* \
Places the size if *path* and the index in an ID of size 2 and send this
ID. Then sends the Vector *path*. Returns $0$ if successful, a warning
message is printed and a $-1$ is returned if *theChannel* fails to send
the ID or the Vector.
*int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker
&theBroker);* \
Receives in a ID of size 2 the size of the vector and current index.
Creates a new Vector and receives the Vector from the Channel. Returns
$0$ if successful, a warning message is printed and a $-1$ is returned
if *theChannel* fails to receive the Vector or the ID.

```{.cpp}
int Print(OPS_Stream &s, int flag = 0);
```

The object sends to $s$ its type, the current value of $\lambda$.
