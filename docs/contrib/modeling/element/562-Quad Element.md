# Quad Element

<p>This command is used to construct a FourNodeQuad element object which
uses a bilinear isoparametric formulation.</p>

```tcl
element quad $eleTag $iNode $jNode $kNode $lNode $thick
        $type $matTag &lt;$pressure $rho $b1 $b2&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode $kNode $lNode</strong></p></td>
<td><p>four nodes defining element boundaries, input in
counter-clockwise order around the element.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">thick</code></td>
<td><p>element thickness</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">type</code></td>
<td><p>string representing material behavior. The type parameter can be
either "PlaneStrain" or "PlaneStress."</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>tag of nDMaterial</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">pressure</code></td>
<td><p>surface pressure (optional, default = 0.0)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>element mass density (per unit volume) from which a lumped
element mass matrix is computed (optional, default=0.0)</p></td>
</tr>
<tr class="even">
<td><p><strong>$b1 $b2</strong></p></td>
<td><p>constant body forces defined in the isoparametric domain
(optional, default=0.0)</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<ol>
<li>Consistent nodal loads are computed from the pressure and body
forces.</li>
<li>The valid queries to a Quad element when creating an ElementRecorder
object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2
...' Where $matNum refers to the material object at the integration
point corresponding to the node numbers in the isoparametric
domain.</li>
</ol>

## Examples

<hr />
<p>Code Developed by: <span style="color:blue"> Micheal Scott,
Oregon State </span></p>
