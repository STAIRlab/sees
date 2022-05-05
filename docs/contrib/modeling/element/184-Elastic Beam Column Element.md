# Elastic Beam Column Element

<p>This command is used to construct an elasticBeamColumn element
object. The arguments for the construction of an elastic beam-column
element depend on the dimension of the problem, ndm:</p>
<p>For a two-dimensional problem:</p>

```tcl
element elasticBeamColumn $eleTag $iNode $jNode $A $E $Iz
        $transfTag &lt;-mass $massDens&gt; &lt;-cMass&gt;
```
<p>For a three-dimensional problem:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element elasticBeamColumn $eleTag $iNode $jNode $A $E $G
$J $Iy $Iz $transfTag &lt;-mass $massDens&gt;
&lt;-cMass&gt;</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$eleTag</strong></p></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode</strong></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><p><strong>$A</strong></p></td>
<td><p>cross-sectional area of element</p></td>
</tr>
<tr class="even">
<td><p><strong>$E</strong></p></td>
<td><p>Young's Modulus</p></td>
</tr>
<tr class="odd">
<td><p><strong>$G</strong></p></td>
<td><p>Shear Modulus</p></td>
</tr>
<tr class="even">
<td><p><strong>$J</strong></p></td>
<td><p>torsional moment of inertia of cross section</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Iz</strong></p></td>
<td><p>second moment of area about the local z-axis</p></td>
</tr>
<tr class="even">
<td><p><strong>$Iy</strong></p></td>
<td><p>second moment of area about the local y-axis</p></td>
</tr>
<tr class="odd">
<td><p><strong>$transfTag</strong></p></td>
<td><p>identifier for previously-defined coordinate-transformation
(CrdTransf) object</p></td>
</tr>
<tr class="even">
<td><p><strong>$massDens</strong></p></td>
<td><p>element mass per unit length (optional, default = 0.0)</p></td>
</tr>
<tr class="odd">
<td><p><strong>-cMass</strong></p></td>
<td><p>to form consistent mass matrix (optional, default = lumped mass
matrix)</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<p>The valid queries to an elastic beam-column element when creating an
ElementRecorder object are 'force'.</p>
<p>EXAMPLE:</p>
<p>element elasticBeamColumn 1 2 4 5.5 100.0 1e6 9; # elastic element
tag 1 between nodes 2 and 4 with area 5.5, E 100 and Iz 1e6 which uses
transformation 9</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
