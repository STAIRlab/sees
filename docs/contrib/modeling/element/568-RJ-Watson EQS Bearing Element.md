# RJ-Watson EQS Bearing Element

<p>This command is used to construct a RJWatsonEqsBearing element
object, which is defined by two nodes. The iNode represents the masonry
plate and the jNode represents the sliding surface plate. The element
can have zero length or the appropriate bearing height. The bearing has
unidirectional (2D) or coupled (3D) friction properties (with post-yield
stiffening due to the mass-energy-regulator (MER) springs) for the shear
deformations, and force-deformation behaviors defined by
UniaxialMaterials in the remaining two (2D) or four (3D) directions. To
capture the uplift behavior of the bearing, the user-specified
UniaxialMaterial in the axial direction is modified for no-tension
behavior. By default (sDratio = 1.0) P-Delta moments are entirely
transferred to the sliding surface (jNode). It is important to note that
rotations of the sliding surface (rotations at the jNode) affect the
shear behavior of the bearing. To avoid the introduction of artificial
viscous damping in the isolation system (sometimes referred to as
"damping leakage in the isolation system"), the bearing element does not
contribute to the Rayleigh damping by default. If the element has
non-zero length, the local x-axis is determined from the nodal geometry
unless the optional x-axis vector is specified in which case the nodal
geometry is ignored and the user-defined orientation is utilized.</p>
<p>For a two-dimensional problem:</p>

```tcl
element RJWatsonEqsBearing $eleTag $iNode $jNode
        $frnMdlTag $kInit -P $matTag -Vy $matTag -Mz $matTag &lt;-orient $x1 $x2
        $x3 $y1 $y2 $y3&gt; &lt;-shearDist $sDratio&gt; &lt;-doRayleigh&gt;
        &lt;-mass $m&gt; &lt;-iter $maxIter $tol&gt;
```

<p>For a three-dimensional problem:</p>

```tcl
element RJWatsonEqsBearing $eleTag $iNode $jNode
        $frnMdlTag $kInit -P $matTag -Vy $matTag -Vz $matTag -T $matTag -My
        $matTag -Mz $matTag &lt;-orient &lt;$x1 $x2 $x3&gt; $y1 $y2 $y3&gt;
        &lt;-shearDist $sDratio&gt; &lt;-doRayleigh&gt; &lt;-mass $m&gt;
        &lt;-iter $maxIter $tol&gt;
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
<td><p>tag associated with previously-defined <a
href="http://opensees.berkeley.edu/wiki/index.php/FrictionModel_Command">FrictionModel</a></p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">kInit</code></td>
<td><p>initial stiffness of sliding friction component in local shear
direction</p></td>
</tr>
<tr class="odd">
<td><p><strong>-P $matTag</strong></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial in axial
direction</p></td>
</tr>
<tr class="even">
<td><p><strong>-Vy $matTag</strong></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial in shear
direction along local y-axis (MER spring behavior not including
friction)</p></td>
</tr>
<tr class="odd">
<td><p><strong>-Vz $matTag</strong></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial in shear
direction along local z-axis (MER spring behavior not including
friction)</p></td>
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
<td><code class="parameter-table-variable">sDratio</code></td>
<td><p>shear distance from iNode as a fraction of the element length
(optional, default = 0.0)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-flag">-doRayleigh</code></p></td>
<td><p>to include Rayleigh damping from the bearing (optional, default =
no Rayleigh damping contribution)</p></td>
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
<figure>
<img src="/OpenSeesRT/contrib/static/RJWatsonEQSBearingFig01.png"
title="RJWatsonEQSBearingFig01.png" width="600"
alt="RJWatsonEQSBearingFig01.png" />
<figcaption aria-hidden="true">RJWatsonEQSBearingFig01.png</figcaption>
</figure>
<hr />
<p>NOTE:</p>
<p>1) If the element has zero length and optional orientation vectors
are not specified, the local element axes coincide with the global axes.
Otherwise the local z-axis is defined by the cross product between the
x- and y-vectors specified on the command line.</p>
<p>2) Because the friction force is affected by both the axial force and
the slip rate, the element can be sensitive numerically. It is
recommended that for dynamic analysis a smaller time step is being used
than what would be used for a comparable structure with no
isolators.</p>
<p>3) If there is uplift (and therefore impact) in the bearing element,
it can be helpful to use an integration method that provides numerical
damping. Providing some viscous damping for the material that is
assigned to the axial direction can also be helpful in dissipating
impact energy.</p>
<p>4) The valid queries to a RJ-Watson EQS bearing element when creating
an ElementRecorder object are 'force,' 'localForce,' 'basicForce,'
'localDisplacement,' 'basicDisplacement' and 'material $matNum matArg1
matArg2 ...' Where $matNum is the number associated with the material
whose data is to be output.</p>
<hr />

## Examples

<p>For a 2D RJ-Watson EQS bearing: element RJWatsonEqsBearing 1 1 2 1
250.0 -P 1 -Vy 2 -Mz 3 -orient 0 1 0 -1 0 0;</p>
<ul>
<li><a href="TestFPS2d_0.tcl" title="wikilink">TestFPS2d_0.tcl</a>
models a rigid isolated mass and the bearing element has zero length. It
also tests the different friction models.</li>
<li><a href="TestFPS2d_1.tcl" title="wikilink">TestFPS2d_1.tcl</a>
models a rigid isolated mass and the bearing element has finite
length.</li>
<li><a href="TestFPS2d_2.tcl" title="wikilink">TestFPS2d_2.tcl</a>
models an isolated one story stick and the bearing element has finite
length.</li>
<li><a href="TestFPS2d_3.tcl" title="wikilink">TestFPS2d_3.tcl</a>
models an isolated one story one bay building and the bearing element
has finite length.</li>
<li><a href="TestFPS2d_4.tcl" title="wikilink">TestFPS2d_4.tcl</a>
models an isolated five story one bay building and the bearing element
has finite length.</li>
</ul>
<p>For a 3D RJ-Watson EQS bearing: element RJWatsonEqsBearing 1 1 2 1
250.0 -P 1 -Vy 2 -Vz 2 -T 3 -My 4 -Mz 4 -orient 0 0 1 -1 0 0;</p>
<ul>
<li><a href="TestFPS3d_0.tcl" title="wikilink">TestFPS3d_0.tcl</a>
models a rigid isolated mass and the bearing element has zero length. It
also tests the different friction models.</li>
<li><a href="TestFPS3d_1.tcl" title="wikilink">TestFPS3d_1.tcl</a>
models a rigid isolated mass and the bearing element has finite
length.</li>
<li><a href="TestFPS3d_2.tcl" title="wikilink">TestFPS3d_2.tcl</a>
models an isolated one story stick and the bearing element has finite
length.</li>
<li><a href="TestFPS3d_3.tcl" title="wikilink">TestFPS3d_3.tcl</a>
models an isolated one story one bay building and the bearing element
has finite length.</li>
<li><a href="TestFPS3d_4.tcl" title="wikilink">TestFPS3d_4.tcl</a>
models an isolated five story one bay building and the bearing element
has finite length.</li>
</ul>
<p>Download the <a href="Media:GroundMotions.zip"
title="wikilink">GroundMotions.zip</a> as a compressed file or download
<a href="Media:AllFPSExamples.zip"
title="wikilink">AllFPSExamples.zip</a> as a compressed file.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Andreas
Schellenberg, University of California, Berkeley. </span></p>
