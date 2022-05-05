# ZeroLength Element

<p>This command is used to construct a zeroLength element object, which
is defined by two nodes at the same location. The nodes are connected by
multiple UniaxialMaterial objects to represent the force-deformation
relationship for the element.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element zeroLength $eleTag $iNode $jNode -mat $matTag1
$matTag2 ... -dir $dir1 $dir2 ...&lt;-doRayleigh $rFlag&gt; &lt;-orient
$x1 $x2 $x3 $yp1 $yp2 $yp3&gt;</strong></p></td>
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
<td><p><strong>$matTag1 $matTag2 ...</strong></p></td>
<td><p>tags associated with previously-defined
UniaxialMaterials</p></td>
</tr>
<tr class="even">
<td><p><strong>$dir1 $dir2 ...</strong></p></td>
<td><p>material directions:</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>1,2,3 - translation along local x,y,z axes,
respectively;</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>4,5,6 - rotation about local x,y,z axes, respectively</p></td>
</tr>
<tr class="odd">
<td><p><strong>$x1 $x2 $x3</strong></p></td>
<td><p>vector components in global coordinates defining local x-axis
(optional)</p></td>
</tr>
<tr class="even">
<td><p><strong>$yp1 $yp2 $yp3</strong></p></td>
<td><p>vector components in global coordinates defining vector yp which
lies in the local x-y plane for the element. (optional)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$rFlag</strong></p></td>
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
element axes coincide with the global axes. Otherwise the local z-axis
is defined by the cross product between the vectors x and yp vectors
specified on the command line.</p>
<p>The valid queries to a zero-length element when creating an
ElementRecorder object are 'force,' 'deformation,' and 'material $i
matArg1 matArg2 ...' Where $i is an integer indicating which of the
materials whose data is to be output (a 1 corresponds to $matTag1, a 2
to $matTag2, and so on). EXAMPLE:</p>
<p>element zeroLength 1 2 4 -mat 5 6 -dir 1 2; # truss tag 1 between
nodes 2 and 4 acting in directions 1 and 2 with materials 5 and 6
respectively.</p>
<p>element zeroLength 1 1 2 -mat 1 -dir 1 -orient 1 1 0 -1 1 0; # truss
tag 1 between nodes 1 and 2 acting in local direction 1 defined with
material 1. Local direction 1 attains 45 degrees with global X axis</p>
<p>element zeroLength 1 1 2 -mat 1 -dir 1 -doRayleigh 1 -orient 1 1 0 -1
1 0; # the same as the example above but also includes the stiffness of
this element in calculation of the damping matrix if Rayleigh command is
invoked later.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Gregory L. Fenves,
University of Texas, Austin. </span></p>
