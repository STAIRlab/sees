# PySimple1

<p>This command is used to construct a PySimple1 uniaxial material
object:</p>

```tcl
uniaxialMaterial PySimple1 $matTag $soilType $pult $Y50
        $Cd &lt;$c&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">soilType</code></td>
<td><p>soilType = 1 Backbone of p-y curve approximates Matlock (1970)
soft clay relation.</p>
<p>soilType = 2 Backbone of p-y curve approximates API (1993) sand
relation.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">pult</code></td>
<td><p>Ultimate capacity of the p-y material. Note that "p" or "pult"
are distributed loads [force per length of pile] in common design
equations, but are both loads for this uniaxialMaterial [i.e.,
distributed load times the tributary length of the pile].</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Y50</code></p></td>
<td><p>Displacement at which 50% of pult is mobilized in monotonic
loading.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Cd</code></td>
<td><p>Variable that sets the drag resistance within a fully-mobilized
gap as Cd*pult.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">c</code></td>
<td><p>The viscous damping term (dashpot) on the far-field (elastic)
component of the displacement rate (velocity). (optional Default = 0.0).
Nonzero c values are used to represent radiation damping
effects</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<p>In general the HHT algorithm is preferred over a Newmark algorithm
when using this material. This is due to the numerical oscillations that
can develop with viscous damping forces under transient loading with
certain solution algorithms and damping ratios.</p>
<p>EQUATIONS and EXAMPLE RESPONSES:</p>
<p>The equations describing PySimple1 behavior are described in
Boulanger, R. W., Curras, C. J., Kutter, B. L., Wilson, D. W., and
Abghari, A. (1999). "Seismic soil-pile-structure interaction experiments
and analyses." Journal of Geotechnical and Geoenvironmental Engineering,
ASCE, 125(9): 750-759. Only minor changes have been made in its
implementation for OpenSees.</p>
<p>The nonlinear $p-y$ behavior is conceptualized
as consisting of elastic (p-ye), plastic (p-yp), and gap
$(p-y^g)$ components in series. Radiation damping
is modeled by a dashpot on the “far-field” elastic component
$(p-ye)$ of the displacement rate. The gap
component consists of a nonlinear closure spring (pc-yg) in parallel
with a nonlinear drag spring $(p^d-y^g)$. Note
that $y = y^e + y^p + y^g$, and that
&lt;math&gt;p = p^d + p^c&lt;/math&gt;.</p>
<p>The plastic component has an initial range of rigid behavior between

$$-C_r p_\text{ult} &lt; p &lt; C_r p_\text{ult}$$

with $C_r$ = the ratio of
$p/p_\text{ult} $ when plastic yielding first
occurs in virgin loading. The rigid range of $p$,
which is initially $2 C_r p_\text{ult}$,
translates with plastic yielding (kinematic hardening). The rigid range
of $p$ can be constrained to maintain a minimum
size on both the positive and negative loading sides (e.g., 25% of
&lt;math&gt;p\text{ult}&lt;/math&gt;), and this is accomplished by
allowing the rigid range to expand or contract as necessary. Beyond the
rigid range, loading of the plastic $(p-y^p)$
component is described by:</p>
<dl>
<dt></dt>
<dd>
&lt;math&gt;p = p_{\text{ult}} - (p_{\text{ult}} - p_o) \left [\frac{c
y_{50}}{c y_{50} + | z_p - z^p_0|} \right ]^n &lt;/math&gt;
</dd>
</dl>
<p>where $p_\text{ult}$ = the ultimate resistance
of the $p-y$ material in the current loading
direction, $p_o = p$ at the start of the current
plastic loading cycle, $y^p_o = y_p$ at the start
of the current plastic loading cycle, $c$ =
constant to control the tangent modulus at the start of plastic
yielding, and n = an exponent to control sharpness of the
$p-y^p$ curve.</p>
<p>The closure $(p^c-y^g)$ spring is described
by:</p>
<dl>
<dt></dt>
<dd>

$$p^c = 1.8 p_{\text{ult}} \left [\frac{y_{50}}{y_{50} +
50(y_o^\text{+} - y^g)} - \frac{y_{50}}{y_{50} + 50(y_o^\text{-} - y^g)}
\right ] $$

</dd>
</dl>
<p>where $y_o^+$ = memory term for the positive
side of the gap, $y_o^-$= memory term for the
negative side of the gap. The initial values of
$y_o^+$ and $y_o^-$ were
set as $y_{50}/100$ and &lt;math&gt;-
y_{50}/100&lt;/math&gt;, respectively. The factor of 1.8 brings
$p^c$ up to $p_\text{ult}$
during virgin loading to $y_o^+$ (or
&lt;math&gt;y_o^-&lt;/math&gt;). Gap enlargement follows logic similar
to that of Matlock et al. (1978). The gap grows on the positive side
when the plastic deformation occurs on the negative loading side.
Consequently, the $y_o^+$ value equals the
opposite value of the largest past negative value of, &lt;math&gt;y^p +
y^g + 1.5 y_{50}&lt;/math&gt; where the
$1.5y_{50}$ represents some rebounding of the
gap. Similarly, the $y_o^-$ value equals the
opposite value of the largest past positive value of
&lt;math&gt;y^p+y^g-1.5y_{50}&lt;/math&gt;. This closure spring allows
for a smooth transition in the load displacement behavior as the gap
opens or closes.</p>
<p>The nonlinear drag $(p^d-y^g)$ spring is
described by:</p>
<dl>
<dt></dt>
<dd>
&lt;math&gt;p^d = C_d p_{\text{ult}} - (C_d p_{\text{ult}} - p^d_o)
\left [\frac{y_{50}}{y_{50} + 2| y^g - y^g_o|} \right ]^n &lt;/math&gt;
</dd>
</dl>
<p>where $C_d =$ ratio of the maximum drag force
to the ultimate resistance of the p-y material, &lt;math&gt;d^p_o
=p^d&lt;/math&gt; at the start of the current loading cycle, and
$y^g_o = y^g$ at the start of the current loading
cycle.</p>
<p>The flexibility of the above equations can be used to approximate
different p-y backbone relations. Matlock’s (1970) recommended backbone
for soft clay is closely approximated using &lt;math&gt;c =
10&lt;/math&gt;, $n = 5$, and &lt;math&gt;C_r =
0.35&lt;/math&gt;. API’s (1993) recommended backbone for drained sand is
closely approximated using $c = 0.5$,
&lt;math&gt;n = 2&lt;/math&gt;, and $C_r = 0.2$.
PySimple1 is currently implemented to allow use of these two default
sets of values. Values of $p_\text{ult}$,
&lt;math&gt;y_{50}&lt;/math&gt;, and $C_d$ must
then be specified to define the $p-y$ material
behavior.</p>
<p>Viscous damping on the far-field (elastic) component of the p-y
material is included for approximating radiation damping. For
implementation in OpenSees the viscous damper is placed across the
entire material, but the viscous force is calculated as proportional to
the component of velocity (or displacement) that developed in the
far-field elastic component of the material. For example, this correctly
causes the damper force to become zero during load increments across a
fully formed gap. In addition, the total force across the p-y material
is restricted to pult in magnitude so that the viscous damper cannot
cause the total force to exceed the near-field soil capacity. Users
should also be familiar with numerical oscillations that can develop in
viscous damper forces under transient loading with certain solution
algorithms and damping ratios. In general, an HHT algorithm is preferred
over a Newmark algorithm for reducing such oscillations in materials
like PySimple1.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/PySimple1A.gif" title="PySimple1A.gif" alt="PySimple1A.gif" />
<figcaption aria-hidden="true">PySimple1A.gif</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/PySimple1B.gif" title="PySimple1B.gif" alt="PySimple1B.gif" />
<figcaption aria-hidden="true">PySimple1B.gif</figcaption>
</figure>

## Examples

<p>REFERENCES:</p>
<p>"Seismic Soil-pile-strcture interaction experiments and analysis",
Boulanger, R.w., Curras, C.J., Kutter, B.L., Wilson, D.W., and Abghari,
A. (1990). Jornal of Geotechnical and Geoenvironmental Engineering,
ASCS, 125(9):750-759.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Ross Boulanger, UC
Davis </span>This command is used to construct a PySimple1
uniaxial material object:</p>
