THE IMPLEMENTATION WILL HAVE TO CHANGE FOR DOMAIN-DECOMPOSITION ANALYSIS
.. AS DOES THE CONVERGENCE TEST STUFF .. THIS IS BECAUSE USING DOT
PRODUCTS OF VECTORS OBTAINED STRAIGHT FROM SYSTEM OF EQUATION .. MAYBE
MODIFY LinearSOE TO DO THE DOT PRODUCT .. WILL WORK IN DD IF ALL USE ONE
SOE .. WHAT PetSC DOES, TALK WITH P. DEMMEL ABOUT WHAT HE WILL PROVIDE.

# ArcLength 

```cpp
#include <analysis/integrator/ArcLength.h>
```

class ArcLength: public StaticIntegrator\

MovableObject\
Integrator\
IncrementalIntegrator\
StaticIntegrator\

\
ArcLength is a subclass of StaticIntegrator, it is used to when
performing a static analysis on the FE_Model using an arc length method.
In the arc length method implemented by this class, the following
constraint equation is added to
equation [\[staticFormTaylor\]](#staticFormTaylor){reference-type="ref"
reference="staticFormTaylor"} of the StaticIntegrator class:

$$\Delta \U_n^T \Delta \U_n  + \alpha^2 \Delta \lambda_n^2  = \Delta s^2$$

where

$$\Delta \U_n = \sum_{j=1}^{i} \Delta \U_n^{(j)} = \Delta \U_n^{(i)} +
d\U^{(i)}$$

$$\Delta \lambda_n = \sum_{j=1}^{i} \Delta \lambda_n^{(j)} = \Delta \lambda_n^{(i)} +
d\lambda^{(i)}$$

this equation cannot be added directly into
equation [\[staticFormTaylor\]](#staticFormTaylor){reference-type="ref"
reference="staticFormTaylor"} to produce a linear system of $N+1$
unknowns. To add this equation we make some assumptions ala Yang (REF),
which in so doing allows us to solve a system of $N$ unknowns using the
method of ??(REF). Rewriting
equation [\[staticFormTaylor\]](#staticFormTaylor){reference-type="ref"
reference="staticFormTaylor"} as

$$\K_n^{(i)} \Delta \U_n^{(i)} = \Delta \lambda_n^{(i)} \P +
\lambda_n^{(i)} \P - \F_R(\U_n^{(i)}) = \Delta \lambda_n^{(i)} \P + \R_n^{(i)}$$

The idea of ?? is to separate this into two equations:

$$\K_n^{(i)} \Delta \dot{\bf U}_n^{(i)} = \P$$

$$\K_n^{(i)} \Delta \overline{\bf U}_n^{(i)} = \R_n^{(i)}$$

where now

$$\Delta \U_n^{(i)} = \Delta \lambda_n^{(i)} \Delta \dot{\bf U}_n^{(i)} + \Delta \overline{\bf U}_n^{(i)}  
\label{splitForm}$$

We now rewrite the constraint equation based on two conditions:

1.  **$i = 1$**: assuming $\R_n^{(1)} = \zero$, i.e. the system is in
    equilibrium at the start of the iteration, the following is obtained

    $$\Delta \U_n^{(1)} = \Delta \lambda_n^{(1)} \Delta \dot{\bf U}_n^{(1)} + \zero$$

    $$\Delta \lambda_n^{(1)} = \begin{array}{c} + \\ - \end{array}
    \sqrt{\frac{\Delta s^2}{\dot{\bf U}^T \dot{\bf U}+ \alpha^2}}$$

    The question now is whether **+** or **-** should be used. In this
    class, $d \lambda$ from the previous iteration $(n-1)$ is used, if
    it was positive **+** is assumed, otherwise **-**. This may change.
    There are other ideas: ?(REF) number of negatives on diagonal of
    decomposed matrix, \...

2.  **$i > 1$**

    $$\left( \Delta \U_n^{(i)} + d\U^{(i)} \right)^T \left( \Delta \U_n^{(i)} +
    d\U^{(i)} \right) + \alpha^2 \left( \Delta \lambda_n^{(i)} + d\lambda^{(i)}
    \right)^2 = \Delta s^2$$

    $$\Delta {\U_n^{(i)}}^T\Delta \U_n^{(i)} + 2{d\U^{(i)}}^T\Delta \U_n^{(i)} + {d\U^{(i)}}^T d\U^{(i)}
    + \alpha^2 \Delta {\lambda_n^{(i)}}^2
    + 2 \alpha^2 d\lambda^{(i)} \Delta \lambda_n^{(i)} + \alpha^2 {d\lambda^{(i)}}^2
    = \Delta s^2$$

    assuming the constraint equation was solved at $i-1$, i.e.
    ${d\U^{(i)}}^T d\U^{(i)} + \alpha^2 {d\lambda^{(i)}}^2 = \Delta s^2$,
    this reduces to

    $$\Delta {\U_n^{(i)}}^T\Delta \U_n^{(i)} + 2{d\U^{(i)}}^T\Delta \U_n^{(i)} + 
    \alpha^2 \Delta {\lambda_n^{(i)}}^2
    + 2 \alpha^2 d\lambda^{(i)} \Delta \lambda_n^{(i)} 
    = 0$$

    substituting for $\Delta {\U_n^{(i)}}$ using
    equation [\[splitForm\]](#splitForm){reference-type="ref"
    reference="splitForm"} this can be expressed as:

    $$\Delta \lambda_n^{(i)^2} \left( \Delta \dot{\bf U}_n^{(i)} \Delta \dot{\bf U}_n^{(i)} +
    \alpha^2 \right) +
    2* \Delta \lambda_n^{(i)} \left( \Delta \dot{\bf U}_n^{(i)} \Delta \overline{\bf U}_n^{(i)}
    + d\U^{(i)} \Delta \dot{\bf U}_n^{(i)} 
    + \alpha^2d \lambda^{(i)} \right)$$
    $$+ \left (\Delta \overline{\bf U}_n^{(i)} \Delta \overline{\bf U}_n^{(i)} + d\U^{(i)} \Delta
    \overline{\bf U}_n^{(i)}
    \right) =0$$

    which is a quadratic in $\Delta \lambda_n^{(i)}$, which can be
    solved for two roots. The root chosen is the one which will keep a
    positive angle between the incremental displacement before and after
    this step.


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
The integer `INTEGRATOR_TAGS_ArcLength` (defined in  `<classTags.h>`) is
passed to the StaticIntegrator classes constructor. The value of
$\alpha$ is set to *alpha* and $\Delta s$ to *dS*.

\
Invokes the destructor on the Vector objects created in
`domainChanged()`.


```{.cpp}
int newStep(void);
```

`newStep()` performs the first iteration, that is it solves for
$\lambda_n^{(1)}$ and $\Delta \U_n^{(1)}$ and updates the model with
$\Delta \U_n^{(1)}$ and increments the load factor by $\lambda_n^{(1)}$.
To do this it must set the rhs of the LinearSOE to $\P$, invoke
`formTangent()` on itself and solve the LinearSOE to get
$\Delta \dot{\bf U}_n^{(1)}$.

```{.cpp}
int update(const Vector &$\Delta U$);
```

Note the argument $\Delta U$ should be equal to
$\Delta \overline{\bf U}_n^{(i)}$. The object then determines
$\Delta \dot{\bf U}_n^{(i)}$ by setting the rhs of the linear system of
equations to be $\P$ and then solving the linearSOE. It then solves for
$\Delta \lambda_n^{(i)}$ and $\Delta \U_n^{(i)}$ and updates the model
with $\Delta \U_n^{(i)}$ and increments the load factor by $\Delta
\lambda_n^{(i)}$. Sets the vector $x$ in the LinearSOE object to be
equal to $\Delta \U_n^{(i)}$ before returning (this is for the
convergence test stuff.

The object creates the Vector objects it needs. Vectors are created to
stor $\P$, $\Delta \overline{\bf U}_n^{(i)}$,
$\Delta \dot{\bf U}_n^{(i)}$, $\Delta
\overline{\bf U}_n^{(i)}$, $dU^{(i)}$. To form $\P$, the current load
factor is obtained from the model, it is incremented by $1.0$,
`formUnbalance()` is invoked on the object, and the $b$ vector is
obtained from the linearSOE. This is $\P$, the load factor on the model
is then decremented by $1.0$.
*int sendSelf(int commitTag, Channel &theChannel);* \
Places the values of $\Delta s$ and $\alpha$ in a vector of size $2$ and
invokes `sendVector()` on *theChannel*. Returns $0$ if successful, a
warning message is printed and a $-1$ is returned if *theChannel* fails
to send the Vector.
*int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker
&theBroker);* \
Receives in a Vector of size 2 the values of $\Delta s$ and $\alpha$.
Returns $0$ if successful, a warning message is printed, $\delta
\lambda$ is set to $0$, and a $-1$ is returned if *theChannel* fails to
receive the Vector.

```{.cpp}
int Print(OPS_Stream &s, int flag = 0);
```

The object sends to $s$ its type, the current value of $\lambda$, and
$\delta \lambda$.
