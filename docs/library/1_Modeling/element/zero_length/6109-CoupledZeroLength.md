# CoupledZeroLength

<p>This command is used to construct a CoupledZeroLength element object,
which is defined by two nodes at the same location. The nodes are
connected a single UniaxialMaterial element to represent the
force-deformation relationship for the element in a 2d plane. Unlike a
ZeroLength element which can only provide a rectangular force
interaction surface in a 2d plane, this element provides a circular
force interaction surface.</p>

```tcl
element CoupledZeroLength $eleTag $iNode $jNode $dirn1
        $dirn2 $matTag < $rFlag >
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">iNode jNode</code></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>tags associated with previously-defined UniaxialMaterial</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">dir1 dir2</code></p></td>
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

truss tag 1 between nodes 2 and 4 acting in directions 5 and 6 with material 7:
```tcl
element CoupledZeroLength 1 2 4 5 6 7; 
```

<hr />

## Theory

If change in element end displacements for 2 dof of interest are d1
and d2:

<p>the deformation (strain in uniaxial material) of the material is set
to be:</p>

$$\epsilon = sqrt( \delta_1^2 + \delta_2^2)$$

and if resulting force (stress from uniaxial material) is Sigma then
the force computed for the two directions 1 and 2 are:</p>
$$F_1 = (\Sigma * \delta 1) / \epsilon$$

$$F_2 = (\Sigma * \delta 2) / \epsilon$$

>NOTE: in case where $\epsilon = 0.0$, the
>forces are computed using $\Sigma$ and the last
>committed set of displacements that were not zero.

<hr />
<p>Code developed by: <span style="color:blue"> fmk
</span></p>

