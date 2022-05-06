# SSPbrick Element

<p>This command is used to construct a SSPbrick element object.</p>

```tcl
element SSPbrick $eleTag $iNode $jNode $kNode $lNode
        $mNode $nNode $pNode $qNode $matTag &lt;$b1 $b2
        $b3&gt;
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique integer tag identifying element object</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode $kNode $lNode $mNode $nNode $pNode
$qNode</strong></p></td>
<td><p>the eight nodes defining the element, input in counterclockwise
order (same node numbering scheme as for the <a
href="Standard_Brick_Element" title="wikilink"> stdBrick Element</a>)
(-ndm 3 -ndf 3)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique integer tag associated with previously-defined nDMaterial
object</p></td>
</tr>
<tr class="even">
<td><p><strong>$b1 $b2 $b3</strong></p></td>
<td><p>constant body forces in global x-, y-, and z-directions,
respectively (optional, default = 0.0)</p></td>
</tr>
</tbody>
</table>
<hr />
<p>The SSPbrick element is an eight-node hexahedral element using
physically stabilized single-point integration (SSP --&gt; Stabilized
Single Point). The stabilization incorporates an enhanced assumed strain
field, resulting in an element which is free from volumetric and shear
locking. The elimination of shear locking results in greater coarse mesh
accuracy in bending dominated problems, and the elimination of
volumetric locking improves accuracy in nearly-incompressible problems.
Analysis times are generally faster than corresponding full integration
elements.</p>
<p><strong>NOTES:</strong></p>
<ol>
<li>Valid queries to the SSPbrick element when creating an
ElementalRecorder object correspond to those for the nDMaterial object
assigned to the element (e.g., 'stress', 'strain'). Material response is
recorded at the single integration point located in the center of the
element.</li>
<li>The SSPbrick element was designed with intentions of duplicating the
functionality of the <a href="Standard_Brick_Element" title="wikilink">
stdBrick Element</a>. If an example is found where the SSPbrick element
cannot do something that works for the <a href="Standard_Brick_Element"
title="wikilink"> stdBrick Element</a>, e.g., material updating, please
contact the developers listed below so the bug can be fixed.</li>
</ol>
<p><strong>EXAMPLES:</strong></p>
<p>SSPbrick element definition with element tag 1, nodes 1, 2, 3, 4, 5,
6, 7, and 8, material tag 1, x- and y-directed body forces of zero, and
z-directed body force of -10.0</p>
<p>element SSPbrick 1 1 2 3 4 5 6 7 8 1 0.0 0.0 -10.0</p>
<p>Elemental recorders for stress and strain when using the SSPbrick
element (note the difference from the <a href="Standard_Brick_Element"
title="wikilink"> stdBrick Element</a>)</p>
<p>recorder Element -eleRange 1 $numElem -time -file stress.out stress
recorder Element -eleRange 1 $numElem -time -file strain.out strain</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Chris McGann,
Pedro Arduino, &amp; Peter Mackenzie-Helnwein, at the University of
Washington </span></p>
<hr />
