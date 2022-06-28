# ReinforcingSteel

This command is used to construct a `ReinforcingSteel` uniaxial
material object. This object is intended to be used in a reinforced
concrete fiber section as the steel reinforcing material.

::: {apidoc="opensees.uniaxial.ReinforcingSteel"}
:::

```tcl
uniaxialMaterial ReinforcingSteel $matTag $fy $fu $Es $Esh $esh $eult 
        < -GABuck $lsr $beta $r $gama >
        < -DMBuck $lsr < $alpha > >
        < -CMFatigue $Cf $alpha $Cd > 
        < -IsoHard < $a1 < $limit > > >
```

<hr />
<table>
<tbody>

<tr class="even">
  <td><code class="parameter-table-variable">matTag</code></td>
  <td>Material tag.</td>
</tr>
<tr class="odd">
  <td><code class="parameter-table-variable">fy</code></td>
  <td>yield stress.</td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fu</code></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Es</code></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Esh</code></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">esh</code></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">eult</code></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-flag">-GABuck</code></p></td>
<td>
<!--
</tr>
</tbody>
</table>
<p>&lt;blockquote&gt;</p>
-->
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">lsr</code></td>
<td><p>Slenderness Ratio (see Figure 2)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">beta</code></td>
<td><p>Amplification factor for the buckled stress strain curve. (see
Figure 3)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">r</code></td>
<td><p>Buckling reduction factor</p>
<dl>
<dt></dt>
<dd>
r can be a real number between [0.0 and 1.0]
</dd>
</dl>
<dl>
<dt></dt>
<dd>
`r=1.0` full reduction (no buckling)
</dd>
</dl>
<dl>
<dt></dt>
<dd>
r=0.0 no reduction
</dd>
</dl>
<dl>
<dt></dt>
<dd>
0.0&lt;r&lt;1.0 linear interpolation between buckled and unbuckled
curves
</dd>
</dl></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">gamma</code></td>
<td><p>Buckling constant (see Figures 3 and 4)</p></td>
</tr>
</tbody>
</table>
</td>
</tr>

<!--
<p>&lt;/blockquote&gt;</p>
<table>
<tbody>
-->
<tr class="odd">
<td><p><code class="parameter-table-flag">-DMBuck</code></p></td>
<td><p>Buckling model based on Dhakal and Maekawa (2002)</p>
<!--
</td>
</tr>
</tbody>
</table>
<p>&lt;blockquote&gt;</p>
-->
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">lsr</code></td>
<td><p>Slenderness Ratio (see Figure 2)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>Adjustment Constant usually between 0.75 and 1.0</p>
<dl>
<dt></dt>
<dd>
Default: alpha=1.0, this parameter is optional.
</dd>
</dl></td>
</tr>
</tbody>
</table>
</tr>

<!--
<p>&lt;/blockquote&gt;</p>
<table>
<tbody>
-->
<tr class="odd">
<td><p><code class="parameter-table-flag">-CMFatigue</code></p></td>
<td><p>Coffin-Manson Fatigue and Strength Reduction</p>

<!--
</td>
</tr>
</tbody>
</table>
<p>&lt;blockquote&gt;</p>
-->

<table>
<tbody>
<tr class="odd">
<td><p><code>Cf</code></p></td>
<td><p>Coffin-Manson constant C (see Figure 5)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>Coffin-Manson constant a (see Figure 5)</p>
</td>
</tr>
<tr class="odd">
<td><p><strong>$C<sub
class="subscript">d</sub></strong></p></td>
<td><p>Cyclic strength reduction constant (see Figure 6 and Equation
3)</p></td>
</tr>
</tbody>
</table>
</td></tr>

<!--
<p>&lt;/blockquote&gt;</p>
<table>
<tbody>
<tr class="odd">
-->
<td><p><code class="parameter-table-flag">-IsoHard</code></p></td>
<td><p>Isotropic Hardening / Diminishing Yield Plateau</p>
<!--
</td>
</tr>
</tbody>
</table>
<p>&lt;blockquote&gt;</p>
-->

<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">a1</code></p></td>
<td><p>Hardening constant (default = 4.3)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">limit</code></td>
<td><p>Limit for the reduction of the yield plateau. % of original
plateau length to remain (0.01 &lt; limit &lt; 1.0 )</p>
<dl>
<dt></dt>
<dd>
Limit =1.0, then no reduction takes place (default =0.01)
</dd>
</dl></td>
</tr>
</tbody>
</table>
</td>
</tr>

<!--
<p>&lt;/blockquote&gt;</p>
<table>
<tbody>
-->
<tr class="odd">
<td><p><code class="parameter-table-flag">-MPCurveParams</code></p></td>
<td><p>Menegotto and Pinto Curve Parameters see Fig 6b</p>
<!--
</td>
</tr>
</tbody>
</table>
<p>&lt;blockquote&gt;</p>
-->
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">R1</code></p></td>
<td><p>(default = 0.333)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">R2</code></p></td>
<td><p>(default = 18)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">R3</code></p></td>
<td><p>(default = 4)</p></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

:::


<p><strong>NOTE:</strong> This simulation is based on the Chang and
Mander(1994) uniaxial steel model. The simulation has incorporated
additional reversal memory locations to better control stress
overshooting (default is 10 branches but this can be easily modified by
changing the variable "`LastRule_RS`" within the header file
"`ReinforcingSteel.h`"). The cycle counting method implemented in the
routine achieves the same result as rainflow counting. Fatigue
parameters are based on the Coffin-Manson equation for plastic strain
amplitude as indicated in Figure 6a. The buckling simulations
incorporated consist of a variation on Gomes and Appleton (1997) and
Dhakal and Maekawa (2002). The buckling and fatigue portions of this
simulation are still being further enhanced and refined. Additional
buckling and fatigue options should be available in the near future.</p>

<figure>
<img src="/OpenSeesRT/contrib/static/ReinfSteel2430.png" alt="ReinfSteel2430.png" />
<figcaption>Figure 1: Material Constants</figcaption>
</figure>

### Backbone curve 

The backbone curve shown in Figure 1 is used as a bounding surface for the
reinforcing bar simulation. This backbone curve is shifted as described by
Chang and Mander (1994) to account for Isotropic hardening. This backbone can
be obtained by utilizing simple tension test data. Within the material class,
the backbone curve is transformed from engineering stress space to natural
stress space (accounting for change in area as the bar is stressed.) This
allows the single backbone to represent both tensile and compressive
stress-strain relations. The tension and compression backbone curves are not
the same in engineering stress space for this model! This transformation
assumes small strain relations described by Dodd and Restrepo-Posada (1995)

The softening region (strain greater than `eult`), shown in Figure 1,
is a localization effect due to necking and is a function of the gage
length used during measurement. This geometric effect is ignored in this
simulation. In this simulation, it is assumed that there is no softening
in natural stress space. Because the simulation always converts back to
engineering stress space, you will observe some softening in the tension
response due to the reduction in area, however this will be much smaller
than that shown in the original backbone curve proposed by Chang and
Mander.

### Diminishing yield plateau
It has been observed that when a reinforcing bar is subjected to plastic strain reversals within
the yield plateau, strain hardening will initiate at a lower strain that
that of the same bar loaded monotonically. Additionally, isotropic
hardening can result from repeated strain reversals and is commonly
related to accumulated plastic strain. These two aspects of the
stress-strain behavior of steel bars are somewhat related and that by
shortening the yield plateau as a function of accumulated plastic
strain, the model will have some capability to simulate both the
diminishing yield plateau and isotropic hardening. The Chang and Mander
model, on which this formulation is based, models only anisotropic
hardening by shifting the backbone curves and by targeting previous
reversal points on the backbone curves. By adding a component of
isotropic hardening, the model has additional capabilities and is able
to more accurately simulate test data.

Accumulated plastic strain is tracked within the material model for
each branch, plateau adjustments are made only in the outer branches for
simplicity. The plastic strain due to the backbone curve is ignored so
that a monotonically loaded sample can be calibrated to a monotonic test
sample more easily.

### Buckling Models

<figure>
<img src="/OpenSeesRT/contrib/static/ReinfSteel2431.png" alt="ReinfSteel2431.png" />
<figcaption>Figure 2: Slenderness Defined</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/ReinfSteel2432.png" title="ReinfSteel2432.png"
alt="ReinfSteel2432.png" />
<figcaption aria-hidden="true">Figure 3: Buckling Parameters</figcaption>
</figure>

#### Gomes and Appleton buckled curve

Figure 3 describes the use of the
buckling parameters modified from Gomes and Appleton (1997). $\beta$ is an
amplification factor that allows the user to scale the buckling curve.
This is useful to adjust the location of the bifurcation point. The $r$
factor is used to adjust the curve between the buckled curve and the
unbuckled curve. The variable $r$ can only be a real number between $0.0$
and $1.0$. The $\gamma$ factor is the positive stress location about which the
buckling factor is initiated. This factor was introduced to avoid kinks
in the reloading branch. The implementation of the $\gamma$ factor is shown in
Figure 3. The basic idea is that the stress strain curves are reduced
toward the positive stress $\gamma f_{su}$. The value $\gamma$
should be between $0.0$ and $1.0$. A $\gamma$ of $0.0$ will factor to the 
zero stress axis. This will usually produce
a kink in the reloading curve at the zero stress location. Good results
have been obtained using the following values for the buckling
constants.

<p><img src="/OpenSeesRT/contrib/static/ReinfSteel2433.png" title="ReinfSteel2433.png"
alt="ReinfSteel2433.png" /> or <img src="/OpenSeesRT/contrib/static/ReinfSteel2434.png"
title="ReinfSteel2434.png" alt="ReinfSteel2434.png" /></p>

Figure 4 displays the buckling behavior due to the variation of the
different constants. The response shown on the upper left is the
unbuckled case. In each of the other cases, buckling behavior is defined
by the constants shown.

<figure>
<img src="/OpenSeesRT/contrib/static/ReinfSteel2435.png" alt="ReinfSteel2435.png" />
<figcaption>Figure 4: Effect of Sample Parameters in the Gomes and Appleton Buckling Model</figcaption>
</figure>


#### Dhakal and Maekawa buckled curve

The buckling model described in this section is based on Dhakal and
Maekawa (2002). This model takes two terms, $\ell_{sr}$ and $a$. $\ell_{sr}$ is the slenderness
ratio as described in Figure 2 and $a$ is an amplification factor. Dhakal and
Maekawa suggest a value of $a =1.0$ for linear strain hardening and $a =0.75$ for
elastic perfectly plastic material behavior. The material model in this
implementation is neither linear strain hardening nor elastic perfectly
plastic. However, since the material model does include strain hardening $a=1.0$
has been assumed as the default value. Figure 5 shows the unbuckled vs buckled
stress strain response curves.

<figure>
<img src="/OpenSeesRT/contrib/static/ReinfSteel2436.png" title="ReinfSteel2436.png"
alt="ReinfSteel2436.png" />
<figcaption>Figure 5: Effect of Suggested Parameters in the Dhakal and Maekawa Buckling Model</figcaption>
</figure>

### Cyclic Degradation

$C_f$ and $a$ are factors used to relate the number of half cycles to fracture to the
half cycle plastic strain amplitude (Figure 6a). Plastic strain half
cycle amplitude is defined by Equation 1. The total half cycle strain
amplitude,, is shown in Figure 6b as the change in strain from reversal
A to reversal B. $C_f$ and a are
used to define a cumulative damage factor, $D$, as described in Equation
2.

<p><img src="/OpenSeesRT/contrib/static/ReinfSteel2438.png" title="ReinfSteel2438.png"
alt="ReinfSteel2438.png" /><img src="/OpenSeesRT/contrib/static/ReinfSteel2439.png"
title="ReinfSteel2439.png" alt="ReinfSteel2439.png" /></p>
<p>Figure 6a: Coffin-Manson Constants Figure 6b: Half Cycle Terms Defined</p>
<p><img src="/OpenSeesRT/contrib/static/ReinfSteel2440.png" title="ReinfSteel2440.png"
alt="ReinfSteel2440.png" /> (1) <img src="/OpenSeesRT/contrib/static/ReinfSteel2441.png"
title="ReinfSteel2441.png" alt="ReinfSteel2441.png" /> (2)</p>

The cumulative damage factor is zero at no damage and $1.0$ at
fracture. Once a bar has been determined to have fractured, the strength
is rapidly degraded to zero.

<figure>
<img src="/OpenSeesRT/contrib/static/ReinfSteel2442.png" title="ReinfSteel2442.png"
alt="ReinfSteel2442.png" />
<figcaption>Figure 7: Strength Reduction</figcaption>
</figure>

A degrade constant, $K_1$, is
used to describe loss in strength due to damage or other phenomenon
resulting in softening due to plastic reversals. The degradation is
currently assumed to have a simple linear relationship with $D$. This is
used to correlate strength degradation to the cumulative damage factor.
This linear relationship is shown in Equation 3.

$$
\phi_{S R}=K_{1} D
$$
<p><!-- <img src="/OpenSeesRT/contrib/static/ReinfSteel2443.png" title="ReinfSteel2443.png"
alt="ReinfSteel2443.png" /> --> 
(3)</p>

Alternately this simple linear equation can be rewritten in a way
that makes the strength degradation independent of the number of half
cycles to failure. Keeping the failure and degradation terms independent
is convenient for calibration. Equation 3 is rewritten below utilizing
the strength degradation constant $C_d$.

<p><img src="/OpenSeesRT/contrib/static/ReinfSteel2444.png" title="ReinfSteel2444.png"
alt="ReinfSteel2444.png" /> (4)</p>
<p>The constants K<sub class="subscript">1</sub>, and
$C_d$ can be related as shown in
Equation 5.</p>
<p><img src="/OpenSeesRT/contrib/static/ReinfSteel2445.png" title="ReinfSteel2445.png"
alt="ReinfSteel2445.png" /> (5)</p>

Suggested starting values have been obtained from data reported by
Brown and Kunnath (2000) for bars with a slenderness of $6$. Keep in mind
that this experimental data is limited and additional calibration may be
necessary to capture realistic behavior in a reinforcing bar embedded in
concrete and influenced by other factors such as confinement.

|        |          |
|--------|----------|
| $a$    | $0.506$  |
| $C_f$  | $0.260$  |
| $C_d$  | $0.389$  |

#### Sample Simulations of Degradation behavior

$a$ is best obtained from calibration of test results. $a$ is used to
relate damage from one strain range to an equivalent damage at another
strain range. This is usually constant for a material type.

$C_f$ is the ductility constant used to adjust the number of cycles to
failure. A higher value for $C_f$ will result in a lower damage for 
each cycle. A higher value $C_f$ translates to a larger number of
cycles to failure.

$C_d$ is the strength reduction constant. A larger value for $C_d$ will result
in a lower reduction of strength for each cycle. The four charts shown in
Figure 8 demonstrate the effect that some of the variables have on the cyclic
response.

<figure>
<img src="/OpenSeesRT/contrib/static/ReinfSteel2446.png" alt="ReinfSteel2446.png" />
<figcaption>Figure 8: Fatigue and Degradation Parameter Examples</figcaption>
</figure>

In Figure 8, the upper left response contains no strength degradation by
setting the $C_d$ variable to 0.0. The upper right response shows strength
degradation due to the suggested values of $C_f$, $a$, and $C_d$. The response
shown on the lower left demonstrates the change in the response when the
suggested values of $C_f$ and $a$ are used with $C_d=0.6$. Making the value of
$C_d$ larger results in less strength reduction due to damage. The response on
the lower right once again returns to the suggested values but $C_f$ is changed
to 0.15. This results in a more rapid accumulation of damage causing the bar to
fail sooner. Note however that the strength degradation is unaffected by the
more rapid accumulation of damage. The strength reduction and failure are not
interdependent making the model easier to calibrate.

## References
<ul>
<li>Chang, G. and Mander, J. (1994). "Seismic Energy Based Fatigue
  Damage Analysis of Bridge Columns: Part I - Evaluation of Seismic
  Capacity." NCEER Technical Report 94-0006.</li>
<li>Dodd, L. and Restrepo-Posada, J. (1995). "Model for Predicting
  Cyclic Behavior of Reinforcing Steel" J. Struct. Eng., 121(3),
  433-445.</li>
<li>Gomes, A., and Appleton, J. (1997). "Nonlinear Cyclic Stress-Strain
  Relationship of Reinforcing Bars Including Buckling." Eng. Struct.,
  19(10), 822-826.</li>
<li>Brown, J. and Kunnath, S.K. (2000). "Low Cycle Fatigue Behavior of
  Longitudinal Reinforcement in Reinforced Concrete Bridge Columns." NCEER
  Technical Report 00-0007.</li>
<li>Dhakal, R. and Maekawa, K. (2002). "Modeling for Postyield Buckled
  of Reinforcement" J. Struct. Eng., 128(9), 1139-1147.</li>
</ul>

<table>
<tbody>
<tr class="odd">
<td><p><strong>Code developed by:</strong></p></td>
<td><p>Jon Mohle M.S., P.E.</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>Sashi Kunnath: <a
href="http://cee.engr.ucdvis.edu/faculty/kunnath/kunnath.htm">http://cee.engr.ucdvis.edu/faculty/kunnath/kunnath.htm</a></p></td>
</tr>
</tbody>
</table>

