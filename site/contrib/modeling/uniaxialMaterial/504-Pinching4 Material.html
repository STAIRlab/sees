# Pinching4 Material

<p>This command is used to construct a uniaxial material that represents
a 'pinched' load-deformation response and exhibits degradation under
cyclic loading. Cyclic degradation of strength and stiffness occurs in
three ways: unloading stiffness degradation, reloading stiffness
degradation, strength degradation.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>uniaxialMaterial Pinching4 $matTag $ePf1 $ePd1 $ePf2
$ePd2 $ePf3 $ePd3 $ePf4 $ePd4 &lt;$eNf1 $eNd1 $eNf2 $eNd2 $eNf3 $eNd3
$eNf4 $eNd4&gt; $rDispP $rForceP $uForceP &lt;$rDispN $rForceN $uForceN
&gt; $gK1 $gK2 $gK3 $gK4 $gKLim $gD1 $gD2 $gD3 $gD4 $gDLim $gF1 $gF2
$gF3 $gF4 $gFLim $gE $dmgType</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><strong>$ePf1 $ePf2 $ePf3 $ePf4</strong></p></td>
<td><p>floating point values defining force points on the positive
response envelope</p></td>
</tr>
<tr class="odd">
<td><p><strong>$ePd1 $ePd2 $ePd3 $ePd4</strong></p></td>
<td><p>floating point values defining deformation points on the positive
response envelope</p></td>
</tr>
<tr class="even">
<td><p><strong>$eNf1 $eNf2 $eNf3 $eNf4</strong></p></td>
<td><p>floating point values defining force points on the negative
response envelope</p></td>
</tr>
<tr class="odd">
<td><p><strong>$eNd1 $eNd2 $eNd3 $eNd4</strong></p></td>
<td><p>floating point values defining deformation points on the negative
response envelope</p></td>
</tr>
<tr class="even">
<td><p><strong>$rDispP</strong></p></td>
<td><p>floating point value defining the ratio of the deformation at
which reloading occurs to the maximum historic deformation
demand</p></td>
</tr>
<tr class="odd">
<td><p><strong>$fFoceP</strong></p></td>
<td><p>floating point value defining the ratio of the force at which
reloading begins to force corresponding to the maximum historic
deformation demand</p></td>
</tr>
<tr class="even">
<td><p><strong>$uForceP</strong></p></td>
<td><p>floating point value defining the ratio of strength developed
upon unloading from negative load to the maximum strength developed
under monotonic loading</p></td>
</tr>
<tr class="odd">
<td><p><strong>$rDispN</strong></p></td>
<td><p>floating point value defining the ratio of the deformation at
which reloading occurs to the minimum historic deformation
demand</p></td>
</tr>
<tr class="even">
<td><p><strong>$fFoceN</strong></p></td>
<td><p>floating point value defining the ratio of the force at which
reloading begins to force corresponding to the minimum historic
deformation demand</p></td>
</tr>
<tr class="odd">
<td><p><strong>$uForceN</strong></p></td>
<td><p>floating point value defining the ratio of strength developed
upon unloading from negative load to the minimum strength developed
under monotonic loading</p></td>
</tr>
<tr class="even">
<td><p><strong>$gK1 $gK2 $gK3 $gK4 $gKLim</strong></p></td>
<td><p>floating point values controlling cyclic degradation model for
unloading stiffness degradation</p></td>
</tr>
<tr class="odd">
<td><p><strong>$gD1 $gD2 $gD3 $gD4 $gDLim</strong></p></td>
<td><p>floating point values controlling cyclic degradation model for
reloading stiffness degradation</p></td>
</tr>
<tr class="even">
<td><p><strong>$gF1 $gF2 $gF3 $gF4 $gFLim</strong></p></td>
<td><p>floating point values controlling cyclic degradation model for
strength degradation</p></td>
</tr>
<tr class="odd">
<td><p><strong>$gE</strong></p></td>
<td><p>floating point value used to define maximum energy dissipation
under cyclic loading. Total energy dissipation capacity is defined as
this factor multiplied by the energy dissipated under monotonic
loading.</p></td>
</tr>
<tr class="even">
<td><p><strong>$dmgType</strong></p></td>
<td><p>string to indicate type of damage (option: "cycle",
"energy")</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<figure>
<img src="Piinching4.jpg" title="Piinching4.jpg" alt="Piinching4.jpg" />
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
&lt;math&gt;t_i&lt;/math&gt;, $k_0$ is the
initial unloading stiffness (for the case of no damage), and
&lt;math&gt;\delta k_i&lt;/math&gt;(defined below) is the value of the
stiffness damage index at time $t_i$.</p>
<dl>
<dt></dt>
<dd>

$$d_{\text{max i}} = d_{\text{max 0}}(1 -\delta
d_i)$$

</dd>
</dl>
<p>where $d_{\text{max i}}$ is the deformation
demand that defines the end of the reload cycle for increasing
deformation demand, $d_{\text{max 0}} $ is the
maximum historic deformation demand (which would be the deformation
demand defining the end of the reload cycle if degradation of reloading
stiffness is ignored), and $\delta d_i$ (defined
below) is the value of reloading stiffness damage index at time
&lt;math&gt;t_i&lt;/math&gt;.</p>
<dl>
<dt></dt>
<dd>

$$f_{\text{max i}} = f_{\text{max 0}}(1 -\delta
f_i)$$

</dd>
</dl>
<p>where $f_{\text{max i}}$ is the current
envelope maximum strength at time $t_i$,
$f_{\text{max 0}} $ is the initial envelope
maximum strength for the case of no damage, and &lt;math&gt;\delta
f_i&lt;/math&gt; (defined below) is the value of strength value index at
time $t_i$.</p>
<p>The damage indices $\delta k_i$,
&lt;math&gt;\delta d_i&lt;/math&gt;, and &lt;math&gt;\delta
f_i&lt;/math&gt;, may be defined to be a function of displacement
history only ($dmgType = "cycle") or displacement history and energy
accumulation ($dmgType = "energy"). For either case, all of the damage
indices are computed using the same basic equation.</p>
<p>If the damage indices are assumed to be a function of displacement
history and energy accumulation, the unloading stiffness damage index,
$\delta k_i$ is computed as follows:</p>
<dl>
<dt></dt>
<dd>

$$\delta k_i = \left( \text{gK1} (d_{max})^\text{gK3} +
\text{gK2} \left (\frac{E_i}{E_\text{monotonic}} \right )^\text{gK3}
\right ) &lt;= \text{gKLim}$$

</dd>
</dl>
<p>where</p>
<dl>
<dt></dt>
<dd>

$$(d_{max} = \text{max} \left[ \frac{d_\text{max
i}}{\text{def}_\text{max}}, \frac{d_\text{min i}}{\text{def}_\text{min}}
\right ]$$

</dd>
</dl>
<hr />
<p>EXAMPLE:</p>
<p><a href="Pinching4MaterialExample"
title="wikilink">Pinching4MaterialExample</a></p>
<hr />
<p>DESCRIPTION:</p>
<p>Stiffness and strength are assumed to deteriorate due to the imposed
"load" history. The same basic equations are used to describe
deterioration in strength, unloading stiffness and reloading
stiffness:</p>
<hr />
<p>REFERENCES:</p>
<p><a
href="http://peer.berkeley.edu/publications/peer_reports/reports_2003/0310.pdf">PEER
2003/10</a></p>
<hr />
<p>Code Developed by: <span style="color:blue"> Nilinjan Mitra,
University of Washington</span></p>
