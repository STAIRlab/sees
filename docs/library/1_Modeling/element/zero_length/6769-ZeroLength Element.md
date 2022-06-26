# ZeroLength

This command is used to construct a zeroLength element object, which
is defined by two nodes at the same location. The nodes are connected by
multiple UniaxialMaterial objects to represent the force-deformation
relationship for the element.

```tcl
element zeroLength $eleTag $iNode $jNode 
        -mat $matTag1 $matTag2 ... -dir $dir1 $dir2 ... 
        < -doRayleigh $rFlag > < -orient $x1 $x2 $x3 $yp1 $yp2 $yp3 >
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
<td><p><code>matTag1 matTag2 ...</code></p></td>
<td><p>tags associated with previously-defined UniaxialMaterials</p></td>
</tr>
<tr class="even">
<td><p><code>dir1 dir2 ...</code></p></td>
<td><p>material directions:</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>`1`, `2`, `3` - translation along local $x$, $y$, $z$ axes, respectively;</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>`4`, `5`, `6` - rotation about local $x$, $y$, $z$ axes, respectively</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">x1 x2 x3</code></p></td>
<td><p>vector components in global coordinates defining local x-axis
(optional)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">yp1 yp2 yp3</code></p></td>
<td><p>vector components in global coordinates defining vector yp which
lies in the local $x$-$y$ plane for the element. (optional)</p></td>
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
<p>If the optional orientation vectors are not specified, the local
  element axes coincide with the global axes. Otherwise the local $z$-axis
  is defined by the cross product between the vectors x and yp vectors
  specified on the command line.</p>
<p>The valid queries to a zero-length element when creating an
  ElementRecorder object are `force`, `deformation`, and 
  `material $i matArg1 matArg2 ...` Where $i is an integer indicating which of the
  materials whose data is to be output (a 1 corresponds to `$matTag1`, a 2
  to `$matTag2`, and so on). 

EXAMPLES:

Truss tag 1 between nodes 2 and 4 acting in directions 1 and 2 with materials 5 and 6
respectively.

```tcl
element zeroLength 1 2 4 -mat 5 6 -dir 1 2;
```

Truss tag 1 between nodes 1 and 2 acting in local direction 1 defined with
material 1. Local direction 1 attains 45 degrees with global $X$ axis:

```tcl
element zeroLength 1 1 2 -mat 1 -dir 1 -orient 1 1 0 -1 1 0; 
```

The same as the example above but also includes the stiffness of
this element in calculation of the damping matrix if Rayleigh command is
invoked later.</p>

```tcl
element zeroLength 1 1 2 -mat 1 -dir 1 -doRayleigh 1 -orient 1 1 0 -1 1 0; 
```

<hr />
<p>Code developed by: <span style="color:blue"> Gregory L. Fenves,
University of Texas, Austin. </span></p>

