---
title: StaticAnalysis
description: |
  StaticAnalysis is a subclass of Analysis, it is used 
  to perform a static analysis on the Domain.
...

# StaticAnalysis

```cpp
#include <analysis/analysis/StaticAnalysis.h>

class StaticAnalysis: public Analysis;
```

## Description

`StaticAnalysis` is a subclass of `Analysis`, it is used to perform a static
analysis on the Domain. The following are the aggregates of such an
analysis type:

-  **AnalysisModel** - a container class holding the `FE_Element` and
   `DOF_Group` objects created by the `ConstraintHandler` object.

-  **ConstraintHandler** - a class which creates the DOF_Group and
   FE_Element objects, the type of objects created depending on how the
   specified constraints in the domain are to be handled.

-  **DOF_Numberer** - a class responsible for providing equation
   numbers to the individual degrees of freedom in each DOF_Group
   object.

-  **LinearSOE** - a numeric class responsible for the creation and
   subsequent solution of large systems of linear equations of the form
   $Ax = b$, where $A$ is a matrix and $x$ and $b$ are vectors.

-  **StaticIntegrator** - an algorithmic class which provides methods
   which are invoked by the FE_Element to determine their current
   tangent and residual matrices; that is this is the class that sets
   up the system of equations. It also provides the `update()` method
   which is invoked to set up the appropriate dof response values once
   the solution algorithm has formed and solved the system of
   equations.

-  **EquiSolnAlgo** - an algorithmic class specifying the sequence of
   operations to be performed in setting up and solving the finite
   element equation which can be represented by the equation K(U) U =
   P(U).

## Class Interface

### Constructors

```cpp
StaticAnalysis(Domain &theDomain, 
         ConstraintHandler &theHandler, 
         DOF_Numberer &theNumberer, 
         AnalysisModel &theModel,
         EquiSolnAlgo &theSolnAlgo,
         LinearSOE &theSOE, 
         StaticIntegrator &theIntegrator,
         int numIncrements = 1);
```

The constructor is responsible for setting the links between the objects
in the aggregation. To do this it invokes `setLinks(theDomain)` on
*theModel*, `setLinks(theDomain,theModel,theIntegrator)`{.cpp} on
*theHandler*, `setLinks(theModel)` on *theNumberer*, *setLinks(theModel,
theSOE)* on *theIntegrator*, and *setLinks(theModel,theAnalysis,
theIntegrator, theSOE)* on *theSolnAlgo*. The constructor also sets the
number of analysis steps that will be performed to be *numIncrements*.

### Destructor

Does nothing. `clearAll()` must be invoked if the destructor on the
objects in the aggregation need to be invoked.


### Public Methods

```cpp
int analyze(int numSteps);
```

Invoked to perform a static analysis on the FE_Model. The analysis The
`StaticAnalysis` object performs the following:

```cpp
// while ̄ while w̄hile ̄ 
for (int i=0; i < numSteps; i++) {
  if (theDomain->hasDomainChanged() == true)
    this->domainChanged();
  theIntegrator.newStep();
  theSolnAlgo.solveCurrentStep();
  theIntegrator.commit();
}
```

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

```cpp
int domainChange(void);
```

This is a method invoked by the analysis during the analysis method if
the Domain has changed. The method invokes the following:

1.  It invokes `clearAll()` on `theModel` which causes the `AnalysisModel`
    to clear out its list of `FE_Elements` and `DOF_Groups`, and
    `clearAll()` on `theHandler`.

2.  It then invokes `handle()` on `theHandler`. This causes the
    constraint handler to recreate the appropriate FE_Element and
    DOF_Groups to perform the analysis subject to the boundary
    conditions in the modified domain.

3.  It then invokes `number()` on `theNumberer`. This causes the DOF
    numberer to assign equation numbers to the individual dof's. Once
    the equation numbers have been set the numberer then invokes
    `setID()` on all the FE_Elements in the model. Finally the numberer
    invokes `setNumEqn()` on the model.

4.  It invokes `setSize(theModel.getDOFGraph())`{.cpp} on `theSOE` which
    causes the system of equation to determine its size based on the
    connectivity of the dofs in the analysis model.

5.  Finally `domainChanged()` is invoked on both `theIntegrator` and
    *theAlgorithm*. Returns `0` if successful. At any stage above, if an
    error occurs the method is stopped, a warning message is printed and
    a negative number is returned.



#### Public Methods to vary the type of Analysis

```cpp
int setNumIncrements(int numIncrements);
```

To set the number of incremental steps in the analysis to be
*numIncrements*. Returns $0$.

```cpp
int setAlgorithm(EquiSolnAlgo &theAlgorithm);
```

To change the algorithm between analysis. It first invokes the
destructor on the old SolutionAlgorithm object associated with the
analysis. It then sets the SolutionAlgorithm associated with the
analysis to be *newAlgorithm* and sets the links for this object by
invoking `setLinks()`. Checks then to see if the domain has changed, if
true it invokes `domainChanged()`, otherwise it invokes
`domainChanged()` on the new SolutionAlgorithm. Returns $0$ if
successful, a warning message and a negative number if not.

```cpp
int setIntegrator(StaticIntegrator &theIntegrator);
```

To change the integration scheme between analysis. It first invokes the
destructor on the old Integrator object associated with the analysis. It
then sets the SolutionAlgorithm associated with the analysis to be
*newAlgorithm* and sets the links for this object by invoking
`setLinks()`. It also invokes `setLinks()` on the ConstraintHandler and
SolutionAlgorithm objects. Checks then to see if the domain has changed,
if true it invokes `domainChanged()`, otherwise it invokes
`domainChanged()` on the new Integrator. Returns $0$ if successful, a
warning message and a negative number if not.


```cpp
int setLinearSOE(LinearSOE &theSOE);
```

To change the linear system of equation object between analysis. It
first invokes the destructor on the old LinearSOE object associated with
the analysis. It then sets the SolutionAlgorithm associated with the
analysis to be *newSOE*. links for this object by invoking `setLinks()`.
It then invokes `setLinks()` on the ConstraintHandler and
SolutionAlgorithm objects. Checks then to see if the domain has changed,
if true it invokes `domainChanged()`, otherwise it invokes `setSize()`
on the new LinearSOE. Returns $0$ if successful, a warning message and a
negative number if not.

