# QzSimple1 Material

<p>This command is used to construct a QzSimple1 uniaxial material
object:</p>

```tcl
uniaxialMaterial QzSimple1 $matTag $qzType $qult $Z50
        &lt;$suction $c&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><strong>$qzType</strong></p></td>
<td><p>qzType = 1 Backbone of q-z curve approximates Reese and O'Neill's
(1987) relation for drilled shafts in clay.</p>
<p>qzType = 2 Backbone of q-z curve approximates Vijayvergiya's (1977)
relation for piles in sand.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$qult</strong></p></td>
<td><p>Ultimate capacity of the q-z material. SEE NOTE 1.</p></td>
</tr>
<tr class="even">
<td><p><strong>$Z50</strong></p></td>
<td><p>Displacement at which 50% of qult is mobilized in monotonic
loading. SEE NOTE 2.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$suction</strong></p></td>
<td><p>Uplift resistance is equal to suction*qult. Default = 0.0. The
value of suction must be 0.0 to 0.1.*</p></td>
</tr>
<tr class="even">
<td><p><strong>$c</strong></p></td>
<td><p>The viscous damping term (dashpot) on the far-field (elastic)
component of the displacement rate (velocity). Default = 0.0. Nonzero c
values are used to represent radiation damping effects.*</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<ol>
<li>$qult: Ultimate capacity of the q-z material. Note that "q" or
"qult" are stresses [force per unit area of pile tip] in common design
equations, but are both loads for this uniaxialMaterial [i.e., stress
times tip area].</li>
<li>$Y50: Displacement at which 50% of pult is mobilized in monotonic
loading. Note that Vijayvergiya's relation (qzType=2) refers to a
"critical" displacement (zcrit) at which qult is fully mobilized, and
that the corresponding z50 would be 0. 125zcrit.</li>
<li>optional args $suction and $c must either both be omitted or both
provided.</li>
</ol>
<p>EQUATIONS and EXAMPLE RESPONSES:</p>
<p>The equations describing QzSimple1 behavior are similar to those for
p-y materials by Boulanger, R. W., Curras, C. J., Kutter, B. L., Wilson,
D. W., and Abghari, A. (1999). "Seismic soil-pile-structure interaction
experiments and analyses." Journal of Geotechnical and Geoenvironmental
Engineering, ASCE, 125(9): 750-759. Modifications were required for
representing the different responses of a $q-z$
material in compression versus uplift.</p>
<p>The nonlinear q-z behavior is conceptualized as consisting of elastic
(q-&lt;math&gt;z^e&lt;/math&gt;), plastic
(q-&lt;math&gt;z^p&lt;/math&gt;), and gap
(&lt;math&gt;q-z^g&lt;/math&gt;) components in series. Radiation damping
is modeled by a dashpot on the “far-field” elastic component
(&lt;math&gt;q-z^e&lt;/math&gt;) of the displacement rate. The gap
component consists of a bilinear closure spring
(&lt;math&gt;q^c-z^g&lt;/math&gt;) in parallel with a nonlinear drag
spring (&lt;math&gt;q^d-z^g&lt;/math&gt;). Note that &lt;math&gt;z = z^e
+ z^p + z^g&lt;/math&gt;, and that &lt;math&gt;q = q^d +
q^c&lt;/math&gt;.</p>
<p>The plastic component has an initial range of rigid behavior between

$$-C_r q_\text{ult} &lt; q &lt; C_r q_\text{ult}$$

with $C_r$ = the ratio of
$\frac{q}{q_{\text{ult}}}$ when plastic yielding
first occurs in virgin loading. The rigid range of q, which is initially
&lt;math&gt;2 C_r q_\text{ult}&lt;/math&gt;, translates and grows with
plastic yielding. The rigid range of q is constrained to a maximum size
of $0.7q_{\text{ult}}$. Beyond the rigid range,
loading of the plastic (&lt;math&gt;q-z^p&lt;/math&gt;) component is
described by:</p>
<dl>
<dt></dt>
<dd>
&lt;math&gt;q = q_{\text{ult}} - (q_{\text{ult}} - q_0) \left [\frac{c *
z_{50}}{c * z_{50} + | z_p - z^p_0|} \right ] &lt;/math&gt;
</dd>
</dl>
<p>where $q_ult$ = the ultimate resistance of the
$q-z$ material in the current loading direction,
$q_o = q$ at the start of the current plastic
loading cycle, p $z^p_o = z^p$ at the start of
the current plastic loading cycle, and c and n are constants that
control the shape of $q-z^p$ curve.</p>
<p>The closure (&lt;math&gt;q^c-z^g&lt;/math&gt;) component is simply a
bilinear elastic spring, which is relatively rigid in compression and
extremely flexible in tension (uplift).</p>
<p>The nonlinear drag (&lt;math&gt;q^d-z^g&lt;/math&gt;) component is
used to allow thethe specification of some minimum “suction” on the pile
tip during uplift. It is described by:</p>
<dl>
<dt></dt>
<dd>
&lt;math&gt;q^d = C_d q_\text{ult} - (C_d q_{\text{ult}} - q^d_0) \left
[\frac{z_{50}}{z_{50} + 2| z^g - z^g_0|} \right ] &lt;/math&gt;
</dd>
</dl>
<p>where $C_d$ = ratio of the maximum drag
(suction) force to the ultimate resistance of the
$q-z$ material, &lt;math&gt;q^d_o =
q^d&lt;/math&gt; at the start of the current loading cycle, and
$z^g_o = z^g$ at the start of the current loading
cycle.</p>
<p>The flexibility of the above equations can be used to approximate
different q-z backbone relations. Reese and O’Neill’s (1987) recommended
backbone for drilled shafts in clay is closely approximated using
&lt;math&gt;c = 0.35&lt;/math&gt;, $n = 1.2$, and
&lt;math&gt;C_r = 0.2&lt;/math&gt;. Vijayvergiya’s (1977) recommended
backbone for piles in sand is closely approximated using &lt;math&gt;c =
12.3&lt;/math&gt;, $n = 5.5$, and &lt;math&gt;C_r
= 0.3&lt;/math&gt;.</p>
<p>QzSimple1 is currently implemented to allow use of these two default
sets of values. Values of $q_\text{ult}$,
&lt;math&gt;z_50&lt;/math&gt;, and suction (i.e.,
&lt;math&gt;C_d&lt;/math&gt;) must then be specified to define the
$q-z$ material behavior.</p>
<p>Viscous damping on the far-field (elastic) component of the
$q-z$ material is included for approximating
radiation damping. For implementation in OpenSees the viscous damper is
placed across the entire material, but the viscous force is calculated
as proportional to the component of velocity (or displacement) that
developed in the far-field elastic component of the material. For
example, this correctly causes the damper force to become zero during
load increments across a fully formed gap in uplift. In addition, the
total force across the $q-z$ material is
restricted to $q_\text{ult}$ in magnitude so that
the viscous damper cannot cause the total force to exceed the near-field
soil capacity. Users should also be familiar with numerical oscillations
that can develop in viscous damper forces under transient loading with
certain solution algorithms and damping ratios. In general, an HHT
algorithm is preferred over a Newmark algorithm for reducing such
oscillations in materials like QzSimple1.</p>
<p>Examples of the monotonic backbones and cyclic loading response of
QzSimple1 are given in the following plots.</p>
<figure>
<img src="QzSimple1A.gif" title="QzSimple1A.gif" alt="QzSimple1A.gif" />
<figcaption aria-hidden="true">QzSimple1A.gif</figcaption>
</figure>
<figure>
<img src="QzSimple1B.gif" title="QzSimple1B.gif" alt="QzSimple1B.gif" />
<figcaption aria-hidden="true">QzSimple1B.gif</figcaption>
</figure>
<p>EXAMPLE:</p>
<p>REFERENCES:</p>
<p>"Seismic Soil-pile-strcture interaction experiments and analysis",
Boulanger, R.W., Curras, C.J., Kutter, B.L., Wilson, D.W., and Abghari,
A. (1990). Jornal of Geotechnical and Geoenvironmental Engineering,
ASCS, 125(9):750-759.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Ross Boulanger, UC
Davis </span>This command is used to construct a PySimple1
uniaxial material object:</p>
