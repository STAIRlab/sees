# TzSimple1

<p>This command is used to construct a TzSimple1 uniaxial material
object:</p>

```tcl
uniaxialMaterial TzSimple1 $matTag $tzType $tult $z50 < $c >
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
<td><p>soilType = 1 Backbone of t-z curve approximates Reese and O'Neill
(1987).</p>
<p>soilType = 2 Backbone of t-z curve approximates Mosher (1984)
relation.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">tult</code></td>
<td><p>Ultimate capacity of the t-z material. SEE NOTE 1.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Z50</code></p></td>
<td><p>Displacement at which 50% of tult is mobilized in monotonic
loading.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">c</code></td>
<td><p>The viscous damping term (dashpot) on the far-field (elastic)
component of the displacement rate (velocity). (optional Default = 0.0).
See NOTE 2.</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<ol>
<li>The argument tult is the ultimate capacity of the t-z material. Note
that “t” or “tult” are shear</li>
</ol>
<p>stresses [force per unit area of pile surface] in common design
equations, but are both loads for this uniaxialMaterial [i.e., shear
stress times the tributary area of the pile].</p>
<ol>
<li>Nonzero c values are used to represent radiation damping
effects</li>
</ol>

<p>EQUATIONS and EXAMPLE RESPONSES:</p>
<p>The equations describing PySimple1 behavior are described in
Boulanger, R. W., Curras, C. J., Kutter, B. L., Wilson, D. W., and
Abghari, A. (1999). "Seismic soil-pile-structure interaction experiments
and analyses." Journal of Geotechnical and Geoenvironmental Engineering,
ASCE, 125(9): 750-759. Only minor changes have been made in its
implementation for OpenSees.</p>

The nonlinear t-z behavior is conceptualized as consisting of elastic
( $t-z^e$ ) and plastic
( $t-z^p$ ) components in series. Radiation damping
is modeled by a dashpot on the “far-field” elastic component
( $t-z^e$ ) of the displacement rate. Note that
 $z = z^e + z^p$ , and that  $t = t^e = t^p$ .

<p>The plastic component is described by:</p>

$$t^p = t_{\text{ult}} - (t_{\text{ult}} - t^p_0) \left
[\frac{c z_{50}}{c z_{50} + | z_p - z^p_0|} \right ] $$



where $t_{ult} = $ the ultimate resistance of
the t-z material in the current loading direction, $t^p_o = t^p$ at the start of the current plastic loading cycle,
$z^p_0 = z^P$ at the start of the current plastic
loading cycle, and c = a constant and n = an exponent that define the
shape of the $t-z^p$ curve.

<p>The elastic component can be conveniently expressed as:</p>
<dl>
<dt></dt>
<dd>

$$t^e = C_e \frac{t_{\text{ult}}}{z_{50}} z^e$$

</dd>
</dl>

where $C_e$ = a constant that defines the
normalized elastic stiffness. The value of $C_e$
is not an independent parameter, but rather depends on the constants c
&amp; n (along with the fact that $t = 0.5 t_{\text{ult}}$ at $z = z_{50}$).

<p>The flexibility of the above equations can be used to approximate
different t-z backbone relations. Reese and O’Neill’s (1987) recommended
backbone for drilled shafts is closely approximated using c = 0.5, n =
1.5, and Ce = 0.708. Mosher’s (1984) recommended backbone for axially
loaded piles in sand is closely approximated using c = 0.6, n = 0.85,
and Ce = 2.05. TzSimple1 is currently implemented to allow use of these
two default sets of values. Values of tult and z50 must then be
specified to define the t-z material behavior.</p>
<p>Viscous damping on the far-field (elastic) component of the t-z
material is included for approximating radiation damping. For
implementation in OpenSees the viscous damper is placed across the
entire material, but the viscous force is calculated as proportional to
the component of velocity (displacement rate) that developed in the
far-field elastic component of the material. In addition, the total
force across the t-z material is restricted to tult in magnitude so that
the viscous damper cannot cause the total force to exceed the near-field
soil capacity. Users should also be familiar with numerical oscillations
that can develop in viscous damper forces under transient loading with
certain solution algorithms and damping ratios. In general, an HHT
algorithm is preferred over a Newmark algorithm for reducing such
oscillations in materials like TzSimple1.</p>
<p>Examples of the cyclic loading response of TzSimple1 are given in the
following plots. Note that the response for tzType = 2 has greater
nonlinearity at smaller displacements (and hence greater hysteretic
damping) and that it approaches tult more gradually (such that t/tult is
still well below</p>
<figure>
<img src="/OpenSeesRT/contrib/static/TzSimple1.gif" title="TzSimple1.gif" alt="TzSimple1.gif" />
<figcaption aria-hidden="true">TzSimple1.gif</figcaption>
</figure>

## Examples

<p>REFERENCES:</p>
<p>"Seismic Soil-pile-strcture interaction experiments and analysis",
Boulanger, R.W., Curras, C.J., Kutter, B.L., Wilson, D.W., and Abghari,
A. (1990). Jornal of Geotechnical and Geoenvironmental Engineering,
ASCS, 125(9):750-759.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Ross Boulanger, UC
Davis </span></p>
