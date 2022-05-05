# SurfaceLoad Element

<p>This command is used to construct a SurfaceLoad element object.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element SurfaceLoad $eleTag $iNode $jNode $kNode $lNode
$p</strong></p></td>
</tr>
</tbody>
</table>
<table>
<tbody>
<tr class="odd">
<td><p><strong>$eleTag</strong></p></td>
<td><p>unique integer tag identifying element object</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode $kNode $lNode</strong></p></td>
<td><p>the four nodes defining the element, input in counterclockwise
order (-ndm 3 -ndf 3)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$p</strong></p></td>
<td><p>applied pressure loading normal to the surface, outward is
positive, inward is negative</p></td>
</tr>
</tbody>
</table>
<hr />
<p>The SurfaceLoad element is a four-node element which can be used to
apply surface pressure loading to 3D brick elements. The SurfaceLoad
element applies energetically-conjugate forces corresponding to the
input scalar pressure to the nodes associated with the element. As these
nodes are shared with a 3D brick element, the appropriate nodal loads
are therefore applied to the brick.</p>
<p><strong>NOTES:</strong></p>
<ol>
<li>There are no valid ElementalRecorder queries for the SurfaceLoad
element. Its sole purpose is to apply nodal forces to the adjacent brick
element.</li>
<li>The pressure loading from the SurfaceLoad element can be applied in
a load pattern. See the analysis example below.</li>
</ol>
<p><strong>EXAMPLES:</strong></p>
<p>SurfaceLoad element definition with element tag 1, nodes 1, 2, 3, and
4, and pressure of -10.0</p>
<p>element SurfaceLoad 1 1 2 3 4 -10.0</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Chris McGann,
Pedro Arduino, &amp; Peter Mackenzie-Helnwein, at the University of
Washington </span></p>
<hr />
<p><strong>EXAMPLE ANALYSIS:</strong></p>
<p>The example input file below involves applying a compressive 0.1 kPa
loading to a four-element mesh of brick elements. The applied loading is
increased linearly over the first 0.1 seconds of pseudo-time, then held
constant.</p>
<p>&lt;source lang="tcl"&gt; wipe</p>
<p>model BasicBuilder -ndm 3 -ndf 3</p>
<ol>
<li>nodes</li>
</ol>
<p>node 1 0.0 0.0 6.0 node 2 3.0 0.0 6.0 node 3 6.0 0.0 6.0 node 4 0.0
0.0 3.0 node 5 3.0 0.0 3.0 node 6 6.0 0.0 3.0 node 7 0.0 0.0 0.0 node 8
3.0 0.0 0.0 node 9 6.0 0.0 0.0 node 10 0.0 3.0 6.0 node 11 3.0 3.0 6.0
node 12 6.0 3.0 6.0 node 13 0.0 3.0 3.0 node 14 3.0 3.0 3.0 node 15 6.0
3.0 3.0 node 16 0.0 3.0 0.0 node 17 3.0 3.0 0.0 node 18 6.0 3.0 0.0</p>
<ol>
<li>boundary conditions</li>
</ol>
<p>fix 1 1 1 1 fix 2 1 1 1 fix 3 1 1 1 fix 4 1 1 1 fix 5 1 1 1 fix 6 1 1
1 fix 7 1 1 1 fix 8 1 1 1 fix 9 1 1 1</p>
<ol>
<li>material</li>
</ol>
<p>nDMaterial ElasticIsotropic 1 25000.0 0.0</p>
<ol>
<li>brick elements</li>
</ol>
<p>element SSPbrick 1 1 2 5 4 10 11 14 13 1 element SSPbrick 2 2 3 6 5
11 12 15 14 1 element SSPbrick 3 4 5 8 7 13 14 17 16 1 element SSPbrick
4 5 6 9 8 14 15 18 17 1</p>
<ol>
<li>surface load elements</li>
</ol>
<p>element SurfaceLoad 5 10 11 14 13 -0.1 element SurfaceLoad 6 11 12 15
14 -0.1 element SurfaceLoad 7 13 14 17 16 -0.1 element SurfaceLoad 8 14
15 18 17 -0.1</p>
<ol>
<li>recorders</li>
</ol>
<p>recorder Node -file displacement.out -time -nodeRange 1 18 -dof 2
disp recorder Node -file reactions.out -time -nodeRange 1 18 -dof 2
reaction recorder Element -file stress.out -time -eleRange 1 4
stress</p>
<ol>
<li>load pattern</li>
</ol>
<p>pattern Plain 1 {Series -time {0 0.1 10000} -values {0 1 1} -factor
1} { eleLoad -ele 5 -type -surfaceLoad eleLoad -ele 6 -type -surfaceLoad
eleLoad -ele 7 -type -surfaceLoad eleLoad -ele 8 -type -surfaceLoad
}</p>
<ol>
<li>analysis</li>
</ol>
<p>constraints Transformation test NormDispIncr 1e-5 50 1 algorithm
Newton numberer Plain system SparseSPD integrator LoadControl 0.01
analysis Static</p>
<p>analyze 105</p>
<p>wipe &lt;/source&gt;</p>
