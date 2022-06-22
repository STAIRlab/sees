---
description: Concrete01 Material With Stuff in the Cracks
...

# Concrete01WithSITC

<p>This command is used to construct a modified uniaxial Kent-Scott-Park
concrete material object with degraded linear unloading/reloading
stiffness according to the work of Karsan-Jirsa and no tensile strength.
The modification is to model the effect of Stuff In The Cracks (SITC).
The command is as follows:</p>

```tcl
uniaxialMaterial Concrete01WithSITC $matTag $fpc $epsc0
        $fpcu $epsU < $endStrainSITC >
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fpc</code></td>
<td><p>concrete compressive strength at 28 days (compression is
negative)*</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epsc0</code></td>
<td><p>concrete strain at maximum strength*</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fpcu</code></td>
<td><p>concrete crushing strength *</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epsU</code></td>
<td><p>concrete strain at crushing strength*</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">endStrainSITC</code></td>
<td><p>optional, default = 0.03</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<ul>
<li>Compressive concrete parameters should be input as negative
values.</li>
</ul>
<ul>
<li>The initial slope for this model is (2*$fpc/$epsc0)</li>
</ul>
<hr />
## References
<p>J.F. Stanton and H.D. McNiven, "The Development of a Mathematical
Model to Predict the Flexural Response of Reinforced Concrete Beams to
Cyclic Loads, Using System Identification", EERC Report Number 79/02,
January 1979.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Won Lee, Stanford
</span></p>
