\
# PenaltyMP_FE 

```cpp
#include <analysis/fe_ele/penalty/PenaltyMP_FE.h>
```

class PenaltyMP_FE: public FE_Element ;\

FE_Element\

\
PenaltyMP_FE is a subclass of FE_Element used to enforce a multi point
constraint, of the form $\U_c = \C_{cr} \U_r$, where $\U_c$ are the
constrained degrees-of-freedom at the constrained node, $\U_r$ are the
retained degrees-of-freedom at the retained node and $\C_{cr}$ a matrix
defining the relationship between these degrees-of-freedom.

To enforce the constraint a matrix $\alpha \C^T \C$ is added to the
tangent for the degrees-of-freedom $[\U_c$ $\U_r]$, where $\C = [-\I$
$\C_{cr}]$. Nothing is added to the residual.

// Constructor\

\
// Destructor\

\
// Public Methods\

\

\

\
To construct a PenaltyMP_FE element to enforce the constraint specified
by the `MP_Constraint` *theMP* using a default value for $\alpha$ of
$alpha$. The FE_Element class constructor is called with the integers
$2$ and the size of the *retainedID* plus the size of the
*constrainedID* at the `MP_Constraint` *theMP*. A Matrix and a Vector
object are created for adding the contributions to the tangent and the
residual. The residual is zeroed. A Matrix is created to store the $C$
Matrix. If the `MP_Constraint` is not time varying, the components of this
Matrix are determined, then the contribution to the tangent
$\alpha C^TC$ is determined and finally the $C$ matrix is destroyed.
Links are set to the retained and constrained nodes. A warning message
is printed and the program is terminated if either not enough memory is
available for the Matrices and Vector or the constrained and retained
Nodes do not exist in the Domain.

\
Invokes delete on any Matrix or Vector objects created in the
constructor that have not yet been destroyed.

\
Causes the PenaltyMP_FE to determine the mapping between it's equation
numbers and the degrees-of-freedom. This information is obtained by
using the mapping information at the DOF_Group objects associated with
the constrained and retained nodes to determine the mappings between the
degrees-of-freedom identified in the *constrainedID* and the
*retainedID* at the `MP_Constraint` *theMP*. Returns $0$ if successful.
Prints a warning message and returns a negative number if an error
occurs: $-2$ if the Node has no associated DOF_Group, $-3$ if the
constrained DOF specified is invalid for this Node (sets corresponding
ID component to $-1$ so nothing is added to the tangent) and $-4$ if the
ID in the DOF_Group is too small for the Node (again setting
corresponding ID component to $-1$).

If the `MP_Constraint` is time-varying, from the `MP_Constraint` *theMP* it
obtains the current $C_{cr}$ matrix; it then forms the $C$ matrix and
finally it sets the tangent matrix to be $\alpha
C^TC$. Returns the tangent matrix.

Returns the residual, a $\zero$ Vector.
*virtual const Vector &getTangForce(const Vector &disp, double fact =
1.0);* \
CURRENTLY just returns the $0$ residual. THIS WILL NEED TO CHANGE FOR
ELE-BY-ELE SOLVERS.
