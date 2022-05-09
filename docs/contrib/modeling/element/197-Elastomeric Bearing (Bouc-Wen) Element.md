# Elastomeric Bearing (Bouc-Wen) Element

<p>This command is used to construct an elastomericBearing element
object, which is defined by two nodes. The element can have zero length
or the appropriate bearing height. The bearing has unidirectional (2D)
or coupled (3D) plasticity properties for the shear deformations, and
force-deformation behaviors defined by UniaxialMaterials in the
remaining two (2D) or four (3D) directions. By default (sDratio = 0.5)
P-Delta moments are equally distributed to the two end-nodes. To avoid
the introduction of artificial viscous damping in the isolation system
(sometimes referred to as "damping leakage in the isolation system"),
the bearing element does not contribute to the Rayleigh damping by
default. If the element has non-zero length, the local x-axis is
determined from the nodal geometry unless the optional x-axis vector is
specified in which case the nodal geometry is ignored and the
user-defined orientation is utilized.</p>
<p>For a two-dimensional problem:</p>

```tcl
element elastomericBearingBoucWen $eleTag $iNode $jNode
        $kInit $qd $alpha1 $alpha2 $mu $eta $beta $gamma -P $matTag -Mz $matTag
        &lt;-orient $x1 $x2 $x3 $y1 $y2 $y3&gt; &lt;-shearDist $sDratio&gt;
        &lt;-doRayleigh&gt; &lt;-mass $m&gt;
```

<p>For a three-dimensional problem:</p>

```tcl
element elastomericBearingBoucWen $eleTag $iNode $jNode
        $kInit $qd $alpha1 $alpha2 $mu $eta $beat $gamma -P $matTag -T $matTag
        -My $matTag -Mz $matTag &lt;-orient &lt;$x1 $x2 $x3&gt; $y1 $y2 $y3&gt;
        &lt;-shearDist $sDratio&gt; &lt;-doRayleigh&gt; &lt;-mass
        $m&gt;
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
<td><code class="parameter-table-variable">kInit</code></td>
<td><p>initial elastic stiffness in local shear direction</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">qd</code></td>
<td><p>characteristic strength</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">alpha1</code></p></td>
<td><p>post yield stiffness ratio of linear hardening component</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">alpha2</code></p></td>
<td><p>post yield stiffness ratio of non-linear hardening
component</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">mu</code></td>
<td><p>exponent of non-linear hardening component</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">eta</code></td>
<td><p>yielding exponent (sharpness of hysteresis loop corners) (default
= 1.0)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">beta</code></td>
<td><p>first hysteretic shape parameter (default = 0.5)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">gamma</code></td>
<td><p>second hysteretic shape parameter (default = 0.5)</p></td>
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
<td><p><code class="parameter-table-variable">x1 x2 x3</code></p></td>
<td><p>vector components in global coordinates defining local x-axis
(optional)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">y1 y2 y3</code></p></td>
<td><p>vector components in global coordinates defining local y-axis
(optional)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">sDratio</code></td>
<td><p>shear distance from iNode as a fraction of the element length
(optional, default = 0.5)</p></td>
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
</tbody>
</table>
<p><img src="/OpenSeesRT/contrib/static/ElastomericBearingBoucWenFig01.png"
title="ElastomericBearingBoucWenFig01.png" width="600"
alt="ElastomericBearingBoucWenFig01.png" /> <img
src="ElastomericBearingBoucWenFig02.png"
title="ElastomericBearingBoucWenFig02.png" width="400"
alt="ElastomericBearingBoucWenFig02.png" /></p>
<hr />
<p>NOTE:</p>
<p>1) If the element has zero length and optional orientation vectors
are not specified, the local element axes coincide with the global axes.
Otherwise the local z-axis is defined by the cross product between the
x- and y-vectors specified on the command line.</p>
<p>2) Elastomeric bearings are very stiff in compression, but not rigid.
It is not a good idea to specify an extremely large axial stiffness
(such as 1E10), because it can lead to problems with numerical
sensitivity. Always specify a realistic value for the stiffness of the
material that is assigned along the axial direction. To assign different
compression and tension stiffness the <a
href="http://opensees.berkeley.edu/wiki/index.php/Elastic_Material">Elastic</a>
or <a
href="http://opensees.berkeley.edu/wiki/index.php/ElasticMultiLinear_Material">ElasticMultiLinear</a>
material can be used.</p>
<p>3) The valid queries to an elastomeric bearing element when creating
an ElementRecorder object are 'force,' 'localForce,' 'basicForce,'
'localDisplacement,' 'basicDisplacement' and 'material $matNum matArg1
matArg2 ...' Where $matNum is the number associated with the material
whose data is to be output.</p>
<hr />

## Examples

<p>element elastomericBearingBoucWen 1 1 2 20.0 2.50 0.02 0.0 3.0 1.0
0.5 0.5 -P 1 -Mz 2; # for a 2D elastomeric bearing</p>
<p>element elastomericBearingBoucWen 1 1 2 20 2.50 0.02 0.0 3.0 1.0 0.5
0.5 -P 1 -T 2 -My 3 -Mz 4; # for a 3D elastomeric bearing</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Andreas
Schellenberg, University of California, Berkeley. </span></p>
