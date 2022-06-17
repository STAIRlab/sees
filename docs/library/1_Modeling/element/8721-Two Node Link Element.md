# Two Node Link Element

<p>This command is used to construct a twoNodeLink element object, which
is defined by two nodes. The element can have zero or non-zero length.
This element can have 1 to 6 degrees of freedom, where only the
transverse and rotational degrees of freedom are coupled as long as the
element has non-zero length. In addition, if the element length is
larger than zero, the user can optionally specify how the P-Delta
moments around the local x- and y-axis are distributed among a moment at
node i, a moment at node j, and a shear couple. The sum of these three
ratios is always equal to 1. In addition the shear center can be
specified as a fraction of the element length from the iNode. The
element does not contribute to the Rayleigh damping by default. If the
element has non-zero length, the local x-axis is determined from the
nodal geometry unless the optional x-axis vector is specified in which
case the nodal geometry is ignored and the user-defined orientation is
utilized. It is important to recognize that if this element has zero
length, it does not consider the geometry as given by the nodal
coordinates, but utilizes the user-defined orientation vectors to
determine the directions of the springs.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element twoNodeLink $eleTag $iNode $jNode -mat $matTags
-dir $dirs &lt;-orient &lt;$x1 $x2 $x3&gt; $y1 $y2 $y3&gt; &lt;-pDelta
(4 $Mratio)&gt; &lt;-shearDist (2 $sDratios)&gt; &lt;-doRayleigh&gt;
&lt;-mass $m&gt;</strong></p></td>
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
<td><p><code class="parameter-table-variable">iNode jNode</code></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTags</code></td>
<td><p>tags associated with previously-defined UniaxialMaterial
objects</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">dirs</code></td>
<td><p>material directions:</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p><em>2D-case</em>: 1,2 - translations along local x,y axes; 3 -
rotation about local z axis</p></td>
</tr>
<tr class="even">
<td></td>
<td><p><em>3D-case</em>: 1,2,3 - translations along local x,y,z axes;
4,5,6 - rotations about local x,y,z axes</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">x1 x2 x3</code></p></td>
<td><p>vector components in global coordinates defining local x-axis
(optional)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">y1 y2 y3</code></p></td>
<td><p>vector components in global coordinates defining local y-axis
(optional)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Mratios</code></td>
<td><p>P-Delta moment contribution ratios, size of ratio vector is 2 for
2D-case and 4 for 3D-case</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>(entries: [My_iNode, My_jNode, Mz_iNode, Mz_jNode]) My_iNode +
My_jNode &lt;= 1.0, Mz_iNode + Mz_jNode &lt;= 1.0.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>Remaining P-Delta moments are resisted by shear couples.
(optional)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">sDratios</code></td>
<td><p>shear distances from iNode as a fraction of the element length,
size of ratio vector is 1 for 2D-case and 2 for 3D-case</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>(entries: [dy_iNode, dz_iNode] (optional, default = [0.5
0.5])</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-flag">-doRayleigh</code></p></td>
<td><p>to include Rayleigh damping from the element (optional, default =
no Rayleigh damping contribution)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">m</code></td>
<td><p>element mass (optional, default = 0.0)</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/TwoNodeLinkElement.png" title="TwoNodeLinkElement.png"
alt="TwoNodeLinkElement.png" />
<figcaption aria-hidden="true">TwoNodeLinkElement.png</figcaption>
</figure>
<hr />
<p>NOTE:</p>
<p>If the element has zero length and optional orientation vectors are
not specified, the local element axes coincide with the global axes.
Otherwise the local z-axis is defined by the cross product between the
x- and y-vectors specified on the command line.</p>
<p>The valid queries to a twoNodeLink element when creating an
ElementRecorder object are 'force,' 'localForce,' 'basicForce,'
'localDisplacement,' 'basicDisplacement' and 'material $matNum matArg1
matArg2 ...' Where $matNum is the number associated with the material
whose data is to be output.</p>
<hr />

## Examples

<p>2D: element twoNodeLink 1 1 2 -mat 1 2 3 -dir 1 2 3;</p>
<p>3D: element twoNodeLink 1 1 2 -mat 1 2 3 -dir 1 2 6;</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Andreas
Schellenberg, University of California, Berkeley. </span></p>
