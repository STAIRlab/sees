---
title: Concrete02
description: Hognestad curve with linear tension softening
...

# Concrete02

::: {apidoc="opensees.uniaxial.Concrete02"}
```tcl
uniaxialMaterial Concrete02 $matTag $fpc $epsc0 $fpcu $epsU 
        $lambda $ft $Ets
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
<td><code class="parameter-table-variable">lambda</code></td>
<td><p>ratio between unloading slope at $epscu and initial
slope</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ft</code></td>
<td><p>tensile strength</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Ets</code></td>
<td><p>tension softening stiffness (absolute value) (slope of the linear
tension softening branch)</p></td>
</tr>
</tbody>
</table>
:::

<p>NOTE:</p>
<ul>
<li>Compressive concrete parameters should be input as negative
values.</li>
</ul>
<ul>
<li>The initial slope for this model is (2*$fpc/$epsc0)</li>
</ul>
<p>REFERENCE:</p>
<p>Mohd Hisham Mohd Yassin, "Nonlinear Analysis of Prestressed Concrete
Structures under Monotonic and Cycling Loads", PhD dissertation,
University of California, Berkeley, 1994.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Concrete02.jpg" title="Concrete02.jpg" alt="Concrete02.jpg" />
<figcaption aria-hidden="true">Concrete02.jpg</figcaption>
</figure>
<p>Comparison of Hysteretic Stress-Strain Relation for Concerete01
versus Concrete02 materials.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Concrete02Hysteretic.jpg" title="Concrete02Hysteretic.jpg"
alt="Concrete02Hysteretic.jpg" />
<figcaption aria-hidden="true">Concrete02Hysteretic.jpg</figcaption>
</figure>
<hr />
<p>Code Developed by: <span style="color:blue"> Filip Filippou, UC
Berkeley </span></p>
<p>Images Developed by: <span style="color:blue"> Silvia Mazzoni
</span></p>
