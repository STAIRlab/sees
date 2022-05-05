# BeamContact3D

<p>This command is used to construct a BeamContact3D element object.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element BeamContact3D $eleTag $iNode $jNode $cNode $lNode
$radius $crdTransf $matTag $gTol $fTol &lt;$cFlag$&gt;</strong></p></td>
</tr>
</tbody>
</table>
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique integer tag identifying element object</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode</strong></p></td>
<td><p>retained nodes (-ndm 3 -ndf 6)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">cNode</code></td>
<td><p>constrained node (-ndm 3 -ndf 3)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">lNode</code></td>
<td><p>Lagrange multiplier node (-ndm 3 -ndf 3)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">radius</code></td>
<td><p>constant radius of circular beam associated with beam
element</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">crdTransf</code></td>
<td><p>unique integer tag associated with previously-defined <a
href="Geometric_Transformation_Command" title="wikilink">
geometricTransf</a> object</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique integer tag associated with previously-defined nDMaterial
object</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">gTol</code></td>
<td><p>gap tolerance</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fTol</code></td>
<td><p>force tolerance</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">cFlag</code></td>
<td><p>optional initial contact flag</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>$cFlag = 0 &gt;&gt; contact between bodies is initially assumed
(DEFAULT)</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>$cFlag = 1 &gt;&gt; no contact between bodies is initially
assumed</p></td>
</tr>
</tbody>
</table>
<hr />
<p>The BeamContact3D element is a three-dimensional beam-to-node contact
element which defines a frictional contact interface between a beam
element and a separate body. The retained nodes (6 DOF) are the
endpoints of the beam element, and the constrained node (3 DOF) is a
node from a second body. The Lagrange multiplier node (3 DOF) is
required to enforce the contact condition. Each contact element should
have a unique Lagrange multiplier node. The Lagrange multiplier node
should not be fixed, otherwise the contact condition will not work.</p>
<p><strong>NOTE:</strong></p>
<ol>
<li>The BeamContact3D element has been written to work exclusively with
the <a href="ContactMaterial3D" title="wikilink">ContactMaterial3D
nDMaterial</a> object.</li>
<li>The valid recorder queries for this element are:
<ol>
<li><em>force</em> - returns the contact force acting on the constrained
node in vector form.</li>
<li><em>frictionforce</em> - returns the frictional force acting on the
constrained node in vector form.</li>
<li><em>forcescalar</em> - returns the scalar magnitudes of the single
normal and two tangential contact forces.</li>
<li><em>masterforce</em> - returns the reactions (forces only) acting on
the retained nodes.</li>
<li><em>mastermoment</em> - returns the reactions (moments only) acting
on the retained nodes.</li>
<li><em>masterreaction</em> - returns the full reactions (forces and
moments) acting on the retained nodes.</li>
<li>The BeamContact3D elements are set to consider frictional behavior
as a default, but the frictional state of the BeamContact3D element can
be changed from the input file using the <a href="setParameter"
title="wikilink">setParameter</a> command. When updating, value of 0
corresponds to the frictionless condition, and a value of 1 signifies
the inclusion of friction. An example command for this update procedure
is provided below</li>
</ol></li>
<li>The BeamContact3D element works well in static and pseudo-static
analysis situations.</li>
<li>In transient analysis, the presence of the contact constraints can
effect the stability of commonly-used time integration methods in the
HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of
alternative time-integration methods which numerically damp spurious
high frequency behavior may be required. The <a href="TRBDF2"
title="wikilink">TRBDF2</a> integrator is an effective method for this
purpose. The Newmark integrator can also be effective with proper
selection of the gamma and beta coefficients. The trapezoidal rule,
i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to
instability related to the contact constraints and is not
recommended.</li>
</ol>
<p><strong>EXAMPLES:</strong></p>
<p>BeamContact3D element with tag 1, connectivity with nodes 1, 2, 3,
and 4, beam radius of 0.25, <a href="Geometric_Transformation_Command"
title="wikilink"> geomTransf</a> object with tag 1, material with tag 1,
gap and force tolerances of 1.0e-10, and a contact flag set to assume
initial contact.</p>
<p>element BeamContact3D 1 1 2 3 4 0.25 1 1 1.0e-10 1.0e-10 0</p>
<p>Update all of the BeamContact3D elements with tags between 10 and 20
to consider a frictionless interface</p>
<p>setParameter -value 0 -eleRange 10 20 friction</p>
<p><strong>REFERENCES:</strong></p>
<p>Laursen, T. A. (2002). <em>Computational Contact and Impact
Mechanics.</em> Springer-Verlag, Berlin.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Kathryn Petek,
Pedro Arduino, &amp; Peter Mackenzie-Helnwein, at the University of
Washington </span></p>
<hr />
