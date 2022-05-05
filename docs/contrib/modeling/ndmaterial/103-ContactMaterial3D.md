# ContactMaterial3D

<p>This command is used to construct a ContactMaterial3D nDMaterial
object.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>nDMaterial ContactMaterial3D $matTag $mu $G $c
$t</strong></p></td>
</tr>
</tbody>
</table>
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique integer tag identifying nDMaterial object</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">mu</code></td>
<td><p>interface frictional coefficient</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">G</code></td>
<td><p>interface stiffness parameter</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">c</code></td>
<td><p>interface cohesive intercept</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">t</code></td>
<td><p>interface tensile strength</p></td>
</tr>
</tbody>
</table>
<hr />
<p>The ContactMaterial3D nDMaterial defines the constitutive behavior of
a frictional interface between two bodies in contact. The interface
defined by this material object allows for sticking, frictional slip,
and separation between the two bodies in a three-dimensional analysis. A
regularized Coulomb frictional law is assumed. Information on the theory
behind this material can be found in, e.g. Wriggers (2002).</p>
<p><strong>NOTE:</strong></p>
<ol>
<li>The ContactMaterial3D nDMaterial has been written to work with the
<a href="SimpleContact3D" title="wikilink">SimpleContact3D</a> and <a
href="BeamContact3D" title="wikilink">BeamContact3D</a> element
objects.</li>
<li>There are no valid recorder queries for this material other than
those which are listed with those elements.</li>
</ol>
<p><strong>EXAMPLE:</strong> ContactMaterial3D nDmaterial with tag 1</p>
<p>nDMaterial ContactMaterial3D 1 0.1 1000.0 0.0 0.0</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Kathryn Petek,
Pedro Arduino, &amp; Peter Mackenzie-Helnwein, at the University of
Washington </span></p>
<hr />
<p>References:</p>
<ol>
<li>Wriggers, P. (2002). <em>Computational Contact Mechanics.</em> John
Wilely &amp; Sons, Ltd, West Sussex, England.</li>
</ol>
