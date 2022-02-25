\
# PenaltySP_FE 

```cpp
#include <analysis/fe_ele/penalty/PenaltySP_FE.h>
```

class PenaltySP_FE: public FE_Element ;\

FE_Element\

\
PenaltySP_FE is a subclass of FE_Element used to enforce a single point
constraint. It does this by adding $\alpha$ to the tangent and
$\alpha * (U\_s - U\_t)$ to the residual at the locations corresponding
to the constrained degree-of-freedom specified by the `SP_Constraint`,
where $U_s$ is the specified value of the constraint and $U_t$ the
current trial displacement at the node corresponding to the constraint.

// Constructor\

\
// Destructor\

\
// Public Methods\

\

\

\
To construct a PenaltySP_FE element to enforce the constraint specified
by the SP_Constraint *theSP* using a value for $\alpha$ of *alpha*
(which, if none is specified, defaults to $1.0e8$). The FE_Element class
constructor is called with the integers $1$ and $1$. A Matrix and a
Vector object of order $1$ are created to return the tangent and
residual contributions, with the tangent entry being set at $\alpha$. A
link to the Node in the Domain corresponding to the SP_Constraint is
also set. A warning message is printed and program terminates if there
is not enough memory or no Node associated with the SP_Constraint exists
in the Domain.

\
Invokes the destructor on the Matrix and Vector objects created in the
constructor.

\
Causes the PenaltySP_FE to determine the mapping between it's equation
numbers and the degrees-of-freedom. From the Node object link, created
in the constructor, the DOF_group corresponding to the Node associated
with the constraint is determined. From this *DOF_Group* object the
mapping for the constrained degree of freedom is determined and the ID
in the base class is set. Returns $0$ if successful. Prints a warning
message and returns a negative number if an error occurs: $-2$ if the
Node has no associated DOF_Group, $-3$ if the constrained DOF specified
is invalid for this Node and $-4$ if the ID in the DOF_Group is too
small for the Node.

Returns the tangent Matrix created in the constructor.

Sets the FE_Elements contribution to the residual to be
$\alpha * (U_s - U_t)$, where $U_s$ is the specified value of the
constraint and $U_t$ the current trial displacement at the node
corresponding to constrained degree-of-freedom. Prints a warning message
and sets this contribution to $0$ if the specified constrained
degree-of-freedom is invalid. Returns this residual Vector set.

*virtual const Vector &getTangForce(const Vector &disp, double fact =
1.0);* \
Sets the FE_Elements contribution to the residual to be
$\alpha * (U\_s - disp\_t)$, where $U\_s$ is the specified value of the
constraint and $disp\_t$ the value in *disp* corresponding to
constrained degree-of-freedom. Prints a warning message and sets this
contribution to $0$ if the mapping, determined in `setID()`, for the the
specified constrained degree-of-freedom lies outside *disp*.
