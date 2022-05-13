# Bbar Plane Strain Quadrilateral

<p>This command is used to construct a four-node quadrilateral element
object, which uses a bilinear isoparametric formulation along with a
mixed volume/pressure B-bar assumption. This element is for plane strain
problems only.</p>

```tcl
element bbarQuad $eleTag $iNode $jNode $kNode $lNode
        $thick $matTag
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">iNode jNode kNode lNode</code></p></td>
<td><p>four nodes defining element boundaries, input in
counter-clockwise order around the element.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">thick</code></td>
<td><p>element thickness</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>tag of nDMaterial</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<ol>
<li>PlainStrain only.</li>
<li>The valid queries to a Quad element when creating an ElementRecorder
object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2
...' Where $matNum refers to the material object at the integration
point corresponding to the node numbers in the isoparametric
domain.</li>
</ol>

## Examples

<hr />
<p>Code Developed by: <span style="color:blue"> Edward Love,
Sandia National Laboratories </span></p>
