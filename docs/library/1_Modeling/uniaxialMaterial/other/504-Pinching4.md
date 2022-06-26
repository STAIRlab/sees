# Pinching4

This command is used to construct a uniaxial material that represents
a "pinched" load-deformation response and exhibits degradation under
cyclic loading. Cyclic degradation of strength and stiffness occurs in
three ways: unloading stiffness degradation, reloading stiffness
degradation, strength degradation.

```tcl
uniaxialMaterial Pinching4 $matTag $ePf1 $ePd1 $ePf2
        $ePd2 $ePf3 $ePd3 $ePf4 $ePd4 
        < $eNf1 $eNd1 $eNf2 $eNd2 $eNf3 $eNd3 $eNf4 $eNd4 > 
        $rDispP $rForceP $uForceP 
        < $rDispN $rForceN $uForceN > 
        $gK1 $gK2 $gK3 $gK4 $gKLim $gD1 $gD2 $gD3 $gD4 $gDLim $gF1 $gF2
        $gF3 $gF4 $gFLim $gE $dmgType
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><code>ePf1 ePf2 ePf3 ePf4</code></p></td>
<td><p>floating point values defining force points on the positive
response envelope</p></td>
</tr>
<tr class="odd">
<td><p><code>ePd1 ePd2 ePd3 ePd4</code></p></td>
<td><p>floating point values defining deformation points on the positive
response envelope</p></td>
</tr>
<tr class="even">
<td><p><code>eNf1 eNf2 eNf3 eNf4</code></p></td>
<td><p>floating point values defining force points on the negative
response envelope</p></td>
</tr>
<tr class="odd">
<td><p><code>eNd1 eNd2 eNd3 eNd4</code></p></td>
<td><p>floating point values defining deformation points on the negative
response envelope</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rDispP</code></td>
<td><p>floating point value defining the ratio of the deformation at
which reloading occurs to the maximum historic deformation
demand</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fFoceP</code></td>
<td><p>floating point value defining the ratio of the force at which
reloading begins to force corresponding to the maximum historic
deformation demand</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">uForceP</code></td>
<td><p>floating point value defining the ratio of strength developed
upon unloading from negative load to the maximum strength developed
under monotonic loading</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rDispN</code></td>
<td><p>floating point value defining the ratio of the deformation at
which reloading occurs to the minimum historic deformation
demand</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fFoceN</code></td>
<td><p>floating point value defining the ratio of the force at which
reloading begins to force corresponding to the minimum historic
deformation demand</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">uForceN</code></td>
<td><p>floating point value defining the ratio of strength developed
upon unloading from negative load to the minimum strength developed
under monotonic loading</p></td>
</tr>
<tr class="even">
<td><p><code>gK1 gK2 gK3 gK4 gKLim</code></p></td>
<td><p>floating point values controlling cyclic degradation model for
unloading stiffness degradation</p></td>
</tr>
<tr class="odd">
<td><p><code>gD1 gD2 gD3 gD4 gDLim</code></p></td>
<td><p>floating point values controlling cyclic degradation model for
reloading stiffness degradation</p></td>
</tr>
<tr class="even">
<td><p><code>gF1 gF2 gF3 gF4 gFLim</code></p></td>
<td><p>floating point values controlling cyclic degradation model for
strength degradation</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">gE</code></td>
<td><p>floating point value used to define maximum energy dissipation
under cyclic loading. Total energy dissipation capacity is defined as
this factor multiplied by the energy dissipated under monotonic
loading.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">dmgType</code></td>
<td><p>string to indicate type of damage (option: "cycle",
"energy")</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Piinching4.jpg" title="Piinching4.jpg" alt="Piinching4.jpg" />
<figcaption aria-hidden="true">Piinching4.jpg</figcaption>
</figure>
<p>Damage Models:</p>
<p>Stiffness and strength are assumed to deteriorate due to the imposed
"load" history. The same basic equations are used to describe
deterioration in strength, unloading stiffness and reloading
stiffness:</p>
<dl>
<dt></dt>
<dd>

$$k_i = k_0(1 -\delta k_i)$$

</dd>
</dl>
<p>where $k_i$ is the unloading stiffness at time
$t_i$, $k_0$ is the
initial unloading stiffness (for the case of no damage), and
$\delta k_i$ (defined below) is the value of the
stiffness damage index at time $t_i$.</p>
<dl>
<dt></dt>
<dd>

$$d_{\text{max i}} = d_{\text{max 0}}(1 -\delta
d_i)$$

</dd>
</dl>

where $d_{\text{max i}}$ is the deformation
demand that defines the end of the reload cycle for increasing
deformation demand, $d_{\text{max 0}} $ is the
maximum historic deformation demand (which would be the deformation
demand defining the end of the reload cycle if degradation of reloading
stiffness is ignored), and $\delta d_i$ (defined
below) is the value of reloading stiffness damage index at time $t_i$.


$$f_{\text{max i}} = f_{\text{max 0}}(1 -\delta
f_i)$$


where $f_{\text{max i}}$ is the current envelope maximum strength at time $t_i$,
$f_{\text{max 0}} $ is the initial envelope maximum strength for the case of no 
damage, and $\delta f_i$ (defined below) is the value of strength value index at
time $t_i$.

The damage indices $\delta k_i$, $\delta d_i$, and $\delta f_i$, may be defined 
to be a function of displacement history only (`dmgType = "cycle"`) or displacement 
history and energy accumulation (`dmgType = "energy"`). For either case, all of the damage
indices are computed using the same basic equation.

If the damage indices are assumed to be a function of displacement
history and energy accumulation, the unloading stiffness damage index,
$\delta k_i$ is computed as follows:

$$\delta k_i = \left( \text{gK1} (d_{max})^\text{gK3} +
\text{gK2} \left (\frac{E_i}{E_\text{monotonic}} \right )^\text{gK3}
\right ) \le \text{gKLim}$$

where

$$(d_{max} = \text{max} \left[ \frac{d_\text{max
i}}{\text{def}_\text{max}}, \frac{d_\text{min i}}{\text{def}_\text{min}}
\right ]$$


## Examples

<p><a href="Pinching4MaterialExample" title="wikilink">Pinching4MaterialExample</a></p>

<hr />

<p>DESCRIPTION:</p>
<p>Stiffness and strength are assumed to deteriorate due to the imposed
"load" history. The same basic equations are used to describe
deterioration in strength, unloading stiffness and reloading
stiffness:</p>

<hr />

## References
<p><a
href="http://peer.berkeley.edu/publications/peer_reports/reports_2003/0310.pdf">PEER
2003/10</a></p>

<hr />
<p>Code developed by: <span style="color:blue"> Nilinjan Mitra,
University of Washington</span></p>

