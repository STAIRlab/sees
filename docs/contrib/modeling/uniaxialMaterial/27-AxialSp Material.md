 # AxialSp

<p>This command is used to construct a uniaxial AxialSp material object.
This material model produces axial stress-strain curve of elastomeric
bearings.</p>

```tcl
uniaxialMaterial AxialSp $matTag $sce $fty $fcy &lt;$bte $bty $bcy $fcr&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">sce</code></td>
<td><p>compressive modulus</p></td>
</tr>
<tr class="odd">
<td><p><strong>$fty $fcy</strong></p></td>
<td><p>yield stress under tension (<strong>$fty</strong>) and
compression (<strong>$fcy</strong>) (see note 1)</p></td>
</tr>
<tr class="even">
<td><p><strong>$bte $bty $bcy</strong></p></td>
<td><p>reduction rate for tensile elastic range (<strong>$bte</strong>),
tensile yielding (<strong>$bty</strong>) and compressive yielding
(<strong>$bcy</strong>) (see note 1)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fcr</code></td>
<td><p>target point stress (see note 1)</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<p>1) Input parameters are required to satisfy followings.</p>
<p><strong>$fcy</strong> &lt; 0.0 &lt; <strong>$fty</strong></p>
<p>0.0 &lt;= <strong>$bty</strong> &lt; <strong>$bte</strong> &lt;=
1.0</p>
<p>0.0 &lt;= <strong>$bcy</strong> &lt;= 1.0</p>
<p><strong>$fcy</strong> &lt;= <strong>$fcr</strong> &lt;= 0.0</p>
<p><img src="/OpenSeesRT/contrib/static/AxialSp_note1.png" title="AxialSp_note1.png" width="250"
alt="AxialSp_note1.png" />
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; <img
src="AxialSp_note2.png" title="AxialSp_note2.png" width="250"
alt="AxialSp_note2.png" /></p>
<hr />

## Examples

<p><a href="Media:AxialSp_sample.tcl"
title="wikilink">AxialSp_sample.tcl</a></p>
<figure>
<img src="/OpenSeesRT/contrib/static/AxialSp_StressStrain.png" title="AxialSp_StressStrain.png"
width="300" alt="AxialSp_StressStrain.png" />
<figcaption aria-hidden="true">AxialSp_StressStrain.png</figcaption>
</figure>
<hr />
<p>Code Developed by: <span style="color:blue"> mkiku
</span></p>
