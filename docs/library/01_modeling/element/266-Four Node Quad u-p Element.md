# Four Node Quad u-p Element

<p><strong>FourNodeQuadUP</strong> is a four-node plane-strain element
using bilinear isoparametric formulation. This element is implemented
for simulating dynamic response of solid-fluid fully coupled material,
based on Biot's theory of porous medium. Each element node has 3
degrees-of-freedom (DOF): DOF 1 and 2 for solid displacement (u) and DOF
3 for fluid pressure (p).</p>
<p><strong>Please</strong> <a
href="PressureDependMultiYield-quadUP_element" title="wikilink"> click
here</a> <strong>for examples.</strong></p>
<p>OUTPUT INTERFACE: Pore pressure can be recorded at an element node
using OpenSees Node Recorder:</p>
<p><strong>recorder Node &lt;-file $fileName&gt; &lt;-time&gt; &lt;-node
($nod1 $nod2 …)&gt; -dof 3 vel</strong></p>
<p>See OpenSees command manual (McKenna and Fenves 2001) for nodal
displacement, velocity, or acceleration recorders.</p>
<p>The valid queries to a quadUP element when creating an
ElementRecorder are 'force', 'stiffness', or 'material matNum matArg1
matArg2 ...', where matNum represents the material object at the
corresponding integration point.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element quadUP $eleTag $iNode $jNode $kNode $lNode $thick
$matTag $bulk $fmass $hPerm $vPerm &lt;$b1=0 $b2=0
$t=0&gt;</strong></p></td>
</tr>
</tbody>
</table>
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>A positive integer uniquely identifying the element among all
elements</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode, $jNode, $kNode, $lNode</strong></p></td>
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
<td><p>Combined undrained bulk modulus B&lt;sub&gt;c&lt;/sub&gt;
relating changes in pore pressure and volumetric strain, may be
approximated by:</p>
<p>B&lt;sub&gt;c&lt;/sub&gt; &amp;asymp; B&lt;sub&gt;f&lt;/sub&gt;/n</p>
<p>where B&lt;sub&gt;f&lt;/sub&gt; is the bulk modulus of fluid phase
(2.2x10&lt;sup&gt;6&lt;/sup&gt; kPa (or 3.191x10&lt;sup&gt;5&lt;/sup&gt;
psi) for water), and n the initial porosity.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fmass</code></td>
<td><p>Fluid mass density</p></td>
</tr>
<tr class="odd">
<td><p><strong>$hPerm, $vPerm</strong></p></td>
<td><p>Permeability coefficient in horizontal and vertical directions
respectively.</p></td>
</tr>
<tr class="even">
<td><p><strong>$b1, $b2</strong></p></td>
<td><p>Optional gravity acceleration components in horizontal and
vertical directions respectively (defaults are 0.0)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">t</code></td>
<td><p>Optional uniform element normal traction, positive in tension
(default is 0.0)</p></td>
</tr>
</tbody>
</table>
<p>TYPICAL RANGE OF PERMEABILITY COEFFICIENT</p>
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
<td><p>&gt;1.0x10&lt;sup&gt;-1&lt;/sup&gt; cm/s (or
3.94x10&lt;sup&gt;-2&lt;/sup&gt; in/s)</p></td>
<td><p>1.0x10&lt;sup&gt;-3&lt;/sup&gt; cm/s (or 3.94
x10&lt;sup&gt;-4&lt;/sup&gt; in/s) ~ 1.0x10&lt;sup&gt;-1&lt;/sup&gt;
cm/s (or 3.94 x10&lt;sup&gt;-2&lt;/sup&gt; in/s)</p></td>
<td><p>1.0x10&lt;sup&gt;-5&lt;/sup&gt; cm/s (or 3.94
x10&lt;sup&gt;-6&lt;/sup&gt; in/s) ~ 1.0x10&lt;sup&gt;-3&lt;/sup&gt;
cm/s (or 3.94 x10&lt;sup&gt;-4&lt;/sup&gt; in/s)</p></td>
<td><p>1.0x10&lt;sup&gt;-7&lt;/sup&gt; cm/s (or 3.94
x10&lt;sup&gt;-8&lt;/sup&gt; in/s) ~ 1.0x10&lt;sup&gt;-5&lt;/sup&gt;
cm/s (or 3.94 x10&lt;sup&gt;-6&lt;/sup&gt; in/s)</p></td>
<td><p>&lt;1.0x10&lt;sup&gt;-7&lt;/sup&gt; cm/s (or 3.94x10
&lt;sup&gt;-8&lt;/sup&gt; in/s)</p></td>
</tr>
</tbody>
</table>
<p>Code Developed by: <span style="color:blue"> UC San Diego (Dr.
Zhaohui Yang)</span>:</p>
<hr />
<p>UC San Diego Soil Model: </p>
