# Elastic-Perfectly Plastic Gap

<p>This command is used to construct an elastic perfectly-plastic gap
uniaxial material object.</p>

```tcl
uniaxialMaterial ElasticPPGap $matTag $E $Fy $gap
        < $eta > < damage >
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">E</code></td>
<td><p>tangent</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Fy</code></td>
<td><p>stress or force at which material reaches plastic state</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">gap</code></td>
<td><p>initial gap (strain or deformation)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">eta</code></td>
<td><p>hardening ratio (=Eh/E), which can be negative</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">damage</code></td>
<td><p>an optional string to specify whether to accumulate damage or not
in the material. With the default string, "noDamage" the gap material
will re-center on load reversal. If the string "damage" is provided this
recentering will not occur and gap will grow.</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/ElasticPPGap.gif" title="ElasticPPGap.gif"
alt="ElasticPPGap.gif" />
<figcaption aria-hidden="true">ElasticPPGap.gif</figcaption>
</figure>

## Examples

<figure>
<embed src="_ElasticPPGap.tcl" title="_ElasticPPGap.tcl" />
<figcaption aria-hidden="true">_ElasticPPGap.tcl</figcaption>
</figure>
<p>&lt;tcl&gt;ElasticPPGap.tcl&lt;/tcl&gt;</p>
<p><img src="/OpenSeesRT/contrib/static/ElasticPPGapPlotA.png" title="ElasticPPGapPlotA.png"
alt="ElasticPPGapPlotA.png" /> <img src="/OpenSeesRT/contrib/static/ElasticPPGapPlotB.png"
title="ElasticPPGapPlotB.png" alt="ElasticPPGapPlotB.png" /></p>
<hr />
<p>Code Developed by: <span style="color:blue"> Kevin Mackie,
University of Central Florida</span></p>
