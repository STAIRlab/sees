NEED TO ADD ADD_INERTIA_LOAD TO INTERFACE .. SEE EARTHQUAKE_PATTERN
CLASS.

# BeamWithHinges2D 

```cpp
#include <element/BeamWithHinges2D.h>
```

class BeamWithHinges2D: public DomainComponent\

TaggedObject\
MovableObject\
DomainComponent\
Element\

\
BeamWithHinges2D is a beam-column element which uses the force based
formulation for its state determination. This element has material
non-linear hinges at both ends and exhibits linear elastic behavior
through its interior region, including linear elastic shear effects.

// Constructors\

\

\
// Destructor\

\
// Public Methods dealing with Nodes and dof\

\

\
// Public Methods dealing with State\

\

\
// Public Methods for obtaining Linearized Stiffness, Mass and Damping
Matrices\

\

\

// Public Methods for obtaining Resisting Forces\

\

\

\
Constructs a BeamWithHinges2D object with tag *tag*, unique among all
elements in the domain. The end nodes of the element are set to be those
with tags *nodeI* and *nodeJ*. The elastic properties of the interior
beam region are set to be *E*, the modulus of elasticity; *I*, the
second moment of area of the beam cross-section; *A*, the beam
cross-sectional area; *G*, the shear modulus; and *alpha*, the
cross-section shape factor for elastic shear effects. Element hinges are
created by obtaining copies of *sectionI* and *sectionJ*. The hinge
lengths are specified as ratios of the total element length, *ratioI*
and *ratioJ*. The element distributed load (reference value) is set to
be *distrLoad*, and the element mass density per unit length is
*massDens*.

Constructs a BeamWithHinges2D object with tag *tag*, unique among all
elements in the domain. The end nodes of the element are set to be those
with tags *nodeI* and *nodeJ*. The elastic properties of the interior
beam region are set to be *E*, the modulus of elasticity; *I*, the
second moment of area of the beam cross-section; *A*, the beam
cross-sectional area; *G*, the shear modulus; and *alpha*, the
cross-section shape factor for elastic shear effects. Element hinges are
created by obtaining copies of *sectionI* and *sectionJ*. The hinge
lengths are specified as ratios of the total element length, *ratioI*
and *ratioJ*. The element mass density per unit length is *massDens*.

Constructs a blank BeamWithHinges2D object.

\
Invokes the section destructors.

\
Returns 2, the number of external nodes for this element.

Returns an ID containing the tags of the two external nodes for this
element.

Returns 6, the number of degrees of freedom for this element.

```{.cpp}
int commitState(void);
```

Invokes `commitState()` on each section and returns the sum of the
result of these invocations.

```{.cpp}
int revertToLastCommit(void);
```

Invokes `revertToLastCommit()` on each section and returns the sum of
the result of these invocations.

```{.cpp}
int revertToStart(void);
```

Invokes `revertToStart()` on each section and returns the sum of the
result of these invocations.

```{.cpp}
const Matrix &getTangentStiff(void);
```

Computes the element flexibility matrix, then returns its inverse, the
element stiffness matrix. The element flexibility is the sum of the
hinge flexibilities, $\mathbf{f}_I$ and $\mathbf{f}_J$, and the elastic
flexibility of the beam interior, $\mathbf{f}_{mid}$.

$$\label{eq:fele}
\fbas := \int_{0}^{L}{\bint^T \fsec \bint \: dx} = \mathbf{f}_I + \mathbf{f}_{mid} + \mathbf{f}_J$$

The flexibility of the beam interior is obtained in closed form,

$$\mathbf{f}_{mid} = \int_{l_I}^{L-l_J}{\bint^T \fsec_{mid} \bint \: dx}$$

where $\bint$ is the force interpolation matrix,

$$\bint := \left[
   \begin{array}{c c c}
      1 &           0 &               0 \\
      0 & \frac{x}{L} & \frac{x}{L} - 1 \\
      0 & \frac{1}{L} &     \frac{1}{L}
   \end{array} 
 \right]$$

and $\fsec$ is the elastic section flexibility of the beam interior.

$$\fsec_{mid} = \left[
   \begin{array}{c c c}
      \frac{1}{EA} &            0 &                   0 \\
                 0 & \frac{1}{EI} &                   0 \\
                 0 &            0 & \frac{1}{\alpha GA}
   \end{array}
 \right]$$

The hinge flexibilities, $\mathbf{f}_I$ and $\mathbf{f}_J$, are obtained
by the midpoint integration rule,

$${\mathbf{f}}_i = \bint(x_i)^T \fsec_i \bint(x_i) * l_i, \:\: i=I,J$$

where $x_i$ is the midpoint of hinge $i$, measured along the length of
the beam, and is the point at which the force interpolation matrix,
$\bint$ is evaluated. The flexiblity, $\fsec_i$, is obtained from the
constitutive relation for section $i$.
The element stiffness is then obtained by inversion of the element
flexibility, given by Equation
[\[eq:fele\]](#eq:fele){reference-type="ref" reference="eq:fele"}.

$$\label{eq:kele}
\kbas = \fbas^{-1}$$

The element then obtains the matrix, $\mathbf{A}$, which transforms the
element basic stiffness from its corotating frame to the global frame of
reference. The transformed stiffness matrix, $\kele$, is then assembled
into the structural system of equations.

$$\kele = \mathbf{A}^T \kbas \mathbf{A}$$\

```{.cpp}
const Matrix &getSecantStiff(void);
```

To return the elements secant stiffness matrix. THIS SECANT MAY BE
REMOVED.

```{.cpp}
const Matrix &getDamp(void);
```

To return the damping matrix.

```{.cpp}
const Matrix &getMass(void);
```

Returns the element lumped mass matrix, $\mele$. It is assumed that the
mass density per unit length, $\rho$, is constant along the entire
element, including the hinge regions.

$$\label{eq:mele}
\mele = \left[
   \begin{array}{c c c c c c}
      \frac{\rho L}{2} & 0 & 0 & 0 & 0 & 0 \\
      0 & \frac{\rho L}{2} & 0 & 0 & 0 & 0 \\
      0 & 0 & 0 & 0 & 0 & 0 \\
      0 & 0 & 0 & \frac{\rho L}{2} & 0 & 0 \\
      0 & 0 & 0 & 0 & \frac{\rho L}{2} & 0 \\
      0 & 0 & 0 & 0 & 0 & 0
   \end{array}
 \right]$$


```{.cpp}
void zeroLoad(void);
```

This is a method invoked to zero the element load contributions to the
residual.

```{.cpp}
const Vector &getResistingForce(void);
```

Returns the element resisting force vector. The basic element force
vector is obtained as the product of the basic element stiffness,
$\kbas$, given by Equation [\[eq:kele\]](#eq:kele){reference-type="ref"
reference="eq:kele"}, and the basic element deformations, $\vbas$.

$$\qbas = \kbas \vbas$$

The basic element force vector is then transformed from the corotating
frame to the global frame of reference. The transformed force vector is
then assembled into the structural system of equations.

$$\label{eq:qele}
\qele = \mathbf{A}^T \qbas$$\

```{.cpp}
const Vector &getResistingForceIncInertia(void);
```

Returns the element resisting force vector, $\tilde{\qele}$ with inertia
forces included,

$$\tilde{\qele} = \qele - \mele \ddot{\mathbf u}$$

where $\qele$ and $\mele$ are obtained from Equations
[\[eq:qele\]](#eq:qele){reference-type="ref" reference="eq:qele"} and
[\[eq:mele\]](#eq:mele){reference-type="ref" reference="eq:mele"},
respectively, and $\ddot{\mathbf u}$ is the vector of trial nodal
accelerations for the element.
