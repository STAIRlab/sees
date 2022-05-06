# CoupledZeroLength Element

<p>This command is used to construct a CoupledZeroLength element object,
which is defined by two nodes at the same location. The nodes are
connected a single UniaxialMaterial element to represent the
force-deformation relationship for the element in a 2d plane. Unlike a
ZeroLength element which can only provide a rectangular force
interaction surface in a 2d plane, this element provides a circular
force interaction surface.</p>

```tcl
element CoupledZeroLength $eleTag $iNode $jNode $dirn1
        $dirn2 $matTag &lt;$rFlag&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode</strong></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>tags associated with previously-defined UniaxialMaterial</p></td>
</tr>
<tr class="even">
<td><p><strong>$dir1 $dir2</strong></p></td>
<td><p>the two directions, 1 through ndof.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rFlag</code></td>
<td><p>optional, default = 0</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>rFlag = 0 NO RAYLEIGH DAMPING (default)</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>rFlag = 1 include rayleigh damping</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<p>The valid queries to a zero-length element when creating an
ElementRecorder object are 'force,' and 'material matArg1 matArg2
...'</p>

## Examples

<p>element CoupledZeroLength 1 2 4 5 6 7; # truss tag 1 between nodes 2
and 4 acting in directions 5 and 6 with material 7.</p>
<hr />

## Theory

<p>if change in element end displacements for 2 dof of interest are d1
and d2:</p>
<p>the deformation (strain in uniaxial material) of the material is set
to be:</p>
<p>&lt;math&gt;\epsilon = sqrt( \delta 1^2 + \delta
2^2)&lt;/math&gt;</p>
<p>and if resulting force (stress from uniaxial material) is Sigma then
the force computed for the two directions 1 and 2 are:</p>
<p>&lt;math&gt; F_1 = (\Sigma * \delta 1) / \epsilon &lt;/math&gt;
&lt;math&gt; F_2 = (\Sigma * \delta 2) / \epsilon &lt;/math&gt;</p>
<p>NOTE: in case where $\epsilon = 0.0$, the
forces are computed using $\Sigma$ and the last
committed set of displacements that were not zero.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
