\
# ConstraintHandler 

```cpp
#include <analysis/handler/ConstraintHandler.h>
```

class ConstraintHandler: public MovableObject\

MovableObject\

\
The ConstraintHandler class is an abstract base class. Its purpose is to
define the interface common among all subclasses. A constraint handler
is responsible for:

1.  creating the FE_Element and DOF_Group objects and adding them to the
    AnalysisModel.

2.  setting the initial dof equation numbers to $-1$, $-2$ or $-3$. A
    $-1$ indicates to the DOF_Numberer object that no equation number is
    to be allocated for this dof, a $-3$ that this dof is to be among
    the last group of dof to be numbered.

3.  deleting the DOF_Group and FE_Element objects that it created.


// Constructor\

\
// Destructor\

\
// Public Methods\

\

\
// Protected Methods\

\

\

The integer *classTag* is passed to the MovableObject constructor.

\
Does nothing.

\
Invoked to set the links that the ConstraintHandler will need. These
include links to the Domain, *theDomain*, for which the
ConstraintHandler object will apply the constraints and the
AnalysisModel, *theModel*, to which the ConstraintHandler will add the
FE_Element and DOF_Group objects.

Invoked to handle the constraints imposed on the domain by the
SP_Constraints and MP_Constraints. The ConstraintHandler object does
this by instantiating the appropriate FE_ELement and DOF_Group objects
and adding them to the AnalysisModel. For all the dofs in each DOF_Group
the ConstraintHandler sets initial equation numbers as either $-1$, $-2$
or $-3$: A $-1$ indicates to the DOF_Numberer object that no equation
number is to be allocated for this dof, a $-2$ that an equation number
is to be given for the dof, and a $-3$ that an equation number is to be
allocated and that this dof is to be among the last group of dof to be
numbered,i.e. all dof initially assigned a $-3$ are to be given a higher
equation number than those given a $-2$. Those dof with a $-3$ should
include all those dof associated with the nodes whose tags are in
*nodesToBeNumberedLast*. Returns a positive number if successfully, a
negative integer if not; the positive number is to be set at the number
of dof assigned a value $-3$ (this will be the number of external dof
for a subdomain), the negative value of which depends on the type of
ConstraintHandler. For subdomains the constraint handler is responsible
for setting the FE_Element by calling *setFE_elementPtr*.

```{.cpp}
virtual void clearAll(void) =0;
```

Invoked to inform the ConstraintHandler object that the FE_Elements and
DOF_Groups it constructed are no longer part of the AnalysisModel. The
ConstraintHandler can delete these objects if necessary; or the
ConstraintHandler can store them and use them in subsequent calls to
`handle()`.

\
A const member function to return the Domain object associated with the
ConstraintHandler, *theDomain*.

```{.cpp}
AnalysisModel \*getAnalysisModelPtr(void) const;
```

A const member function to return the AnalysisModel object associated
with the ConstraintHandler, *theModel*.

```{.cpp}
Integrator \*getIntegratorPtr(void) const;
```

A const member function to return the Integrator object associated with
the ConstraintHandler, *theIntegrator*.
