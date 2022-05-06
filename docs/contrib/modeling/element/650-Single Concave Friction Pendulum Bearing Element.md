# Single Concave Friction Pendulum Bearing Element

<p>This command is used to construct a singleFPBearing element object,
which is defined by two nodes. The iNode represents the concave sliding
surface and the jNode represents the articulated slider. The element can
have zero length or the appropriate bearing height. The bearing has
unidirectional (2D) or coupled (3D) friction properties (with post-yield
stiffening due to the concave sliding surface) for the shear
deformations, and force-deformation behaviors defined by
UniaxialMaterials in the remaining two (2D) or four (3D) directions. To
capture the uplift behavior of the bearing, the user-specified
UniaxialMaterial in the axial direction is modified for no-tension
behavior. P-Delta moments are entirely transferred to the concave
sliding surface (iNode). It is important to note that rotations of the
concave sliding surface (rotations at the iNode) affect the shear
behavior of the bearing. If the element has non-zero length, the local
x-axis is determined from the nodal geometry unless the optional x-axis
vector is specified in which case the nodal geometry is ignored and the
user-defined orientation is utilized.</p>
<p>For a two-dimensional problem:</p>

```tcl
element singleFPBearing $eleTag $iNode $jNode $frnMdlTag
        $R $h $uy -P $matTag -Mz $matTag &lt;-orient $x1 $x2 $x3 $y1 $y2 $y3&gt;
        &lt;-mass $m&gt; &lt;-iter $maxIter $tol&gt;
```

<p>For a three-dimensional problem:</p>

```tcl
element singleFPBearing $eleTag $iNode $jNode $frnMdlTag
        $R $h $uy -P $matTag -T $matTag -My $matTag -Mz $matTag &lt;-orient
        &lt;$x1 $x2 $x3&gt; $y1 $y2 $y3&gt; &lt;-mass $m&gt; &lt;-iter $maxIter
        $tol&gt;
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
<td><code class="parameter-table-variable">frnMdlTag</code></td>
<td><p>tag associated with previously-defined FrictionModel</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">R</code></td>
<td><p>radius of concave sliding surface</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">h</code></td>
<td><p>height of articulated slider</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">uy</code></td>
<td><p>yield displacement</p></td>
</tr>
<tr class="odd">
<td><p><strong>-P $matTag</strong></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial in axial
direction</p></td>
</tr>
<tr class="even">
<td><p><strong>-T $matTag</strong></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial in
torsional direction</p></td>
</tr>
<tr class="odd">
<td><p><strong>-My $matTag</strong></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial in moment
direction around local y-axis</p></td>
</tr>
<tr class="even">
<td><p><strong>-Mz $matTag</strong></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial in moment
direction around local z-axis</p></td>
</tr>
<tr class="odd">
<td><p><strong>$x1 $x2 $x3</strong></p></td>
<td><p>vector components in global coordinates defining local x-axis
(optional)</p></td>
</tr>
<tr class="even">
<td><p><strong>$y1 $y2 $y3</strong></p></td>
<td><p>vector components in global coordinates defining local y-axis
(optional)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">m</code></td>
<td><p>element mass (optional, default = 0.0)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">maxIter</code></td>
<td><p>maximum number of iterations to undertake to satisfy element
equilibrium (optional, default = 20)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">tol</code></td>
<td><p>convergence tolerance to satisfy element equilibrium (optional,
default = 1E-8)</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<p>If the element has zero length and optional orientation vectors are
not specified, the local element axes coincide with the global axes.
Otherwise the local z-axis is defined by the cross product between the
x- and y-vectors specified on the command line.</p>
<p>The valid queries to a single concave friction pendulum bearing
element when creating an ElementRecorder object are 'force,'
'localForce,' 'basicForce,' 'localDisplacement,' 'basicDisplacement' and
'material $matNum matArg1 matArg2 ...' Where $matNum is the number
associated with the material whose data is to be output.</p>
<p>EXAMPLES:</p>
<p>element singleFPBearing 1 1 2 1 37.28 2.60 0.01 -P 1 -Mz 2 -orient 0
1 0 -1 0 0; # for a 2D single concave friction pendulum bearing</p>
<p>element singleFPBearing 1 1 2 1 37.28 2.60 0.01 -P 1 -T 2 -My 3 -Mz 4
-orient 0 0 1 -1 0 0; # for a 3D single concave friction pendulum
bearing</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Andreas
Schellenberg, University of California, Berkeley. </span></p>
