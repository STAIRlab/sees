# ShellNL

This command is used to construct a ShellNL element object, a
lagrangian nine-noded shell element.

```tcl
element ShellNL $eleTag $node1 $node2 ... $node9 $secTag
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><code>node1 ... node9</code></p></td>
<td><p>nine nodes defining element boundaries, input is the typical,
firstly four corner nodes counter-clockwise, then mid-side nodes
counter-clockwise and finally the central node.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">secTag</code></td>
<td><p>tag associated with previously-defined SectionForceDeformation
object. Currently must be either a PlateFiberSection, or
ElasticMembranePlateSection</p></td>
</tr>
</tbody>
</table>
<hr />

<p>NOTE:</p>

The valid queries to a Quad element when creating an `ElementRecorder`
are 'forces', 'stresses,' and 

  'material $matNum matArg1 matArg2 ...' 

Where $matNum refers to the material object at the integration
point corresponding to the node numbers in the isoparametric
domain.

<hr />

## Examples

```tcl
set t 10.0 
model basic -ndm 3 -ndf 6 
nDMaterial ElasticIsotropic 1 200000 0.3 
nDMaterial PlateFiber 2 1 
section PlateFiber 3 2 $t 
element ShellNL 1 1 27 29 3 14 28 16 2 15 3
```

## References
<p>Zienkiewicz o.c., Taylor r.l. vol. 2. The finite element method.
Solid mechanics. Elsevier 2000</p>

<hr />
<p>Code Developed by: <span style="color:blue"> Leopoldo Tesser,
Diego A. Talledo</span></p>
