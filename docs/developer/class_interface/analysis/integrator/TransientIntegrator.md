\
# TransientIntegrator 

```cpp
#include <analysis/integrator/TransientIntegrator.h>
```

class TransientIntegrator: public Integrator\

MovableObject\
Integrator\
IncrementalIntegrator\

Newmark\
HHT\
Wilson-$\Theta$\

TransientIntegrator is an abstract subclass of IncrementalIntegrator. A
subclass of it is used when performing a nonlinear transient analysis of
the problem using a direct integration method. The TransientIntegrator
class redefines the `formTangent()` method of the IncrementalIntegrator
class and it defines a new method `newStep()` which is invoked by the
DirectIntegrationAnalysis class at each new time step.
In nonlinear transient finite element problems we seek a solution ($\U$,
$\dot \U$, $\ddot \U$) to the nonlinear vector function

$$\R(\U,\Ud, \Udd) = \P(t) - \F_I(\Udd) - \F_R(\U, \Ud) = \zero
\label{femGenForm}$$

The most widely used technique for solving the transient non-linear
finite element equation,
equation [\[femGenForm\]](#femGenForm){reference-type="ref"
reference="femGenForm"}, is to use an incremental direct integration
scheme. In the incremental formulation, a solution to the equation is
sought at successive time steps $\Delta
t$ apart.

$$\R(\U_{n \Delta t},\Ud_{n \Delta t}, \Udd_{n \Delta t}) = \P(n \Delta t) -
\F_I(\Udd_{n \Delta t}) - \F_R(\U_{n \Delta t}, \Ud_{n \Delta t})
\label{fullTimeForm}$$

For each time step, t, the integration schemes provide two operators,
$\I_1$ and $\I_2$, to relate the velocity and accelerations at the time
step as a function of the displacement at the time step and the response
at previous time steps:

$$\dot \U_{t} = {\I}_1 (\U_t, \U_{t-\Delta t}, \dot \U_{t-\Delta t},
\ddot \U_{t - \Delta t}, \U_{t - 2\Delta t}, \dot \U_{t - 2 \Delta t}. ..., )
\label{I1}$$

$$\ddot \U_{t} = {\I}_2 (\U_t, \U_{t-\Delta t}, \dot \U_{t-\Delta t},
\ddot \U_{t - \Delta t}, \U_{t - 2\Delta t}, \dot \U_{t - 2 \Delta t}. ..., )
\label{I2}$$

These allow us to rewrite
equation [\[fullTimeForm\]](#fullTimeForm){reference-type="ref"
reference="fullTimeForm"}, in terms of a single response quantity,
typically the displacement:

$$\R(\U_t) = \P(t) - \F_I(\Udd_t) - \F_R(\U_t, \Ud_t)
\label{genForm}$$

The solution of this equation is typically obtained using an iterative
procedure, i.e. making an initial prediction for $\U_{t}$, denoted
$\U_{t}^{(0)}$ a sequence of approximations $\U_{t}^{(i)}$, $i=1,2, ..$
is obtained which converges (we hope) to the solution $\U_{t}$. The most
frequently used iterative schemes, such as Newton-Raphson, modified
Newton, and quasi Newton schemes, are based on a Taylor expansion of
equation [\[genForm\]](#genForm){reference-type="ref"
reference="genForm"} about $\U_{t}$:

$$\R(\U_{t}) = 
\R(\U_{t}^{(i)}) +
\left[ {\frac{\partial \R}{\partial \U_t} \vert}_{\U_{t}^{(i)}}\right]
\left( \U_{t} - \U_{t}^{(i)} \right)$$

$$\R(\U_{t}) = 
 \P (t) 
 - \f_{I} \left( \ddot \U_{t}^{(i)} \right) -
\f_{R} \left( \dot \U_{t}^{(i)}, \U_{t}^{(i)} \right)$$ $$- \left[
   \M^{(i)} {\I}_2'
+  \C^{(i)} {\I}_1'
+ \K^{(i)}  \right]
 \left( \U_{t} - \U_{t}^{(i)} \right)
\label{femGenFormTaylor}$$

To start the iteration scheme, trial values for $\U_{t}$, $\dot
\U_{t}$ and $\ddot \U_{t}$ are required. These are obtained by assuming
$\U_{t}^{(0)} = \U_{t-\Delta t}$. The $\dot \U_{t}^{(0)}$ and
$\ddot \U_{t}^{(0)}$ can then be obtained from the operators for the
integration scheme.
Subclasses of TransientIntegrators provide methods informing the
FE_Element and DOF_Group objects how to build the tangent and residual
matrices and vectors. They also provide the method for updating the
response quantities at the DOFs with appropriate values; these values
being some function of the solution to the linear system of equations.

// Constructor\

\
// Destructor\

\
// Public Methods\

\

\

\
The integer *classTag* is passed to the IncrementalIntegrator classes
constructor.

\
Does nothing.

\
Invoked to form the structure tangent matrix. The method is rewritten
for this class to include inertia effects from the nodes. The method
iterates over both the FE_Elements and DOF_Groups invoking methods to
form their contributions to the $A$ matrix of the LinearSOE and then
adding these contributions to the $A$ matrix. The method performs the
following:

::: {.tabbing}
while ̄ while w̄hile ̄ theSysOfEqn.zeroA();\
DOF_EleIter &theDofs = theAnalysisModel.getDOFs();\
while((dofPtr = theDofs()) $\neq$ 0)\
dofPtr-$>$formTangent(theIntegrator);\
theSOE.addA(dofPtr-$>$getTangent(this), dofPtr-$>$getID())\
FE_EleIter &theEles = theAnalysisModel.getFEs();\
while((elePtr = theEles()) $\neq$ 0)\
theSOE.addA(elePtr-$>$getTangent(this), elePtr-$>$getID(), $1.0$)\
:::

Returns $0$ if successful, otherwise a $-1$ if an error occurred while
trying to add the stiffness. The two loops are introduced for the
FE_Elements, to allow for efficient parallel programming when the
FE_Elements are associated with a ShadowSubdomain.

```{.cpp}
virtual int formEleResidual(FE_Element \*theEle);
```

Called upon by the FE_Element *theEle* to determine it's contribution to
the rhs of the equation. The following are invoked before $0$ is
returned.

::: {.tabbing}
while ̄ while w̄hile ̄ theEle-$>$zeroResidual()\
theEle-$>$addRIncInertiaToResid()\
:::


```{.cpp}
virtual int formNodUnbalance(DOF_Group \*theDof);
```

Called upon by the DOF_Group *theDof* to determine it's contribution to
the rhs of the equation. The following are invoked before $0$ is
returned.

::: {.tabbing}
while ̄ while w̄hile ̄ theDof-$>$zeroUnbalance()\
theDof-$>$addPIncInertiaToUnbalance()\
:::


```{.cpp}
virtual int newStep(double deltaT) =0;
```

Invoked to inform the integrator that the transient analysis is
proceeding to the next time step. To return $0$ if successful, a
negative number if not.
