---
description: Multiple-Vertical-Line-Element-Model for RC Walls
...

# MVLEM 

```tcl
element MVLEM $eleTag $Dens $iNode $jNode $m $c -thick {Thicknesses} \
    -width {Widths} -rho {Reinforcing_ratios} \
    -matConcrete {Concrete_tags} -matSteel {Steel_tags} \
    -matShear {Shear_tag}
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>Unique element object tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Dens</code></td>
<td><p>Wall density</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">iNode jNode</code></p></td>
<td><p>End node tags</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">m</code></td>
<td><p>Number of element macro-fibers</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">c</code></td>
<td><p>Location of center of rotation from the iNode, <em>c</em> = 0.4
(recommended)</p></td>
</tr>
<tr class="even">
<td><p><strong>{Thicknesses}</strong></p></td>
<td><p>Array of <em>m</em> macro-fiber thicknesses</p></td>
</tr>
<tr class="odd">
<td><p><strong>{Widths}</strong></p></td>
<td><p>Array of <em>m</em> macro-fiber widths</p></td>
</tr>
<tr class="even">
<td><p><strong>{Reinforcing_ratios}</strong></p></td>
<td><p>Array of <em>m</em> reinforcing ratios corresponding to
macro-fibers; for each fiber: rho&lt;sub
class="subscript"&gt;i&lt;/sub&gt; = A&lt;sub
class="subscript"&gt;s,i&lt;/sub&gt;/A&lt;sub
class="subscript"&gt;gross,i&lt;/sub&gt; (1 &lt; i &lt; m)</p></td>
</tr>
<tr class="odd">
<td><p><strong>{Concrete _tags}</strong></p></td>
<td><p>Array of <em>m</em> <em>uniaxialMaterial</em> tags for
concrete</p></td>
</tr>
<tr class="even">
<td><p><strong>{Steel_tags}</strong></p></td>
<td><p>Array of <em>m</em> <em>uniaxialMaterial</em> tags for
steel</p></td>
</tr>
<tr class="odd">
<td><p><strong>{Shear_tag}</strong></p></td>
<td><p>Tag of <em>uniaxialMaterial</em> for shear material</p></td>
</tr>
</tbody>
</table>
<hr />
<p><strong>Element Recorders:</strong></p>
<p>The following recorders are available with the <strong>MVLEM</strong>
element:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>globalForce</strong></p></td>
<td><p>Element global forces</p></td>
</tr>
<tr class="even">
<td><p><strong>Curvature</strong></p></td>
<td><p>Element curvature</p></td>
</tr>
<tr class="odd">
<td><p><strong>Shear_Force_Deformation</strong></p></td>
<td><p>Element shear force-deformation relationship</p></td>
</tr>
<tr class="even">
<td><p><strong>Fiber_Strain</strong></p></td>
<td><p>Vertical strains in <em>m</em> fibers along the
cross-section</p></td>
</tr>
<tr class="odd">
<td><p><strong>Fiber_Stress_Concrete</strong></p></td>
<td><p>Vertical concrete stresses in <em>m</em> fibers along the
cross-section</p></td>
</tr>
<tr class="even">
<td><p><strong>Fiber_Stress_Steel</strong></p></td>
<td><p>Vertical steel stresses in <em>m</em> fibers along the
cross-section</p></td>
</tr>
</tbody>
</table>

<p><strong>Code developed by:</strong></p>
<p><a href="mailto:kkolozvari@fullerton.edu"><span style="color:blue"> Kristijan Kolozvari</span>
<span style="color:black"></a>, California State University, Fullerton</p>
<p><span style="color:blue"> Kutay Orakcal&lt;span
style="color:black"&gt;, Bogazici University, Istanbul, Turkey</p>
<p><span style="color:blue"> John Wallace&lt;span
style="color:black"&gt;, Univeristy of California, Los Angeles</p>
<p>The <strong>MVLEM</strong> element command is used to generate a
two-dimensional Multiple-Vertical-Line-Element-Model (MVLEM; Vulcano et
al., 1988; Orakcal et al., 2004, Kolozvari et al., 2015) for simulation
of flexure-dominated RC wall behavior. A single model element
incorporates six global degrees of freedom, three of each located at the
center of rigid top and bottom beams, as illustrated in Figure 1a. The
axial/flexural response of the <strong>MVLEM</strong> is simulated by a
series of uniaxial elements (or macro-fibers) connected to the rigid
beams at the top and bottom (e.g., floor) levels, whereas the shear
response is described by a shear spring located at height <em>ch</em>
from the bottom of the wall element (Figure 1a). Shear and flexural
responses of the model element are uncoupled. The relative rotation
between top and bottom faces of the wall element occurs about the point
located on the central axis of the element at height <em>ch</em> (Figure
1b). Rotations and resulting transverse displacements are calculated
based on the wall curvature, derived from section and material
properties, corresponding to the bending moment at height <em>ch</em> of
each element (Figure 1b). A value of <em>c</em>=0.4 was recommended by
Vulcano et al. (1988) based on comparison of the model response with
experimental results.</p>

<p><strong>Source:</strong>
/usr/local/cvs/OpenSees/SRC/element/MVLEM/</p>
<figure>
<img src="/OpenSeesRT/contrib/static/MVLEM.jpg"
title="Figure 1. a) MVLEM Element, b) MVLEM Rotations and Displacements"
width="700"
alt="Figure 1. a) MVLEM Element, b) MVLEM Rotations and Displacements" />
<figcaption aria-hidden="true">Figure 1. a) MVLEM Element, b) MVLEM
Rotations and Displacements</figcaption>
</figure>
<hr />

<p><strong>Input Format:</strong></p>

<hr />

## Examples

```tcl
Element MVLEM 1 0.0 1 2 8 0.4 -thick 4 4 4 4 4 4 4 4 \
    -width 7.5 1.5 7.5 7.5 7.5 7.5 1.5 7.5 \
    -rho 0.0293 0.0 0.0033 0.0033 0.0033 0.0033 0.0 0.0293 \
    -matConcrete 3 4 4 4 4 4 4 3 -matSteel 1 2 2 2 2 2 2 1 \
    -matShear 5
Recorder Element -file MVLEM_Fgl.out -time -ele 1 globalForce
Recorder Element -file MVLEM_FiberStrain.out -time -ele 1 Fiber_Strain
```

---------------------------

## References

<p>1) Kolozvari K., Orakcal K., and Wallace J. W. (2015). "Shear-Flexure
Interaction Modeling of reinforced Concrete Structural Walls and Columns
under Reversed Cyclic Loading", Pacific Earthquake Engineering Research
Center, University of California, Berkeley, <a
href="http://peer.berkeley.edu/publications/peer_reports/reports_2015/webPEER-2015-12-kolozvari.pdf">PEER
Report No. 2015/12</a></p>
<p>2) Orakcal K. (2004). "Nonlinear Modeling and Analysis of Slender
Reinforced Concrete Walls", PhD Dissertation, Department of Civil and
Environmental Engineering, University of California, Los Angeles.</p>
<p>3) Orakcal K., Conte J.P., and Wallace J.W. (2004). “Flexural
Modeling of Reinforced Concrete Structural Walls - Model Attributes”,
ACI Structural Journal, V. 101, No. 5, pp 688-698.</p>
<p>4) Orakcal K. and Wallace J.W. (2006). “Flexural Modeling of
Reinforced Concrete Structural Walls - Experimental Verification”, ACI
Structural Journal, V. 103, No. 2, pp. 196-206.</p>
<p>5) Vulcano A., Bertero V.V., and Colotti V. (1988). “Analytical
Modeling of RC Structural Walls”, Proceedings, 9th World Conference on
Earthquake Engineering, V. 6, Tokyo-Kyoto, Japan, pp. 41-46.</p>
<hr />
<p><strong>Example 1. Simulation of Flexural Behavior of a Slender RC
Wall Specimen under Cyclic Loading using MVLEM Model</strong></p>
<p>Application of the MVLEM element for simulation of flexural response
of RC walls is illustrated using the RC wall specimen RW2 tested by
Thomsen and Wallace (1995). The specimen was tested under constant axial
load and cyclic lateral displacement history applied at the top of the
wall. Input parameters and selected output results are presented in the
following sections.</p>
<p><strong>E1.1. Model Calibration</strong></p>
<p>Specimen RW2 was 144 <em>in</em> tall, 48 <em>in</em> wide and 4
<em>in</em> thick, resulting in aspect ratio of 3.0 (slender wall).
Figure E1.1 displays model discretization of the RW2 cross-section, with
eight uniaxial elements defined along the length of the wall. The
analytical model was discretized along wall height with 16
<strong>MVLEM</strong> elements with element heights in agreement with
instrumentation provided on the specimen to allow consistent strain
comparisons between model and experimental results. The material models
were calibrated to match as tested material properties. Details about
model calibration and experimental validation are provided by Orakcal
(2004), and Orakcal and Wallace (2004).</p>
<figure>
<img src="/OpenSeesRT/contrib/static/MVLEM_E1.png"
title="Figure E1.1. Geometry and Discretization of Wall Specimen RW2"
width="650"
alt="Figure E1.1. Geometry and Discretization of Wall Specimen RW2" />
<figcaption aria-hidden="true">Figure E1.1. Geometry and Discretization
of Wall Specimen RW2</figcaption>
</figure>
<p><strong>E1.2. Input Files</strong></p>
<p>Input files (.<em>tcl</em>) used to build the wall model and perform
displacement-controlled analysis can be found in <strong><a
href="Media:Example_1._MVLEM.zip" title="wikilink">Example 1.
MVLEM.zip</a></strong>:</p>
<ul>
<li>MVLEM_RW2.tcl - model generation and definition of analysis
parameters</li>
<li>gravity.tcl - application of gravity load</li>
<li>dispControl.tcl - application of lateral displacement history (run
this file)</li>
<li>LibAnalysisStaticParameters.tcl - definition of static analysis
parameters</li>
<li>LibGeneratePeaks.tcl - generation of displacement history</li>
</ul>
<p><strong>E1.3. Analysis Results</strong></p>
<p>Flexural load-deformation responses predicted by the
<strong>MVLEM</strong> model and measured during the experiment are
shown on Figure E1.2.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/MVLEM_E2.png"
title="Figure E1.2. Experimental and Analytical Load versus Flexural Deformation Relationships"
width="450"
alt="Figure E1.2. Experimental and Analytical Load versus Flexural Deformation Relationships" />
<figcaption aria-hidden="true">Figure E1.2. Experimental and Analytical
Load versus Flexural Deformation Relationships</figcaption>
</figure>
<p>Figure E1.3 illustrates the sensitivity of analytical predictions
obtained using the <strong>MVLEM</strong> to the optional gap closure
parameter of the <a
href="http://opensees.berkeley.edu/wiki/index.php/ConcreteCM_-_Complete_Concrete_Model_by_Chang_and_Mander_(1994)"><strong>ConcreteCM</strong></a>
model (<strong>-GapClose $gap</strong>), which allows consideration of
different intensities of gradual gap closure in concrete (Figure E1.3a),
as well as selection of the steel material model <a
href="http://opensees.berkeley.edu/wiki/index.php/SteelMPF_-_Menegotto_and_Pinto_(1973)_Model_Extended_by_Filippou_et_al._(1983)"><strong>SteelMPF</strong></a>
versus <a
href="http://opensees.berkeley.edu/wiki/index.php/Steel02_Material_--_Giuffr%C3%A9-Menegotto-Pinto_Model_with_Isotropic_Strain_Hardening"><strong>Steel02</strong></a>
(Figure E1.3b). It can be observed from Figure E1.3a that pinching
characteristics of the response are slightly more pronounced when less
gradual gap closure versus more gradual gap closure (i.e.,
<strong>gap</strong>=0 versus <strong>gap</strong>=1) is adopted. Figure
E1.3b illustrates that the wall yield capacity as well as pinching
characteristics of the behavior predicted by the <strong>MVLEM</strong>
vary slightly when <strong>SteelMPF</strong> versus
<strong>Steel02</strong> is used.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/MVLEM_E3.png"
title="Figure E1.3. Sensitivity of Analytical Results to Material Modeling Parameters of: a) Concrete, and b) Steel"
width="700"
alt="Figure E1.3. Sensitivity of Analytical Results to Material Modeling Parameters of: a) Concrete, and b) Steel" />
<figcaption aria-hidden="true">Figure E1.3. Sensitivity of Analytical
Results to Material Modeling Parameters of: a) Concrete, and b)
Steel</figcaption>
</figure>
<p>For illustration purposes, additional response predictions obtained
using the <strong>MVLEM</strong> model are presented in Figure E1.4 and
Figure E1.5, where analytically-predicted strain histories at the
outermost and central wall fibers, and concrete and steel strain-stress
relationships at the outermost fiber are presented, respectively.
Responses are obtained using <strong>MVLEM</strong> recorders
<em>Fiber_Strain</em>, <em>Fiber_Stress_Concrete</em>, and
<em>Fiber_Stress_Steel</em>.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/MVLEM_4.png"
title="Figure E1.4. Analytical Strain Histories at Outermost and Central Wall Fibers"
width="500"
alt="Figure E1.4. Analytical Strain Histories at Outermost and Central Wall Fibers" />
<figcaption aria-hidden="true">Figure E1.4. Analytical Strain Histories
at Outermost and Central Wall Fibers</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/MVLEM_5.png"
title="Figure E1.5. Analytically Predicted Stress-Strain Relationships at Wall Outermost Fiber: a) Concrete, b) Steel"
width="700"
alt="Figure E1.5. Analytically Predicted Stress-Strain Relationships at Wall Outermost Fiber: a) Concrete, b) Steel" />
<figcaption aria-hidden="true">Figure E1.5. Analytically Predicted
Stress-Strain Relationships at Wall Outermost Fiber: a) Concrete, b)
Steel</figcaption>
</figure>
