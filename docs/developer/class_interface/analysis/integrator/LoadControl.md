\
# LoadControl 

```cpp
#include <analysis/integrator/LoadControl.h>
```

class LoadControl: public StaticIntegrator\

MovableObject\
Integrator\
IncrementalIntegrator\
StaticIntegrator\

\
LoadControl is a subclass of StaticIntegrator, it is used to when
performing a static analysis on the FE_Model using the load control
method. In the load control method, the following constraint equation is
added to
equation [\[staticFormTaylor\]](#staticFormTaylor){reference-type="ref"
reference="staticFormTaylor"} of the StaticIntegrator class:

$$\lambda_n^{(i)} - \lambda_{n-1} = \delta \lambda_n$$

where $\delta \lambda_n$ depends on $\delta \lambda_{n-1}$, the load
increment at the previous time step, $J_{n-1}$, the number of iterations
required to achieve convergence in the previous load step, and $Jd$, the
desired number of iteraions. $\delta
\lambda_n$ is bounded by $\delta \lambda_{min}$ and
$\delta \lambda_{max}$.
$$\delta \lambda_n = max \left( \delta \lambda_{min}, min \left(
\frac{Jd}{J_{n-1}} \delta \lambda_{n-1}, \delta \lambda_{max} \right) \right)$$

Knowing $\lambda_n^{(i)}$ prior to each iteration, the $N+1$ unknowns in
equation [\[staticFormTaylor\]](#staticFormTaylor){reference-type="ref"
reference="staticFormTaylor"}, is reduced to $N$ unknowns and results in
the following equation:

$$\R(\U_{n}) = \lambda_n^{(i)} \P 
 - \f_{R}\left(\U_{n}^{(i)} \right) - 
\K_n^{(i)} 
(\U_{n} - \U_{n}^{(i)})  
\label{staticFormLoadControl}$$


// Constructors\

\
// Destructor\

\
// Public Methods\

\

\
// Public Methods for Output\

\

\

\
The integer INTEGRATOR_TAGS_LoadControl (defined in $<$classTags.h$>$)
is passed to the StaticIntegrator classes constructor.
$\delta \lambda_1$ is the load factor used in the first step. The
arguments $Jd$, $\delta \lambda_{min}$, and $\delta
\lambda_{max}$ are used in the determination of the increment in the
load factor at each step.

\
Does nothing.


```{.cpp}
int newStep(void);
```

The object obtains the current value of $\lambda$ from the AnalysisModel
object. It increments this by $\delta \lambda_n$.

$$\delta \lambda_n = max \left( \delta \lambda_{min}, min \left(
\frac{Jd}{J_{n-1}} \delta \lambda_{n-1}, \delta \lambda_{max} \right) \right)$$

It will then invoke `applyLoadDomain(0.0, $\lambda$)`{.cpp} on the
AnalysisModel object. Returns $0$ if successful. A warning message is
printed and a $-1$ is returned if no AnalysisModel is associated with
the object.

```{.cpp}
int update(const Vector &$\Delta U$);
```

Invoked this causes the object to first increment the DOF_Group
displacements with $\Delta U$, by invoking *incrDisp($\Delta U)$* on the
AnalysisModel, and then to update the domain, by invoking
`updateDomain()` on the AnalysisModel. Returns $0$ if successful, a
warning message and a $-1$ is returned if no AnalysisModel is associated
with the object.

Sets the value of the load increment in `newStep()` to be $\delta
\lambda$. Returns $0$.
*int sendSelf(int commitTag, Channel &theChannel);* \
Places in a vector if size 5 the value of $\delta \lambda_{n-1}$, $Jd$,
$J_{n-1}$, $\delta \lambda_{min}$ and $\delta \lambda_{max}$) and then
sends the Vector. Returns $0$ if successful, a warning message is
printed and a $-1$ is returned if *theChannel* fails to send the
Vector.
*int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker
&theBroker);* \
Receives in a Vector of size 5 the data that was sent in `sendSelf()`.
Returns $0$ if successful, a warning message is printed, $\delta
\lambda$ is set to $0$, and a $-1$ is returned if *theChannel* fails to
receive the Vector.

```{.cpp}
int Print(OPS_Stream &s, int flag = 0);
```

The object sends to $s$ its type, the current value of $\lambda$, and
$\delta \lambda$.
