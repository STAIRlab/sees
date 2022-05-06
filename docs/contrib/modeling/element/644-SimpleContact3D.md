# SimpleContact3D

<p>This command is used to construct a SimpleContact3D element
object.</p>

```tcl
element SimpleContact3D $eleTag $iNode $jNode $kNode
        $lNode $cNode $lNode $matTag $gTol $fTol
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique integer tag identifying element object</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode $kNode $lNode</strong></p></td>
<td><p>retained nodes (-ndm 3 -ndf 3)</p></td>
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
</tbody>
</table>
<hr />
<p>The SimpleContact3D element is a three-dimensional node-to-surface
contact element which defines a frictional contact interface between two
separate bodies. The retained nodes are the nodes which define a surface
of a hexahedral element on the first body, and the constrained node is a
node from the second body. The Lagrange multiplier node is required to
enforce the contact condition. This node should not be shared with any
other element in the domain. Information on the theory behind this
element can be found in, e.g. Wriggers (2002).</p>
<p><strong>NOTE:</strong></p>
<ol>
<li>The SimpleContact3D element has been written to work exclusively
with the <a href="ContactMaterial3D" title="wikilink">ContactMaterial3D
nDMaterial</a> object.</li>
<li>The valid recorder queries for this element are:
<ol>
<li><em>force</em> - returns the contact force acting on the constrained
node in vector form.</li>
<li><em>frictionforce</em> - returns the frictional force acting on the
constrained node in vector form.</li>
<li><em>forcescalar</em> - returns the scalar magnitudes of the single
normal and two tangential contact forces.</li>
<li>The SimpleContact3D elements are set to consider frictional behavior
as a default, but the frictional state of the SimpleContact3D element
can be changed from the input file using the <a href="setParameter"
title="wikilink">setParameter</a> command. When updating, value of 0
corresponds to the frictionless condition, and a value of 1 signifies
the inclusion of friction. An example command for this update procedure
is provided below</li>
</ol></li>
<li>The SimpleContact3D element works well in static and pseudo-static
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
<p><strong>EXAMPLE:</strong></p>
<p>SimpleContact3D element with tag 1, connectivity with nodes 1, 2, 3,
4, 5, 6, 7, and 8, material with tag 1, and gap and force tolerances of
1.0e-10.</p>
<p>element SimpleContact3D 1 1 2 3 4 5 6 7 8 1 1.0e-10 1.0e-10</p>
<p>Update all of the SimpleContact3D elements with tags between 10 and
20 to consider a frictionless interface</p>
<p>setParameter -value 0 -eleRange 10 20 friction</p>
<p><strong>REFERENCES:</strong></p>
<ol>
<li>Wriggers, P. (2002). <em>Computational Contact Mechanics.</em> John
Wiley &amp; Sons, Ltd, West Sussex, England.</li>
<li>Laursen, T. A. (2002). <em>Computational Contact and Impact
Mechanics.</em> Springer-Verlag, Berlin.</li>
</ol>
<hr />
<p>Code Developed by: <span style="color:blue"> Kathryn Petek,
Pedro Arduino, &amp; Peter Mackenzie-Helnwein, at the University of
Washington </span></p>
<hr />
