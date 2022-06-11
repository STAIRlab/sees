# SFI MVLEM - Cyclic Shear-Flexure Interaction Model for RC Walls

<p><strong>Code developed by:</strong></p>
<p><a href="mailto:kkolozvari@fullerton.edu"><span style="color:blue"> Kristijan Kolozvari</span>
<span style="color:black"></a>, California State University, Fullerton</p>
<p><span style="color:blue"> Kutay Orakcal&lt;span
style="color:black"&gt;, Bogazici University, Istanbul, Turkey</p>
<p><span style="color:blue"> John Wallace&lt;span
style="color:black"&gt;, Univeristy of California, Los Angeles</p>
<p>The <strong>SFI_MVLEM</strong> command is used to construct a
Shear-Flexure Interaction Multiple-Vertical-Line-Element Model
(SFI-MVLEM, Kolozvari et al., 2015a, b, c), which captures interaction
between axial/flexural and shear behavior of RC structural walls and
columns under cyclic loading. The <strong>SFI_MVLEM</strong> element
(Figure 1) incorporates 2-D RC panel behavior described by the
Fixed-Strut-Angle-Model (nDMaterial <a
href="http://opensees.berkeley.edu/wiki/index.php/FSAM_-_2D_RC_Panel_Constitutive_Behavior"><strong>FSAM</strong></a>;
Ulugtekin, 2010; Orakcal et al., 2012), into a 2-D macroscopic
fiber-based model (MVLEM). The interaction between axial and shear
behavior is captured at each RC panel (macro-fiber) level, which further
incorporates interaction between shear and flexural behavior at the
<strong>SFI_MVLEM</strong> element level.</p>
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
<td><p><code class="parameter-table-variable">iNode jNode</code></p></td>
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
shall be used with nDMaterial <a
href="http://opensees.berkeley.edu/wiki/index.php/FSAM_-_2D_RC_Panel_Constitutive_Behavior"><strong>FSAM</strong></a>,
which is a 2-D plane-stress constitutive relationship representing
reinforced concrete panel behavior.</p>
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
<em>$Response</em>-s refer to nDMaterial <a
href="http://opensees.berkeley.edu/wiki/index.php/FSAM_-_2D_RC_Panel_Constitutive_Behavior"><strong>FSAM</strong></a>.</p></td>
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
<p>1) Kolozvari K., Orakcal K., and Wallace J. W. (2015a).
"Shear-Flexure Interaction Modeling of reinforced Concrete Structural
Walls and Columns under Reversed Cyclic Loading", Pacific Earthquake
Engineering Research Center, University of California, Berkeley, <a
href="http://peer.berkeley.edu/publications/peer_reports/reports_2015/webPEER-2015-12-kolozvari.pdf">PEER
Report No. 2015/12</a></p>
<p>2) Kolozvari K., Orakcal K., and Wallace J. W. (2015b). ”Modeling of
Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural
Walls. I: Theory”, ASCE Journal of Structural Engineering, 141(5),
04014135 <a
href="http://dx.doi.org/10.1061/(ASCE)ST.1943-541X.0001059">doi</a></p>
<p>3) Kolozvari K., Tran T., Orakcal K., and Wallace, J.W. (2015c).
”Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete
Structural Walls. II: Experimental Validation”, ASCE Journal of
Structural Engineering, 141(5), 04014136 <a
href="http://dx.doi.org/10.1061/(ASCE)ST.1943-541X.0001083">doi</a></p>
<p>4) Kolozvari K. (2013). “Analytical Modeling of Cyclic Shear-Flexure
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
width="800"
alt="Figure E1.6. Predicted Stress-Strain Behavior for Concrete: a) Strut 1, b) Strut 2" />
<figcaption aria-hidden="true">Figure E1.6. Predicted Stress-Strain
Behavior for Concrete: a) Strut 1, b) Strut 2</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/Example2_6.png"
title="Figure E1.7. Predicted Stress-Strain Behavior for Steel: a) Horizontal (X), b) Vertical (Y)"
width="800"
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
width="780"
alt="Figure E2.10. Predicted Stress-Strain Behavior for Concrete: a) Strut 1, b) Strut 2" />
<figcaption aria-hidden="true">Figure E2.10. Predicted Stress-Strain
Behavior for Concrete: a) Strut 1, b) Strut 2</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/SFI_MVLEM_E2_11.png"
title="Figure E2.11. Predicted Stress-Strain Behavior for Steel: a) Horizontal (X), b) Vertical (Y)"
width="780"
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
