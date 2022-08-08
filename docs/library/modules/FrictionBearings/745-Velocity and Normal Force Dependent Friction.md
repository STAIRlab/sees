# Velocity and Normal Force Dependent Friction

This command is used to construct a VelNormalFrcDep friction model
object.

```tcl
frictionModel VelNormalFrcDep $frnTag $aSlow $nSlow
        $aFast $nFast $alpha0 $alpha1 $alpha2 $maxMuFact
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">frnTag</code></td>
<td><p>unique friction model object tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">aSlow</code></td>
<td><p>constant for coefficient of friction at low velocity</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">nSlow</code></td>
<td><p>exponent for coefficient of friction at low velocity</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">aFast</code></td>
<td><p>constant for coefficient of friction at high velocity</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">nFast</code></td>
<td><p>exponent for coefficient of friction at high velocity</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alpha0</code></td>
<td><p>constant rate parameter coefficient</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">alpha1</code></p></td>
<td><p>linear rate parameter coefficient</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">alpha2</code></p></td>
<td><p>quadratic rate parameter coefficient</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">maxMuFact</code></td>
<td><p>factor for determining the maximum coefficient of friction. This
value prevents the friction coefficient from exceeding an unrealistic
maximum value when the normal force becomes very small. The maximum
friction coefficient is determined from μFast, for example μ ≤
$maxMuFac*μFast.</p></td>
</tr>
</tbody>
</table>
<hr />

## Theory

1. Define the friction coefficient at slow (μSlow) and fast (μFast)
   velocity [1] (Figure 3):
   <dl>
   <dt></dt>
   <dd>
   <dl>
   <dt></dt>
   <dd>
   μSlow = aSlow*N^(nSlow-1)
   </dd>
   </dl>
   </dd>
   </dl>
   <dl>
   <dt></dt>
   <dd>
   <dl>
   <dt></dt>
   <dd>
   μFast = aFast*N^(nFast-1)
   </dd>
   </dl>
   </dd>
   </dl>
   where `aSlow`, `aFast`, `nSlow` ≤ 1, `nFast` ≤ 1 are constants that determine
   the friction coefficient models. As the friction coefficients μSlow and
   μFast are unitless, the user must be careful to define the constants to
   coincide with the units of the model input data.

2. The friction coefficient as a function of velocity is [2]:
   <dl>
   <dt></dt>
   <dd>
   <dl>
   <dt></dt>
   <dd>
   μ = μFast - (μFast-μSlow )*exp(-a*udot)
   </dd>
   </dl>
   </dd>
   </dl>

   where udot is the velocity at the sliding interface and a is a rate
   parameter.

3. In this friction model, a is assumed to be dependent on axial
   force $N$ through:
   $$
   a = \alpha_0 + \alpha_1 N + \alpha_2 N^2
   $$
   where $\alpha_0$, $\alpha_1$ and $\alpha_2$ are constants, with units of Time/Length,
   Time/Length/Force and Time/Length/Force<sup class="superscript">2</sup> respectively.

<figure>
<img src="/OpenSeesRT/contrib/static/TPB_Nhan_Fig3.jpg" title="TPB_Nhan_Fig3.jpg" width="300" />
<figcaption aria-hidden="true">TPB_Nhan_Fig3.jpg</figcaption>
</figure>

<hr />
<p>SPECIAL CASES:</p>
1. Constant friction coefficient:
   <dl>
   <dt></dt>
   <dd>
   <dl>
   <dt></dt>
   <dd>
   <strong>μ = const:</strong> `nSlow` = `nFast` = 1.0; `aSlow` = $aFast = μ;
   all other constants defining μ are arbitrary.
   </dd>
   </dl>
   </dd>
   </dl>

2. Friction coefficient varies with velocity but is independent of
   vertical force:
   <dl>
   <dt></dt>
   <dd>
   <dl>
   <dt></dt>
   <dd>
   <strong>μ is independent of vertical force:</strong> $nSlow = $nFast =
   1.0; $alpha0 = a (rate parameter); $alpha1 = $alpha2 = 0.
   </dd>
   </dl>
   </dd>
   </dl>

3. Friction coefficient varies with vertical force but is independent
   of velocity:
   <dl>
   <dt></dt>
   <dd>
   <dl>
   <dt></dt>
   <dd>
   <strong>μ is independent of velocity:</strong> $nSlow = $nFast; $aSlow =
   $aFast; all other constants defining μ are arbitrary.
   </dd>
   </dl>
   </dd>
   </dl>

<hr />

## Examples

```tcl
set muSlow 0.12
set muFast 0.18
set nSlow 0.8
set nFast 0.7
set alpha0 25.0
set alpha1 0.0
set alpha2 0.0
frictionModel VelNormalFrcDep 1 [expr $muSlow/pow($W,$nSlow-1.0)] \
        $nSlow [expr $muFast/pow($W,$nFast-1.0)] $nFast $alpha0 $alpha1 $alpha2 3.0
```


## References
<p>[1] Bowden F.P., Tabor D. (1964). "The friction and lubrication of
solids - part II." Oxford University Press, London, Great Britain,
1964.</p>
<p>[2] Constantinou M.C., Mokha A., Reinhorn A. (1990). "Teflon bearings
in base isolation. II: Modeling." Journal of Structural Engineering
(ASCE) 1990; 116(2): 455-474</p>

<p>RELATED TO:</p>
<ul>
<li><a
href="http://opensees.berkeley.edu/wiki/index.php/Flat_Slider_Bearing_Element">Flat
Slider Bearing Element</a></li>
<li><a
href="http://opensees.berkeley.edu/wiki/index.php/Single_Friction_Pendulum_Bearing_Element">Single
Friction Pendulum Bearing Element</a></li>
<li><a
href="http://opensees.berkeley.edu/wiki/index.php/Triple_Friction_Pendulum_Element">Triple
Friction Pendulum Bearing Element</a></li>
</ul>

<hr />
<p>Code Developed by: <span style="color:blue"> Nhan D. Dao,
University of Nevada - Reno. E-mail: nhan.unr@gmail.com
</span></p>

