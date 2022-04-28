# LagrangeSP_FE 

```cpp
#include <analysis/fe_ele/lagrange/LagrangeSP_FE.h>

class LagrangeSP_FE:
public FE_Element
```


`LagrangeSP_FE` is a subclass of [`FE_Element`](../FE_Element) used to enforce a single point
constraint. It does this by adding to the tangent and the residual:
$$\left[ \begin{array}{cc} 0 & \alpha \\ \alpha & 0 \end{array}
\right] ,
\left\{ \begin{array}{c} 0 \\ \alpha(u_s - u_t) \end{array} \right\}$$
at the locations corresponding to the constrained degree-of-freedom
specified by the SP_Constraint and the lagrange multiplier
degree-of-freedom introduced by the LagrangeConstraintHandler for this
constraint, where $U_s$ is the specified value of the constraint and
$U_t$ the current trial displacement at the node corresponding to the
constraint.

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\
To construct a LagrangeSP_FE element to enforce the constraint specified
by the SP_Constraint *theSP* using a value for $\alpha$ of *alpha*
(which, if none is specified, defaults to $1.0$). The FE_Element class
constructor is called with the integers $2$ and $2$. A Matrix and a
Vector object of order $2$ are created to return the tangent and
residual contributions, with the tangent entries (0,1) and (1,0) set at
$\alpha$. A link to the Node in the Domain corresponding to the
SP_Constraint is also set. A warning message is printed and program
terminates if there is not enough memory or no Node associated with the
SP_Constraint exists in the Domain, or DOF_Group is associated with the
Node.

\
Invokes the destructor on the Matrix and Vector objects created in the
constructor.

\
Causes the LagrangeSP_FE to determine the mapping between it's equation
numbers and the degrees-of-freedom. From the Node object link, created
in the constructor, the DOF_group corresponding to the Node associated
with the constraint is determined. From this *DOF_Group* object the
mapping for the constrained degree of freedom is determined and the
myID(0) in the base class is set. The myID(1) is determined from the
Lagrange DOF_Group *theGroup* passed in the constructor. Returns $0$ if
successful. Prints a warning message and returns a negative number if an
error occurs: $-2$ if the Node has no associated DOF_Group, $-3$ if the
constrained DOF specified is invalid for this Node and $-4$ if the ID in
the DOF_Group is too small for the Node.

Returns the tangent Matrix created in the constructor.

Sets the FE_Elements contribution to the residual:
$$\left\{ \begin{array}{c} 0 \\ \alpha(u_s - u_t) \end{array} \right\}$$
where $U_s$ is the specified value of the constraint and $U_t$ the
current trial displacement at the node corresponding to constrained
degree-of-freedom. Prints a warning message and sets this contribution
to $0$ if the specified constrained degree-of-freedom is invalid.
Returns this residual Vector.

```cpp
virtual const Vector &getTangForce(const Vector &disp, double fact = 1.0);
```
Sets the `FE_Elements` contribution to the residual:
$$\left\{ \begin{array}{c} 0 \\ \alpha(u_s - u_t) \end{array} \right\}$$
where $U_s$ is the specified value of the constraint and $U_t$ the
current trial displacement in `disp` corresponding to constrained
degree-of-freedom. Prints a warning message and sets this contribution
to $0$ if the specified constrained degree-of-freedom is invalid.
