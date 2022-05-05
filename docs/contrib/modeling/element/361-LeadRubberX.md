# LeadRubberX

<p>This command is used to construct a LeadRubberX bearing element
object in three-dimension. The 3D continuum geometry of a lead rubber
bearing is modeled as a 2-node, 12 DOF discrete element. It extends the
formulation of <a href="ElastomericX" title="wikilink">ElastomericX</a>
by including strength degradation in lead rubber bearing due to heating
of the lead-core. The LeadRubberX element requires only the geometric
and material properties of an elastomeric bearing as arguments. The
material models in six direction are formulated within the element from
input arguments. The time-dependent values of mechanical properties
(e.g., shear stiffness, buckling load capacity, temperature in the
lead-core, yield strength) can also be recorded using the "parameters"
<a href="#Recorders" title="wikilink">recorder</a>.</p>
<p>For a 3D problem:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element LeadRubberX $eleTag $Nd1 $Nd2 $Fy $alpha $Gr
$Kbulk $D1 $D2 $ts $tr $n &lt;&lt;$x1 $x2 $x3&gt; $y1 $y2 $y3&gt;
&lt;$kc&gt; &lt;$PhiM&gt; &lt;$ac&gt; &lt;$sDratio&gt; &lt;$m&gt;
&lt;$cd&gt; &lt;$tc&gt; &lt;$qL&gt; &lt;$cL&gt; &lt;$kS&gt; &lt;$aS&gt;
&lt;$tag1&gt; &lt;$tag2&gt; &lt;$tag3&gt; &lt;$tag4&gt;
&lt;$tag5&gt;</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$eleTag</strong></p></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$Nd1 $Nd2</strong></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Fy</strong></p></td>
<td><p>yield strength</p></td>
</tr>
<tr class="even">
<td><p><strong>$alpha</strong></p></td>
<td><p>post-yield stiffness ratio</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Gr</strong></p></td>
<td><p>shear modulus of elastomeric bearing</p></td>
</tr>
<tr class="even">
<td><p><strong>$Kbulk</strong></p></td>
<td><p>bulk modulus of rubber</p></td>
</tr>
<tr class="odd">
<td><p><strong>$D1</strong></p></td>
<td><p>internal diameter</p></td>
</tr>
<tr class="even">
<td><p><strong>$D2</strong></p></td>
<td><p>outer diameter (excluding cover thickness)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$ts</strong></p></td>
<td><p>single steel shim layer thickness</p></td>
</tr>
<tr class="even">
<td><p><strong>$tr</strong></p></td>
<td><p>single rubber layer thickness</p></td>
</tr>
<tr class="odd">
<td><p><strong>$n</strong></p></td>
<td><p>number of rubber layers</p></td>
</tr>
<tr class="even">
<td><p><strong>$x1 $x2 $x3</strong></p></td>
<td><p>vector components in global coordinates defining local x-axis
(optional)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$y1 $y2 $y3</strong></p></td>
<td><p>vector components in global coordinates defining local y-axis
(optional)</p></td>
</tr>
<tr class="even">
<td><p><strong>$kc</strong></p></td>
<td><p>cavitation parameter (optional, default = 10.0)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$PhiM</strong></p></td>
<td><p>damage parameter (optional, default = 0.5)</p></td>
</tr>
<tr class="even">
<td><p><strong>$ac</strong></p></td>
<td><p>strength reduction parameter (optional, default = 1.0)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$sDratio</strong></p></td>
<td><p>shear distance from iNode as a fraction of the element length
(optional, default = 0.5)</p></td>
</tr>
<tr class="even">
<td><p><strong>$m</strong></p></td>
<td><p>element mass (optional, default = 0.0)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$cd</strong></p></td>
<td><p>viscous damping parameter (optional, default = 0.0)</p></td>
</tr>
<tr class="even">
<td><p><strong>$tc</strong></p></td>
<td><p>cover thickness (optional, default = 0.0)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$qL</strong></p></td>
<td><p>density of lead (optional, default = 11200 kg/m3)</p></td>
</tr>
<tr class="even">
<td><p><strong>$cL</strong></p></td>
<td><p>specific heat of lead (optional, default = 130 N-m/kg
oC)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$kS</strong></p></td>
<td><p>thermal conductivity of steel (optional, default = 50 W/m
oC)</p></td>
</tr>
<tr class="even">
<td><p><strong>$aS</strong></p></td>
<td><p>thermal diffusivity of steel (optional, default = 1.41e-05
m2/s)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$tag1</strong></p></td>
<td><p>Tag to include cavitation and post-cavitation (optional, default
= 0)</p></td>
</tr>
<tr class="even">
<td><p><strong>$tag2</strong></p></td>
<td><p>Tag to include buckling load variation (optional, default =
0)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$tag3</strong></p></td>
<td><p>Tag to include horizontal stiffness variation (optional, default
= 0)</p></td>
</tr>
<tr class="even">
<td><p><strong>$tag4</strong></p></td>
<td><p>Tag to include vertical stiffness variation (optional, default =
0)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$tag5</strong></p></td>
<td><p>Tag to include strength degradation in shear due to heating of
lead core (optional, default = 0)</p></td>
</tr>
</tbody>
</table>
<p><strong>Important note:</strong></p>
<p>Because default values of heating parameters are in SI units, user
must override the default heating parameters values if using Imperial
units &lt;br /&gt; User should distinguish between yield strength of
elastomeric bearing (Fy) and characteristic strength (Qd):
Qd=Fy*(1-alpha)</p>
<h2 id="physical_model_and_mechanical_properties">Physical Model and
Mechanical Properties</h2>
<p>The physical model of an elastomeric bearing is considered as a
two-node, twelve degrees-of-freedom discrete element. The two nodes are
connected by six springs that represent the mechanical behavior in the
six basic directions of a bearing. The degrees of freedom and discrete
spring representation of an elastomeric bearing are shown in the below
figures.</p>
<p><img src="Elastomeric3DModel.png"
title="inline|Physical continuum model" height="300"
alt="inline|Physical continuum model" /> <img
src="ElastomericDiscreteSpring.png"
title="inline|Discrete spring representation" height="300"
alt="inline|Discrete spring representation" /></p>
<p>The general form of element force vector, $$,
and element stiffness matrix,&lt;math&gt;&lt;/math&gt; , for element
representation considered above is given by equation below:</p>
<p>&lt;math&gt;=\left[ \begin{matrix} Axial \\ Shear1 \\ Shear2 \\
Torsion \\ Rotation1 \\ Rotation2 \\ \end{matrix} \right];\ \ \ \ \ \
=\left[ \begin{matrix} Axial &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\
0 &amp; Shear1 &amp; Shear12 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; Shear21
&amp; Shear2 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; Torsion
&amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; Rotation1 &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; Rotation2 \\ \end{matrix}
\right]&lt;/math&gt;</p>
<p>The coupling of the two shear springs is considered directly by using
a coupled bidirectional model. All other springs are uncoupled. The
coupling of vertical and horizontal directions are considered indirectly
by using expressions for mechanical properties in one direction that are
dependent on the response parameters in the other direction. Linear
uncoupled springs are considered in the torsion and the two rotational
springs as they are not expected to significantly affect the response of
an elastomeric bearing. The off-diagonal terms due to coupling between
axial and shear, and axial and rotation, are not considered in the
two-spring model (Koh and Kelly, 1987) used here. An exact model would
have non-zero values of these off-diagonal terms. A discussion on the
formulation of the two-spring model and the exact model is presented in
Ryan et al.(1991). The subscript b refers to the element’s basic
coordinate system. When the model is implemented in software programs,
response quantities are transformed between the basic, local and global
coordinates to perform computations.</p>
<p>The discrete spring model presented here has the advantages of easy
implementation and being computationally efficient. The mechanical
properties of the six springs (also referred to as material models in
OpenSees) are defined using analytical solutions available from the
analysis of elastomeric bearings. The expression for mechanical
properties, including stiffness and buckling load capacity, are derived
using explicit consideration for geometric nonlinearity due to large
displacement effects. The material models in six directions are:</p>
<ul>
<li>Axial direction: a new mathematical model that captures the behavior
under cyclic tension <a
href="http://onlinelibrary.wiley.com/doi/10.1002/eqe.2431/abstract">Link</a></li>
<li>Two shear directions: a special case of the Bouc-Wen model extended
by Nagarajaiah et al.(1991) for seismic isolation bearings combined with
a strength degradation model of Kalpakidis et al.(2010)</li>
<li>Torsion: a linear elastic model</li>
<li>Two rotational directions: linear elastic models</li>
</ul>
<p>In addition to the behavior captured by existing bearing elements,
this element can capture following characteristics:</p>
<ol>
<li>Cavitation and post-cavitation behavior in tension (tag1)</li>
<li>Variation in critical buckling load capacity due to lateral
displacement (tag2)</li>
<li>Variation in horizontal shear stiffness with axial load on the
bearing (tag3)</li>
<li>Variation in vertical axial stiffness with horizontal displacement
(tag4)</li>
<li>Strength degradation in cyclic shear loading due to heating of lead
core (tag5)</li>
</ol>
<p>User may choose to include an individual or a combination of these
behaviors through user tags (include:1, exclude:0) in their
analysis.</p>
<p>For the full capabilities of this element, users are referred to: <a
href="http://onlinelibrary.wiley.com/doi/10.1002/eqe.2431/abstract">EESD
Article</a></p>
<h2
id="consideration_of_characteristics_to_include_under_extreme_loading">Consideration
of characteristics to include under extreme loading</h2>
<p>A recent paper by <a
href="http://www.sciencedirect.com/science/article/pii/S002954931500254X">Kumar
et. al (2015)</a> explains which of the five tags should be included in
the analysis. Although the analysis presented in the paper is for the
base-isolated NPP, the conclusions are valid for design earthquake and
maximum considered earthquake for regular building structures as well.
Following are few thumb rules that can be followed: tag 1: Unless you
are investigating the tensile behavior, the effect of the tensile model
on shear response is insignificant. tag 2: It is recommended to use tag
to include variable buckling load capacity. It affects the compression
capacity and shear stiffness. The apparent softening in shear
force-deformation behavior at high axial load is due to this. A constant
buckling load will show less softening. tag 3: Recommended if axial load
expected during the loading is more than 10% of the buckling load
capacity. tag2+tag3 provides greater softening. tag 4: Unless you are
investigating the axial behavior, the effect of the tensile model on
shear response is insignificant. tag 5: Recommended for long duration
and low frequency ground motions. Effect is more prominent at beyond
design basis earthquakes.</p>
<h2 id="verification_and_validation">Verification and validation</h2>
<p>This is element has been verified per ASME guidelines. A great deal
of effort has gone into benchmarking performance of this user element
using experimental data and verification using same element implement in
LS-DYNA and ABAQUS. Users are referred to the <a
href="https://www.sciencedirect.com/science/article/pii/S0141029617340324">Engineering
Structures Paper</a> for complete details. Additional information is
also presented in <a
href="https://www.researchgate.net/publication/280841152_Verification_and_validation_of_models_of_elastomeric_seismic_isolation_bearings">SMiRT23
Paper</a> and chapter 4 of the MCEER Report <a
href="https://www.researchgate.net/publication/292607987_Seismic_isolation_of_nuclear_power_plants_using_elastomeric_bearings">MCEER
15-0008</a>.</p>
<p>Update: The LR isolator element is now implemented in the Mastadon
software <a
href="https://mooseframework.inl.gov/mastodon/manuals/include/materials/lr_isolator-user.html">LR
Isolator Element</a> at Idaho National Laboratory by the research group
working at University at Buffalo and Idaho National Laboratory.</p>
<h2 id="recorders">Recorders</h2>
<p>In addition to regular recorders provided by the bearing elements (<a
href="Element_Recorder" title="wikilink"> Element Recorder</a>), this
element can also record instantaneous values of cavitation force (Fcn),
buckling load capacity (Fcrn), vertical stiffness (Kv), horizontal
stiffness (ke), temperature increase (dT), and yield strength (qYield)
using the "Parameters" recorder in that order.</p>
<p>Example: recorder Element &lt;-file $fileName&gt; -time &lt;-ele
($ele1 $ele2 ...)&gt; Parameters recorder Element -file param.out -time
-ele 1 Parameters</p>
<p>To check if bearing has buckled or cavitated, an user can obtain the
histories of Fcn and Fcrn as described above and divide the axial force
(obtained from basicForce recorder, qb(2)) by Fcn and Fcrn at each time
step, which provides demand vs capacity (D/C) ratios at each time step.
If Fcn/qb(0) &gt; 1.0 : Cavitation, or Fcrn/qb(0)&gt;1.0 : Buckling.</p>
<h2 id="examples">Examples</h2>
<p>An example is presented here in which a lead rubber bearing (large
size bearing in Kalpakidis et al. (2010)) is subjected to a shear
harmonic loading in laboratory (SEESL at UB). The response obtained from
LeadRubberX element in OpenSees is compared with the experimental
results.</p>
<p>Excitation files: <embed src="Excitation.zip"
title="Excitation.zip" /> ‎</p>
<p>Tcl files: <img src="LDRgravity.tcl‎" title="LDRgravity.tcl‎"
alt="LDRgravity.tcl‎" /> <img src="LDRtest.tcl‎" title="LDRtest.tcl‎"
alt="LDRtest.tcl‎" /></p>
<figure>
<img src="LDRcomparison.png"
title="inline|Numerical and experimental response comparison"
height="600"
alt="inline|Numerical and experimental response comparison" />
<figcaption aria-hidden="true">inline|Numerical and experimental
response comparison</figcaption>
</figure>
<h2 id="references">References</h2>
<ol>
<li>Kumar, M., Whittaker, A., and Constantinou, M. (2014). "An advanced
numerical model of elastomeric seismic isolation bearings." Earthquake
Engineering &amp; Structural Dynamics, 43(13), 1955-1974. <a
href="http://onlinelibrary.wiley.com/doi/10.1002/eqe.2431/abstract">Link</a></li>
<li>Kumar, M., Whittaker, A., and Constantinou, M. (2015). "Experimental
investigation of cavitation in elastomeric seismic isolation bearings."
Engineering Structures, 101, 290-305. <a
href="http://www.sciencedirect.com/science/article/pii/S0141029615004575">Link</a></li>
<li>Kumar, M., Whittaker, A., and Constantinou, M. (2015). "Response of
base-isolated nuclear structures to extreme earthquake shaking." Nuclear
Engineering and Design, 295, 860-874. <a
href="http://www.sciencedirect.com/science/article/pii/S002954931500254X">Link</a></li>
<li>Kumar, M., and Whittaker, A. (2018). "Cross-platform implementation,
verification and validation of advanced mathematical models of
elastomeric seismic isolation bearings." Engineering Structures, 175,
926-943. <a
href="https://www.sciencedirect.com/science/article/pii/S0141029617340324">Link</a></li>
<li>Kalpakidis, I. V., Constantinou, M. C., and Whittaker, A. S. (2010).
"Modeling strength degradation in lead-rubber bearings under earthquake
shaking." Earthquake Engineering and Structural Dynamics, 39(13),
1533-1549.</li>
</ol>
<hr />
<p>Code Developed by: <span style="color:blue"> Manish Kumar,
University at Buffalo, SUNY </span></p>
<p>Any bugs in this element can be reported to mkumar2 AT buffalo dot
edu</p>
