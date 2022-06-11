# Joint2D

<p>This command is used to construct a two-dimensional beam-column-joint
element object. The two dimensional beam-column joint is idealized as a
parallelogram shaped shear panel with adjacent elements connected to its
mid-points. The midpoints of the parallelogram are referred to as
external nodes. These nodes are the only analysis components that
connect the joint element to the surrounding structure.</p>

```tcl
element Joint2D $eleTag $Nd1 $Nd2 $Nd3 $Nd4 $NdC
        &lt;$Mat1 $Mat2 $Mat3 $Mat4&gt; $MatC $LrgDspTag
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Nd1 Nd2 Nd3 Nd4</code></p></td>
<td><p>integer tags indicating four external nodes where the joint
element is connected to the adjoining beam-column element</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">NdC</code></td>
<td><p>integer tags indicating the central node of beam-column joint
(the tag is used to generate the internal node, thus, the node should
not exist in the domain or be used by any other node)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Mat1</code></p></td>
<td><p>uniaxial material tag for interface rotational spring at node 1.
Use a zero tag to indicate the case that a beam-column element is
rigidly framed to the joint. (optional)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">Mat2</code></p></td>
<td><p>uniaxial material tag for interface rotational spring at node 2.
Use a zero tag to indicate the case that a beam-column element is
rigidly framed to the joint. (optional)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Mat3</code></p></td>
<td><p>uniaxial material tag for interface rotational spring at node 3.
Use a zero tag to indicate the case that a beam-column element is
rigidly framed to the joint. (optional)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">Mat4</code></p></td>
<td><p>uniaxial material tag for interface rotational spring at node 4.
Use a zero tag to indicate the case that a beam-column element is
rigidly framed to the joint. (optional)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">MatC</code></td>
<td><p>uniaxial material tag for rotational spring of the central node
that describes shear panel behavior</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">LrgDspTag</code></td>
<td><p>an integer indicating the flag for considering large
deformations:</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>0 - for small deformations and constant geometry</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>1 - for large deformations and time varying geometry</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>2 - for large deformations ,time varying geometry and length
correction</p></td>
</tr>
</tbody>
</table>
<p><img src="/OpenSeesRT/contrib/static/Joint2D_panelZone.GIF" title="Joint2D_panelZone.GIF"
alt="Joint2D_panelZone.GIF" /> <img src="/OpenSeesRT/contrib/static/Joint2D_v2.GIF"
title="Joint2D_v2.GIF" alt="Joint2D_v2.GIF" /></p>
<p>NOTES:</p>
<ol>
<li>The nodes must be located such that the main chords bisect. The node
tags shall be entered in a clockwise or counter-clockwise order.</li>
<li>In the case that the beam-column element is rigidly framed to the
joint, the tag for materials $Mat1 to $Mat4 shall be zero.</li>
<li>The shear panel uniaxial material (with the tag $MatC) shall be
calibrated for shear-equivalent moment versus shear distortion. In the
calibration formulations the shear-equivalent moment is calculated by
multiplying the joint average shear stress to the joint panel
volume.</li>
<li>The element connects the external nodes to the central node via
multi-point constraints, and Joint2D must be used along with either the
Penalty or the Transformation constraint handler.</li>
<li>If the LrgDspTag flag is set to zero the element uses a constant
constraint matrix for small-deformation formulation. In the
large-deformation formulation the constraint matrix is time varying and
it is updated at every converged time step.</li>
<li>Valid inquires to the joint element include:
<ol>
<li>centralNode - The displacement components of the central node</li>
<li>deformation - Interface rotations and the shear panel
deformation</li>
<li>force - Nodal moments and the joint panel shear-equivalent
moment</li>
<li>size - Length of the main chord (element size)</li>
<li>stiffness - Joint element stiffness matrix</li>
<li>defoANDforce - Joint deformation components followed by the nodal
moments</li>
</ol></li>
</ol>
<hr />

## Examples

<ol>
<li>element Joint2D 12 1 2 3 4 112 10 0; # constructs a Joint2D element
with tag 12 that is connected to nodes 1, 2, 3, and 4. The element will
generate a center node with tag 112, and it uses the uniaxial material
object with tag 10 as the shear panel rotational spring. This joint
element does not have rotational springs at external nodes and does not
include large deformations.</li>
<li>element Joint2D 13 5 6 7 8 113 11 0 11 0 10 2; # constructs a
Joint2D element with tag 13 that is connected to nodes 5, 6, 7, and 8.
The element will generate a center node with tag 113, and it uses the
uniaxial material object with tag 11 for nodes 5 and 7, and rigid
connections for nodes 6 and 8 to prevent member end rotations. The shear
panel behavior is modeled with uniaxial material with tag 10. The
generated multipoint constraint matrices will be time varying to cover
large deformations and the nodal positions will be corrected to maintain
the initial joint size.</li>
</ol>
<hr />
<p>REFERENCES:</p>
<p>Arash Altoontash, 2004, "Simulation and damage models for performance
assessment of reinforced concrete beam-column joints", PhD Dissertation,
Stanford University, California, USA. <a
href="http://opensees.berkeley.edu/OpenSees/doc/Altoontash_Dissertation.pdf">1</a></p>
<hr />
<p>Code Developed by: <span style="color:blue"> Arash
Altoontash</span></p>
