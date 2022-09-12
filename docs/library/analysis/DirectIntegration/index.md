# DirectIntegrationAnalysis 

```python
class DirectIntegrationAnalysis(model, patterns, strategy)
```

`DirectIntegrationAnalysis` is used to perform a transient analysis using an
incremental approach on the `model`.


The following are the aggregates of such an
analysis type:

-   `model` (**AnalysisModel**) - a container class holding the `FE_Element` and
    `DOF_Group` objects created by the ConstraintHandler object.

-   `integrator` (**TransientIntegrator**) - an algorithmic class which provides
    methods which are invoked by the `FE_Element` to determine their
    current tangent and residual matrices. That is, this is the class
    that sets up the system of equations. 

    $$\mathbf{M \ddot{U}}+\mathbf{C \dot{U}}+\mathbf{P}_{r}(\mathbf{U})=\mathbf{P}(t)$$

    It also provides the `commit()` method which is invoked to set up the
    appropriate dof response values once the solution algorithm has formed and
    solved the system of equations.

-   `constraints` (**ConstraintHandler**) - a class which creates the `DOF_Group` and
    `FE_Element` objects, the type of objects created depending on how the
    specified constraints in the domain are to be handled.

-   `numberer` (**DOF_Numberer**) - a class responsible for providing equation
    numbers to the individual degrees of freedom in each `DOF_Group`
    object.

-   `system` (**LinearSOE**) - a numeric class responsible for the creation and
    subsequent solution of large systems of linear equations of the form
    $Ax = b$, where $A$ is a matrix and $x$ and $b$ are vectors.

-   `algorithm` (**EquiSolnAlgo**) - an algorithmic class specifying the sequence of
    operations to be performed in setting up and solving the finite
    element equation which can be represented by the equation $K(U) U = P(U)$.


### Transient Integrators
Determing the next time step for an analysis including inertial effects is done by the following schemes

- [Newmark](TransientIntegrator/Newmark) -- The two parameter time-stepping method developed by Newmark
- [HHT](TransientIntegrator/HHT) -- The three parameter Hilbert-Hughes-Taylor time-stepping method
- [Generalized Alpha](TransientIntegrator/GeneralizedAlpha) -- Generalization of the HHT algorithm with improved numerical damping
- [Central Difference]() -- Approximates velocity and acceleration by centered finite differences of displacement
- [TRBDF2](TRBDF2) --  A composite scheme that alternates between the Trapezoidal scheme and a 3 point backward Euler scheme.
- [Explicit difference](Explicitdifference) -- 

## Theory

In nonlinear transient finite element problems we seek a solution 
($\U$, $\dot \U$, $\ddot \U$) to the nonlinear vector equation

$${\bf R}({\bf U},\Ud, \Udd) = {\bf P}(t) - {\bf F}_I(\Udd) - {\bf F}_R({\bf U}, {\dot { \bf U}}) = \zero$$
{#femGenForm}

The most widely used technique for solving the transient non-linear finite element equation,
equation [\[femGenForm](#femGenForm){reference-type="ref"
reference="femGenForm"}, is to use an incremental direct integration
scheme. In the incremental formulation, a solution to the equation is
sought at successive time steps $\Delta t$ apart.

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
equation [\[fullTimeForm](#fullTimeForm){reference-type="ref"
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
equation [\[genForm](#genForm){reference-type="ref"
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
Subclasses of `TransientIntegrator` provide methods informing the
`FE_Element` and `DOF_Group` objects how to build the tangent and residual
matrices and vectors. They also provide the method for updating the
response quantities at the DOFs with appropriate values; these values
being some function of the solution to the linear system of equations.



## Implementation

```cpp
#include <analysis/analysis/DirectIntegrationAnalysis.h>

class DirectIntegrationAnalysis: public TransientAnalysis;
```

### Constructor and Destructor

```cpp
DirectIntegrationAnalysis::DirectIntegrationAnalysis(
                 Domain              &the_Domain,
                 ConstraintHandler   &theHandler,
                 DOF_Numberer        &theNumberer,
                 AnalysisModel       &theModel,
                 EquiSolnAlgo        &theSolnAlgo,
                 LinearSOE           &theLinSOE,
                 TransientIntegrator &theTransientIntegrator,
                 ConvergenceTest     *theConvergenceTest,
                 int                 num_SubLevels,
                 int                 num_SubSteps
)
```


The constructor is responsible for setting up all
links needed by the objects in the aggregation. It invokes
`setLinks(theDomain)` on `theModel`,
`setLinks(theDomain,theModel,theIntegrator)` on `theHandler`,
`setLinks(theModel)` on `theNumberer`, `setLinks(theModel, theSOE)`{.cpp} on
`theIntegrator` and `setLinks(theModel,theAnalysis, theIntegrator, theSOE)` 
on `theSolnAlgo`.
Sets theModel and theSysOFEqn to 0 and the Algorithm to the one supplied.

```cpp
~DirectIntegrationAnalysis
```
Does nothing. `clearAll()` must be invoked if the destructor on the
objects in the aggregation need to be invoked.

### Public Methods

:::{.admonition}
```cpp
int analyze(int steps, double dT);
```
:::
Invokes `analyzeStep(dT)` `steps` number of times.

:::{.admonition}
```cpp
int analyzeStep(double dT);
```
:::
Invoked to perform a transient analysis on the `FE_Model`. The method
checks to see if the domain has changed before it performs the analysis.
The `DirectIntegrationAnalysis` object performs the following:

```cpp
theAnalysisModel->analysisStep(dT);

if (theDomain->hasDomainChanged() != this->domainStamp)
  this->domainChanged();

theIntegrator->newStep(dT);
theAlgorithm->solveCurrentStep();
theIntegrator->commit();
```

The type of analysis performed, depends on the type of the objects in
the analysis aggregation. If any of the methods invoked returns a
negative number, an error message is printed, `revertToLastCommit()` is
invoked on the Domain, and a negative number is immediately returned.
Returns a $0$ if the algorithm is successful.

:::{.admonition}
```{.cpp}
void clearAll(void);
```
:::
Will invoke the destructor on all the objects in the aggregation. NOTE
this means they must have been constructed using `new()`, otherwise a
segmentation fault can occur.

:::{.admonition}
```{.cpp}
void domainChange(void);
```
:::
This is a method invoked by a domain which indicates to the analysis
that the domain has changed. The method invokes the following:

1. It invokes `clearAll()` on `theModel` which causes the `AnalysisModel`
   to clear out its list of `FE_Elements` and `DOF_Groups`, and
   `clearAll()` on `theHandler`.

2. It then invokes `handle()` on `theHandler`. This causes the
   constraint handler to recreate the appropriate `FE_Element` and
   `DOF_Groups` to perform the analysis subject to the boundary
   conditions in the modified domain.

3. It then invokes `numberDOF()` on `theNumberer`. This causes the DOF
   numberer to assign equation numbers to the individual DOFs. Once the
   equation numbers have been set the numberer then invokes `setID()` on all the
   `FE_Elements` in the model. Finally the `DOF_Numberer` invokes `setNumEqn()`
   on `theAnalysisModel`.

4. Then `doneNumberingDOF()` is invoked on the `ConstraintHandler` which
   invokes `setID()` on all the `FE_Elements` in the model. 

5. It invokes `setSize(theModel.getDOFGraph())`{.cpp} on `theSOE` and
   `theEigenSOE` which causes the system of equation to determine its size
   based on the connectivity of the dofs in the analysis model.

6. It then invokes `domainChanged()` on `theIntegrator` and
   `theAlgorithm` to inform these objects that changes have occurred in
   the model.

Returns $0$ if successful. At any stage above, if an
error occurs the method is stopped, a warning message is printed and
a negative number is returned.


### Public Methods to vary the type of Analysis

:::{.admonition}
```cpp
int setAlgorithm(EquiSolnAlgo &theNewAlgorithm)
```
:::
To change the algorithm between analysis. It first invokes the
destructor on the old `SolutionAlgorithm` object associated with the
analysis. It then sets the `SolutionAlgorithm` associated with the
analysis to be `newAlgorithm` and sets the links for this object by
invoking `setLinks()`. Checks then to see if the domain has changed, if
true it invokes `domainChanged()`, otherwise it invokes
`domainChanged()` on the new SolutionAlgorithm. Returns $0$ if
successful, a warning message and a negative number if not.

:::{.admonition}
```cpp
int setIntegrator(TransientIntegrator &theNewIntegrator)
```
:::
To change the integration scheme between analysis. It first invokes the
destructor on the old Integrator object associated with the analysis. It
then sets the SolutionAlgorithm associated with the analysis to be
`newAlgorithm` and sets the links for this object by invoking
`setLinks()`. It also invokes `setLinks()` on the ConstraintHandler and
SolutionAlgorithm objects. Checks then to see if the domain has changed,
if true it invokes `domainChanged()`, otherwise it invokes
`domainChanged()` on the new Integrator. Returns $0$ if successful, a
warning message and a negative number if not.

:::{.admonition}
```cpp
int setLinearSOE(LinearSOE &theNewSOE);
int setEigenSOE(EigenSOE &theNewSOE);
```
:::
To change the respective system of equation object between analysis. It
first invokes the destructor on the old LinearSOE object associated with
the analysis. It then sets the SolutionAlgorithm associated with the
analysis to be `newSOE`. links for this object by invoking `setLinks()`.
It then invokes `setLinks()` on the ConstraintHandler and
SolutionAlgorithm objects. Checks then to see if the domain has changed,
if true it invokes `domainChanged()`, otherwise it invokes `setSize()`
on the new LinearSOE. Returns $0$ if successful, a warning message and a
negative number if not.

