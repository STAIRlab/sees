# CatenaryCableElement

<p>This command is used to construct a catenary cable element
object.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element CatenaryCable $tag $iNode $jNode $weight $E $A
$L0 $alpha $temperature_change $rho $errorTol $Nsubsteps
$massType</strong></p></td>
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
<td><p><strong>$iNode $jNode</strong></p></td>
<td><p>end nodes (3 dof per node)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">E</code></td>
<td><p>elastic modulus of the cable material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">A</code></td>
<td><p>cross-sectional area of element</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">L0</code></td>
<td><p>unstretched length of the cable</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>coefficient of thermal expansion</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">temperature_change</code></td>
<td><p>temperature change for the element</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>mass per unit length</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">errortol</code></td>
<td><p>allowed tolerance for within-element equilbrium (Newton-Rhapson
iterations)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Nsubsteps</code></td>
<td><p>number of within-element substeps into which equilibrium
iterations are subdivided (not number of steps to convergence)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">massType</code></td>
<td><p>Mass matrix model to use (<strong>$massType = 0</strong> lumped
mass matrix, <strong>$massType = 1</strong> rigid-body mass matrix (in
development))</p></td>
</tr>
</tbody>
</table>
<p>This cable is a flexibility-based formulation of the catenary cable.
An iterative scheme is used internally to compute equilibrium. At each
iteration, node i is considered fixed while node j is free. End-forces
are applied at node-j and its displacements computed. Corrections to
these forces are applied iteratively using a Newton-Rhapson scheme (with
optional sub-stepping via <strong>$Nsubsteps</strong>) until nodal
displacements are within the provided tolerance
(<strong>$errortol</strong>). When convergence is reached, a stiffness
matrix is computed by inversion of the flexibility matrix and rigid-body
mode injection.</p>
<p>Notes:</p>
<ol>
<li>The stiffness of the cable comes from the large-deformation
interaction between loading and cable shape. Therefore, all cables must
have distributed forces applied to them. See example. Should not work
for only nodal forces.</li>
<li>Valid queries to the CatenaryCable element when creating an
ElementalRecorder object correspond to 'forces', which output the
end-forces of the element in global coordinates (3 for each node).</li>
<li>Only the lumped-mass formulation is currently available.</li>
<li>The element does up 100 internal iterations. If convergence is not
achieved, will result in error and some diagnostic information is
printed out.</li>
</ol>
<hr />
<p>Code Developed by: <span style="color:blue">Pablo Ibañez and <a
href="http://www.joseabell.com">José A. Abell at Universidad de los
Andes, Chile</a></span></p>
<p>EXAMPLE:</p>
<p>&lt;source lang="tcl"&gt;</p>
<ol>
<li>This example implements a slight modification of the verification
test from reference #1.</li>
<li></li>
</ol>
<p>model BasicBuilder -ndm 3 -ndf 3</p>
<p>set x 30. ; #Set to example from paper x = 30, 60, 80, 100. Will not
work for x=0.01, system ill-conditioned.</p>
<p>node 1 0.0 0.0 90.0 node 2 [expr $x/2] 0.0 40.0 node 3 $x 60 30.</p>
<p>fix 1 1 1 1 fix 2 0 1 0 fix 3 1 1 1</p>
<p>set w3 -0.00001 set E 3.e7 set A 1. set L0 100. set alfa 6.5e-6 set
cambiodetemp 100. set rho [expr $w3 / 9.81]</p>
<p>set errorTol 1e-6 set NSubSteps 20</p>
<p>element CatenaryCable 1 1 2 $w3 $E $A [expr $L0/2] $alfa
$cambiodetemp $rho $errorTol $NSubSteps 0 element CatenaryCable 2 2 3
$w3 $E $A [expr $L0/2] $alfa $cambiodetemp $rho $errorTol $NSubSteps
0</p>
<p>set NSteps 10 timeSeries Linear 1 -factor 1</p>
<p>pattern Plain 2 1 { eleLoad -ele 1 2 -type -beamUniform 0. 0. -1
}</p>
<p>recorder Node -file "disp.txt" -time -nodeRange 1 3 -dof 1 2 3 disp
recorder Element -file "forces.txt" -time -eleRange 1 2 force</p>
<p>system FullGeneral constraints Plain numberer Plain test NormDispIncr
1.0e-5 100 1 integrator LoadControl [expr 1.0/$NSteps] algorithm Newton
analysis Static</p>
<p>analyze $NSteps</p>
<p>print -node 2 &lt;/source&gt;</p>
<p>Results should be:</p>
<p>Node: 2 Coordinates : 15 0 40 Disps: 8.58693 0 2.82578 unbalanced
Load: 0 0 0 ID : 0 -1 1</p>
<p>Compare the forces.txt (for node 3) file with the results from
reference [1].</p>
<h2 id="references">References</h2>
<p>1. Salehi Ahmad Abad, M., Shooshtari, A., Esmaeili, V., &amp; Naghavi
Riabi, A. (2013). Nonlinear analysis of cable structures under general
loadings. Finite Elements in Analysis and Design, 73, 11-19. <a
href="https://doi.org/10.1016/j.finel.2013.05.002">https://doi.org/10.1016/j.finel.2013.05.002</a></p>
<p>2. Thai, H. T., &amp; Kim, S. E. (2011). Nonlinear static and dynamic
analysis of cable structures. Finite Elements in Analysis and Design,
47(3), 237-246. <a
href="https://doi.org/10.1016/j.finel.2010.10.005">https://doi.org/10.1016/j.finel.2010.10.005</a></p>
