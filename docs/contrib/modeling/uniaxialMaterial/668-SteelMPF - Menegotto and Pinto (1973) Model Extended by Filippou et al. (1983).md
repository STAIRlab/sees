# SteelMPF - Menegotto and Pinto (1973) Model Extended by Filippou et al. (1983)

<p><strong>Developed and Implemented by:</strong></p>
<p><a href="mailto:kkolozvari@fullerton.edu"><span style="color:blue"> Kristijan Kolozvari</span>
<span style="color:black"></a>, California State University, Fullerton</p>
<p><span style="color:blue"> Kutay Orakcal&lt;span
style="color:black"&gt;, Bogazici University, Istanbul, Turkey</p>
<p><span style="color:blue"> John Wallace&lt;span
style="color:black"&gt;, Univeristy of California, Los Angeles</p>
<p>This command is used to construct a uniaxialMaterial
<strong>SteelMPF</strong> (Kolozvari et al., 2015), which represents the
well-known uniaxial constitutive nonlinear hysteretic material model for
steel proposed by Menegotto and Pinto (1973), and extended by Filippou
et al. (1983) to include isotropic strain hardening effects. The
relationship is in the form of curved transitions (Figure 1), each from
a straight-line asymptote with slope E&lt;sub
class="subscript"&gt;0&lt;/sub&gt; (modulus of elasticity) to another
straight-line asymptote with slope E&lt;sub
class="subscript"&gt;1&lt;/sub&gt; = bE&lt;sub
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
each strain reversal. The model allows calibration of isotropic
hardening parameters in both compression and tension through optional
input variables <em>a&lt;sub class="subscript"&gt;1&lt;/sub&gt;</em> and
<em>a&lt;sub class="subscript"&gt;2&lt;/sub&gt;</em> for isotropic
strain hardening in compression, and <em>a&lt;sub
class="subscript"&gt;3&lt;/sub&gt;</em> and <em>a&lt;sub
class="subscript"&gt;4&lt;/sub&gt;</em> for isotropic strain hardening
tension, and uses default values of <em>a&lt;sub
class="subscript"&gt;1&lt;/sub&gt;</em> = <em>a&lt;sub
class="subscript"&gt;3&lt;/sub&gt;</em> = 0.0 and <em>a&lt;sub
class="subscript"&gt;2&lt;/sub&gt;</em> = <em>a&lt;sub
class="subscript"&gt;4&lt;/sub&gt;</em> = 1.0 that yield no isotropic
strain hardening for either compression or tension. To incorporate
isotropic strain hardening in compression, the recommended parameters
are <em>a&lt;sub class="subscript"&gt;1&lt;/sub&gt;</em> = 0.01 and
<em>a&lt;sub class="subscript"&gt;2&lt;/sub&gt;</em> = 7.0. To
incorporate isotropic strain hardening in tension, the recommended
parameters are <em>a&lt;sub class="subscript"&gt;3&lt;/sub&gt;</em> =
0.01 and <em>a&lt;sub class="subscript"&gt;4&lt;/sub&gt;</em> = 7.0.</p>
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
        $R0 $cR1 $cR2 &lt;$a1 $a2 $a3 $a4&gt;
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
<td><p><strong>$cR1</strong></p></td>
<td><p>Curvature degradation parameter (a1 = 0.925 recommended)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$cR2</strong></p></td>
<td><p>Curvature degradation parameter (a2 = 0.15 or 0.0015
recommended)</p></td>
</tr>
<tr class="even">
<td><p><strong>$a1</strong></p></td>
<td><p>Isotropic hardening in compression parameter (optional, default =
0.0). Shifts compression yield envelope by a proportion of compressive
yield strength after a maximum plastic tensile strain of
$a2($fyp/$E0)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$a2</strong></p></td>
<td><p>Isotropic hardening in compression parameter (optional, default =
1.0). See explanation of a1.</p></td>
</tr>
<tr class="even">
<td><p><strong>$a3</strong></p></td>
<td><p>Isotropic hardening in tension parameter (optional, default =
0.0). Shifts tension yield envelope by a proportion of tensile yield
strength after a maximum plastic compressive strain of
$a3($fyn/$E0).</p></td>
</tr>
<tr class="odd">
<td><p><strong>$a4</strong></p></td>
<td><p>Isotropic hardening in tension parameter (optional, default =
1.0). See explanation of a3.</p></td>
</tr>
</tbody>
</table>
<hr />
<p><strong>Example:</strong></p>
<p>uniaxialMaterial SteelMPF 1 60 60 29000 0.02 0.02 20.0 0.925 0.15</p>
<hr />
<p><strong>Discussion:</strong></p>
<p>Although the Menegotto-Pinto model is already available in OpenSees
(e.g., [<a
href="http://opensees.berkeley.edu/wiki/index.php/Steel02_Material_--_Giuffr%C3%A9-Menegotto-Pinto_Model_with_Isotropic_Strain_Hardening">http://opensees.berkeley.edu/wiki/index.php/Steel02_Material_--_Giuffr%C3%A9-Menegotto-Pinto_Model_with_Isotropic_Strain_Hardening</a><strong>Steel02</strong>]),
the formulation of <strong>SteelMPF</strong> introduces several
distinctive features compared to existing models. For example, the model
allows definition of different yield stress values and strain hardening
ratios for tension and compression, and it considers degradation of
cyclic curvature parameter <em>R</em> for strain reversals in both pre-
and post- yielding regions, which could produce more accurate
predictions of yield capacity for some RC wall specimens (<a
href="http://opensees.berkeley.edu/wiki/index.php/MVLEM_-_Multiple-Vertical-Line-Element-Model_for_RC_Walls"><strong>element
MVLEM</strong></a>, Example 1), whereas <strong>Steel02</strong>
considers the degradation in post-yielding region only. Strain-stress
relationships obtained using <strong>SteelMPF</strong> and
<strong>Steel02</strong> are compared in Figure 2 for a strain history
that includes strain reversals at strain values equal to one-half of the
yield strain (i.e., ε&lt;sub class="subscript"&gt;r&lt;/sub&gt; = ±0.001
= ε&lt;sub class="subscript"&gt;y&lt;/sub&gt;/2).</p>
<figure>
<img src="/OpenSeesRT/contrib/static/SteelMPF_1.png"
title="Figure 2. Comparing the degradation of cyclic curvature in the pre-yielding region for Steel02 and SteelMPF"
width="500"
alt="Figure 2. Comparing the degradation of cyclic curvature in the pre-yielding region for Steel02 and SteelMPF" />
<figcaption aria-hidden="true">Figure 2. Comparing the degradation of
cyclic curvature in the pre-yielding region for Steel02 and
SteelMPF</figcaption>
</figure>
<p>Furthermore, it has been observed from the strain-stress
relationships obtained from quasi-static or dynamic analyses using
existing steel models in OpenSees (e.g., <strong>Steel02</strong>) that
after partial unloading occurs in a model element caused by dynamic
loading or stress re-distribution under quasi-static loading due to
concrete cracking or crushing, the Menegotto-Pinto formulation produces
stress overshooting in the cyclic stress-strain behavior of reinforcing
steel. This overshooting effect is not behavioral and causes
non-physical hardening in the stress-strain behavior, upon reloading
from the partial unloading loop. This phenomenon is illustrated in
Figure 3 for the <strong>Steel02</strong> model in OpenSees. This
anomaly results in overestimation of steel stresses predicted by the
<strong>Steel02</strong> model upon return from partial unloading,
yielding strain-stress curve that may not represent the physical
constitutive behavior of reinforcing steel under cyclic loading. This
limitation in the Menegotto-Pinto model formulation has also been
acknowledged by Filippou et al. (1983). The overshooting effect observed
in the existing OpenSees material model for reinforcing steel (e.g.,
<strong>Steel02</strong>) has been remedied in
<strong>SteelMPF</strong>, via manipulating the model formulation so
that reloading behavior after partial unloading cannot overshoot the
previous loading loop in the cyclic stress-strain behavior. The
comparison between strain-stress relationships obtained using
<strong>SteelMPF</strong> and <strong>Steel02</strong> for a strain
history that includes low-amplitude unloading followed by reloading is
presented in Figure 3.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Steel_MPF_02.png"
title="Figure 3. Comparing the stress overshooting upon reloading from low-amplitude unloading for Steel02 and SteelMPF"
width="500"
alt="Figure 3. Comparing the stress overshooting upon reloading from low-amplitude unloading for Steel02 and SteelMPF" />
<figcaption aria-hidden="true">Figure 3. Comparing the stress
overshooting upon reloading from low-amplitude unloading for Steel02 and
SteelMPF</figcaption>
</figure>
<hr />
<p><strong>References:</strong></p>
<p>1) Filippou F.C., Popov, E.P., and Bertero, V.V. (1983). "Effects of
Bond Deterioration on Hysteretic Behavior of Reinforced Concrete
Joints". Report EERC 83-19, Earthquake Engineering Research Center,
University of California, Berkeley.</p>
<p>2) Kolozvari K., Orakcal K., and Wallace J. W. (2015). "Shear-Flexure
Interaction Modeling of reinforced Concrete Structural Walls and Columns
under Reversed Cyclic Loading", Pacific Earthquake Engineering Research
Center, University of California, Berkeley, <a
href="http://peer.berkeley.edu/publications/peer_reports/reports_2015/webPEER-2015-12-kolozvari.pdf">PEER
Report No. 2015/12</a></p>
<p>3) Menegotto, M., and Pinto, P.E. (1973). Method of analysis of
cyclically loaded RC plane frames including changes in geometry and
non-elastic behavior of elements under normal force and bending.
Preliminary Report IABSE, vol 13.</p>
