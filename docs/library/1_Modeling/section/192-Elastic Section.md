# Elastic Section

<p>This command allows the user to construct an ElasticSection. The
inclusion of shear deformations is optional.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>section Elastic $secTag $E $A $Iz &lt;$G
$alphaY&gt;</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>section Elastic $secTag $E $A $Iz $Iy $G $J &lt;$alphaY
$alphaZ&gt;</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">secTag</code></p></td>
<td><p>unique section tag</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">E</code></p></td>
<td><p>Young's Modulus</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">A</code></p></td>
<td><p>cross-sectional area of section</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Iz</code></p></td>
<td><p>second moment of area about the local z-axis</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">Iy</code></p></td>
<td><p>second moment of area about the local y-axis (required for 3D
analysis)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">G</code></p></td>
<td><p>Shear Modulus (optional for 2D analysis, required for 3D
analysis)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">J</code></p></td>
<td><p>torsional moment of inertia of section (required for 3D
analysis)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">alphaY</code></p></td>
<td><p>shear shape factor along the local y-axis (optional)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">alphaZ</code></p></td>
<td><p>shear shape factor along the local z-axis (optional)</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<ul>
<li>The elastic section can be used in the nonlinear beam column
elements, which is useful in the initial stages of developing a complex
model.</li>
</ul>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
# ElasticSection3D 

```cpp
#include <material/section/ElasticSection3D.h>

class ElasticSection3D : public SectionForceDeformation
```

TaggedObject\
MovableObject\
Material\
SectionForceDeformation\


ElasticSection3D provides the implementation of a section which exhibits
uncoupled elastic behavior in axial, moment, shear, and torsion
response.

### Constructor

\

### Destructor

\
// Public Methods\

\

\

\

\

\

\

\

// Public Methods for Output\

\

\

To construct an ElasticSection3D with an integer identifier *tag*, an
elastic modulus of $E$, a second moment of area about the local z-axis,
$I_z$, a second moment of area about the local y-axis, $I_y$, a polar
moment of intertia of $J$, a section area of $A$, an elastic shear
modulus of $G$, and a shape factor of $\alpha$. The integers *tag* and
MAT_TAG_ElasticSection3D, defined in  `<classTags.h>`, are passed to
the SectionForceDeformation class constructor.

Constructs a blank ElasticSection3D object.

\
Does nothing.

\
Sets the value of the section deformation vector, $\esec$ to be *def*.
The section deformation vector, $\esec$, is defined by

$$\esec := \left[
   \begin{array}{c}
       \epsilon_a \\
       \kappa_z   \\
       \kappa_y   \\
       \gamma_y   \\
       \gamma_z   \\
       \phi
   \end{array} 
 \right]$$

where $\epsilon_a$ is the axial strain, $\kappa_z$ is the curvature
about the local z-axis, $\kappa_z$ is the curvature about the local
z-axis, $\gamma_y$ is the shear strain along the local y-axis,
$\gamma_z$ is the shear strain along the local z-axis, and $\phi$ is the
angle of twist. Returns $0$.

Returns the current value of the section deformation vector, $\esec$.

Returns the section stress resultants, $\ssec$, the product of the
section stiffness matrix, $\ksec$, and the section deformation vector,
$\esec$,

$$\ssec = \ksec \esec = \left[
   \begin{array}{c}
       P     \\
       M_z   \\
       M_z   \\
       V_y   \\
       V_y   \\
       T
   \end{array} 
 \right]$$

where $P$ is the axial force, $M_z$ is the bending moment about the
local z-axis, $M_y$ is the bending moment about the local y-axis, $V_y$
is the shear force along the local y-axis, $V_z$ is the shear force
along the local z-axis, and $T$ is the torque.

Returns the value of $\ssec$ calculated at the previous state
determination.

Returns the section stiffness matrix, $\ksec$, where

$$\ksec = \left[
   \begin{array}{cccccc}
       EA &  0 &  0 & 0 & 0 & 0  \\
        0 & EI_z & 0 & 0 & 0 & 0 \\
        0 & 0 & EI_y & 0 & 0 & 0 \\
        0 & 0 & 0 & \alpha GA & 0 & 0 \\
        0 & 0 & 0 & 0 & \alpha GA & 0 \\
        0 & 0 & 0 & 0 & 0 & GJ
   \end{array} 
 \right]$$\

Returns the section stiffness matrix, $\ksec$.

Overrides the base class implementation and returns the section
flexibility matrix, $\fsec$, where

$$\fsec = \left[
   \begin{array}{cccccc}
       \frac{1}{EA} & 0 & 0 & 0 & 0 & 0 \\
       0 & \frac{1}{EI_z} & 0 & 0 & 0 & 0 \\
       0 & 0 & \frac{1}{EI_y} & 0 & 0 & 0 \\
       0 & 0 & 0 & \frac{1}{\alpha GA} & 0 & 0 \\ 
       0 & 0 & 0 & 0 & \frac{1}{\alpha GA} & 0 \\
       0 & 0 & 0 & 0 & 0 & \frac{1}{GJ}
   \end{array} 
 \right]$$\

Overrides the base class implementation and returns the section
flexibility matrix, $\fsec$.

Returns $0$.

Returns $0$.

Returns $0$.

Returns a pointer to a new ElasticSection3D object, constructed using
the same values of *tag*, $E$, $A$, $I_z$, $I_y$, $J$, $G$, and
$\alpha$. It is up to the caller to ensure that the destructor is
invoked.

Returns the section ID code that indicates the ordering of section
response quantities. For this section, axial response is the first
quantity, bending about the local z-axis is the second, bending about
the local y-axis is the third, shear along the local y-axis is the
fourth, shear along the local z-axis is the fifth, and torsion is the
sixth.
$$code := \left[
   \begin{array}{c}
       2 \\
       1 \\
       4 \\
       3 \\
       5 \\
       6
   \end{array} 
 \right]$$\

Returns 6.

Creates a Vector of size $8$ into which it places *tag*, $E$, $A$,
$I_z$, $I_y$, $J$, $G$, and $\alpha$. Invokes `sendVector()` on
*theChannel* using the ElasticSection3D objects *dbTag*, the integer
*commitTag* and the Vector as arguments. Returns $0$ if successful, a
warning message and a negative number are returned if the Channel object
fails to send the Vector.

Creates a Vector of size $8$. Invokes `recvVector()` on *theChannel*
using the ElasticSection3D objects *dbTag*, the integer *commitTag* and
the Vector as arguments. Using the data in the Vector to set its *tag*,
$E$, $A$, $I_z$, $I_y$, $J$, $G$, and $\alpha$. Returns $0$ if
successful, a warning message is printed and a negative number is
returned if the Channel object fails to receive the Vector.

Prints to the stream *s* the object's *tag*, $E$, $A$, $I_z$, $I_y$,
$J$, $G$, and $\alpha$ values.
