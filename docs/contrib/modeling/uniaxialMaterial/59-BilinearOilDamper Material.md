# BilinearOilDamper Material

<p>This command is used to construct a BilinearOilDamper material, which
simulates the hysteretic response of bilinear oil dampers with relief
valve. Two adaptive iterative algorithms have been implemented and
validated to solve numerically the constitutive equations within a
bilinear oil damper with a high-precision accuracy.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>uniaxialMaterial BilinearOilDamper $matTag $K $Cd &lt;$Fr
$p&gt; &lt;$LGap&gt; &lt; $NM $RelTol $AbsTol
$MaxHalf&gt;</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><strong>$K</strong></p></td>
<td><p>Elastic stiffness of linear spring to model the axial flexibility
of an oil damper (brace and damper portion)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Cd</strong></p></td>
<td><p>Viscous damping coefficient of an oil damper (before
relief)</p></td>
</tr>
<tr class="even">
<td><p><strong>$Fr</strong></p></td>
<td><p>Damper relief load (default=1.0, Damper property)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$p</strong></p></td>
<td><p>Post-relief viscous damping coefficient ratio (default=1.0,
linear oil damper)</p></td>
</tr>
<tr class="even">
<td><p><strong>$LGap</strong></p></td>
<td><p>gap length to simulate the gap length due to the pin tolerance
(default=0.0: zero tolerance)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$NM</strong></p></td>
<td><p>Employed adaptive numerical algorithm (default value NM = 1; 1 =
Dormand-Prince54, 2=adaptive finite difference)</p></td>
</tr>
<tr class="even">
<td><p><strong>$RelTol</strong></p></td>
<td><p>Tolerance for absolute relative error control of the adaptive
iterative algorithm (default value 10^-6)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$AbsTol</strong></p></td>
<td><p>Tolerance for absolute error control of adaptive iterative
algorithm (default value 10^-10)</p></td>
</tr>
<tr class="even">
<td><p><strong>$MaxHalf</strong></p></td>
<td><p>Maximum number of sub-step iterations within an integration step
(default value 15)</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>
<hr />
<p><strong>Examples:</strong></p>
<table>
<tbody>
<tr class="odd">
<td><p><strong><em>1. Input parameters:</em></strong></p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>Assume a bilinear oil damper with axial stiffness K=200.0kN/mm,
viscous damping coefficient C=6.0KN/(mm/s), relief load Fr=1000.0KN,
p=0.1.</p></td>
</tr>
<tr class="even">
<td><p>The input parameters for the material should be as
follows:</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>uniaxialMaterial BilinearOilDamper 1 200.0 6.0 1000 0.1</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Using these properties, Figure 1c shows the hysteretic response
of this damper for sinusoidal displacement increments of 12, 24 and 36mm
and a frequency f = 1.0Hz. Figures 1a-1d show the damper hysteresis with
varying post-relief viscous damping coefficient ratio (p=1.0, 0.5, 0.1,
0.0).</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><figure>
<img src="BOD_1.png"
title=" Figure 1.Oil Damper with various post-relief viscous damping coefficient ratios"
width="550"
alt=" Figure 1.Oil Damper with various post-relief viscous damping coefficient ratios" />
<figcaption aria-hidden="true"> Figure 1.Oil Damper with various
post-relief viscous damping coefficient ratios</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Assume a bilinear oil damper with axial stiffness K=200.0kN/mm,
viscous damping coefficient C=6.0KN/(mm/s), relief load Fr=1000.0KN,
p=0.1 and LGap = 0.5mm due to the pin tolerance at the damper
ends.</p></td>
</tr>
<tr class="odd">
<td><p>The input parameters for the material should be as
follows:</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>uniaxialMaterial BilinearOilDamper 1 200.0 6.0 1000 0.1
0.5</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>Using these properties, Figure 2c shows the hysteretic response
of this damper for sinusoidal displacement increments of 0.5, 1 and
1.5mm and a frequency f = 1.0Hz. Figures 2a-2d show the damper
hysteresis with varying gap length (LGap = 0.0, 0.2. 0.5. 1.0
mm)</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><figure>
<img src="BODgap_2.png"
title=" Figure 2.Oil Damper with various gap lengths" width="550"
alt=" Figure 2.Oil Damper with various gap lengths" />
<figcaption aria-hidden="true"> Figure 2.Oil Damper with various gap
lengths</figcaption>
</figure></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table>
<hr />
<p><strong>References</strong>:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>[1]</strong></p></td>
<td><p>Akcelyan, S., Lignos, D. G., Hikino, T. (2018). “Adaptive
Numerical Method Algorithms for Nonlinear Viscous and Bilinear Oil
Damper Models Subjected to Dynamic Loading.” Soil Dynamics and
Earthquake Engineering, 113, 488-502. <a
href="http://doi.org/10.1016/j.soildyn.2018.06.021">1</a>.</p></td>
</tr>
<tr class="even">
<td><p><strong>[2]</strong></p></td>
<td><p>Akcelyan, S. (2017). "Seismic retrofit of existing steel tall
buildings with supplemental damping devices." Ph.D. Dissertation, McGill
University, Canada.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Code Developed and Implemented by : <span style="color:blue">
<strong><em><a href="http://sarvenakcelyan.com">Sarven
Akcelyan</a><strong><em>&amp;</em></strong><a
href="http://dimitrios-lignos.research.mcgill.ca/PLignos.html">Prof.
Dimitrios G. Lignos</a></em></strong>, (McGill University)
</span></p>
