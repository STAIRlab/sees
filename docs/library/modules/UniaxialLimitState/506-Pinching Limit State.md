# Pinching Limit State Material

<p>This command is used to construct a uniaxial material that simulates
a pinched load-deformation response and exhibits degradation under
cyclic loading. This material works with the <a
href="RotationShearCurve" title="wikilink">RotationShearCurve</a> limit
surface that can monitor a key deformation and/or a key force in an
associated frame element and trigger a degrading behavior in this
material when a limiting value of the deformation and/or force are
reached. The material can be used in two modes: 1) direct input mode,
where pinching and damage parameters are directly input; and 2)
calibrated mode for shear-critical concrete columns, where only key
column properties are input for model to fully define pinching and
damage parameters.</p>

<h2 id="mode_1_direct_input"><strong>MODE 1: Direct Input</strong></h2>

```tcl
uniaxialMaterial PinchingLimitStateMaterial $matTag
        $nodeT $nodeB $driftAxis $Kelas $crvTyp $crvTag
        $YpinchUPN $YpinchRPN $XpinchRPN $YpinchUNP
        $YpinchRNP $XpinchRNP
        $dmgStrsLimE $dmgDispMax
        $dmgE1 $dmgE2 $dmgE3 $dmgE4 $dmgELim
        $dmgR1 $dmgR2 $dmgR3 $dmgR4 $dmgRLim
        <code class="tcl-variable">dmgRCyc</code>
        $dmgS1 $dmgS2 $dmgS3 $dmgS4 $dmgSLim
        <code class="tcl-variable">dmgSCyc</code></p></td>
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique material object integer tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">nodeT</code></td>
<td><p>integer node tag to define the first node at the extreme end of
the associated flexural frame member (L3 or D5 in Figure)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">nodeB</code></td>
<td><p>integer node tag to define the last node at the extreme end of
the associated flexural frame member (L2 or D2 in Figure)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">driftAxis</code></td>
<td><p>integer to indicate the drift axis in which lateral-strength
degradation will occur. This axis should be orthogonal to the axis of
measured rotation (see $rotAxis in Rotation Shear Curve
definition)</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>driftAxis = 1 - Drift along the x-axis driftAxis = 2 - Drift
along the y-axis driftAxis = 3 - Drift along the z-axis</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Kelas</code></td>
<td><p>floating point value to define the initial material elastic
stiffness (Kelastic); Kelas &gt; 0</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">crvTyp</code></td>
<td><p>integer flag to indicate the type of limit curve associated with
this material.</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>crvTyp = 0 - No limit curve crvTyp = 1 - axial limit curve crvTyp
= 2 - <a href="RotationShearCurve"
title="wikilink">RotationShearCurve</a></p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">crvTag</code></td>
<td><p>integer tag for the unique limit curve object associated with
this material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">YpinchUPN</code></td>
<td><p>floating point unloading force pinching factor for loading in the
negative direction</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>Note: This value must be between zero and unity</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">YpinchRPN</code></td>
<td><p>floating point reloading force pinching factor for loading in the
negative direction</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>Note: This value must be between negative one and unity</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">XpinchRPN</code></td>
<td><p>floating point reloading displacement pinching factor for loading
in the negative direction</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>Note: This value must be between negative one and unity</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">YpinchUNP</code></td>
<td><p>floating point unloading force pinching factor for loading in the
positive direction</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>Note: This value must be between zero and unity</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">YpinchRNP</code></td>
<td><p>floating point reloading force pinching factor for loading in the
positive direction</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>Note: This value must be between negative one and unity</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">XpinchRNP</code></td>
<td><p>floating point reloading displacement pinching factor for loading
in the positive direction</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>Note: This value must be between negative one and unity</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">dmgStrsLimE</code></td>
<td><p>floating point force limit for elastic stiffness damage
(typically defined as the lowest of shear strength or shear at flexrual
yielding).</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>This value is used to compute the maximum deformation at flexural
yield (δmax Eq. 1) and using the initial elastic stiffness (Kelastic)
the monotonic energy (Emono Eq. 1) to yield. Input 1 if this type of
damage is not required and set $dmgE1, $dmgE2, $dmgE3, $dmgE4, and
$dmgELim to zero</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">dmgDispMax</code></td>
<td><p>floating point for ultimate drift at failure (δmax Eq. 1) and is
used for strength and stiffness damage.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>This value is used to compute the monotonic energy at axial
failure (Emono Eq. 2) by computing the area under the backbone in the
positive loading direction up to δmax. Input 1 if this type of damage is
not required and set $dmgR1, $dmgR2, $dmgR3, $dmgR4, and $dmgRLim to
zero for reloading stiffness damage. Similarly set $dmgS1, $dmgS2,
$dmgS3, $dmgS4, and $dmgSLim to zero if reloading strength damage is not
required</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">dmgE1 dmgE2 dmgE3 dmgE4</code></p></td>
<td><p>floating point elastic stiffness damage factors
<em>α1,α2,α3,α4</em> shown in Eq. 1</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">dmgELim</code></td>
<td><p>floating point elastic stiffness damage limit <em>Dlim</em> shown
in Eq. 1; Note: This value must be between zero and unity</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">dmgR1 dmgR2 dmgR3 dmgR4</code></p></td>
<td><p>floating point reloading stiffness damage factors
<em>α1,α2,α3,α4</em> shown in Eq. 1</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">dmgRLim</code></td>
<td><p>floating point reloading stiffness damage limit <em>Dlim</em>
shown in Eq. 1; Note: This value must be between zero and unity</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">dmgRCyc</code></td>
<td><p>floating point cyclic reloading stiffness damage index; Note:
This value must be between zero and unity</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">dmgS1 dmgS2 dmgS3 dmgS4</code></p></td>
<td><p>floating point backbone strength damage factors
<em>α1,α2,α3,α4</em> shown in Eq. 1</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">dmgSLim</code></td>
<td><p>floating point backbone strength damage limit <em>Dlim</em> shown
in Eq. 1; Note: This value must be between zero and unity</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">dmgSCyc</code></td>
<td><p>floating point cyclic backbone strength damage index; Note: This
value must be between zero and unity</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h2
id="mode_2_calibrated_model_for_shear_critical_concrete_columns"><strong>MODE
2: Calibrated Model for Shear-Critical Concrete Columns</strong></h2>
<table>
<tbody>
<tr class="odd">
<td><p><strong>uniaxialMaterial PinchingLimitStateMaterial $matTag
$nodeT $nodeB $driftAxis $Kelas $crvTyp $crvTag $eleTag $b $d $h $a $st
$As $Acc $ld $db $rhot $f'c $fy $fyt</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique material object integer tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">nodeT</code></td>
<td><p>integer node tag to define the first node at the extreme end of
the associated flexural frame member (L3 or D5 in Figure)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">nodeB</code></td>
<td><p>integer node tag to define the last node at the extreme end of
the associated flexural frame member (L2 or D2 in Figure)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">driftAxis</code></td>
<td><p>integer to indicate the drift axis in which lateral-strength
degradation will occur. This axis should be orthogonal to the axis of
measured rotation (see $rotAxis in Rotation Shear Curve
definition)</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>driftAxis = 1 - Drift along the x-axis driftAxis = 2 - Drift
along the y-axis driftAxis = 3 - Drift along the z-axis</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Kelas</code></td>
<td><p>floating point value to define the shear stiffness (Kelastic) of
the shear spring prior to shear failure</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>Kelas = -4 - Shear stiffness calculated assuming double curvature
and shear springs at both column element ends</p>
<p>Kelas = -3 - Shear stiffness calculated assuming double curvature and
a shear spring at one column element end</p>
<p>Kelas = -2 - Shear stiffness calculated assuming single curvature and
shear springs at both column element ends</p>
<p>Kelas = -1 - Shear stiffness calculated assuming single curvature and
a shear spring at one column element end</p>
<p>Kelas &gt; 0 - Shear stiffness is the input value</p>
<p>Note: integer inputs allow the model to know whether column height
equals the shear span (cantelever) or twice the shear span (double
curvature). For columns in frames, input the value for the case that
best approximates column end conditions or manually input shear
stiffness (typically double curvature better estimates framed column
behavior)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">crvTag</code></td>
<td><p>integer tag for the unique limit curve object associated with
this material</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>integer element tag to define the associated beam-column element
used to extract axial load</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">b</code></td>
<td><p>floating point column width (inches)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">d</code></td>
<td><p>floating point column depth (inches)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">h</code></td>
<td><p>floating point column height (inches)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">a</code></td>
<td><p>floating point shear span length (inches)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">st</code></td>
<td><p>floating point transverse reinforcement spacing (inches) along
column height</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">As</code></td>
<td><p>floating point total area (inches squared) of longitudinal steel
bars in section</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Acc</code></td>
<td><p>floating point gross confined concrete area (inches squared)
bounded by the transverse reinforcement in column section</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ld</code></td>
<td><p>floating point development length (inches) of longitudinal bars
using ACI 318-11 Eq. 12-1 and Eq. 12-2</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">db</code></td>
<td><p>floating point diameter (inches) of longitudinal bars in column
section</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rhot</code></td>
<td><p>floating point transverse reinforcement ratio
(Ast/st.db)</p></td>
</tr>
<tr class="even">
<td><p><strong>$f'c</strong></p></td>
<td><p>floating point concrete compressive strength (ksi)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fy</code></td>
<td><p>floating point longitudinal steel yield strength (ksi)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fyt</code></td>
<td><p>floating point transverse steel yield strength (ksi)</p></td>
</tr>
</tbody>
</table>
<hr />

<p>DESCRIPTION:</p>
<figure>
<img src="/OpenSeesRT/contrib/static/PinchingLimitStateMaterial2.png"
title="PinchingLimitStateMaterial2.png" width="550"
alt="PinchingLimitStateMaterial2.png" />
<figcaption
aria-hidden="true">PinchingLimitStateMaterial2.png</figcaption>
</figure>
<figure>
<img src="PinchingLimitStateMaterial1-2.jpg"
title="PinchingLimitStateMaterial1-2.jpg"
alt="PinchingLimitStateMaterial1-2.jpg" />
<figcaption
aria-hidden="true">PinchingLimitStateMaterial1-2.jpg</figcaption>
</figure>

<p>The material model coupled with the <a href="RotationShearCurve"
title="wikilink">RotationShearCurve</a> limit surface: 1) has the
ability to continually monitor forces and deformations in the flexural
elements for conditions that trigger lateral-strength degradation, 2)
has a built-in function that compensates for flexural deformation
offsets that arise from the degrading behavior of the material in shear
springs, and 3) is able to trigger lateral-strength degradation through
either a limiting lateral force or element deformations (whichever is
reached first). The material introduces several functionalities that
give users a high degree of control over the triggering of strength
degradation and the ensuing cyclic degrading behavior. Damage algorithms
are implemented to control the degrading behavior through elastic
stiffness, reloading stiffness, and backbone strength degradation (Fig. 2). 
The rate of damage accumulation can be controlled by energy-,
displacement-, and cycle-based damage computation algorithms.</p>

During the degrading behavior, the model automatically adjusts
reloading stiffness to achieve a symmetric global-element lateral
load-vs lateral displacement behavior. The model does so by
automatically adjusting the reloading stiffness and backbone curve of
the material model to compensate for dissymmetry introduced by the
unloading of the flexural elements in series with shear springs governed
by the model.

<p>DAMAGE:</p>
Damage accumulations effects based on numbers of cycles can be
introduced to reloading stiffness and backbone strength through the
simple parameters $dmgRCyc and $dmgSCyc with values ranging from 0 to 1.

<p>Elastic stiffness, reloading stiffness, and strength can be adjusted
using the following energy and displacement damage model (from Mitra and
Lowes (2007)):</p>

<figure>
<img src="/OpenSeesRT/contrib/static/PinchingLimitStateMaterialEq1.png"
title="PinchingLimitStateMaterialEq1.png" width="350"
alt="PinchingLimitStateMaterialEq1.png" />
<figcaption
aria-hidden="true">PinchingLimitStateMaterialEq1.png</figcaption>
</figure>
<hr />

## Examples

The following are sample scripts for using the <a
href="Pinching_Limit_State_Material" title="wikilink">Pinching Limit
State Material</a> and associated limit surface (<a
href="RotationShearCurve" title="wikilink">RotationShearCurve</a>) to
simulate the behavior of a shear-critical reinforced concrete column
tested by Sezen and Moehle (2006) (Specimen 1).

The scripts below are for a material model and limit surface that are
applied to zero-length shear springs in series with fiber-section column
elements (see references below for more detail).

<p><strong>Mode 1: Direct Parameter Input</strong></p>

```tcl
limitCurve RotationShearCurve 1 3 1 3 3 -1 -1 -10.0 0.0175
uniaxialMaterial PinchingLimitStateMaterial 9 6 2 1 3057.9 2 1 0.3 \
        0.2 0.0 0.3 0.2 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 \
        0.0 0.0 0.0 0.0 0.0 0.3
```

<figure>
<img src="/OpenSeesRT/contrib/static/Pinchingmaterial_fitted_sp1.png"
title="Pinchingmaterial_fitted_sp1.png" width="400"
alt="Pinchingmaterial_fitted_sp1.png" />
<figcaption
aria-hidden="true">Pinchingmaterial_fitted_sp1.png</figcaption>
</figure>

<p><strong>Mode 2: Calibrated Model Input</strong></p>

```tcl
limitCurve RotationShearCurve 1 3 1 3 3 -1 -1 0 1 16.0 13.625 16.0 \
        115.75 6.0 6.28 169.0 43.0 1.0 0.00393 -3.177 65.5 66.6 0.0
<p>uniaxialMaterial PinchingLimitStateMaterial 9 6 2 1 -3 2 2 1 16.0 \
        13.625 16.0 57.88 6.0 6.28 169.0 43.0 1.0 0.00393 -3.177 65.5 66.6
```

<figure>
<img src="/OpenSeesRT/contrib/static/PinchingLimitState_Sp1-c.png"
title="PinchingLimitState_Sp1-c.png" width="400"
alt="PinchingLimitState_Sp1-c.png" />
<figcaption aria-hidden="true">PinchingLimitState_Sp1-c.png</figcaption>
</figure>


## References
1. LeBorgne M. R., 2012, "Modeling the Post Shear Failure Behavior of
  Reinforced Concrete Columns." Austin, Texas: University of Texas at
  Austin, PhD, 301.

2. LeBorgne, M.R., Ghannoum, W.M., 2013, "Analytical Element for
  Simulating Lateral-Strength Degradation in Reinforced Concrete Columns
  and Other Frame Members," Journal of Structural Engineering, V. 140, No.
  7, pp. 04014038 1-12. doi: 10.1061/(ASCE)ST.1943-541X.0000925

3. LeBorgne, M.R., Ghannoum, W.M., 2014, "Calibrated Analytical
Element for Lateral-Strength Degradation of Reinforced Concrete
Columns," Engineering Structures, V. 81, pp. 35-48.

3. Ghannoum W. M., Moehle J. P., 2012, "Rotation-Based Shear Failure
  Model for Lightly Confined Reinforced Concrete Columns," Journal of
  Structural Engineering, V. 138, No. 10, 1267-78.

4. Mitra Nilanjan, Lowes Laura N., 2007, "Evaluation, Calibration,
  and Verification of a Reinforced Concrete Beam--Column Joint Model,"
  Journal of Structural Engineering, V. 133, No. 1, 105-20.

5. Sezen Halil, Moehle Jack P., 2006, "Seismic Tests of Concrete
  Columns with Light Transverse Reinforcement," ACI Structural Journal, V.
  103, No. 6, 842-9.


<hr />

<p>Code Developed by: <span style="color:blue"> Matthew Leborgne
and Wassim M. Ghannoum, University of Texas at Austin</span></p>
