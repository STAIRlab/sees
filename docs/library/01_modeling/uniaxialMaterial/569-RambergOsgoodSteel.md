# RambergOsgoodSteel

<p>This command is used to construct a Ramberg-Osgood steel material
object.</p>

```tcl
uniaxialMaterial RambergOsgoodSteel $matTag $fy $E0 $a $n
```
<hr />
<table>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">matTag</code></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fy</code></td>
<td>yield strength</td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">E0</code></td>
<td>initial elastic tangent</td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">a</code></td>
yield offset parameter. A commonly used value for <code>a</code> is $0.002$
</tr>
<tr class="even">
<td><code class="parameter-table-variable">n</code></td>
<td>
Parameters to control the transition from elastic to plastic branches. Additionally controls the hardening of the material: by increasing the "n" hardening ratio will be decreased.
Commonly used values for <code>n</code> are 5 or greater.
</td>
</tr>
</tbody>
</table>

<hr />
<p><strong>Introduction to the Ramberg-Osgood’s Material
Model:</strong></p>
<p>In earthquake engineering, Ramberg-Osgood functions are often used to
model the behavior of structural steel materials and components. These
functions are obtained when the power is normalized to an arbitrary
strain, ε0, for which the plastic component of the strain, εplastic, is
not zero. Generally the yield strain, εy, provides a good choice for
normalization of strain, the Ramberg-Osgood function is expressed as
[1]:</p>

$$
\varepsilon=\frac{\sigma}{E_{0}}+a\left(\frac{\sigma}{\sigma_{0}}\right)^{n}
$$

<p>Where E0 is the initial elastic modulus and σ0 is equal to Eε0.</p>
<hr />

<p><strong>More explanation about parameter “a” (yielding offset)</strong></p>
The value “a” which is equal to ασ/E_0 can be seen as a yield offset,
as shown in Fig.1. This comes from the fact that

$$
\epsilon=\dfrac{(1+\alpha) \sigma_{0}}{E}
$$

<p>when σ=σ0.</p>
<p>Accordingly (see Fig.1):</p>
<figure>
<img src="/OpenSeesRT/contrib/static/RambergOsgoodSteel03.png" title="RambergOsgoodSteel03.png"
width="400" alt="RambergOsgoodSteel03.png" />
<figcaption aria-hidden="true">RambergOsgoodSteel03.png</figcaption>
</figure>

Values for α can also be found by means of fitting to experimental
data, although for some materials, it can be fixed in order to have the
yield offset equal to the accepted value of strain of 0.2%, which means
[2]: $\alpha \frac{\sigma}{E_{0}}=0.002$ .

<!-- <img src="/OpenSeesRT/contrib/static/RambergOsgoodSteel06.png"
title="RambergOsgoodSteel06.png" width="100"
alt="RambergOsgoodSteel06.png" /> -->

<figure>
<img src="/OpenSeesRT/contrib/static/RambergOsgoodSteel02.png"
title="Fig. 1: Generic representation of the Stress-Strain curve by means of the Ramberg-Osgood equation. Strain corresponding to the yield point is the sum of the elastic and plastic components."
width="400"
alt="Fig. 1: Generic representation of the Stress-Strain curve by means of the Ramberg-Osgood equation. Strain corresponding to the yield point is the sum of the elastic and plastic components." />
<figcaption aria-hidden="true">Fig. 1: Generic representation of the
Stress-Strain curve by means of the Ramberg-Osgood equation. Strain
corresponding to the yield point is the sum of the elastic and plastic
components.</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/RambergOsgoodSteel01.png"
title="Fig. 2: RambergOsgoodSteel Material -- Hysteretic Behavior of Model"
width="500"
alt="Fig. 2: RambergOsgoodSteel Material -- Hysteretic Behavior of Model" />
<figcaption aria-hidden="true">Fig. 2: RambergOsgoodSteel Material --
Hysteretic Behavior of Model</figcaption>
</figure>
<hr />

## References
1. Michel Bruneau, Chia-Ming Uang Andrew Whittaker. “Ductile Design of Steel Structures” McGraw-Hill
   Professional, 1997, ISBN: 0070085803 - 978-0070085800 

2. Ramberg, W., &amp; Osgood, W. R. (1943). “Description of stress-strain curves by
   three parameters.” Technical Note No. 902, National Advisory Committee
   For Aeronautics, Washington DC.

<hr />

<p><strong>Contact Authors:</strong></p>

<p>Reza Rahimi, Graduate Research Assistant of Structural Engineering,
Dalhousie University, reza.rahimi@dal.ca</p>
<p>Reza Sepasdar, Graduate Research Assistant of Structural Engineering,
Dalhousie University, reza.sepasdar@dal.ca</p>
<p>Mohammad Reza Banan, Associate Professor of Civil Engineering,
Department of Civil and Environmental Engineering, Shiraz University,
Shiraz, Iran, banan@shirazu.ac.ir</p>
