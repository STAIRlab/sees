# MultipleShearSpring Element

<p>This command is used to construct a multipleShearSpring (MSS) element
object, which is defined by two nodes. This element consists of a series
of identical shear springs arranged radially to represent the isotropic
behavior in the local y-z plane.</p>

```tcl
element multipleShearSpring $eleTag $iNode $jNode
        $nSpring -mat $matTag &lt;-lim $dsp&gt; &lt;-orient &lt;$x1 $x2 $x3&gt;
        $yp1 $yp2 $yp3&gt; &lt;-mass $m&gt;
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$inode $jnode</strong></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">nSpring</code></td>
<td><p>number of springs</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>tag associated with previously-defined UniaxialMaterial
object</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">dsp</code></td>
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
<td><code class="parameter-table-variable">m</code></td>
<td><p>element mass</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<p>1) If <code class="tcl-variable">dsp</code> is positive and the shear deformation of
MSS exceeds <code class="tcl-variable">dsp</code>, this element calculates equivalent
coefficient to adjust force and stiffness of MSS. The adjusted MSS force
and stiffness reproduce the behavior of the previously defined uniaxial
material under monotonic loading in every direction. If
<code class="tcl-variable">dsp</code> is zero, the element does not calculate the
equivalent coefficient.</p>
<p>2) The valid queries to a multipleShearSpring element when creating
an ElementRecorder object are 'globalForce', 'localForce', 'basicForce',
'localDisplacement' and 'basicDeformation'.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/MultipleShearSpring_Model.png"
title="MultipleShearSpring_Model.png" width="300"
alt="MultipleShearSpring_Model.png" />
<figcaption
aria-hidden="true">MultipleShearSpring_Model.png</figcaption>
</figure>
<hr />

## Examples

<p>element multipleShearSpring 1 1 2 16 -mat 1</p>
<p><a href="Media:MultipleShearSpring_Sample.tcl"
title="wikilink">MultipleShearSpring_Sample.tcl</a>, <a
href="Media:MultipleShearSpring_input_X.tcl"
title="wikilink">MultipleShearSpring_input_X.tcl</a>, <a
href="Media:MultipleShearSpring_input_Y.tcl"
title="wikilink">MultipleShearSpring_input_Y.tcl</a></p>
<p><img src="/OpenSeesRT/contrib/static/MultipleShearSpring_ForceDeformation_1y.png"
title="MultipleShearSpring_ForceDeformation_1y.png" width="250"
alt="MultipleShearSpring_ForceDeformation_1y.png" />
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; <img
src="MultipleShearSpring_path.png" title="MultipleShearSpring_path.png"
width="250" alt="MultipleShearSpring_path.png" /></p>
<p><img src="/OpenSeesRT/contrib/static/MultipleShearSpring_ForceDeformation_2y.png"
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
