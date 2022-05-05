# Concrete01 Material -- Zero Tensile Strength

<p>This command is used to construct a uniaxial Kent-Scott-Park concrete
material object with degraded linear unloading/reloading stiffness
according to the work of Karsan-Jirsa and no tensile strength. (REF:
Fedeas).</p>

```tcl
uniaxialMaterial Concrete01 $matTag $fpc $epsc0 $fpcu
        $epsU
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
</tbody>
</table>
<p>NOTE:</p>
<ul>
<li>Compressive concrete parameters should be input as negative values
(if input as positive, they will be converted to negative
internally).</li>
</ul>
<ul>
<li>The initial slope for this model is (2*$fpc/$epsc0)</li>
</ul>
<figure>
<img src="Concrete01.gif" title="Concrete01.gif" alt="Concrete01.gif" />
<figcaption aria-hidden="true">Concrete01.gif</figcaption>
</figure>
<p>Typical Hysteretic Stress-Strain Relation for material</p>
<p>EXAMPLE:</p>
<p>uniaxialMaterial Concrete01 1 -4.0 -0.002 0.0 -0.005; # the concrete
material with tag 1 reaches compressive strength of 4.0 at strain of
0.002 and reaches ultimate strength of 0.0 at strain of 0.005.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Concrete01Hysteretic.jpg" title="Concrete01Hysteretic.jpg"
alt="Concrete01Hysteretic.jpg" />
<figcaption aria-hidden="true">Concrete01Hysteretic.jpg</figcaption>
</figure>
<hr />
<p>Code Developed by: <span style="color:blue"> Filip Filippou, UC
Berkeley </span></p>
<p>Images Developed by: <span style="color:blue"> Silvia Mazzoni
</span></p>
