---
title: Concrete07
description: Chang & Mander’s 1994 Concrete Model
...

# Concrete07


Concrete07 is an implementation of Chang and Mander's 1994 concrete
model with simplified unloading and reloading curves. Additionally the
tension envelope shift with respect to the origin proposed by Chang and
Mander has been removed. The model requires eight input parameters to
define the monotonic envelope of confined and unconfined concrete in the
following form:

```tcl
uniaxialMaterial Concrete07 $matTag $fc $ec $Ec $ft $et $xp $xn $r
```

----------------------------------------------------------------------

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fc</code></td>
<td><p>concrete compressive strength (compression is negative)*</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ec</code></td>
<td><p>concrete strain at maximum compressive strength*</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Ec</code></td>
<td><p>Initial Elastic modulus of the concrete</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ft</code></td>
<td><p>tensile strength of concrete (tension is positive)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">et</code></td>
<td><p>tensile strain at max tensile strength of concrete</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">xp</code></td>
<td><p>Non-dimensional term that defines the strain at which the
straight line descent begins in tension</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">xn</code></td>
<td><p>Non-dimensional term that defines the strain at which the
straight line descent begins in compression</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">r</code></td>
<td><p>Parameter that controls the nonlinear descending branch</p></td>
</tr>
</tbody>
</table>

<p><img src="/OpenSeesRT/contrib/static/Concrete07.png" title="Concrete07.png" alt="Concrete07.png" /> <a
href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/4055.htm">check this page!</a></p>

<hr />

<p>NOTES:</p>

- Compressive concrete parameters should be input as negative values.


### Unconfined Concrete

For unconfined concrete, the peak compressive strength fc in the
above figure is f'c0 and corresponding strain ec is e'c0. Assuming that
the compressive strength for unconfined concrete is readily available,
the key parameters required for the model can be found using the
following recommendations which include:

$$
\begin{aligned}
&f_{c 0}^{\prime}=\text { compressive strength (psi) } \\
&\varepsilon_{c 0}=\frac{f_{c 0}^{\prime}}{4000} \\
&E_{c}=185,000 *\left(f_{c 0}^{\prime}\right)^{\frac{1}{8}} \\
&f_{t}=7.5 * \sqrt{f_{c 0}^{\prime}} \\
&\varepsilon_{t}=\frac{2 * f_{t}}{E_{c}} \\
&x_{p}=2 \\
&x_{n}=2.3 \\
&r=\frac{f_{c 0}^{\prime}}{750}-1.9
\end{aligned}
$$

<figure>
<img src="/OpenSeesRT/contrib/static/US_Customary_Units.png" alt="US_Customary_Units.png" />
<figcaption aria-hidden="true">US_Customary_Units.png</figcaption>
</figure>

$$
\begin{aligned}
&f_{c 0}=\text { cylinder strength (MPa) } \\
&\varepsilon_{c 0}=\frac{f_{c 0}^{\prime} \frac{1}{4}}{28} \\
&E_{c}=8,200 *\left(f_{c 0}^{\prime}\right)^{\frac{3}{8}} \\
&f_{t}=0.62 * \sqrt{f_{c o}^{\prime}} \\
&\varepsilon_{t}=\frac{2 * f_{t}}{E_{c}} \\
&x_{p}=2 \\
&x_{n}=2.3 \\
&r=\frac{f_{c 0}^{\prime}}{5.2}-1.9
\end{aligned}
$$

<figure>
<img src="/OpenSeesRT/contrib/static/SI_Metric_Units.png" title="SI_Metric_Units.png"
alt="SI_Metric_Units.png" />
<figcaption aria-hidden="true">SI_Metric_Units.png</figcaption>
</figure>


### Confined Concrete
Confinement increases the strength and ductility of concrete. These
effects are accounted in the above figure by replaceing the peak
compressive strength and the corresponding strain with f' cc and e'cc,
respectively. The value of r is also decreased. The recommended approach
to define all critical parameters needed to model the confined concrete
under compression are as follows:

$$
f_{c c}^{\prime}=f_{c 0}^{\prime} *\left(1+k_{1} * x^{\prime}\right)
$$

<p>where:</p>

$$
\begin{aligned}
&f_{c 0}^{\prime}=\text { unconfined peak compressive strength } \\
&k_{1}=A *\left[0.1+\frac{0.9}{1+B * x^{\prime}}\right] \\
&x^{\prime}=\frac{f_{l 1}+f_{l 2}}{2 f_{c 0}^{\prime}} \\
&A=6.886-(0.6069+17.275 \mathrm{q}) e^{-4.989 \mathrm{q}} \\
&B=\frac{4.5}{\frac{5}{A}\left[0.9849-0.6306 e^{-3.8939 \mathrm{q}}\right]-0.1}-5
&q=\frac{f_{l 1}}{f_{l 2}} \quad f_{l 2} \geq f_{l 1} \\
&\varepsilon_{c c}^{\prime}=\varepsilon_{c 0}\left(1+k_{2} * x^{\prime}\right) \\
&k_{2}=5 \mathrm{k}_{1} \quad \text { for normal strength transverse reinforcement } \\
&k_{2}=3 \mathrm{k}_{1} \quad \text { for high strength transverse reinforcement } \\
&x_{n}=30 \text { (value is recommended in order to follow the descending branch to large strains) } \\
&n=\frac{E_{c} * \varepsilon_{c c}}{f_{c c}^{\prime}} \\
&r=\frac{n}{n-1}
\end{aligned}
$$

<figure>
<img src="/OpenSeesRT/contrib/static/Confined_Concrete_Parameters.png"
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
<img src="/OpenSeesRT/contrib/static/Hysteretic_behavior_of_Concrete07.png"
title="Hysteretic_behavior_of_Concrete07.png"
alt="Hysteretic_behavior_of_Concrete07.png" />
<figcaption
aria-hidden="true">Hysteretic_behavior_of_Concrete07.png</figcaption>
</figure>

`Concrete07` gives larger residual displacements than Concrete03.
Concrete07 also has a higher initial stiffness compared with Concrete03
and has a much slower softening post-peak in tension. Chang and Mander
state that the abrupt loss of capacity shown in Concrete03 in tension is
due to testing conditions and not representative of the true material
behavior.

<figure>
<img src="/OpenSeesRT/contrib/static/Comp1.png" title="Comp1.png" alt="Comp1.png" />
<figcaption aria-hidden="true">Comp1.png</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/Comp2.png" title="Comp2.png" alt="Comp2.png" />
<figcaption aria-hidden="true">Comp2.png</figcaption>
</figure>


### Axial Load

If the material model is used in a section that is going to be
subjected to cyclic loading, problems can occur if there is no axial
load on the section. The section should be subjected to axial load due
to the self weight of the element. If the material is loaded into
tension without any compression strain, and then reversed, the model
will target $-0.00002$ strain if cracking has not occurred or 5% of the
peak strain if cracking has occurred. The increased value after cracking
is due to material being wedged in the open cracks. Users are encouraged
to apply some axial load to the section equal to the self weight of the
element or a small amount if the user does want minimal axial load. Less
than 0.05% of f'cAg is adequate to ensure a stable response. This will
then be used instead of the default behavior described above.

<hr />

## References
<ol>
- Chang, G.A., and Mander, J.B., (1994) "Seismic Energy Based Fatigue
  Damage Ananlysis of Bridge Columns:Part 1 - Evaluation of Seismic
  Capacity," NCEER Technical Report No. NCEER-94-0006 State University of
  New York, Buffalo, N.Y.
- Waugh, J., (2009) "Nonlinear analysis of T-shaped concrete walls
  subjected to multi-directional displacements", PhD Thesis, Iowa State
  University, IA.

<hr />

<p>Code developed by: <span style="color:blue"> Jonathan Waugh,
Iowa State University </span> and <span style="color:blue">
Sri Sritharan, Iowa State University </span></p>

