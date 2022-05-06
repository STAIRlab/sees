 # AxialSpHD

<p>This command is used to construct a uniaxial AxialSpHD material
object. This material model produces axial stress-strain curve of
elastomeric bearings including hardening behavior.</p>

```tcl
uniaxialMaterial AxialSpHD $matTag $sce $fty $fcy
        &lt;$bte $bty $bth $bcy $fcr $ath&gt;
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
<td><p><strong>$bte $bty $bth $bcy</strong></p></td>
<td><p>reduction rate for tensile elastic range (<strong>$bte</strong>),
tensile yielding (<strong>$bty</strong>), tensile hardening
(<strong>$bth</strong>) and compressive yielding (<strong>$bcy</strong>)
(see note 1)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fcr</code></td>
<td><p>target point stress (see note 1)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ath</code></td>
<td><p>hardening strain ratio to yield strain (see note 1)</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<p>1) Input parameters are required to satisfy followings.</p>
<p><strong>$fcy</strong> &lt; 0.0 &lt; <strong>$fty</strong></p>
<p>0.0 &lt;= <strong>$bty</strong> &lt; <strong>$bth</strong> &lt;
<strong>$bte</strong> &lt;= 1.0</p>
<p>0.0 &lt;= <strong>$bcy</strong> &lt;= 1.0</p>
<p><strong>$fcy</strong> &lt;= <strong>$fcr</strong> &lt;= 0.0</p>
<p>1.0 &lt;= <strong>$ath</strong></p>
<p><img src="/OpenSeesRT/contrib/static/AxialSpHD_note1.png" title="AxialSpHD_note1.png"
width="250" alt="AxialSpHD_note1.png" />
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; <img
src="AxialSpHD_note2.png" title="AxialSpHD_note2.png" width="250"
alt="AxialSpHD_note2.png" /></p>
<hr />

## Examples

<p><a href="Media:AxialSpHD_sample.tcl"
title="wikilink">AxialSpHD_sample.tcl</a></p>
<figure>
<img src="/OpenSeesRT/contrib/static/AxialSpHD_StressStrain.png" title="AxialSpHD_StressStrain.png"
width="300" alt="AxialSpHD_StressStrain.png" />
<figcaption aria-hidden="true">AxialSpHD_StressStrain.png</figcaption>
</figure>
<hr />
<p>Code Developed by: <span style="color:blue"> mkiku
</span></p>
