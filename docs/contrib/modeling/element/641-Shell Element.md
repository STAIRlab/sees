# ShellMITC4

<p>This command is used to construct a ShellMITC4 element object, which
uses a bilinear isoparametric formulation in combination with a modified
shear interpolation to improve thin-plate bending performance.</p>

```tcl
element ShellMITC4 $eleTag $iNode $jNode $kNode $lNode $secTag
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
<td><code class="parameter-table-variable">secTag</code></td>
<td><p>tag associated with previously-defined SectionForceDeformation
object. Currently must be either a PlateFiberSection, or
ElasticMembranePlateSection</p></td>
</tr>
</tbody>
</table>

<hr />

<p>Notes:</p>
- The valid queries to a Quad element when creating an ElementRecorder
  object are 'forces', 'stresses,' and 

      'material $matNum matArg1 matArg2 ...' 
  Where `$matNum` refers to the material object at the integration
  point corresponding to the node numbers in the isoparametric
  domain.

- This is a 3D element with 6 dofs and CAN NOT be used in 2D
  domain.

<hr />

## Examples

```tcl
set t 100.0 
model basic -ndm 3 -ndf 6 
nDMaterial ElasticIsotropic 1 200000 0.3 
nDMaterial PlateFiber 4 1 
set secArgs "7"
section PlateFiber $secArgs 4 $t 
set EleType ShellMITC4 
block2D $n1 $n2 1 1 $EleType $secArgs {
  1  0.0   0.0   0.0 
  2  0.0    10   0.0 
  3 1000    10   0.0 
  4 1000   0.0   0.0 
}
```

## References
<p>Dvorkin,Bathe, A continuum mechanics based four node shell element
for general nonlinear analysis, Eng.Comput.,1,77-88,1984</p>

<hr />


Original implementation by: <span style="color:blue">Ed "C++" Love</span> 

Reimplementation by: <span style="color:blue">Leopoldo Tesser, Diego A. Talledo, Véronique Le Corvec </span>

