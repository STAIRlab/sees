# BbarBrick u-p Element

<p><strong>bbarBrickUP</strong> is a 8-node mixed volume/pressure
element, which uses a tri-linear isoparametric formulation.</p>
<p>Each node has 4 degrees-of-freedom (DOF): DOFs 1 to 3 for solid
displacement (u) and DOF 4 for fluid pressure (p). This element is
implemented for simulating dynamic response of solid-fluid fully coupled
material, based on Biot's theory of porous medium.</p>
<p><strong>Please</strong> <a
href="http://quakesim.net/index.php?title=Examples">click here</a>
<strong>for examples.</strong></p>
<p>OUTPUT INTERFACE:</p>
<p>Pore pressure can be recorded at an element node using OpenSees Node
Recorder:</p>
<p><strong>recorder Node &lt;-file $fileName&gt; &lt;-time&gt; &lt;-node
($nod1 $nod2 …)&gt; -dof 3 vel</strong></p>
<p>See OpenSees command manual (McKenna and Fenves 2001) for nodal
displacement, velocity, or acceleration recorders.</p>
<p>The valid queries to a bbarBrickUP element when creating an
ElementRecorder are 'force', 'stiffness', or 'material matNum matArg1
matArg2 ...', where matNum represents the material object at the
corresponding integration point.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element bbarBrickUP $eleTag $Node1 $Node2 $Node3 $Node4
$Node5 $Node6 $Node7 $Node8 $matTag $bulk $fmass $PermX $PermY $PermZ
&lt;$bX=0 $bY=0 $bZ=0&gt;</strong></p></td>
</tr>
</tbody>
</table>
<figure>
<img src="BrickUp.png" title="BrickUp.png" alt="BrickUp.png" />
<figcaption aria-hidden="true">BrickUp.png</figcaption>
</figure>
<table>
<tbody>
<tr class="odd">
<td><p><strong>$eleTag</strong></p></td>
<td><p>A positive integer uniquely identifying the element among all
elements</p></td>
</tr>
<tr class="even">
<td><p><strong>$Node1,… $Node8</strong></p></td>
<td><p>Eight element node (previously defined) numbers (see figure above
for order of numbering).</p></td>
</tr>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>Tag of an NDMaterial object (previously defined) of which the
element is composed</p></td>
</tr>
<tr class="even">
<td><p><strong>$bulk</strong></p></td>
<td><p>Combined undrained bulk modulus B&lt;sub&gt;c&lt;/sub&gt;
relating changes in pore pressure and volumetric strain, may be
approximated by:</p>
<p>B&lt;sub&gt;c&lt;/sub&gt; &amp;asymp; B&lt;sub&gt;f&lt;/sub&gt;/n</p>
<p>where B&lt;sub&gt;f&lt;/sub&gt; is the bulk modulus of fluid phase
(2.2x10&lt;sup&gt;6&lt;/sup&gt; kPa (or 3.191x10&lt;sup&gt;5&lt;/sup&gt;
psi) for water), and n the initial porosity.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$fmass</strong></p></td>
<td><p>Fluid mass density</p></td>
</tr>
<tr class="even">
<td><p><strong>$permX, $permY, $permZ</strong></p></td>
<td><p>Permeability coefficients in x, y, and z directions
respectively.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$bX, $bY, $bZ</strong></p></td>
<td><p>Optional gravity acceleration components in x, y, and z
directions directions respectively (defaults are 0.0)</p></td>
</tr>
</tbody>
</table>
<p>Code Developed by: <span style="color:blue"> UC San Diego (Dr.
Zhaohui Yang)</span>:</p>
<hr />
<p>UC San Diego Soil Model: </p>
