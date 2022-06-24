
# SSPquad

This command is used to construct a SSPquad element.

```tcl
element SSPquad $eleTag $iNode $jNode $kNode $lNode
        $matTag $type $thick < $b1 $b2 >
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique integer tag identifying element object</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">iNode jNode kNode lNode</code></p></td>
<td><p>the four nodes defining the element, input in counterclockwise
order (-ndm 2 -ndf 2)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">thick</code></td>
<td><p>thickness of the element in out-of-plane direction</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">type</code></td>
<td><p>string to relay material behavior to the element, can be either
"PlaneStrain" or "PlaneStress"</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique integer tag associated with previously-defined nDMaterial
object</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">b1 b2</code></p></td>
<td><p>constant body forces in global x- and y-directions, respectively
(optional, default = 0.0)</p></td>
</tr>
</tbody>
</table>

<hr />
The SSPquad element is a four-node quadrilateral element using
physically stabilized single-point integration (SSP --&gt; Stabilized
Single Point). The stabilization incorporates an assumed strain field in
which the volumetric dilation and the shear strain associated with the
the hourglass modes are zero, resulting in an element which is free from
volumetric and shear locking. The elimination of shear locking results
in greater coarse mesh accuracy in bending dominated problems, and the
elimination of volumetric locking improves accuracy in
nearly-incompressible problems. Analysis times are generally faster than
corresponding full integration elements. The formulation for this
element is identical to the solid phase portion of the SSPquadUP element
as described by McGann et al. (2012).

<p><strong>NOTES:</strong></p>
<ol>
<li>Valid queries to the SSPquad element when creating an
   ElementalRecorder object correspond to those for the nDMaterial object
   assigned to the element (e.g., 'stress', 'strain'). Material response is
   recorded at the single integration point located in the center of the
   element.</li>
<li>The SSPquad element was designed with intentions of duplicating the
   functionality of the <a href="Quad_Element" title="wikilink">Quad
   Element</a>. If an example is found where the SSPquad element cannot do
   something that works for the <a href="Quad_Element" title="wikilink">Quad Element</a>, 
   e.g., material updating, please contact the developers listed below so the bug can be fixed.</li>
</ol>

<p><strong>EXAMPLES:</strong></p>
<p>SSPquad element definition with element tag 1, nodes 1, 2, 3, and 4,
material tag 1, plane strain conditions, unit thickness, horizontal body
force of zero, and vertical body force of -10.0</p>

```tcl
element SSPquad 1 1 2 3 4 1 "PlaneStrain" 1.0 0.0 -10.0
```

Elemental recorders for stress and strain when using the SSPquad
element (note the difference from the <a href="Quad_Element"
title="wikilink">Quad Element</a>)

```tcl
recorder Element -eleRange 1 $numElem -time -file stress.out stress
recorder Element -eleRange 1 $numElem -time -file strain.out strain
```

<p><strong>EXAMPLE ANALYSIS:</strong></p>
<p>The input file shown below creates a cantilever beam subject to a
parabolic shear stress distribution at the free end. The beam is modeled
with only one element over the height to test the coarse-mesh accuracy
of the designated quadrilateral element. Anti-symmetry conditions hold,
only the top half of the beam is modeled.</p>
<p>Try running this with the SSPquad element and the <a
href="Quad_Element" title="wikilink">Quad Element</a>. Compare the
results to each other and to the beam solution to see shear locking in
action. Volumetric locking in the <a href="Quad_Element"
title="wikilink">Quad Element</a> can be observed by increasing
Poisson's ratio to $0.49$.</p>


```tcl
<li>#</li>
<li>Coarse-mesh cantilever beam analysis. The beam is #</li>
<li>modeled with only 4 elements and uses anti-symmetry. #</li>
<li>#</li>
<li>---&gt; Basic units used are kN and meters #</li>
<li>#

wipe
model BasicBuilder -ndm 2 -ndf 2

<li>beam dimensions</li>

set L 24.0 set D 3.0

<li>define number and size of elements</li>

set nElemX 4 set nElemY 1 set nElemT [expr $nElemX*$nElemY] set
sElemX [expr $L/$nElemX] set sElemY [expr $D/$nElemY]
set nNodeX [expr $nElemX + 1] set nNodeY [expr $nElemY + 1] set
nNodeT [expr $nNodeX*$nNodeY]

<li>create the nodes</li>

set nid 1 set count 0.0 for {set j 1} {$j &lt;= $nNodeY} {incr j 1} {
for {set i 1} {$i &lt;= $nNodeX} {incr i 1} { node $nid [expr 0.0 +
$count*$sElemX] [expr ($j-1)*$sElemY] set nid [expr $nid + 1] set count
[expr $count + 1] } set count 0.0 }

<li>boundary conditions</li>

fix 1 1 1 fix [expr $nElemY*$nNodeX+1] 1 0 for {set k 2} {$k &lt;=
$nNodeX} {incr k 1} { fix $k 1 0 }

<li>define material</li>

set matID 1 set E 20000 set nu 0.25 nDMaterial ElasticIsotropic
$matID $E $nu

<li>create elements</li>

set thick 1.0 set b1 0.0 set b2 0.0 set count 1 for {set j 1} {$j
&lt;= $nNodeY} {incr j 1} { for {set i 1} {$i &lt;= $nNodeX} {incr i 1}
{ if {($i &lt; $nNodeX) &amp;&amp; ($j &lt; $nNodeY)} { set nI [expr
$i+($j-1)*$nNodeX] set nJ [expr $i+($j-1)*$nNodeX+1] set nK [expr
$i+$j*$nNodeX+1] set nL [expr $i+$j*$nNodeX] element SSPquad $count $nI
$nJ $nK $nL $matID "PlaneStrain" $thick $b1 $b2
set count [expr $count+1] } } }

<li>create recorders</li>

set step 0.1
recorder Node -time -file results/d1p1m1.out -dT $step -nodeRange 1
$nNodeT -dof 1 2 disp 
recorder Element -eleRange 1 $nElemT -time -file
results/s1p1m1.out -dT $step stress 
recorder Element -eleRange 1 $nElemT
-time -file results/e1p1m1.out -dT $step strain

<li>create loading</li>

set P -300.0;
pattern Plain 3 {Series -time {0 10 15} -values {0 1 1} -factor 1} {
load $nNodeT 0.0 [expr 0.1875*$P] load $nNodeX 0.0 [expr 0.3125*$P]
load [expr $nNodeX+1] 0.0 [expr -0.1875*$P] }

<li>create analysis</li>

integrator LoadControl 0.1 numberer RCM system SparseGeneral
constraints Transformation test NormDispIncr 1e-5 40 1 algorithm Newton
analysis Static
analyze 105
wipe 
```

## References
- McGann, C. R., Arduino, P., and Mackenzie-Helnwein, P. (2012).
  “Stabilized single-point 4-node quadrilateral element for dynamic
  analysis of fluid saturated porous media.” <em>Acta Geotechnica</em>,
  7(4), 297-311.


<hr />
<p>Code developed by: <span style="color:blue"> Chris McGann,
Pedro Arduino, &amp; Peter Mackenzie-Helnwein, at the University of
Washington </span></p>

