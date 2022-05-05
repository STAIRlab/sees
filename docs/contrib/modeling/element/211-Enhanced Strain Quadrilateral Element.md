# Enhanced Strain Quadrilateral Element

<p>This command is used to construct a four-node quadrilateral element,
which uses a bilinear isoparametric formulation with enhanced strain
modes.</p>

```tcl
element enhancedQuad $eleTag $iNode $jNode $kNode $lNode
        $thick $type $matTag
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
<td><p>string representing material behavior. Valid options depend on
the NDMaterial object and its available material formulations. The type
parameter can be either "PlaneStrain" or "PlaneStress."</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>tag of nDMaterial</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<ol>
<li>The valid queries to a Quad element when creating an ElementRecorder
object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2
...' Where $matNum refers to the material object at the integration
point corresponding to the node numbers in the isoparametric
domain.</li>
</ol>
<p>EXAMPLE:</p>
<p>REFERENCES:</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Edward Love,
Sandia National Laboratories </span></p>
