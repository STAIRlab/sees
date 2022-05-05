# Steel02 Material -- Giuffré-Menegotto-Pinto Model with Isotropic Strain Hardening

<p>This command is used to construct a uniaxial Giuffre-Menegotto-Pinto
steel material object with isotropic strain hardening.</p>

```tcl
uniaxialMaterial Steel02 $matTag $Fy $E $b $R0 $cR1 $cR2
        &lt;$a1 $a2 $a3 $a4 $sigInit&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Fy</code></td>
<td><p>yield strength</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">E0</code></td>
<td><p>initial elastic tangent</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">b</code></td>
<td><p>strain-hardening ratio (ratio between post-yield tangent and
initial elastic tangent)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$R0 $CR1 $CR2</strong></p></td>
<td><p>parameters to control the transition from elastic to plastic
branches. Recommended values: <strong>$R0</strong>=between 10 and 20,
<strong>$cR1</strong>=0.925, <strong>$cR2</strong>=0.15</p></td>
</tr>
<tr class="even">
<td><p><strong>$a1</strong></p></td>
<td><p>isotropic hardening parameter, increase of compression yield
envelope as proportion of yield strength after a plastic strain of
$a2*($Fy/E0). (optional)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$a2</strong></p></td>
<td><p>isotropic hardening parameter (see explanation under $a1).
(optional default = 1.0).</p></td>
</tr>
<tr class="even">
<td><p><strong>$a3</strong></p></td>
<td><p>isotropic hardening parameter, increase of tension yield envelope
as proportion of yield strength after a plastic strain of $a4*($Fy/E0).
(optional default = 0.0)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$a4</strong></p></td>
<td><p>isotropic hardening parameter (see explanation under $a3).
(optional default = 1.0)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">sigInit</code></td>
<td><p>Initial Stress Value (optional, default: 0.0) the strain is
calculated from epsP=$sigInit/$E if (sigInit!= 0.0) { double epsInit =
sigInit/E; eps = trialStrain+epsInit; } else eps = trialStrain;</p></td>
</tr>
</tbody>
</table>
<p>more on <a href="OpenSees_uniaxialMaterial_Arguments_--_Steel02"
title="wikilink">OpenSees uniaxialMaterial Arguments -- Steel02</a></p>
<p>REFERENCE:</p>
<p>Filippou, F. C., Popov, E. P., Bertero, V. V. (1983). "Effects of
Bond Deterioration on Hysteretic Behavior of Reinforced Concrete
Joints". Report EERC 83-19, Earthquake Engineering Research Center,
University of California, Berkeley.</p>
<p>Steel02 Material -- Material Parameters of Monotonic Envelope</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Steel02Monotonic.jpg" title="Steel02Monotonic.jpg"
alt="Steel02Monotonic.jpg" />
<figcaption aria-hidden="true">Steel02Monotonic.jpg</figcaption>
</figure>
<p>Steel02 Material -- Hysteretic Behavior of Model w/o Isotropic
Hardening</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Steel02HystereticA.jpg" title="Steel02HystereticA.jpg"
alt="Steel02HystereticA.jpg" />
<figcaption aria-hidden="true">Steel02HystereticA.jpg</figcaption>
</figure>
<p>Steel02 Material -- Hysteretic Behavior of Model with Isotropic
Hardening in Compression</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Steel02HystereticB.jpg" title="Steel02HystereticB.jpg"
alt="Steel02HystereticB.jpg" />
<figcaption aria-hidden="true">Steel02HystereticB.jpg</figcaption>
</figure>
<p>Steel01 Material -- Hysteretic Behavior of Model with Isotropic
Hardening in Tension</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Steel02HystereticC.jpg" title="Steel02HystereticC.jpg"
alt="Steel02HystereticC.jpg" />
<figcaption aria-hidden="true">Steel02HystereticC.jpg</figcaption>
</figure>
<hr />
<p>Code Developed by: <span style="color:blue"> Filip Filippou, UC
Berkeley </span></p>
<p>Images Developed by: <span style="color:blue"> Silvia Mazzoni
</span></p>
