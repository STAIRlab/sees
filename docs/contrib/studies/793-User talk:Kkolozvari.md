# User talk:Kkolozvari

<h2
id="element_mvlem___multiple_vertical_line_element_model_for_rc_walls">Element
MVLEM - Multiple-Vertical-Line-Element-Model for RC Walls</h2>
<p><strong>Developed and Implemented by:</strong></p>
<p><span style="color:blue"> Kristijan Kolozvari&lt;span
style="color:black"&gt;, California State University, Fullerton</p>
<p><span style="color:blue"> Kutay Orakcal&lt;span
style="color:black"&gt;, Bogazici University, Istanbul, Turkey</p>
<p><span style="color:blue"> John Wallace&lt;span
style="color:black"&gt;, Univeristy of California, Los Angeles</p>
<p>The <strong>MVLEM</strong> element command is used to generate a
two-dimensional Multiple-Vertical-Line-Element-Model (MVLEM; Vulcano et
al., 1988; Orakcal et al., 2004) for simulation of flexure-dominated RC
wall behavior. A single model element incorporates six global degrees of
freedom, three of each located at the center of rigid top and bottom
beams, as illustrated in Figure 1a. The axial/flexural response of the
<strong>MVLEM</strong> is simulated by a series of uniaxial elements (or
macro-fibers) connected to the rigid beams at the top and bottom (e.g.,
floor) levels, whereas the shear response is described by a shear spring
located at height <em>ch</em> from the bottom of the wall element
(Figure 1a). Shear and flexural responses of the model element are
uncoupled. The relative rotation between top and bottom faces of the
wall element occurs about the point located on the central axis of the
element at height <em>ch</em> (Figure 1b). Rotations and resulting
transverse displacements are calculated based on the wall curvature,
derived from section and material properties, corresponding to the
bending moment at height <em>ch</em> of each element (Figure 1b). A
value of <em>c</em>=0.4 was recommended by Vulcano et al. (1988) based
on comparison of the model response with experimental results.</p>
<p><strong>Source:</strong>
/usr/local/cvs/OpenSees/SRC/element/MVLEM/</p>
<figure>
<img src="/OpenSeesRT/contrib/static/MVLEM.JPG"
title="Figure 1. a) MVLEM Element, b) MVLEM Rotations and Displacements"
width="700"
alt="Figure 1. a) MVLEM Element, b) MVLEM Rotations and Displacements" />
<figcaption aria-hidden="true">Figure 1. a) MVLEM Element, b) MVLEM
Rotations and Displacements</figcaption>
</figure>
<hr />
<p><strong>Input Format:</strong></p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>Element MVLEM $eleTag $Dens $iNode $jNode $m $c -thick
{Thicknesses} -width {Widths} -rho {Reinforcing_ratios} -matConcrete
{Concrete_tags} -matSteel {Steel_tags} -matShear
{Shear_tag}</strong></p></td>
</tr>
</tbody>
</table>
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
<td><p><strong>$iNode $jNode</strong></p></td>
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
<hr />
<p><strong>Examples:</strong></p>
<p>Element MVLEM 1 0.0 1 2 8 0.4 -thick 4 4 4 4 4 4 4 4 -width 7.5 1.5
7.5 7.5 7.5 7.5 1.5 7.5 -rho 0.0293 0.0 0.0033 0.0033</p>
<p>0.0033 0.0033 0.0 0.0293 -matConcrete 3 4 4 4 4 4 4 3 -matSteel 1 2 2
2 2 2 2 1 -matShear 5</p>
<p>Recorder Element -file MVLEM_Fgl.out -time -ele 1 globalForce</p>
<p>Recorder Element -file MVLEM_FiberStrain.out -time -ele 1
Fiber_Strain</p>
<hr />
<p><strong>References:</strong></p>
<p>1) Orakcal K., Conte J.P., and Wallace J.W. (2004). “Flexural
Modeling of Reinforced Concrete Structural Walls - Model Attributes”,
ACI Structural Journal, V. 101, No. 5, pp 688-698.</p>
<p>2) Orakcal K. and Wallace J.W. (2006). “Flexural Modeling of
Reinforced Concrete Structural Walls - Experimental Verification”, ACI
Structural Journal, V. 103, No. 2, pp. 196-206.</p>
<p>3) Vulcano A., Bertero V.V., and Colotti V. (1988). “Analytical
Modeling of RC Structural Walls”, Proceedings, 9th World Conference on
Earthquake Engineering, V. 6, Tokyo-Kyoto, Japan, pp. 41-46.</p>
<p>4) Orakcal K. (2004). "Nonlinear Modeling and Analysis of Slender
Reinforced Concrete Walls", PhD Dissertation, Department of Civil and
Environmental Engineering, University of California, Los Angeles.</p>
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
href="Media:Example_1-MVLEM.zip" title="wikilink">Example 1.
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
parameter of the <strong>ConcreteCM</strong> model (<strong>-GapClose
$gap</strong>, <strong>LINK</strong>), which allows consideration of
different intensities of gradual gap closure in concrete (Figure E1.3a),
as well as selection of the steel material model
<strong>SteelMPF</strong> versus <strong>Steel02</strong> (Figure
E1.3b). It can be observed from Figure E1.3a that pinching
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
<h2
id="element_sfi_mvlem___cyclic_shear_flexure_interaction_model_for_rc_walls">Element
SFI_MVLEM - Cyclic Shear-Flexure Interaction Model for RC Walls</h2>
<p><strong>Developed and Implemented by:</strong></p>
<p><span style="color:blue"> Kristijan Kolozvari&lt;span
style="color:black"&gt;, California State University, Fullerton</p>
<p><span style="color:blue"> Kutay Orakcal&lt;span
style="color:black"&gt;, Bogazici University, Istanbul, Turkey</p>
<p><span style="color:blue"> John Wallace&lt;span
style="color:black"&gt;, Univeristy of California, Los Angeles</p>
<p>The <strong>SFI_MVLEM</strong> command is used to construct a
Shear-Flexure Interaction Multiple-Vertical-Line-Element Model
(SFI-MVLEM, Kolozvari et al., 2014a, b), which captures interaction
between axial/flexural and shear behavior of RC structural walls and
columns under cyclic loading. The <strong>SFI_MVLEM</strong> element
(Figure 1) incorporates 2-D RC panel behavior described by the
Fixed-Strut-Angle-Model (nDMaterial FSAM; Ulugtekin, 2010; Orakcal et
al., 2012), into a 2-D macroscopic fiber-based model (MVLEM). The
interaction between axial and shear behavior is captured at each RC
panel (macro-fiber) level, which further incorporates interaction
between shear and flexural behavior at the <strong>SFI_MVLEM</strong>
element level.</p>
<p><strong>Source:</strong>
/usr/local/cvs/OpenSees/SRC/element/SFI_MVLEM/</p>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_1.png"
title="Figure 1. a) SFI_MVLEM Element, b) RC Panel Element (nDMaterial FSAM)"
width="650"
alt="Figure 1. a) SFI_MVLEM Element, b) RC Panel Element (nDMaterial FSAM)" />
<figcaption aria-hidden="true">Figure 1. a) SFI_MVLEM Element, b) RC
Panel Element (nDMaterial FSAM)</figcaption>
</figure>
<hr />
<p><strong>Input Format:</strong></p>

```tcl
Element SFI_MVLEM $eleTag $iNode $jNode $m $c -thick
        {Thicknesses} -width {Widths} -mat {Material_tags}
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>Unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode</strong></p></td>
<td><p>End node tags</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">m</code></td>
<td><p>Number of element macro-fibers</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">c</code></td>
<td><p>Location of center of rotation with from the iNode, <em>c</em> =
0.4 (recommended)</p></td>
</tr>
<tr class="odd">
<td><p><strong>{Thicknesses}</strong></p></td>
<td><p>Array of <em>m</em> macro-fiber thicknesses</p></td>
</tr>
<tr class="even">
<td><p><strong>{Widths}</strong></p></td>
<td><p>Array of <em>m</em> macro-fiber widths</p></td>
</tr>
<tr class="odd">
<td><p><strong>{Material_tags}</strong></p></td>
<td><p>Array of <em>m</em> macro-fiber <em>nDMaterial</em>&lt;sup
class="superscript"&gt;1&lt;/sup&gt; tags</p></td>
</tr>
</tbody>
</table>
<p>&lt;sup
class="superscript"&gt;1&lt;/sup&gt;<strong>SFI_MVLEM</strong> element
shall be used with nDMaterial <strong>FSAM</strong>, which is a 2-D
plane-stress constitutive relationship representing reinforced concrete
panel behavior.</p>
<hr />
<p><strong>Element Recorders:</strong></p>
<p>The following recorders are available with the
<strong>SFI_MVLEM</strong> element:</p>
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
<td><p><strong>ShearDef</strong></p></td>
<td><p>Element shear deformation</p></td>
</tr>
<tr class="even">
<td><p><strong>RCPanel $fibTag $Response</strong></p></td>
<td><p>Returns RC panel (macro-fiber) <em>$Response</em> for a
<em>$fibTag</em>-th panel (1 ≤ <em>fibTag</em> ≤ m). For available
<em>$Response</em>-s refer to nDMaterial FSAM
(<strong>LINK</strong>).</p></td>
</tr>
</tbody>
</table>
<hr />
<p><strong>Examples:</strong></p>
<p>Element SFI_MVLEM 1 1 2 5 0.4 -thick 6 6 6 6 6 -width 9 10 10 10 9
-mat 7 6 6 6 7</p>
<p>Recorder Element -file SFI_MVLEM_Fgl.out -time -ele 1 2 3
globalForce</p>
<p>Recorder Element -file SFI_MVLEM_panel_strain.out -time -ele 1
RCPanel 1 panel_strain</p>
<hr />
<p><strong>References:</strong></p>
<p>1) Kolozvari K., Orakcal K., and Wallace J. W. (2015a). ”Modeling of
Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural
Walls. I: Theory”, ASCE Journal of Structural Engineering, 141(5),
04014135 <a
href="http://dx.doi.org/10.1061/(ASCE)ST.1943-541X.0001059">doi</a></p>
<p>2) Kolozvari K., Tran T., Orakcal K., and Wallace, J.W. (2015b).
”Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete
Structural Walls. II: Experimental Validation”, ASCE Journal of
Structural Engineering, 141(5), 04014136 <a
href="http://dx.doi.org/10.1061/(ASCE)ST.1943-541X.0001083">doi</a></p>
<p>3) Kolozvari K. (2013). “Analytical Modeling of Cyclic Shear-Flexure
Interaction in Reinforced Concrete Structural Walls”, PhD Dissertation,
University of California, Los Angeles.</p>
<hr />
<p><strong>Example 1. Simulation of Shear-Flexural Behavior of a
Medium-Rise RC Wall Specimen under Cyclic Loading using the SFI-MVLEM
Model</strong></p>
<p>The behavior of RC wall specimen RW-A15-P10-S78 (Tran and Wallace,
2012) tested under constant axial load and cyclic lateral displacement
history applied at the top of the wall is predicted using the
<strong>SFI_MVLEM</strong> model. The input parameters and output
results are presented in the following sections.</p>
<p><strong>E1.1. Model Calibration</strong></p>
<p>Basic properties of the specimen with model discretization are shown
on Figure E1.1. Detailed information about the test specimen can be
found in paper by Tran and Wallace (2012), whereas details of model
calibration are provided by Kolozvari (2013) and Kolozvari et al.
(2015b).</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Example2_1.png"
title="Figure E1.1. Model discretization: a) Plan view, b) Cross-section"
width="650"
alt="Figure E1.1. Model discretization: a) Plan view, b) Cross-section" />
<figcaption aria-hidden="true">Figure E1.1. Model discretization: a)
Plan view, b) Cross-section</figcaption>
</figure>
<p><strong>E1.2. Input Files</strong></p>
<p>Input files (.<em>tcl</em>) used to build the wall model and perform
displacement-controlled analysis can be found in <strong><a
href="Media:Example_1-SFI_MVLEM.zip" title="wikilink">Example 1.
SFI_MVLEM.zip</a></strong>:</p>
<ul>
<li>SFI_MVLEM_SP4.tcl - model generation and definition of analysis
parameters</li>
<li>gravity.tcl - application of gravity load</li>
<li>dispControl.tcl - application of lateral displacement history (run
this file)</li>
<li>LibAnalysisStaticParameters.tcl - definition of static analysis
parameters</li>
<li>LibGeneratePeaks.tcl - generation of displacement history</li>
</ul>
<p><strong>E1.3. Analysis Results</strong></p>
<p>The following sub-section presents analytical results obtained for
the test specimen described above, using the input files provided. The
results include global wall responses (compared against experimental
results), model element responses, and individual RC panel (macro-fiber)
responses.</p>
<p><em>E1.3.1. Global Wall Responses</em></p>
<p>Analytical and experimental lateral load versus top total
displacement responses and wall cracking patterns are presented on
Figure E1.2, whereas lateral load versus flexural and shear deformations
are shown on Figure E1.3. Total top displacement is obtained from the
top node, shear force is recorded using <em>globalForce</em> element
recorder, total shear displacement is obtained using <em>shearDef</em>
element recorder and crack orientations are obtained using
<em>RCPanel</em> and <em>cracking_angles</em> element recorders.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Example2_2.png"
title="Figure E1.2. Wall responses: a) Load versus Top Displacement Behavior, b) Cracking Patterns"
width="650"
alt="Figure E1.2. Wall responses: a) Load versus Top Displacement Behavior, b) Cracking Patterns" />
<figcaption aria-hidden="true">Figure E1.2. Wall responses: a) Load
versus Top Displacement Behavior, b) Cracking Patterns</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/Example2_3.png"
title="Figure E1.3. Load versus Deformation Behavior for: a) Flexure, b) Shear"
width="650"
alt="Figure E1.3. Load versus Deformation Behavior for: a) Flexure, b) Shear" />
<figcaption aria-hidden="true">Figure E1.3. Load versus Deformation
Behavior for: a) Flexure, b) Shear</figcaption>
</figure>
<p><em>E1.3.2. Model Element Responses</em></p>
<p>Figure E1.4 plots lateral load versus total, flexural and shear
displacement responses, as well as moment versus curvature relationship,
obtained from the analysis for the bottom wall model element. Responses
are recorded using <em>globalForce</em>, <em>ShearDef</em>, and
<em>Curvature</em> element recorders.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Example2_31.png"
title="Figure E1.4. Model Element Responses: a) Shear Force vs. Total Deformation, b) Shear force vs. Flexural Deformation, c) Shear Force vs. Shear Deformation, d) Moment vs. Curvature"
width="650"
alt="Figure E1.4. Model Element Responses: a) Shear Force vs. Total Deformation, b) Shear force vs. Flexural Deformation, c) Shear Force vs. Shear Deformation, d) Moment vs. Curvature" />
<figcaption aria-hidden="true">Figure E1.4. Model Element Responses: a)
Shear Force vs. Total Deformation, b) Shear force vs. Flexural
Deformation, c) Shear Force vs. Shear Deformation, d) Moment vs.
Curvature</figcaption>
</figure>
<p><em>E1.3.3. Reinforced Concrete Panel Responses</em></p>
<p>Various stress-strain responses for an individual boundary panel
element (outermost macro-fiber) within the bottommost wall element are
presented, including total (resultant) stress vs. strain relationships
in the <em>xy</em> plane (Figure E1.5; element <em>RCPanel</em>
recorders: <em>panel_strain</em> and <em>panel_stress</em>),
stress-strain relationships along the two concrete struts (Figure E1.6;
element <em>RCPanel</em> recorders: <em>strain_stress_concrete1</em> and
<em>strain_stress_concrete2</em>), and stress-strain relationship along
horizontal and vertical steel reinforcement (Figure E1.7; element
<em>RCPanel</em> recorders: <em>strain_stress_steelX</em> and
<em>strain_stress_steelY</em>).</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Example2_4.png"
title="Figure E1.5. Panel Total Stress vs. Strain Responses: a) Axial-Horizontal, b) Axial-Vertical, c) Shear"
width="650"
alt="Figure E1.5. Panel Total Stress vs. Strain Responses: a) Axial-Horizontal, b) Axial-Vertical, c) Shear" />
<figcaption aria-hidden="true">Figure E1.5. Panel Total Stress vs.
Strain Responses: a) Axial-Horizontal, b) Axial-Vertical, c)
Shear</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/Example2_5.png"
title="Figure E1.6. Predicted Stress-Strain Behavior for Concrete: a) Strut 1, b) Strut 2"
width="650"
alt="Figure E1.6. Predicted Stress-Strain Behavior for Concrete: a) Strut 1, b) Strut 2" />
<figcaption aria-hidden="true">Figure E1.6. Predicted Stress-Strain
Behavior for Concrete: a) Strut 1, b) Strut 2</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/Example2_6.png"
title="Figure E1.7. Predicted Stress-Strain Behavior for Steel: a) Horizontal (X), b) Vertical (Y)"
width="650"
alt="Figure E1.7. Predicted Stress-Strain Behavior for Steel: a) Horizontal (X), b) Vertical (Y)" />
<figcaption aria-hidden="true">Figure E1.7. Predicted Stress-Strain
Behavior for Steel: a) Horizontal (X), b) Vertical (Y)</figcaption>
</figure>
<hr />
<p><strong>Example 2. Dynamic Analysis of a Coupled Wall-Frame
System</strong></p>
<p>This example illustrates application of the
<strong>SFI_MVLEM</strong> wall model for nonlinear dynamic analysis.
Analytical model of a coupled wall-frame building system was generated
and analyzed under a single ground motion time-history. Brief
description of the building characteristics and the analytical model are
provided in the following sections.</p>
<p><strong>E2.1. Building Description</strong></p>
<p>Plan and elevation/section views of the considered building are shown
in Figure E2.1. The building footprint is 140 <em>ft</em> × 60
<em>ft</em>, with 20 <em>ft</em> long spans. Analysis is conducted for
shaking in the transverse direction only, where the
lateral-force-resisting elements include two identical one-bay frames
located at the building perimeter (axis 1 and 8, Figure E2.1a) and two
identical walls located near the center of the building (axis 4 and 5,
Figure E2.1a). Structural design is performed for a residential building
(I=1.0, risk category I, design category D; ASCE 7-10 S11.5 and S11.6)
for uniformly distributed dead load of 150 <em>psf</em> and live load of
40 <em>psf</em> (ASCE 7-10, Table 4-1), as well as the earthquake
lateral loading obtained using Equivalent Lateral Force Procedure of
ASCE 7-10 (S12.8). The frame was designed to resist 25% of the
earthquake lateral load (Dual System, ASCE 7-10). Concrete compressive
strength of f’&lt;sub class="subscript"&gt;c&lt;/sub&gt; = 5,000
<em>psi</em> and reinforcing steel (both longitudinal and transversal
reinforcement) with yield strength f&lt;sub
class="subscript"&gt;y&lt;/sub&gt; = 60,000 <em>psi</em> were used.
Based on the structural design, cross-section dimensions of 12
<em>in</em> × 240 <em>in</em> (walls), 18 <em>in</em> × 32 <em>in</em>
(beams; width × depth), and 28 <em>in</em> × 28 <em>in</em> (columns)
were adopted. Cross-sections of structural elements with the
reinforcement detailing are provided in Figure E2.2.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_1.png"
title="Figure E2.1. Building Views: a) Plan View, b) Frame Elevation, c) Wall Elevation"
width="500"
alt="Figure E2.1. Building Views: a) Plan View, b) Frame Elevation, c) Wall Elevation" />
<figcaption aria-hidden="true">Figure E2.1. Building Views: a) Plan
View, b) Frame Elevation, c) Wall Elevation</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_2.png"
title="Figure E2.2. Member Cross-Sections: a) Walls, b) Columns, c) Beams"
width="500"
alt="Figure E2.2. Member Cross-Sections: a) Walls, b) Columns, c) Beams" />
<figcaption aria-hidden="true">Figure E2.2. Member Cross-Sections: a)
Walls, b) Columns, c) Beams</figcaption>
</figure>
<p><strong>E2.2. Analytical Model Description</strong></p>
<p>Due to building symmetry and applied direction of the ground motion,
a two-dimensional model consisting of one frame and one wall (Figure
E2.3) is used to simulate the building behavior. The gravity system is
not included in the model (ASCE 7-10) and the assumption of a rigid
diaphragm is implemented within each story level. Tributary mass is
assigned at the element nodes at each story level at locations of axes
of the vertical elements (i.e., wall and columns), whereas gravity load
(dead and live) was assigned according to corresponding tributary areas
as either nodal load at wall-element nodes of each story or uniformly
distributed load along the beams of the frame.</p>
<p>As show on Figure E2.3, the RC wall is modeled using ten equal-length
<strong>SFI_MVLEM</strong> elements along the wall height (i.e., two
elements per story height). Wall discretization in horizontal direction
was performed using six macro-fibers to represent the wall cross
section, where two outer macro-fibers were used to represent the
confined wall boundaries and the remaining four represent the unconfined
wall web. Material models for steel and concrete are calibrated based on
adopted material strengths to represent the behavior of confined and
unconfined concrete and reinforcing steel.</p>
<p>RC frame elements (i.e., beams and columns) are modeled using elastic
beam-column elements by assuming the location of plastic hinges at the
faces of beam-column joints (Figure E2.3a), the behavior of which was
simulated using zero-length elements at locations of hinges and the
elasto-plastic moment-rotation hysteretic model (Modified Ibarra
Krawinkler Deterioration Model; Lignos and Krawinkler, 2011), with
modeling parameters adopted according to beam and column flexural
capacities and the ASCE 41 backbone relationships (Figure E2.3b). The
reduction of flexural stiffness after cracking was considered using
stiffness modifiers for elastic portions of beam and column elements
according to ASCE 41 (Table 6.5).</p>
<p><strong>E2.3. Input Files</strong></p>
<p>Input files (.<em>tcl</em>) used to build the model of a 5-story
wall-frame system and perform gravity and dynamic analysis can be found
in <strong><a href="Media:Example_2-SFI_MVLEM.zip"
title="wikilink">Example 2. SFI_MVLEM.zip</a></strong>:</p>
<ul>
<li>5storyWF_SFI.tcl - model generation, definition of analysis
parameters, gravity analysis</li>
<li>Modal.tcl - modal analysis</li>
<li>Dynamic.tcl - application of earthquake acceleration time-history
(run this file)</li>
<li>MCEScaledEQ1X.acc - earthquake acceleration time history file</li>
<li>DisplayModel2D.tcl - display 2D model</li>
<li>DisplayPlane.tcl - display plane</li>
</ul>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_3.png"
title="Figure E2.3. Analytical Model of Building System: a) Modeling Approach, b) Plastic Hinge Model"
width="650"
alt="Figure E2.3. Analytical Model of Building System: a) Modeling Approach, b) Plastic Hinge Model" />
<figcaption aria-hidden="true">Figure E2.3. Analytical Model of Building
System: a) Modeling Approach, b) Plastic Hinge Model</figcaption>
</figure>
<p><strong>E2.4. Dynamic Analysis Results</strong></p>
<p>Results obtained using analytical model of the building described in
the previous section are presented, including modal properties of the
structure, wall global (i.e., lateral deformations, drifts, shear force,
moments) and local (i.e., vertical strains and rotations) responses.
Responses of the structural elements comprising the RC frame are not
considered.</p>
<p><em>E2.4.1. Dynamic Properties</em></p>
<p>First two building fundamental periods and mode shapes are presented
in Figure E2.4.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_4.png"
title="Figure E2.4. Mode Shapes: a) 1st Mode, b) 2nd Mode" width="800"
alt="Figure E2.4. Mode Shapes: a) 1st Mode, b) 2nd Mode" />
<figcaption aria-hidden="true">Figure E2.4. Mode Shapes: a) 1st Mode, b)
2nd Mode</figcaption>
</figure>
<p><em>E2.4.2. Time-history Responses</em></p>
<p>Time histories of ground motion acceleration, wall top nodal
displacement, and wall base shear force (bottom wall node reaction) are
presented in Figure 2.5; the responses are obtained using
<em>globalForce</em> and <em>Reactions</em> node recorders.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_5.png"
title="Figure E2.5. Global Building Responses" width="500"
alt="Figure E2.5. Global Building Responses" />
<figcaption aria-hidden="true">Figure E2.5. Global Building
Responses</figcaption>
</figure>
<p><em>E2.4.3. Maximum Global Responses over the Wall Height</em></p>
<p>Maximum envelopes of wall lateral displacements and interstory
drifts, and shear force and bending moment are presented in Figure E2.6
and Figure E2.7, respectively. Wall lateral displacements and drifts are
obtained using corresponding node recorders, <em>disp</em> and
<em>drift</em>, whereas shear force and bending moments over the wall
height are recorded using element recorders <em>globalForce</em>.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_6.png"
title="Figure E2.6. Maximum Deformation Responses: a) Lateral Displacements, b) Interstory Drifts"
width="625"
alt="Figure E2.6. Maximum Deformation Responses: a) Lateral Displacements, b) Interstory Drifts" />
<figcaption aria-hidden="true">Figure E2.6. Maximum Deformation
Responses: a) Lateral Displacements, b) Interstory Drifts</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_7.png"
title="Figure E2.7. Maximum Shear Force and Bending Moment over Wall Height"
width="625"
alt="Figure E2.7. Maximum Shear Force and Bending Moment over Wall Height" />
<figcaption aria-hidden="true">Figure E2.7. Maximum Shear Force and
Bending Moment over Wall Height</figcaption>
</figure>
<p><em>E2.4.4. Bottom Wall Element Responses</em></p>
<p>Figure E2.8 plots the responses of the bottom wall element, including
lateral load versus total, flexural and shear displacement, and moment
versus curvature relationship obtained from the dynamic analysis. Note
that wall element shear displacement and curvature time-histories are
obtained using <strong>SFI_MVLEM</strong> element recorders
<em>ShearDef</em> and <em>Curvature</em>, respectively, whereas shear
force and bending moment are recorded using element recorder
<em>globalForce</em>.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_8.png"
title="Figure E2.8. Model Element Responses: a) Lateral Load vs. Displacement, b) Lateral Load vs. Flexural Deformation, c) Lateral Load vs. Shear Deformation, d) Moment vs. Curvature"
width="650"
alt="Figure E2.8. Model Element Responses: a) Lateral Load vs. Displacement, b) Lateral Load vs. Flexural Deformation, c) Lateral Load vs. Shear Deformation, d) Moment vs. Curvature" />
<figcaption aria-hidden="true">Figure E2.8. Model Element Responses: a)
Lateral Load vs. Displacement, b) Lateral Load vs. Flexural Deformation,
c) Lateral Load vs. Shear Deformation, d) Moment vs.
Curvature</figcaption>
</figure>
<p><em>E2.4.5. Single RC Panel Responses</em></p>
<p>Analytically-predicted strain-stress responses of a single RC panel
(macro-fiber) located at the left wall boundary of the bottom wall
element are presented. Global panel stress-strain relationships
presented on Figure E2.9 are obtained using element recorder
<em>RCPanel</em> with commands <em>panel_strain</em> and
<em>panel_stress</em>; the uniaxial behavior of concrete along the two
concrete struts presented on Figure E2.10 are recorded using
<em>strain_stress_concrete1</em> and <em>strain_stress_concrete2</em>
commands; uniaxial stress-strain behavior of horizontal and vertical
reinforcing steel presented on Figure E2.11 are obtained using
<em>strain_stress_steelX</em> and <em>strain_stress_steelY</em>
commands. Other panel responses described in Section 3 could be plotted
in a similar manner.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_9.png"
title="Figure E2.9. Panel Total Stress vs. Strain Responses: a) Axial-Horizontal, b) Axial-Vertical, c) Shear"
width="650"
alt="Figure E2.9. Panel Total Stress vs. Strain Responses: a) Axial-Horizontal, b) Axial-Vertical, c) Shear" />
<figcaption aria-hidden="true">Figure E2.9. Panel Total Stress vs.
Strain Responses: a) Axial-Horizontal, b) Axial-Vertical, c)
Shear</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_10.png"
title="Figure E2.10. Predicted Stress-Strain Behavior for Concrete: a) Strut 1, b) Strut 2"
width="625"
alt="Figure E2.10. Predicted Stress-Strain Behavior for Concrete: a) Strut 1, b) Strut 2" />
<figcaption aria-hidden="true">Figure E2.10. Predicted Stress-Strain
Behavior for Concrete: a) Strut 1, b) Strut 2</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_11.png"
title="Figure E2.11. Predicted Stress-Strain Behavior for Steel: a) Horizontal (X), b) Vertical (Y)"
width="625"
alt="Figure E2.11. Predicted Stress-Strain Behavior for Steel: a) Horizontal (X), b) Vertical (Y)" />
<figcaption aria-hidden="true">Figure E2.11. Predicted Stress-Strain
Behavior for Steel: a) Horizontal (X), b) Vertical (Y)</figcaption>
</figure>
<p>Finally, vertical profiles of maximum vertical strains (Figure
E2.12a) are obtained using element recorder with <em>RCPanel</em> and
<em>panel_strain</em> recorder commands, whereas maximum wall rotations
over the wall height (Figure E2.12b) are derived from element
<em>Curvature</em> recorder. Similarly, the distribution of other wall
responses could be plotted over the wall height (e.g., shear
deformations, etc.).</p>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_12.png"
title="Figure E2.12. Local Responses - Vertical Profiles of Maximum: a) Vertical Strains, b) Rotations"
width="625"
alt="Figure E2.12. Local Responses - Vertical Profiles of Maximum: a) Vertical Strains, b) Rotations" />
<figcaption aria-hidden="true">Figure E2.12. Local Responses - Vertical
Profiles of Maximum: a) Vertical Strains, b) Rotations</figcaption>
</figure>
<h2
id="uniaxialmaterial_steelmpf___steel_material_model_by_menegotto_and_pinto_1973_extended_by_filippou_et_al._1983">uniaxialMaterial
SteelMPF - Steel Material Model by Menegotto and Pinto (1973) extended
by Filippou et al. (1983)</h2>
<p><strong>Developed and Implemented by:</strong></p>
<p><span style="color:blue"> Kristijan Kolozvari&lt;span
style="color:black"&gt;, California State University, Fullerton</p>
<p><span style="color:blue"> Kutay Orakcal&lt;span
style="color:black"&gt;, Bogazici University, Istanbul, Turkey</p>
<p><span style="color:blue"> John Wallace&lt;span
style="color:black"&gt;, Univeristy of California, Los Angeles</p>
<p>This command is used to construct a uniaxialMaterial
<strong>SteelMPF</strong>, which represents the well-known uniaxial
constitutive nonlinear hysteretic material model for steel proposed by
Menegotto and Pinto (1973), and extended by Filippou et al. (1983) to
include isotropic strain hardening effects. The relationship is in the
form of curved transitions (Figure 1), each from a straight-line
asymptote with slope E&lt;sub class="subscript"&gt;0&lt;/sub&gt;
(modulus of elasticity) to another straight-line asymptote with slope
E&lt;sub class="subscript"&gt;1&lt;/sub&gt; = bE&lt;sub
class="subscript"&gt;0&lt;/sub&gt; (yield modulus) where <em>b</em> is
the strain hardening ratio. The curvature of the transition curve
between the two asymptotes is governed by a cyclic curvature parameter
<em>R</em>, which permits the Bauschinger effect to be represented, and
is dependent on the absolute strain difference between the current
asymptote intersection point and the previous maximum or minimum strain
reversal point depending on whether the current strain is increasing or
decreasing, respectively. The strain and stress pairs (ε&lt;sub
class="subscript"&gt;r&lt;/sub&gt;,σ&lt;sub
class="subscript"&gt;r&lt;/sub&gt;) and (ε&lt;sub
class="subscript"&gt;0&lt;/sub&gt;,σ&lt;sub
class="subscript"&gt;0&lt;/sub&gt;) shown on Figure 1 are updated after
each strain reversal.</p>
<p><strong>Source:</strong>
/usr/local/cvs/OpenSees/SRC/material/uniaxial/</p>
<figure>
<img src="/OpenSeesRT/contrib/static/SteelMPF.png"
title="Figure 1. Constitutive Model for Steel (Menegotto and Pinto, 1973)"
width="500"
alt="Figure 1. Constitutive Model for Steel (Menegotto and Pinto, 1973)" />
<figcaption aria-hidden="true">Figure 1. Constitutive Model for Steel
(Menegotto and Pinto, 1973)</figcaption>
</figure>
<hr />
<p><strong>Input Format:</strong></p>

```tcl
uniaxialMaterial SteelMPF $mattag $fyp $fyn $E0 $bp $bn
        $R0 $a1 $a2 &lt;$a3 $a4&gt;
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">mattag</code></td>
<td><p>Unique <em>uniaxialMaterial</em> tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fyp</code></td>
<td><p>Yield strength in tension (positive loading direction)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fyn</code></td>
<td><p>Yield strength in compression (negative loading
direction)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">E0</code></td>
<td><p>Initial tangent modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">bp</code></td>
<td><p>Strain hardening ratio in tension (positive loading
direction)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">bn</code></td>
<td><p>Strain hardening ratio in compression (negative loading
direction)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">R0</code></td>
<td><p>Initial value of the curvature parameter R (R0 = 20
recommended)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">a1</code></p></td>
<td><p>Curvature degradation parameter (a1 = 18.5 recommended)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">a2</code></p></td>
<td><p>Curvature degradation parameter (a2 = 0.15 or 0.0015
recommended)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">a3</code></p></td>
<td><p>Isotropic hardening parameter (optional, default = 0.01)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">a4</code></p></td>
<td><p>Isotropic hardening parameter (optional, default = 7.0)</p></td>
</tr>
</tbody>
</table>
<hr />
<p><strong>Example:</strong></p>
<p>uniaxialMaterial SteelMPF 1 60 60 29000 0.02 0.02 20.0 18.5 0.15</p>
<hr />
<p><strong>Discussion:</strong></p>
<p>Although the Menegotto-Pinto model is already available in OpenSees
(e.g., <strong>Steel02</strong>), the formulation of
<strong>SteelMPF</strong> introduces several distinctive features
compared to existing models. For example, the model allows definition of
different yield stress values and strain hardening ratios for tension
and compression, and it considers degradation of cyclic curvature
parameter <em>R</em> for strain reversals in both pre- and post-
yielding regions, which could produce more accurate predictions of yield
capacity for some RC wall specimens (see <strong>LINK</strong> Example
1), whereas <strong>Steel02</strong> considers the degradation in
post-yielding region only. Strain-stress relationships obtained using
<strong>SteelMPF</strong> and <strong>Steel02</strong> are compared in
Figure 2 for a strain history that includes strain reversals at strain
values equal to one-half of the yield strain (e.i.,
&lt;math&gt;\epsilon&lt;/math&gt;&lt;sub
class="subscript"&gt;r&lt;/sub&gt; = ±0.001 =
&lt;math&gt;\epsilon&lt;/math&gt;&lt;sub
class="subscript"&gt;y/2&lt;/sub&gt;). The model also allows calibration
of isotropic hardening parameters through optional input variables
<em>a&lt;sub class="subscript"&gt;3&lt;/sub&gt;</em> and <em>a&lt;sub
class="subscript"&gt;4&lt;/sub&gt;</em>, and uses default values of
<em>a&lt;sub class="subscript"&gt;3&lt;/sub&gt;</em> = 0.01 and
<em>a&lt;sub class="subscript"&gt;4&lt;/sub&gt;</em> = 7.0 as calibrated
by Filippou et al. (1983) based on test results. To disregard isotropic
strain hardening behavior in <strong>SteelMPF</strong>, parameter
<em>a&lt;sub class="subscript"&gt;3&lt;/sub&gt;</em> needs to be
assigned a zero value (<em>a&lt;sub
class="subscript"&gt;3&lt;/sub&gt;</em> = 0.0).</p>
<figure>
<img src="/OpenSeesRT/contrib/static/SteelMPF_1.png"
title="Figure 2. Comparison of Steel02 and SteelMPF" width="500"
alt="Figure 2. Comparison of Steel02 and SteelMPF" />
<figcaption aria-hidden="true">Figure 2. Comparison of Steel02 and
SteelMPF</figcaption>
</figure>
<hr />
<p><strong>References:</strong></p>
<p>1) Filippou F.C., Popov, E.P., and Bertero, V.V. (1983). "Effects of
Bond Deterioration on Hysteretic Behavior of Reinforced Concrete
Joints". Report EERC 83-19, Earthquake Engineering Research Center,
University of California, Berkeley.</p>
<p>2) Menegotto, M., and Pinto, P.E. (1973). Method of analysis of
cyclically loaded RC plane frames including changes in geometry and
non-elastic behavior of elements under normal force and bending.
Preliminary Report IABSE, vol 13.</p>
<h2
id="uniaxialmaterial_concretecm___complete_concrete_model_by_chang_and_mander_1994">uniaxialMaterial
ConcreteCM - Complete Concrete Model by Chang and Mander (1994)</h2>
<p><strong>Developed and Implemented by:</strong></p>
<p><span style="color:blue"> Kristijan Kolozvari&lt;span
style="color:black"&gt;, California State University, Fullerton</p>
<p><span style="color:blue"> Kutay Orakcal&lt;span
style="color:black"&gt;, Bogazici University, Istanbul, Turkey</p>
<p><span style="color:blue"> John Wallace&lt;span
style="color:black"&gt;, Univeristy of California, Los Angeles</p>
<p>This command is used to construct a uniaxialMaterial
<strong>ConcreteCM</strong>, which is a uniaxial hysteretic constitutive
model for concrete developed by Chang and Mander (1994). This model is a
refined, rule-based, generalized, and non-dimensional constitutive model
that allows calibration of the monotonic and hysteretic material
modeling parameters, and can simulate the hysteretic behavior of
confined and unconfined, ordinary and high-strength concrete, in both
cyclic compression and tension (Figure 1). The model addresses important
behavioral features, such as continuous hysteretic behavior under cyclic
compression and tension, progressive stiffness degradation associated
with smooth unloading and reloading curves at increasing strain values,
and gradual crack closure effects. Details of the model are available in
the report by Chang and Mander (1994).</p>
<figure>
<img src="/OpenSeesRT/contrib/static/ConcreteCM_0.png"
title="Figure 1. Hysteretic Constitutive Model for Concrete by Chang and Mander (1994)"
width="500"
alt="Figure 1. Hysteretic Constitutive Model for Concrete by Chang and Mander (1994)" />
<figcaption aria-hidden="true">Figure 1. Hysteretic Constitutive Model
for Concrete by Chang and Mander (1994)</figcaption>
</figure>
<p>The Chang and Mander (1994) model successfully generates continuous
hysteretic stress-strain relationships with slope continuity for
confined and unconfined concrete in both compression and tension. The
compression envelope curve of the model is defined by the initial
tangent slope, (E&lt;sub class="subscript"&gt;c&lt;/sub&gt;), the peak
coordinate (&lt;math&gt;\epsilon&lt;/math&gt;'&lt;sub
class="subscript"&gt;c&lt;/sub&gt;, f'&lt;sub
class="subscript"&gt;c&lt;/sub&gt;), a parameter (r&lt;sub
class="subscript"&gt;c&lt;/sub&gt;) from Tsai’s (1988) equation defining
the shape of the envelope curve, and a parameter
(&lt;math&gt;\epsilon&lt;/math&gt;&lt;sup
class="superscript"&gt;-&lt;/sup&gt;&lt;sub
class="subscript"&gt;cr&lt;/sub&gt;) to define normalized (with respect
to $\epsilon$'&lt;sub
class="subscript"&gt;c&lt;/sub&gt;) strain where the envelope curve
starts following a straight line, until zero compressive stress is
reached at the spalling strain, $\epsilon$&lt;sub
class="subscript"&gt;sp&lt;/sub&gt;. These parameters can be controlled
based on specific experimental results for a refined calibration of the
compression envelope (Figure 2). Chang and Mander (1994) proposed
empirical relationships for parameters E&lt;sub
class="subscript"&gt;c&lt;/sub&gt;,
&lt;math&gt;\epsilon&lt;/math&gt;'&lt;sub
class="subscript"&gt;c&lt;/sub&gt;, and r&lt;sub
class="subscript"&gt;c&lt;/sub&gt; for unconfined concrete with
compressive strength f'&lt;sub class="subscript"&gt;c&lt;/sub&gt;, based
on review of previous research. Parameters f'&lt;sub
class="subscript"&gt;c&lt;/sub&gt;,
&lt;math&gt;\epsilon&lt;/math&gt;'&lt;sub
class="subscript"&gt;c&lt;/sub&gt;, E&lt;sub
class="subscript"&gt;c&lt;/sub&gt;, r&lt;sub
class="subscript"&gt;c&lt;/sub&gt;, and
&lt;math&gt;\epsilon&lt;/math&gt;&lt;sup
class="superscript"&gt;-&lt;/sup&gt;&lt;sub
class="subscript"&gt;cr&lt;/sub&gt; can also be calibrated to represent
the stress-strain behavior of confined concrete in compression, to
follow the constitutive relationships for confined concrete proposed by
Mander et al (1988) or similar.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/ConcreteCM_1.png"
title="Figure 2. Compression and Tension Envelope Curves" width="500"
alt="Figure 2. Compression and Tension Envelope Curves" />
<figcaption aria-hidden="true">Figure 2. Compression and Tension
Envelope Curves</figcaption>
</figure>
<p>The shape of the tension envelope curve in the model is the same as
that of the compression envelope; however, the tension envelope curve is
shifted to a new origin that is based on the unloading strain from the
compression envelope (Figure 2). As well, the strain ductility
experienced previously on the compression envelope is also reflected on
the tension envelope. The parameters associated with the tension
envelope curve include the tensile strength of concrete (f&lt;sub
class="subscript"&gt;t&lt;/sub&gt;), the monotonic strain at tensile
strength (&lt;math&gt;\epsilon&lt;/math&gt;&lt;sub
class="subscript"&gt;t&lt;/sub&gt;), a parameter (r&lt;sub
class="subscript"&gt;t&lt;/sub&gt;) from Tsai’s (1988) equation defining
the shape of the tension envelope curve, and a parameter
(&lt;math&gt;\epsilon&lt;/math&gt;&lt;sup
class="superscript"&gt;+&lt;/sup&gt;&lt;sub
class="subscript"&gt;cr&lt;/sub&gt;) to define normalized (with respect
to $\epsilon$&lt;sub
class="subscript"&gt;t&lt;/sub&gt;) strain where the tension envelope
curve starts following a straight line, until zero tensile stress is
reached at a strain of $\epsilon$&lt;sub
class="subscript"&gt;crk&lt;/sub&gt;. These parameters can also be
controlled and calibrated based on specific experimental results or
empirical relations proposed by other researchers (e.g., Belarbi and
Hsu, 1994) to model the behavior of concrete in tension and the tension
stiffening phenomenon. Concrete experiencing tension stiffening can be
considered not to crack completely; that is, a large value for parameter
&lt;math&gt;\epsilon&lt;/math&gt;&lt;sup
class="superscript"&gt;+&lt;/sup&gt;&lt;sub
class="subscript"&gt;cr&lt;/sub&gt; (e.g., 10000) can be defined.</p>
<p>Source: /usr/local/cvs/OpenSees/SRC/material/uniaxial/</p>
<hr />
<p><strong>Input Format:</strong></p>

```tcl
uniaxialMaterial ConcreteCM $mattag $fpcc $epcc $Ec $rc
        $xcrn $ft $et $rt $xcrp &lt;-GapClose $gap&gt;
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">mattag</code></td>
<td><p>Unique <em>uniaxialMaterial</em> tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fpcc</code></td>
<td><p>Compressive strength (f'&lt;sub
class="subscript"&gt;c&lt;/sub&gt;)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epcc</code></td>
<td><p>Strain at compressive strength
(&lt;math&gt;\epsilon&lt;/math&gt;'&lt;sub
class="subscript"&gt;c&lt;/sub&gt;)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Ec</code></td>
<td><p>Initial tangent modulus (E&lt;sub
class="subscript"&gt;c&lt;/sub&gt;)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rc</code></td>
<td><p>Shape parameter in Tsai’s equation defined for compression
(r&lt;sub class="subscript"&gt;c&lt;/sub&gt;)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">xcrn</code></td>
<td><p>Non-dimensional critical strain on compression envelope
(&lt;math&gt;\epsilon&lt;/math&gt;&lt;sup
class="superscript"&gt;-&lt;/sup&gt;&lt;sub
class="subscript"&gt;cr&lt;/sub&gt;, where the envelope curve starts
following a straight line)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ft</code></td>
<td><p>Tensile strength (f&lt;sub
class="subscript"&gt;t&lt;/sub&gt;)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rt</code></td>
<td><p>Shape parameter in Tsai’s equation defined for tension (r&lt;sub
class="subscript"&gt;t&lt;/sub&gt;)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">xcrp</code></td>
<td><p>Non-dimensional critical strain on tension envelope
(&lt;math&gt;\epsilon&lt;/math&gt;&lt;sup
class="superscript"&gt;+&lt;/sup&gt;&lt;sub
class="subscript"&gt;cr&lt;/sub&gt;, where the envelope curve starts
following a straight line - large value [e.g., 10000] recommended when
tension stiffening is considered)</p></td>
</tr>
<tr class="even">
<td><p><strong>&lt;-GapClose $gap&gt;</strong></p></td>
<td><p><strong>gap</strong> = 0, less gradual gap closure (default);
<strong>gap</strong> = 1, more gradual gap closure</p></td>
</tr>
</tbody>
</table>
<hr />
<p><strong>Example:</strong></p>
<p>uniaxialMaterial ConcreteCM 1 -6.2 -0.0021 4500 7 1.035 0.30 0.00008
1.2 10000</p>
<p>Example of hysteretic stress-strain history generated by the model
code is illustrated in Figure 3.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/ConcreteCM_2.PNG"
title="Figure 3. Concrete Stress-Strain Behavior" width="500"
alt="Figure 3. Concrete Stress-Strain Behavior" />
<figcaption aria-hidden="true">Figure 3. Concrete Stress-Strain
Behavior</figcaption>
</figure>
<hr />
<p><strong>Discussion:</strong></p>
<p>An optional input parameter <strong>gap</strong> is introduced in the
<strong>ConcreteCM</strong> model implemented in OpenSees for providing
the users with the opportunity to control the intensity of gap closure
in the stress-strain behavior of concrete, which in-turn influences the
level of pinching in the lateral load-displacement behavior of a RC
wall. The original Chang and Mander (1994) model adopts a non-zero
tangent stiffness at zero stress level upon unloading from the tension
envelope, which is represented by gap = 1 in
<strong>ConcreteCM</strong>. Using <strong>gap</strong> = 0 (default)
produces less gradual gap closure, since it assumes zero tangent
stiffness at zero stress level upon unloading from the tension envelope,
and is suitable for most analyses. Figure 4 illustrates the effect of
plastic stiffness upon unloading from tension envelope (E&lt;sup
class="superscript"&gt;+&lt;/sup&gt;&lt;sub
class="subscript"&gt;pl&lt;/sub&gt;) on crack closure, i.e. use of more
gradual (<strong>gap</strong> = 1) or less gradual (<strong>gap</strong>
= 0) gap closure.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/ConcreteCM_3.png"
title="Figure 4. Effect of Plastic Stiffness upon Unloading from Tension Envelope (Epl+) on Crack Closure"
width="500"
alt="Figure 4. Effect of Plastic Stiffness upon Unloading from Tension Envelope (Epl+) on Crack Closure" />
<figcaption aria-hidden="true">Figure 4. Effect of Plastic Stiffness
upon Unloading from Tension Envelope (Epl+) on Crack
Closure</figcaption>
</figure>
<p>Constitutive stress-strain concrete behavior is also implemented in
OpenSees in uniaxialMaterial <strong>Cocnrete07</strong>. However,
<strong>ConcreteCM</strong> incorporates sophisticated
unloading/reloading rules defined originally by Chang and Mander (1994),
as opposed to <strong>Concrete07</strong> that adopts simplified
hysteretic rules. Comparison between stress-strain response predicted
using <strong>ConcreteCM</strong> and <strong>Concrete07</strong> is
shown in Figure 5.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/ConcreteCMvsConcrete07.png"
title="Figure 5. Comparison of ConcreteCM and Concrete07" width="500"
alt="Figure 5. Comparison of ConcreteCM and Concrete07" />
<figcaption aria-hidden="true">Figure 5. Comparison of ConcreteCM and
Concrete07</figcaption>
</figure>
<hr />
<p><strong>References:</strong></p>
<p>1) Belarbi H. and Hsu T.C.C. (1994). “Constitutive Laws of Concrete
in Tension and Reinforcing Bars Stiffened by Concrete”, ACI Structural
Journal, V. 91, No. 4, pp. 465-474.</p>
<p>2) Chang, G.A. and Mander, J.B. (1994), “Seismic Energy Based Fatigue
Damage Analysis of Bridge Columns: Part I - Evaluation of Seismic
Capacity”, NCEER Technical Report No. NCEER-94-0006, State University of
New York, Buffalo.</p>
<p>3) Mander J.B., Priestley M.J.N., and Park R. (1988). “Theoretical
Stress-Strain Model for Confined Concrete”, ASCE Journal of Structural
Engineering, V. 114, No. 8, pp. 1804-1826.</p>
<p>4) Orakcal K.(2004), "Nonlinear Modeling and Analysis of Slender
Reinforced Concrete Walls", PhD Dissertation, Department of Civil and
Environmental Engineering, University of California, Los Angeles.</p>
<h2 id="ndmaterial_fsam___2d_rc_panel_constitutive_behavior">NDMaterial
FSAM - 2D RC Panel Constitutive Behavior</h2>
<p><strong>Developed and Implemented by:</strong></p>
<p><span style="color:blue"> Kristijan Kolozvari&lt;span
style="color:black"&gt;, California State University, Fullerton</p>
<p><span style="color:blue"> Kutay Orakcal&lt;span
style="color:black"&gt;, Bogazici University, Istanbul, Turkey</p>
<p><span style="color:blue"> Leonardo Massone&lt;span
style="color:black"&gt;, University of Chile, Santiago</p>
<p><span style="color:blue"> John Wallace&lt;span
style="color:black"&gt;, Univeristy of California, Los Angeles</p>
<p>This command is used to construct a nDMaterial <strong>FSAM</strong>
(Fixed-Strut-Angle-Model, Figure 1), which is a plane-stress
constitutive model for simulating the behavior of RC panel elements
under generalized, in-plane, reversed-cyclic loading conditions
(Ulugtekin, 2010; Orakcal et al., 2012). In the <strong>FSAM</strong>
constitutive model, the strain fields acting on concrete and reinforcing
steel components of a RC panel are assumed to be equal to each other,
implying perfect bond assumption between concrete and reinforcing steel
bars. While the reinforcing steel bars develop uniaxial stresses under
strains in their longitudinal direction, the behavior of concrete is
defined using stress-strain relationships in biaxial directions, the
orientation of which is governed by the state of cracking in concrete.
Although the concrete stress-strain relationship used in the
<strong>FSAM</strong> is fundamentally uniaxial in nature, it also
incorporates biaxial softening effects including compression softening
and biaxial damage. For transfer of shear stresses across the cracks, a
friction-based elasto-plastic shear aggregate interlock model is
adopted, together with a linear elastic model for representing dowel
action on the reinforcing steel bars (Kolozvari, 2013).</p>
<p><strong>Source:</strong>
/usr/local/cvs/OpenSees/SRC/material/nD/reinforcedConcretePlaneStress/</p>
<figure>
<img src="/OpenSeesRT/contrib/static/FSAM_1.png"
title="Figure 1. FSAM for Converting In-Plane Strains to In-Plane Smeared Stresses on a RC Panel Element"
width="500"
alt="Figure 1. FSAM for Converting In-Plane Strains to In-Plane Smeared Stresses on a RC Panel Element" />
<figcaption aria-hidden="true">Figure 1. FSAM for Converting In-Plane
Strains to In-Plane Smeared Stresses on a RC Panel Element</figcaption>
</figure>
<hr />
<p><strong>Input Format:</strong></p>

```tcl
nDMaterial FSAM $mattag $rho $sX $sY $conc $rouX $rouY
        $nu $alfadow
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">mattag</code></td>
<td><p>Unique nDMaterial tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>Material density</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">sX</code></td>
<td><p>Tag of uniaxialMaterial simulating horizontal (x)
reinforcement</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">sY</code></td>
<td><p>Tag of uniaxialMaterial simulating vertical (y)
reinforcement</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">conc</code></td>
<td><p>Tag of uniaxialMaterial&lt;sup
class="superscript"&gt;1&lt;/sup&gt; simulating concrete</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rouX</code></td>
<td><p>Reinforcing ratio in horizontal (x) direction (rouX = A&lt;sub
class="subscript"&gt;s,x&lt;/sub&gt;/A&lt;sub
class="subscript"&gt;gross,x&lt;/sub&gt;)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rouY</code></td>
<td><p>Reinforcing ratio in vertical (y) direction (rouY = A&lt;sub
class="subscript"&gt;s,y&lt;/sub&gt;/A&lt;sub
class="subscript"&gt;gross,y&lt;/sub&gt;)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">nu</code></td>
<td><p>Concrete friction coefficient (0.0 &lt; nu &lt; 1.5)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">alfadow</code></td>
<td><p>Stiffness coefficient of reinforcement dowel action (0.0 &lt;
alfadow &lt; 0.05)</p></td>
</tr>
</tbody>
</table>
<p>&lt;sup class="superscript"&gt;1&lt;/sup&gt;nDMaterial
<strong>FSAM</strong> shall be used with uniaxialMaterial
<strong>ConcreteCM</strong></p>
<p>Recommended values for parameter of a shear resisting mechanism
(<strong>nu</strong> and <strong>alfadow</strong>, Figure 2) are
provided above. Details about the sensitivity of analytical predictions
using SFI_MVLEM to changes in these parameters are presented by
Kolozvari (2013).</p>
<hr />
<p><strong>Material Recorders:</strong></p>
<p>The following output is available from the <strong>FSAM</strong> RC
panel model:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>panel_strain</strong></p></td>
<td><p>Strains ε&lt;sub class="subscript"&gt;x&lt;/sub&gt;, ε&lt;sub
class="subscript"&gt;y&lt;/sub&gt;, &amp;gamma;&lt;sub
class="subscript"&gt;xy&lt;/sub&gt; (Figure 4)</p></td>
</tr>
<tr class="even">
<td><p><strong>panel_stress</strong></p></td>
<td><p>Resulting panel stresses σ&lt;sub
class="subscript"&gt;x&lt;/sub&gt;, σ&lt;sub
class="subscript"&gt;y&lt;/sub&gt;, &amp;tau;&lt;sub
class="subscript"&gt;xy&lt;/sub&gt; (concrete and steel, Figure
1)</p></td>
</tr>
<tr class="odd">
<td><p><strong>panel_stress_concrete</strong></p></td>
<td><p>Resulting panel concrete stresses σ&lt;sub
class="subscript"&gt;xc&lt;/sub&gt;, σ&lt;sub
class="subscript"&gt;yc&lt;/sub&gt;, &amp;tau;&lt;sub
class="subscript"&gt;xyc&lt;/sub&gt; (Figure 2b)</p></td>
</tr>
<tr class="even">
<td><p><strong>panel_stress_steel</strong></p></td>
<td><p>Resulting panel steel stresses σ&lt;sub
class="subscript"&gt;xs&lt;/sub&gt;, σ&lt;sub
class="subscript"&gt;ys&lt;/sub&gt;, &amp;tau;&lt;sub
class="subscript"&gt;xys&lt;/sub&gt; (Figure 2d)</p></td>
</tr>
<tr class="odd">
<td><p><strong>strain_stress_steelX</strong></p></td>
<td><p>Uniaxial strain and stress of horizontal reinforcement ε&lt;sub
class="subscript"&gt;x&lt;/sub&gt;, σ&lt;sub
class="subscript"&gt;xxs&lt;/sub&gt;</p></td>
</tr>
<tr class="even">
<td><p><strong>strain_stress_steelY</strong></p></td>
<td><p>Uniaxial strain and stress of vertical reinforcement ε&lt;sub
class="subscript"&gt;y&lt;/sub&gt;, σ&lt;sub
class="subscript"&gt;yys&lt;/sub&gt;</p></td>
</tr>
<tr class="odd">
<td><p><strong>strain_stress_concrete1</strong></p></td>
<td><p>Uniaxial strain and stress of concrete strut 1 ε&lt;sub
class="subscript"&gt;c1&lt;/sub&gt;, σ&lt;sub
class="subscript"&gt;c1&lt;/sub&gt;</p></td>
</tr>
<tr class="even">
<td><p><strong>strain_stress_concrete2</strong></p></td>
<td><p>Uniaxial strain and stress of concrete strut 2 ε&lt;sub
class="subscript"&gt;c2&lt;/sub&gt;, σ&lt;sub
class="subscript"&gt;c2&lt;/sub&gt;</p></td>
</tr>
<tr class="odd">
<td><p><strong>strain_stress_interlock1</strong></p></td>
<td><p>Shear strain and stress in concrete along crack 1 ε&lt;sub
class="subscript"&gt;cr1&lt;/sub&gt;, &amp;tau;&lt;sub
class="subscript"&gt;cr1&lt;/sub&gt; (Figure 2c)</p></td>
</tr>
<tr class="even">
<td><p><strong>strain_stress_interlock2</strong></p></td>
<td><p>Shear strain and stress in concrete along crack 2 ε&lt;sub
class="subscript"&gt;cr2&lt;/sub&gt;, &amp;tau;&lt;sub
class="subscript"&gt;cr2&lt;/sub&gt; (Figure 2c)</p></td>
</tr>
<tr class="odd">
<td><p><strong>cracking_angles</strong></p></td>
<td><p>Orientation of concrete cracks</p></td>
</tr>
</tbody>
</table>
<p>Note that recorders for a RC panel (marco-fiber) are invoked as
<strong>SFI_MVLEM</strong> element recorders using command
<strong>RCPanel</strong> and one of the desired commands listed above.
Currently, it is possible to output values only for one macro-fiber
within one or multiple elements.</p>
<hr />
<p><strong>Example:</strong></p>
<p>nDMaterial FSAM 1 0.0 1 2 4 0.0073 0.0606 0.1 0.01</p>
<p>Recorder Element -file MVLEM_panel_strain.out -time -ele 1 RCPanel 1
panel_strain</p>
<figure>
<img src="/OpenSeesRT/contrib/static/FSAM_2.png"
title="Figure 2. Behavior and Input/Output Parameters of the FSAM Constitutive Model"
width="800"
alt="Figure 2. Behavior and Input/Output Parameters of the FSAM Constitutive Model" />
<figcaption aria-hidden="true">Figure 2. Behavior and Input/Output
Parameters of the FSAM Constitutive Model</figcaption>
</figure>
<hr />
<p><strong>References:</strong></p>
<p>1) Kolozvari K. (2013). “Analytical Modeling of Cyclic Shear-Flexure
Interaction in Reinforced Concrete Structural Walls”, PhD Dissertation,
University of California, Los Angeles.</p>
<p>2) Orakcal K., Massone L.M., and Ulugtekin D. (2012). “Constitutive
Modeling of Reinforced Concrete Panel Behavior under Cyclic Loading”,
Proceedings, 15th World Conference on Earthquake Engineering, Lisbon,
Portugal.</p>
<p>3) Ulugtekin D. (2010). “Analytical Modeling of Reinforced Concrete
Panel Elements under Reversed Cyclic Loadings”, M.S. Thesis, Bogazici
University, Istanbul, Turkey.</p>
