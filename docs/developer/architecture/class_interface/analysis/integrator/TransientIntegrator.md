# TransientIntegrator 

```cpp
#include <analysis/integrator/TransientIntegrator.h>

class TransientIntegrator: 
   public Integrator
          MovableObject
          Integrator
          IncrementalIntegrator
```

- [Newmark](Newmark)
- [HHT](HHT)
- [Wilson-$\Theta$](WilsonTheta)
- [Generalized Alpha](GeneralizedAlpha)

`TransientIntegrator` is an abstract subclass of `IncrementalIntegrator`. 
A subclass of it is used when performing a nonlinear transient analysis of
the problem using a direct integration method. The `TransientIntegrator`
class redefines the `formTangent()` method of the `IncrementalIntegrator`
class and it defines a new method `newStep()` which is invoked by the
`DirectIntegrationAnalysis` class at each new time step.
In nonlinear transient finite element problems we seek a solution ($\U$, $\dot \U$, $\ddot \U$) to the nonlinear vector function

$${\bf R}({\bf U},\Ud, \Udd) = {\bf P}(t) - {\bf F}_I(\Udd) - {\bf F}_R(\U, \Ud) = \zero
$$
{#femGenForm}

The most widely used technique for solving the transient non-linear
finite element equation,
equation [\[femGenForm\]](#femGenForm){reference-type="ref"
reference="femGenForm"}, is to use an incremental direct integration
scheme. In the incremental formulation, a solution to the equation is
sought at successive time steps $\Delta
t$ apart.

$$\R({\bf U}_{n \Delta t},\dot{\bf U}_{n \Delta t}, \ddot{\bf U}_{n \Delta t}) = {\bf P}(n \Delta t) -
{\bf F}_I(\ddot{\bf U}_{n \Delta t}) - {\bf F}_R({\bf U}_{n \Delta t}, \dot{\bf U}_{n \Delta t})
$$
{#fullTimeForm}

For each time step, $t$, the integration schemes provide two operators,
$\operatorname{I}_1$ and $\operatorname{I}_2$, to relate the velocity and accelerations at the time
step as a function of the displacement at the time step and the response
at previous time steps:

$$\dot {\bf U}_{t} = {\I}_1 ({\bf U}_t, {\bf U}_{t-\Delta t}, \dot {\bf U}_{t-\Delta t},
\ddot {\bf U}_{t - \Delta t}, {\bf U}_{t - 2\Delta t}, \dot {\bf U}_{t - 2 \Delta t}. ..., )
\label{I1}$$

$$\ddot {\bf U}_{t} = {\I}_2 ({\bf U}_t, {\bf U}_{t-\Delta t}, \dot {\bf U}_{t-\Delta t},
\ddot {\bf U}_{t - \Delta t}, {\bf U}_{t - 2\Delta t}, \dot {\bf U}_{t - 2 \Delta t}. ..., )
\label{I2}$$

These allow us to rewrite
equation [\[fullTimeForm\]](#fullTimeForm){reference-type="ref"
reference="fullTimeForm"}, in terms of a single response quantity,
typically the displacement:

$$\R({\bf U}_t) = {\bf P}(t) - {\bf F}_I(\ddot{\bf U}_t) - {\bf F}_R({\bf U}_t, \dot{\bf U}_t)
\label{genForm}$$

The solution of this equation is typically obtained using an iterative
procedure, i.e. making an initial prediction for ${\bf U}_{t}$, denoted
${\bf U}_{t}^{(0)}$ a sequence of approximations ${\bf U}_{t}^{(i)}$, $i=1,2, ..$
is obtained which converges (we hope) to the solution ${\bf U}_{t}$. The most
frequently used iterative schemes, such as Newton-Raphson, modified
Newton, and quasi Newton schemes, are based on a Taylor expansion of
equation [\[genForm\]](#genForm){reference-type="ref"
reference="genForm"} about ${\bf U}_{t}$:

$$\R({\bf U}_{t}) = 
\R({\bf U}_{t}^{(i)}) +
\left[ {\frac{\partial \R}{\partial {\bf U}_t} \vert}_{{\bf U}_{t}^{(i)}}\right]
\left( {\bf U}_{t} - {\bf U}_{t}^{(i)} \right)$$

$$
\R({\bf U}_{t}) = {\bf P} (t) - {\bf F}_{I} \left( \ddot {\bf U}_{t}^{(i)} \right) - {\bf F}_{R} \left( \dot {\bf U}_{t}^{(i)}, {\bf U}_{t}^{(i)} \right)- \left[
   {\bf M}^{(i)} {\I}_2'
+  {\bf C}^{(i)} {\I}_1'
+ {\bf K}^{(i)}  \right]
 \left( {\bf U}_{t} - {\bf U}_{t}^{(i)} \right)
\label{femGenFormTaylor}$$

To start the iteration scheme, trial values for ${\bf U}_{t}$, $\dot
{\bf U}_{t}$ and $\ddot {\bf U}_{t}$ are required. These are obtained by assuming
${\bf U}_{t}^{(0)} = {\bf U}_{t-\Delta t}$. The $\dot {\bf U}_{t}^{(0)}$ and
$\ddot {\bf U}_{t}^{(0)}$ can then be obtained from the operators for the
integration scheme.
Subclasses of TransientIntegrators provide methods informing the
FE_Element and `DOF_Group` objects how to build the tangent and residual
matrices and vectors. They also provide the method for updating the
response quantities at the DOFs with appropriate values; these values
being some function of the solution to the linear system of equations.

### Constructor


### Destructor


// Public Methods\

\

\


The integer `classTag` is passed to the `IncrementalIntegrator` classes
constructor.

```cpp
```
Does nothing.

```cpp
```

Invoked to form the structure tangent matrix. The method is rewritten
for this class to include inertia effects from the nodes. The method
iterates over both the FE_Elements and DOF_Groups invoking methods to
form their contributions to the $A$ matrix of the LinearSOE and then
adding these contributions to the $A$ matrix. The method performs the
following:

```cpp
// while ̄ while w̄hile ̄ 
theSysOfEqn.zeroA();
DOF_EleIter &theDofs = theAnalysisModel.getDOFs();
while((dofPtr = theDofs()) \neq 0)
dofPtr->formTangent(theIntegrator);
theSOE.addA(dofPtr->getTangent(this), dofPtr->getID())
FE_EleIter &theEles = theAnalysisModel.getFEs();
while((elePtr = theEles()) \neq 0)
theSOE.addA(elePtr->getTangent(this), elePtr->getID(), 1.0)
```

Returns $0$ if successful, otherwise a $-1$ if an error occurred while
trying to add the stiffness. The two loops are introduced for the
FE_Elements, to allow for efficient parallel programming when the
FE_Elements are associated with a ShadowSubdomain.

```{.cpp}
virtual int formEleResidual(FE_Element *theEle);
```

Called upon by the `FE_Element` *theEle* to determine it's contribution to
the rhs of the equation. The following are invoked before $0$ is
returned.

```cpp
// while ̄ while w̄hile ̄ 
theEle-$>$zeroResidual()
theEle-$>$addRIncInertiaToResid()
```


```{.cpp}
virtual int formNodUnbalance(DOF_Group *theDof);
```

Called upon by the `DOF_Group` `theDof` to determine it's contribution to
the rhs of the equation. The following are invoked before $0$ is
returned.

```cpp
// while ̄ while w̄hile ̄ 
theDof->zeroUnbalance()
theDof->addPIncInertiaToUnbalance()
```


```{.cpp}
virtual int newStep(double deltaT) =0;
```

Invoked to inform the integrator that the transient analysis is
proceeding to the next time step. To return $0$ if successful, a
negative number if not.
