# FourNodeQuad u-p Element

<p>This command is used to construct an eFourNodeQuadUP element object.
A FourNodeQuadUP element is a four-node plane-strain element using
bilinear isoparametric formulation. This element is implemented for
simulating dynamic response of solid-fluid fully coupled material, based
on Biot's theory of porous medium. Each element node has 3
degrees-of-freedom (DOF): DOF 1 and 2 for solid displacement (u) and DOF
3 for fluid pressure (p). The arguments for the construction of this
element are:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element quadUP $eleTag $Node1 $Node2 $Node3 $Node4 $thick
$matTag $bulk $fmass $PermX $PermY &lt;$b1=0 $b2=0
$t=0&gt;</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$Node1 .. $Node4</strong></p></td>
<td><p>Four element node (previously defined) numbers in
counter-clockwise order around the element</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">thick</code></td>
<td><p>Element thickness</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>Tag of an NDMaterial object (previously defined) of which the
element is composed</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">bulk</code></td>
<td><p>Combined undrained bulk modulus Bc relating changes in pore
pressure and volumetric strain, may be approximated by: where Bf is the
bulk modulus of fluid phase (2.2x106 kPa for water), and n the initial
porosity.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fmass</code></td>
<td><p>Fluid mass density</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">PermX</code></td>
<td><p>Permeability coefficient in X direction</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">PermY</code></td>
<td><p>Permeability coefficient in Y direction</p></td>
</tr>
<tr class="odd">
<td><p><strong>$bX, $bY</strong></p></td>
<td><p>Optional gravity acceleration components in X and Y directions
respectively (defaults are 0.0)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">t</code></td>
<td><p>Optional uniform element normal traction, positive in tension
(default is 0.0)</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<ol>
<li>This element requires 3 degrees-of-freedom (ndf=3), the 3rd
degree-of-freedom being pore pressure. The Pore pressure can be recorded
at an element node using OpenSees Node Recorder:</li>
</ol>
<p>recorder Node &lt;-file $fileName&gt; &lt;-time&gt; &lt;-node ($nod1
$nod2 …)&gt; -dof 3 vel</p>
<ol>
<li>The valid queries to a quadUP element when creating an
ElementRecorder are 'force', and 'material matNum matArg1 matArg2 ...',
where matNum represents the material object at the corresponding
integration point.</li>
<li>TYPICAL RANGE OF PERMEABILITY COEFFICIENT (cm/s)</li>
</ol>
<table>
<tbody>
<tr class="odd">
<td><p>Gravel</p></td>
<td><p>Sand</p></td>
<td><p>Silty Sand</p></td>
<td><p>Silt</p></td>
<td><p>Clay</p></td>
</tr>
<tr class="even">
<td><p>&gt;1.0x10-1</p></td>
<td><p>1.0x10-3 ~ 1.0x10-1</p></td>
<td><p>1.0x10-5 ~ 1.0x10-3</p></td>
<td><p>1.0x10-7 ~ 1.0x10-5</p></td>
<td><p>&lt;1.0x10-7</p></td>
</tr>
</tbody>
</table>

## Examples

<p>Please visit <a
href="http://cyclic.ucsd.edu/opensees">http://cyclic.ucsd.edu/opensees</a>
for examples.</p>
<p>REFERENCES:</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Zhaohui Yang, UC
San Diego</span></p>
