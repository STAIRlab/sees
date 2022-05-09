# BeamColumnJoint Element

<p>This command is used to construct a two-dimensional beam-column-joint
element object. The element may be used with both two-dimensional and
three-dimensional structures; however, load is transferred only in the
plane of the element.</p>

```tcl
element beamColumnJoint $eleTag $Nd1 $Nd2 $Nd3 $Nd4 $Mat1
        $Mat2 $Mat3 $Mat4 $Mat5 $Mat6 $Mat7 $Mat8 $Mat9 $Mat10 $Mat11 $Mat12
        $Mat13 &lt;$eleHeightFac $eleWidthFac&gt;
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">Tag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Nd1 Nd2 Nd3 Nd4</code></p></td>
<td><p>four nodes</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">Mat1</code></p></td>
<td><p>uniaxial material tag for left bar-slip spring at node 1</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Mat2</code></p></td>
<td><p>uniaxial material tag for right bar-slip spring at node
1</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">Mat3</code></p></td>
<td><p>uniaxial material tag for interface-shear spring at node
1</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Mat4</code></p></td>
<td><p>uniaxial material tag for lower bar-slip spring at node
2</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">Mat5</code></p></td>
<td><p>uniaxial material tag for upper bar-slip spring at node
2</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Mat6</code></p></td>
<td><p>uniaxial material tag for interface-shear spring at node
2</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">Mat7</code></p></td>
<td><p>uniaxial material tag for left bar-slip spring at node 3</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Mat8</code></p></td>
<td><p>uniaxial material tag for right bar-slip spring at node
3</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Mat9</code></td>
<td><p>uniaxial material tag for interface-shear spring at node
3</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Mat10</code></p></td>
<td><p>uniaxial material tag for lower bar-slip spring at node
4</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">Mat11</code></p></td>
<td><p>uniaxial material tag for upper bar-slip spring at node
4</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Mat12</code></p></td>
<td><p>uniaxial material tag for interface-shear spring at node
4</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">Mat13</code></p></td>
<td><p>uniaxial material tag for shear-panel</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">eleHeightFac</code></td>
<td><p>floating point value (as a ratio to the total height of the
element) to be considered for determination of the distance in between
the tension-compression couples (optional, default: 1.0)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">eleWidthFac</code></td>
<td><p>floating point value (as a ratio to the total width of the
element) to be considered for determination of the distance in between
the tension-compression couples (optional, default: 1.0)</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/BeamColumnJoint.png" title="BeamColumnJoint.png"
alt="BeamColumnJoint.png" />
<figcaption aria-hidden="true">BeamColumnJoint.png</figcaption>
</figure>

## Examples

<p><a href="BeamColumnJointExample"
title="wikilink">BeamColumnJointExample</a> - the original file (has
some errors)</p>
<p><a href="BeamColumnJointExample_Corrected"
title="wikilink">BeamColumnJointExample_Corrected</a> (corrected by
Vesna Terzic)</p>
<hr />
<p>REFERENCES:</p>
<p>Lowes, Laura N.; Mitra, Nilanjan; Altoontash, Arash A beam-column
joint model for simulating the earthquake response of reinforced
concrete frames PEER-2003/10 Pacific Earthquake Engineering Research
Center, University of California, Berkeley 2003 59 pages
(400/P33/2003-10)</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Nilanjan Mitra,
Cal Poly</span></p>
