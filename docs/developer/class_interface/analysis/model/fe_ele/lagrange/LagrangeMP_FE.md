# LagrangeMP_FE 

```cpp
#include <analysis/fe_ele/lagrange/LagrangeMP_FE.h>

class LagrangeMP_FE: public FE_Element ;
```

LagrangeMP_FE is a subclass of FE_Element used to enforce a multi point
constraint, of the form ${\bf U}_c = {\bf C}_{cr} {\bf U}_r$, where ${\bf U}_c$ are the
constrained degrees-of-freedom at the constrained node, ${\bf U}_r$ are the
retained degrees-of-freedom at the retained node and ${\bf C}_{cr}$ a matrix
defining the relationship between these degrees-of-freedom.

To enforce the constraint the following are added to the tangent and the
residual:

$$\left[ \begin{array}{cc} 0 & \alpha{\bf C}^t \\ \alpha{\bf C} & 0 \end{array}
\right] ,
\left\{ \begin{array}{c} 0 \\ 0 \end{array} \right\}$$

at the locations
corresponding to the constrained degree-of-freedoms specified by the
MP_Constraint, i.e. $[{\bf U}_c$ ${\bf U}_r]$, and the lagrange multiplier
degrees-of-freedom introduced by the LagrangeConstraintHandler for this
constraint, ${\bf C} = [-\I$ ${\bf C}_{cr}]$. Nothing is added to the residual.

### Constructor


### Destructor


// Public Methods

\

\

\
To construct a LagrangeMP_FE element to enforce the constraint specified
by the `MP_Constraint` *theMP* using a default value for $\alpha$ of
$alpha$. The FE_Element class constructor is called with the integers
$3$ and the two times the size of the *retainedID* plus the size of the
*constrainedID* at the `MP_Constraint` *theMP* plus . A Matrix and a
Vector object are created for adding the contributions to the tangent
and the residual. The residual is zeroed. If the `MP_Constraint` is not
time varying, then the contribution to the tangent is determined. Links
are set to the retained and constrained nodes. The DOF_Group tag ID is
set using the tag of the constrained Nodes DOF_Group, the tag of the
retained Node Dof_group and the tag of the LagrangeDOF_Group,
*theGroup*. A warning message is printed and the program is terminated
if either not enough memory is available for the Matrices and Vector or
the constrained and retained Nodes of their DOF_Groups do not exist.

\
Invokes delete on any Matrix or Vector objects created in the
constructor that have not yet been destroyed.

\
Causes the LagrangeMP_FE to determine the mapping between it's equation
numbers and the degrees-of-freedom. This information is obtained by
using the mapping information at the DOF_Group objects associated with
the constrained and retained nodes and the LagrangeDOF_Group,
*theGroup*. Returns $0$ if successful. Prints a warning message and
returns a negative number if an error occurs: $-2$ if the Node has no
associated DOF_Group, $-3$ if the constrained DOF specified is invalid
for this Node (sets corresponding ID component to $-1$ so nothing is
added to the tangent) and $-4$ if the ID in the DOF_Group is too small
for the Node (again setting corresponding ID component to $-1$).

If the `MP_Constraint` is time-varying, from the `MP_Constraint` `theMP` it
obtains the current $C_{cr}$ matrix; it then adds the contribution to
the tangent matrix. Returns this tangent Matrix.


Returns the residual, a $\zero$ Vector.

```cpp
virtual const Vector &getTangForce(const Vector &disp, double fact = 1.0);
```
CURRENTLY just returns the $0$ residual. THIS WILL NEED TO CHANGE FOR
ELE-BY-ELE SOLVERS.
