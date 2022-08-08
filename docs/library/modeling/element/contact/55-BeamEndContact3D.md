# BeamEndContact3D

<p>This command is used to construct a BeamEndContact3D element
object.</p>

```tcl
element BeamEndContact3D $eleTag $iNode $jNode $cNode
        $lNode $radius $gTol $fTol &lt;$cFlag$&gt;
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique integer tag identifying element object</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">iNode</code></td>
<td><p>retained node from the beam (-ndm 3 -ndf 6)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">jNode</code></td>
<td><p>the remaining node on the beam element with `iNode` (-ndm 3 -ndf
6)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">cNode</code></td>
<td><p>constrained node (-ndm 3 -ndf 3)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">lNode</code></td>
<td><p>Lagrange multiplier node (-ndm 3 -ndf 3)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">radius</code></td>
<td><p>radius of circular beam associated with beam element</p></td>
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
<td><p>`cFlag = 0`: contact between bodies is initially assumed
(DEFAULT)</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>`cFlag = 1`: no contact between bodies is initially assumed</p></td>
</tr>
</tbody>
</table>
<hr />
<p>The BeamEndContact3D element is a node-to-surface contact element
which defines a normal contact interface between the end of a beam
element and a separate body. The first retained node (`iNode`) is the
beam node which is at the end of the beam (i.e. only connected to a
single beam element), the second node (`jNode`) is the remaining node on
the beam element in question. The constrained node (`cNode`) is a node
from a second body. The Lagrange multiplier node (`lNode`) is required to
enforce the contact condition. This node should not be shared with any
other element in the domain, and should be created with the same number
of DOF as the constrained node.</p>
<p>The BeamEndContact3D element enforces a contact condition between a
fictitious circular plane associated with a beam element and a node from
a second body. The normal direction of the contact plane coincides with
the endpoint tangent of the beam element at the retained beam node
(`iNode`). The extents of this circular plane are defined by the radius
input parameter. The retained beam node can only come into contact with
a constrained node which is within the extents of the contact plane.
There is a lag step associated with changing between the 'in contact'
and 'not in contact' conditions.</p>
<p>This element was developed for use in establishing a contact
condition for the tip of a pile modeled as using beam elements and the
underlying soil elements in three-dimensional analysis.</p>
<p><strong>NOTE:</strong></p>
<ol>
<li>The BeamEndContact3D element does not use a material object.</li>
<li>The valid recorder queries for this element are:
<ol>
<li><em>force</em> - returns the contact force acting on the constrained
  node in vector form.</li>
<li><em>masterforce</em> - returns the reactions (forces and moments)
  acting on the retained node.</li>
</ol></li>

<li>The `BeamEndContact3D` element works well in static and pseudo-static
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
<p><strong>EXAMPLE:</strong> BeamEndContact3D element with tag 1, and
connectivity with nodes 1, 2, 3, and 4, beam radius of 0.25, gap and
force tolerances of 1.0e-10, and a contact flag set to initially assume
contact.</p>
<p>element BeamEndContact3D 1 1 2 3 4 0.25 1.0e-10 1.0e-10 0</p>
## References
<p>Laursen, T. A. (2002). <em>Computational Contact and Impact
Mechanics.</em> Springer-Verlag, Berlin.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Chris McGann,
Pedro Arduino, &amp; Peter Mackenzie-Helnwein, at the University of
Washington </span></p>
<hr />
