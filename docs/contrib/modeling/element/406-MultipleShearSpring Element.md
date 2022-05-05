# MultipleShearSpring Element

<p>This command is used to construct a multipleShearSpring (MSS) element
object, which is defined by two nodes. This element consists of a series
of identical shear springs arranged radially to represent the isotropic
behavior in the local y-z plane.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element multipleShearSpring $eleTag $iNode $jNode
$nSpring -mat $matTag &lt;-lim $dsp&gt; &lt;-orient &lt;$x1 $x2 $x3&gt;
$yp1 $yp2 $yp3&gt; &lt;-mass $m&gt;</strong></p></td>
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
<td><p><strong>$inode $jnode</strong></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><p><strong>$nSpring</strong></p></td>
<td><p>number of springs</p></td>
</tr>
<tr class="even">
<td><p><strong>$matTag</strong></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial
object</p></td>
</tr>
<tr class="odd">
<td><p><strong>$dsp</strong></p></td>
<td><p>minimum deformation to calculate equivalent coefficient (see note
1)</p></td>
</tr>
<tr class="even">
<td><p><strong>$x1 $x2 $x3</strong></p></td>
<td><p>vector components in global coordinates defining local
x-axis</p></td>
</tr>
<tr class="odd">
<td><p><strong>$yp1 $yp2 $yp3</strong></p></td>
<td><p>vector components in global coordinates defining vector yp which
lies in the local x-y plane for the element</p></td>
</tr>
<tr class="even">
<td><p><strong>$m</strong></p></td>
<td><p>element mass</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<p>1) If <strong>$dsp</strong> is positive and the shear deformation of
MSS exceeds <strong>$dsp</strong>, this element calculates equivalent
coefficient to adjust force and stiffness of MSS. The adjusted MSS force
and stiffness reproduce the behavior of the previously defined uniaxial
material under monotonic loading in every direction. If
<strong>$dsp</strong> is zero, the element does not calculate the
equivalent coefficient.</p>
<p>2) The valid queries to a multipleShearSpring element when creating
an ElementRecorder object are 'globalForce', 'localForce', 'basicForce',
'localDisplacement' and 'basicDeformation'.</p>
<figure>
<img src="MultipleShearSpring_Model.png"
title="MultipleShearSpring_Model.png" width="300"
alt="MultipleShearSpring_Model.png" />
<figcaption
aria-hidden="true">MultipleShearSpring_Model.png</figcaption>
</figure>
<hr />
<p>EXAMPLE:</p>
<p>element multipleShearSpring 1 1 2 16 -mat 1</p>
<p><a href="Media:MultipleShearSpring_Sample.tcl"
title="wikilink">MultipleShearSpring_Sample.tcl</a>, <a
href="Media:MultipleShearSpring_input_X.tcl"
title="wikilink">MultipleShearSpring_input_X.tcl</a>, <a
href="Media:MultipleShearSpring_input_Y.tcl"
title="wikilink">MultipleShearSpring_input_Y.tcl</a></p>
<p><img src="MultipleShearSpring_ForceDeformation_1y.png"
title="MultipleShearSpring_ForceDeformation_1y.png" width="250"
alt="MultipleShearSpring_ForceDeformation_1y.png" />
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; <img
src="MultipleShearSpring_path.png" title="MultipleShearSpring_path.png"
width="250" alt="MultipleShearSpring_path.png" /></p>
<p><img src="MultipleShearSpring_ForceDeformation_2y.png"
title="MultipleShearSpring_ForceDeformation_2y.png" width="250"
alt="MultipleShearSpring_ForceDeformation_2y.png" />
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; <img
src="MultipleShearSpring_ForceDeformation_2z.png"
title="MultipleShearSpring_ForceDeformation_2z.png" width="250"
alt="MultipleShearSpring_ForceDeformation_2z.png" /></p>
<p>REFERENCES:</p>
<p>Wada. A. and Hirose K. , "Building Frames Subjected to 2D Earthquake
Motion", <em>Seismic Engineering: Research and Practice, American
Society of Civil Engineers</em>, 388-397, 1989.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> mkiku
</span></p>
