# SSPquadUP Element

<p>This command is used to construct a SSPquadUP element object.</p>

```tcl
element SSPquadUP $eleTag $iNode $jNode $kNode $lNode
        $matTag $thick $fBulk $fDen $k1 $k2 $void $alpha &lt;$b1
        $b2&gt;
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
order (-ndm 2 -ndf 3)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique integer tag associated with previously-defined nDMaterial
object</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">thick</code></td>
<td><p>thickness of the element in out-of-plane direction</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fBulk</code></td>
<td><p>bulk modulus of the pore fluid</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fDen</code></td>
<td><p>mass density of the pore fluid</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">k1 k2</code></p></td>
<td><p>permeability coefficients in global x- and y-directions,
respectively</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">void</code></td>
<td><p>voids ratio</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>spatial pressure field stabilization parameter (see discussion
below for more information)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">b1 b2</code></p></td>
<td><p>constant body forces in global x- and y-directions, respectively
(optional, default = 0.0) - <strong>See Note 3</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<p>The SSPquadUP element is an extension of the <a
href="SSPquad_Element" title="wikilink">SSPquad Element</a> for use in
dynamic plane strain analysis of fluid saturated porous media. A mixed
displacement-pressure (u-p) formulation is used, based upon the work of
Biot as extended by Zienkiewicz and Shiomi (1984).</p>
<p>The physical stabilization necessary to allow for reduced integration
incorporates an assumed strain field in which the volumetric dilation
and the shear strain associated with the the hourglass modes are zero,
resulting in an element which is free from volumetric and shear locking.
The elimination of shear locking results in greater coarse mesh accuracy
in bending dominated problems, and the elimination of volumetric locking
improves accuracy in nearly-incompressible problems. Analysis times are
generally faster than corresponding full integration elements.</p>
<p>Equal-order interpolation is used for the displacement and pressure
fields, thus, the SSPquadUP element does not inherently pass the
<em>inf-sup</em> condition, and is not fully acceptable in the
incompressible-impermeable limit (the <a
href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/1098.htm">QuadUP
Element</a> has the same issue). A stabilizing parameter is employed to
permit the use of equal-order interpolation for the SSPquadUP element.
This parameter <code class="tcl-variable">alpha</code> can be computed as</p>
<p>alpha = 0.25*(h^2)/(den*c^2)</p>
<p>where <strong>h</strong> is the element size, <strong>c</strong> is
the speed of elastic wave propagation in the solid phase, and
<strong>den</strong> is the mass density of the solid phase. The
<code class="tcl-variable">alpha</code> parameter should be a small number. With a
properly defined <code class="tcl-variable">alpha</code> parameter, the SSPquadUP
element can produce comparable results to a higher-order element such as
the <a href="Nine_Four_Node_Quad_u-p_Element" title="wikilink">
9_4_QuadUP Element</a> at a significantly lower computational cost and
with a greater ease in mesh generation.</p>
<p>The full formulation for the SSPquadUP element can be found in McGann
et al. (2012) along with several example applications.</p>
<p><strong>NOTES:</strong></p>
<ol>
<li>The SSPquadUP element will only work in dynamic analysis.</li>
<li>For saturated soils, the mass density input into the associated
nDMaterial object should be the saturated mass density.</li>
<li>When modeling soil, the body forces input into the SSPquadUP element
should be the components of the gravitational vector, not the unit
weight.</li>
<li>Fixing the pore pressure degree-of-freedom (dof 3) at a node is a
drainage boundary condition at which zero pore pressure will be
maintained throughout the analysis. Leaving the third dof free allows
pore pressures to build at that node.</li>
<li>Valid queries to the SSPquadUP element when creating an
ElementalRecorder object correspond to those for the nDMaterial object
assigned to the element (e.g., 'stress', 'strain'). Material response is
recorded at the single integration point located in the center of the
element.</li>
<li>The SSPquadUP element was designed with intentions of duplicating
the functionality of the <a
href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/1098.htm">QuadUP
Element</a>. If an example is found where the SSPquadUP element cannot
do something that works for the <a
href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/1098.htm">QuadUP
Element</a>, e.g., material updating, please contact the developers
listed below so the bug can be fixed.</li>
</ol>
<p><strong>EXAMPLES:</strong></p>
<p>SSPquadUP element definition with element tag 1, nodes 1, 2, 3, and
4, material tag 1, unit thickness, bulk modulus of water (kPa), mass
density of water (Mg/m^3), horizontal and vertical permeabilities of
1e-3, voids ratio of 0.7, alpha parameter of 6e-5, horizontal body force
of zero, and vertical body force of -9.81</p>
<p>element SSPquadUP 1 1 2 3 4 1 1.0 2.2e6 1.0 1.0e-3 1.0e-3 0.7 6.0e-5
0.0 -9.81</p>
<p>Elemental recorders for stress and strain when using the SSPquadUP
element (note the difference from the <a
href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/1098.htm">QuadUP
Element</a>)</p>
<p>recorder Element -eleRange 1 $numElem -time -file stress.out stress
recorder Element -eleRange 1 $numElem -time -file strain.out strain</p>
<p>Pore pressure recorder for the SSPquadUP element (pore pressure is
the third degree-of-freedom)</p>
<p>recorder Node -nodeRange 1 $numNode -time -file porePressure.out -dof
3 vel</p>
## References
<p>McGann, C. R., Arduino, P., and Mackenzie-Helnwein, P. (2012).
“Stabilized single-point 4-node quadrilateral element for dynamic
analysis of fluid saturated porous media.” <em>Acta Geotechnica</em>,
7(4), 297-311.</p>
<p>Zienkiewicz, O.C. and Shiomi, T. (1984). "Dynamic behavior of
saturated porous media; the generalized Biot formulation and its
numerical solution." <em>International Journal for Numerical Methods in
Geomechanics</em>, 8, 71-96.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Chris McGann,
Pedro Arduino, &amp; Peter Mackenzie-Helnwein, at the University of
Washington </span></p>
<hr />
