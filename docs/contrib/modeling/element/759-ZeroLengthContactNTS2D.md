# ZeroLengthContactNTS2D

<p>This command is used to construct a zeroLengthContactNTS2D element
object. This is a Node-To-Segment (NTS) frictional contact element used
in two dimensional analysis for contact between elements with 2 DOF
nodes.</p>

```tcl
element zeroLengtContactNTS2D $eleTag -cNdNum $cNdNum
        -rNdNum $rNdNum -Nodes $Nodes $Kn $kt $phi
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$eleTag</strong></p></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$cNdNum</strong></p></td>
<td><p>Number of Constrained Nodes</p></td>
</tr>
<tr class="odd">
<td><p><strong>$rNdNum</strong></p></td>
<td><p>Number of Retained nodes</p></td>
</tr>
<tr class="even">
<td><p><strong>$Nodes ...</strong></p></td>
<td><p>Constrained and Retained node tags respectively</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Kn</strong></p></td>
<td><p>Penalty in normal direction</p></td>
</tr>
<tr class="even">
<td><p><strong>$Kt</strong></p></td>
<td><p>Penalty in tangential direction</p></td>
</tr>
<tr class="odd">
<td><p><strong>$phi</strong></p></td>
<td><p>Friction angle in degrees</p></td>
</tr>
</tbody>
</table>
<p><strong>NOTES:</strong></p>
<ol>
<li>The contact element is node-to-segment (NTS) contact. The relation
follows Mohr-Coulomb frictional law: &lt;math&gt;T = N \times
tan(\phi)&lt;/math&gt;, where $T$ is the
tangential force, $N$ is normal force across the
interface and &lt;math&gt;\phi\,\!&lt;/math&gt; is friction angle.</li>
<li>For 2D contact, constrained nodes and retained nodes must be 2 DOF
and notice that the constrained and retained nodes must be entered in
counterclockwise order.</li>
<li>The resulting tangent from the contact element is non-symmetric.
Switch to the non-symmetric matrix solver if convergence problem is
experienced.</li>
<li>As opposed to node-to-node contact, predefined normal vector for
node-to-segment (NTS) element is not required because contact normal
will be calculated automatically at each step.</li>
<li>contact element is implemented to handle large deformations.</li>
</ol>
<p><strong>EXAMPLE:</strong></p>
<figure>
<img src="zeroLengthContactNTS2Drc.png"
title="zeroLengthContactNTS2Drc.png"
alt="zeroLengthContactNTS2Drc.png" />
<figcaption aria-hidden="true">zeroLengthContactNTS2Drc.png</figcaption>
</figure>
<p>element zeroLengthContactNTS2D 1 -cNdNum 6 -rNdNum 6 - Nodes 5 10 12
3 9 11 1 4 2 8 7 6 1e8 1e8 16</p>
<p><strong>Example 1:</strong></p>
<p>This example simply shows the two quadrilateral elements in normal
contact. The top element is in normal downward uniform force. The Tcl
script of this example can be found <a
href="ZeroLengthContactNTS2D_Example1" title="wikilink">here</a>.</p>
<figure>
<img src="ZeroLengthContactNTS2D_fig2.jpg"
title="ZeroLengthContactNTS2D_fig2.jpg"
alt="ZeroLengthContactNTS2D_fig2.jpg" />
<figcaption
aria-hidden="true">ZeroLengthContactNTS2D_fig2.jpg</figcaption>
</figure>
<p><strong>Example 2:</strong></p>
<p>This example shows two cantilever beams in contact. The beams were
modeled using four-node quadrilateral elements and the end of top beam
was subjected to a linearly increasing displacement. The Tcl scripts for
this example can be found <a href="ZeroLengthContactNTS2D_Example2"
title="wikilink">here</a>.</p>
<figure>
<img src="zeroLengthContactNTS2D_fig3.jpg"
title="zeroLengthContactNTS2D_fig3.jpg"
alt="zeroLengthContactNTS2D_fig3.jpg" />
<figcaption
aria-hidden="true">zeroLengthContactNTS2D_fig3.jpg</figcaption>
</figure>
<p>The following Figure shows the deflections of the two beams.</p>
<figure>
<img src="zeroLengthContactNTS2D_fig4.jpg"
title="zeroLengthContactNTS2D_fig4.jpg"
alt="zeroLengthContactNTS2D_fig4.jpg" />
<figcaption
aria-hidden="true">zeroLengthContactNTS2D_fig4.jpg</figcaption>
</figure>
<p><strong>REFERENCES:</strong></p>
<ol>
<li>P. Wriggers, V.T. Vu and E. Stein, Finite-element formulation of
large deformation impact-contact problems with friction, Comput. Struct.
37 (1990), pp. 319-331.</li>
<li>Peter Wriggers. Computational Contact Mechanics. John Wiley &amp;
Sons Ltd. Chichester, 2002.</li>
</ol>
<hr />
<p>Code Developed by: <span style="color:blue"> <a
href="http://www.roozbehgm.com/">Roozbeh G. Mikola</a>, UC
Berkeley</span> and <span style="color:blue"> <a
href="http://www.ce.berkeley.edu/~sitar/">N. Sitar</a>, UC
Berkeley</span></p>
