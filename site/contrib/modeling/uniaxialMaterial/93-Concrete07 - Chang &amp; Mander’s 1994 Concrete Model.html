# Concrete07 - Chang &amp; Mander’s 1994 Concrete Model

<p>Concrete07 is an implementation of Chang &amp; Mander's 1994 concrete
model with simplified unloading and reloading curves. Additionally the
tension envelope shift with respect to the origin proposed by Chang and
Mander has been removed. The model requires eight input parameters to
define the monotonic envelope of confined and unconfined concrete in the
following form:</p>

```tcl
uniaxialMaterial Concrete07 $matTag $fc $ec $Ec $ft $et
        $xp $xn $r
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><strong>$fc</strong></p></td>
<td><p>concrete compressive strength (compression is negative)*</p></td>
</tr>
<tr class="odd">
<td><p><strong>$ec</strong></p></td>
<td><p>concrete strain at maximum compressive strength*</p></td>
</tr>
<tr class="even">
<td><p><strong>$Ec</strong></p></td>
<td><p>Initial Elastic modulus of the concrete</p></td>
</tr>
<tr class="odd">
<td><p><strong>$ft</strong></p></td>
<td><p>tensile strength of concrete (tension is positive)</p></td>
</tr>
<tr class="even">
<td><p><strong>$et</strong></p></td>
<td><p>tensile strain at max tensile strength of concrete</p></td>
</tr>
<tr class="odd">
<td><p><strong>$xp</strong></p></td>
<td><p>Non-dimensional term that defines the strain at which the
straight line descent begins in tension</p></td>
</tr>
<tr class="even">
<td><p><strong>$xn</strong></p></td>
<td><p>Non-dimensional term that defines the strain at which the
straight line descent begins in compression</p></td>
</tr>
<tr class="odd">
<td><p><strong>$r</strong></p></td>
<td><p>Parameter that controls the nonlinear descending branch</p></td>
</tr>
</tbody>
</table>
<p><img src="Concrete07.png" title="Concrete07.png"
alt="Concrete07.png" /> <a
href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/4055.htm">check
this page!</a></p>
<hr />
<p>NOTES:</p>
<ul>
<li>Compressive concrete parameters should be input as negative
values.</li>
</ul>
<ul>
<li>Unconfined Concrete</li>
</ul>
<p>For unconfined concrete, the peak compressive strength fc in the
above figure is f'c0 and corresponding strain ec is e'c0. Assuming that
the compressive strength for unconfined concrete is readily available,
the key parameters required for the model can be found using the
following recommendations which include:</p>
<figure>
<img src="US_Customary_Units.png" title="US_Customary_Units.png"
alt="US_Customary_Units.png" />
<figcaption aria-hidden="true">US_Customary_Units.png</figcaption>
</figure>
<figure>
<img src="SI_Metric_Units.png" title="SI_Metric_Units.png"
alt="SI_Metric_Units.png" />
<figcaption aria-hidden="true">SI_Metric_Units.png</figcaption>
</figure>
<ul>
<li>Confined Concrete</li>
</ul>
<p>Confinement increases the strength and ductility of concrete. These
effects are accounted in the above figure by replaceing the peak
compressive strength and the corresponding strain with f' cc and e'cc,
respectively. The value of r is also decreased. The recommended approach
to define all critical parameters needed to model the confined concrete
under compression are as follows:</p>
<figure>
<img src="Confined_Concrete.png" title="Confined_Concrete.png"
alt="Confined_Concrete.png" />
<figcaption aria-hidden="true">Confined_Concrete.png</figcaption>
</figure>
<p>where:</p>
<figure>
<img src="Confined_Concrete_Parameters.png"
title="Confined_Concrete_Parameters.png"
alt="Confined_Concrete_Parameters.png" />
<figcaption
aria-hidden="true">Confined_Concrete_Parameters.png</figcaption>
</figure>
<p>The monotonic envelope for the tension side of the confined concrete
follows the same curve that is used for unconfined concrete.</p>
<ul>
<li>Cyclic Behavior</li>
</ul>
<p>The hysteretic rules for cyclic behavior of confined and unconfined
concrete is built into the model and requires no further input from the
user. These rules generally follow the recommendations of Chang and
Mander, which was established based on statistical regression analysis
on the experimental data from cyclic compression tests of a number of
researchers. However, three simplifications were made to the rules
proposed by Chang and Mander which are:</p>
<ol>
<li>Instead of the power function for unloading and reloading paths,
Concrete07 uses tri-linear paths for unloading and reloading. The reason
for this change is to increase the computational efficiency of the
model, as well as numerical stability.</li>
<li>The original model shifts the tension envelope as compression
reloading after a reversal occurs. This shift is deemed unnecessary and
not implemented in Concrete07.</li>
<li>The original model requires an additional strain be applied beyond
the unloading strain to rejoin the monotonic envelope. The Concrete07
rejoins the envelope at the unloading strain; this simplification
increases the numerical stability and computational efficiency.</li>
</ol>
<p>A full description of the Concrete07 material model, modifications to
the Chang and Mander concrete model, and the effects of Concrete07 in
improving the simulation capacity of OpenSees is given in Waugh
(2007).</p>
<p>A comparison of the cyclic behavior of Concrete07 and Concrete03 is
shown in below; a magnified view of the tension region is shown
separately. A confined concrete is used in this illustration so that the
differences between the models behavior is more pronounced.</p>
<figure>
<img src="Hysteretic_behavior_of_Concrete07.png"
title="Hysteretic_behavior_of_Concrete07.png"
alt="Hysteretic_behavior_of_Concrete07.png" />
<figcaption
aria-hidden="true">Hysteretic_behavior_of_Concrete07.png</figcaption>
</figure>
<p>Concrete07 gives larger residual displacements than Concrete03.
Concrete07 also has a higher initial stiffness compared with Concrete03
and has a much slower softening post-peak in tension. Chang and Mander
state that the abrupt loss of capacity shown in Concrete03 in tension is
due to testing conditions and not representative of the true material
behavior.</p>
<figure>
<img src="Comp1.png" title="Comp1.png" alt="Comp1.png" />
<figcaption aria-hidden="true">Comp1.png</figcaption>
</figure>
<figure>
<img src="Comp2.png" title="Comp2.png" alt="Comp2.png" />
<figcaption aria-hidden="true">Comp2.png</figcaption>
</figure>
<ul>
<li>Axial Load</li>
</ul>
<p>If the material model is used in a section that is going to be
subjected to cyclic loading, problems can occur if there is no axial
load on the section. The section should be subjected to axial load due
to the self weight of the element. If the material is loaded into
tension without any compression strain, and then reversed, the model
will target -0.00002 strain if cracking has not occurred or 5% of the
peak strain if cracking has occurred. The increased value after cracking
is due to material being wedged in the open cracks. Users are encouraged
to apply some axial load to the section equal to the self weight of the
element or a small amount if the user does want minimal axial load. Less
than 0.05% of f'cAg is adequate to ensure a stable response. This will
then be used instead of the default behavior described above.</p>
<hr />
<p>REFERENCES:</p>
<ol>
<li>Chang, G.A., and Mander, J.B., (1994) "Seismic Energy Based Fatigue
Damage Ananlysis of Bridge Columns:Part 1 - Evaluation of Seismic
Capacity," NCEER Technical Report No. NCEER-94-0006 State University of
New York, Buffalo, N.Y.</li>
<li>Waugh, J., (2009) "Nonlinear analysis of T-shaped concrete walls
subjected to multi-directional displacements", PhD Thesis, Iowa State
University, IA.</li>
</ol>
<hr />
<p>Code Developed by: <span style="color:blue"> Jonathan Waugh,
Iowa State University </span> and <span style="color:blue">
Sri Sritharan, Iowa State University </span></p>
