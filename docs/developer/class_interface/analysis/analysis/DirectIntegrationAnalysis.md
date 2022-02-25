\
# DirectIntegrationAnalysis 

```cpp
#include <analysis/analysis/DirectIntegrationAnalysis.h>
```

class DirectIntegrationAnalysis: public TransientAnalysis;\

Analysis\
TransientAnalysis\

\
DirectIntegrationAnalysis is a subclass of TransientAnalysis. It is used
to perform a transient analysis using an incremental approach on the
Domain. The following are the aggregates of such an analysis type:

-   **AnalysisModel** - a container class holding the FE_Element and
    DOF_Group objects created by the ConstraintHandler object.

-   **ConstraintHandler** - a class which creates the DOF_Group and
    FE_Element objects, the type of objects created depending on how the
    specified constraints in the domain are to be handled.

-   **DOF_Numberer** - a class responsible for providing equation
    numbers to the individual degrees of freedom in each DOF_Group
    object.

-   **LinearSOE** - a numeric class responsible for the creation and
    subsequent solution of large systems of linear equations of the form
    $Ax = b$, where $A$ is a matrix and $x$ and $b$ are vectors.

-   **TransientIntegrator** - an algorithmic class which provides
    methods which are invoked by the FE_Element to determine their
    current tangent and residual matrices; that is this is the class
    that sets up the system of equations. It also provides the
    `update()` method which is invoked to set up the appropriate dof
    response values once the solution algorithm has formed and solved
    the system of equations.

-   **EquiSolnAlgo** - an algorithmic class specifying the sequence of
    operations to be performed in setting up and solving the finite
    element equation which can be represented by the equation K(U) U =
    P(U).


// Constructor\

\
// Destructor\

\
// Public Methods\

\

\
// Public Methods to vary the type of Analysis\

\

\

\
*tStart*, *tFinish* and *thDomain* are passed to the TransientAnalysis
class constructor. The constructor is responsible for setting up all
links needed by the objects in the aggregation. It invokes
`setLinks(theDomain)` on *theModel*,
*setLinks(theDomain,theModel,theIntegrator)* on *theHandler*,
`setLinks(theModel)` on *theNumberer*, `setLinks(theModel, theSOE)`{.cpp} on
*theIntegrator* and *setLinks(theModel,theAnalysis, theIntegrator,
theSOE)* on *theSolnAlgo*.

\
Does nothing. `clearAll()` must be invoked if the destructor on the
objects in the aggregation need to be invoked.

\
Invoked to perform a transient analysis on the FE_Model. The method
checks to see if the domain has changed before it performs the analysis.
The DirectIntegrationAnalysis object performs the following:

::: {.tabbing}
while ̄ while w̄hile ̄ double time = tStart;\
while (theDomain-$>$getCurrntTime() $<$ tFinish) {\
if (theDomain-$>$hasDomainChanged() == true)\
this-$>$domainChanged();\
theIntegrator-$>$newStep($\delta t$);\
theAlgorithm-$>$solveCurrentStep();\
theIntegrator-$>$commit();\
}
:::

The type of analysis performed, depends on the type of the objects in
the analysis aggregation. If any of the methods invoked returns a
negative number, an error message is printed, `revertToLastCommit()` is
invoked on the Domain, and a negative number is immediately returned.
Returns a $0$ if the algorithm is successful.

```{.cpp}
void clearAll(void);
```

Will invoke the destructor on all the objects in the aggregation. NOTE
this means they must have been constructed using `new()`, otherwise a
segmentation fault can occur.

```{.cpp}
void domainChange(void);
```

This is a method invoked by a domain which indicates to the analysis
that the domain has changed. The method invokes the following:

1.  It invokes `clearAll()` on *theModel* which causes the AnalysisModel
    to clear out its list of FE_Elements and DOF_Groups, and
    `clearAll()` on *theHandler*.

2.  It then invokes `handle()` on *theHandler*. This causes the
    constraint handler to recreate the appropriate FE_Element and
    DOF_Groups to perform the analysis subject to the boundary
    conditions in the modified domain.

3.  It then invokes `number()` on *theNumberer*. This causes the DOF
    numberer to assign equation numbers to the individual dof's. Once
    the equation numbers have been set the numberer then invokes
    `setID()` on all the FE_Elements in the model. Finally the numberer
    invokes `setNumEqn()` on the model.

4.  It then invokes `domainChanged()` on *theIntegrator* and
    *theAlgorithm* to inform these objects that changes have occurred in
    the model.

5.  It invokes `setSize(theModel.getDOFGraph())`{.cpp} on *theSOE* which
    causes the system of equation to determine its size based on the
    connectivity of the dofs in the analysis model.

6.  Finally it invokes `domainChanged()` on *theIntegrator* and
    *theAlgorithm*. Returns $0$ if successful. At any stage above, if an
    error occurs the method is stopped, a warning message is printed and
    a negative number is returned.


```{.cpp}
int setDeltaT(double $\delta t$);
```

Sets the time increment used in the `analyze()` method to $\delta
t$. Returns $0$.

To change the algorithm between analysis. It first invokes the
destructor on the old SolutionAlgorithm object associated with the
analysis. It then sets the SolutionAlgorithm associated with the
analysis to be *newAlgorithm* and sets the links for this object by
invoking `setLinks()`. Checks then to see if the domain has changed, if
true it invokes `domainChanged()`, otherwise it invokes
`domainChanged()` on the new SolutionAlgorithm. Returns $0$ if
successful, a warning message and a negative number if not.

To change the integration scheme between analysis. It first invokes the
destructor on the old Integrator object associated with the analysis. It
then sets the SolutionAlgorithm associated with the analysis to be
*newAlgorithm* and sets the links for this object by invoking
`setLinks()`. It also invokes `setLinks()` on the ConstraintHandler and
SolutionAlgorithm objects. Checks then to see if the domain has changed,
if true it invokes `domainChanged()`, otherwise it invokes
`domainChanged()` on the new Integrator. Returns $0$ if successful, a
warning message and a negative number if not.

To change the linear system of equation object between analysis. It
first invokes the destructor on the old LinearSOE object associated with
the analysis. It then sets the SolutionAlgorithm associated with the
analysis to be *newSOE*. links for this object by invoking `setLinks()`.
It then invokes `setLinks()` on the ConstraintHandler and
SolutionAlgorithm objects. Checks then to see if the domain has changed,
if true it invokes `domainChanged()`, otherwise it invokes `setSize()`
on the new LinearSOE. Returns $0$ if successful, a warning message and a
negative number if not.
