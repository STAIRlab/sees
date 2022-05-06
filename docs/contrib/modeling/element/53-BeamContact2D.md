# BeamContact2D

<p>This command is used to construct a BeamContact2D element object.</p>

```tcl
element BeamContact2D $eleTag $iNode $jNode $cNode $lNode
        $matTag $width $gTol $fTol &lt;$cFlag$&gt;
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique integer tag identifying element object</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode</strong></p></td>
<td><p>retained nodes (-ndm 2 -ndf 3)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">cNode</code></td>
<td><p>constrained node (-ndm 2 -ndf 2)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">lNode</code></td>
<td><p>Lagrange multiplier node (-ndm 2 -ndf 2)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique integer tag associated with previously-defined nDMaterial
object</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">width</code></td>
<td><p>the width of the wall represented by the beam element in plane
strain</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">gTol</code></td>
<td><p>gap tolerance</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fTol</code></td>
<td><p>force tolerance</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">cFlag</code></td>
<td><p>optional initial contact flag</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>$cFlag = 0 &gt;&gt; contact between bodies is initially assumed
(DEFAULT)</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>$cFlag = 1 &gt;&gt; no contact between bodies is initially
assumed</p></td>
</tr>
</tbody>
</table>
<hr />
<p>The BeamContact2D element is a two-dimensional beam-to-node contact
element which defines a frictional contact interface between a beam
element and a separate body. The retained nodes (3 DOF) are the
endpoints of the beam element, and the constrained node (2 DOF) is a
node from a second body. The Lagrange multiplier node (2 DOF) is
required to enforce the contact condition. Each contact element should
have a unique Lagrange multiplier node. The Lagrange multiplier node
should not be fixed, otherwise the contact condition will not work.</p>
<p>Under plane strain conditions in 2D, a beam element represents a unit
thickness of a wall. The width is the dimension of this wall in the 2D
plane. This width should be built-in to the model to ensure proper
enforcement of the contact condition. The <a
href="Excavation_Supported_by_Cantilevered_Sheet_Pile_Wall"
title="wikilink">Excavation Supported by Cantilevered Sheet Pile
Wall</a> practical example provides some further examples and discussion
on the usage of this element.</p>
<p><strong>NOTE:</strong></p>
<ol>
<li>The BeamContact2D element has been written to work exclusively with
the <a href="ContactMaterial2D" title="wikilink">ContactMaterial2D
nDMaterial</a> object.</li>
<li>The valid recorder queries for this element are:
<ol>
<li><em>force</em> - returns the contact force acting on the constrained
node in vector form.</li>
<li><em>frictionforce</em> - returns the frictional force acting on the
constrained node in vector form.</li>
<li><em>forcescalar</em> - returns the scalar magnitudes of the normal
and tangential contact forces.</li>
<li><em>masterforce</em> - returns the reactions (forces and moments)
acting on the retained nodes.</li>
<li>The BeamContact2D elements are set to consider frictional behavior
as a default, but the frictional state of the BeamContact2D element can
be changed from the input file using the <a href="setParameter"
title="wikilink">setParameter</a> command. When updating, value of 0
corresponds to the frictionless condition, and a value of 1 signifies
the inclusion of friction. An example command for this update procedure
is provided below</li>
</ol></li>
<li>The BeamContact2D element works well in static and pseudo-static
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
<p>BeamContact2D element with tag 1, connectivity with nodes 1, 2, 3,
and 4, material with tag 1, width 0.5, gap and force tolerances of
1.0e-10, and a contact flag set to assume initial contact.</p>
<p>element BeamContact2D 1 1 2 3 4 1 0.5 1.0e-10 1.0e-10 0</p>
<p>Update all of the BeamContact2D elements with tags between 10 and 20
to consider a frictionless interface</p>
<p>setParameter -value 0 -eleRange 10 20 friction</p>
<p><strong>REFERENCES:</strong></p>
<p>Laursen, T. A. (2002). <em>Computational Contact and Impact
Mechanics.</em> Springer-Verlag, Berlin.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Chris McGann,
Pedro Arduino, &amp; Peter Mackenzie-Helnwein, at the University of
Washington </span></p>
<hr />
