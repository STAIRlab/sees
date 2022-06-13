---
description: Engineered Cementitious Composites Material
...
# ECC01

<p>This command is used to construct a uniaxial Engineered Cementitious
Composites (ECC)material object based on the ECC material model of Han,
et al. (see references). Reloading in tension and compression is
linear.</p>

```tcl
uniaxialMaterial ECC01 $matTag $sigt0 $epst0 $sigt1
        $epst1 $epst2 $sigc0 $epsc0 $epsc1 $alphaT1 $alphaT2 $alphaC $alphaCU
        $betaT $betaC
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">sigt0</code></td>
<td><p>tensile cracking stress</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epst0</code></td>
<td><p>strain at tensile cracking stress</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">sigt1</code></p></td>
<td><p>peak tensile stress</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">epst1</code></p></td>
<td><p>strain at peak tensile stress</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">sigt2</code></p></td>
<td><p>ultimate tensile strain</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">sigc0</code></td>
<td><p>compressive strength (see NOTES)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">epsc0</code></td>
<td><p>strain at compressive strength (see NOTES)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">epsc1</code></p></td>
<td><p>ultimate compressive strain (see NOTES)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">alphaT1</code></p></td>
<td><p>exponent of the unloading curve in tensile strain hardening
region</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">alphaT2</code></p></td>
<td><p>exponent of the unloading curve in tensile softening
region</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alphaC</code></td>
<td><p>exponent of the unloading curve in the compressive
softening</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">alphaCU</code></td>
<td><p>exponent of the compressive softening curve (use 1 for linear
softening)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">betaT</code></td>
<td><p>parameter to determine permanent strain in tension</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">betaC</code></td>
<td><p>parameter to determine permanent strain in compression</p></td>
</tr>
</tbody>
</table>
<p>NOTES</p>
<p>Compressive ECC parameters should be input as negative values.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/ECC01.gif" title="ECC01.gif" alt="ECC01.gif" />
<figcaption aria-hidden="true">ECC01.gif</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/eccTensile.gif" title="eccTensile.gif" alt="eccTensile.gif" />
<figcaption aria-hidden="true">eccTensile.gif</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/eccCompression.gif" title="eccCompression.gif"
alt="eccCompression.gif" />
<figcaption aria-hidden="true">eccCompression.gif</figcaption>
</figure>
<hr />
## References
<ol>
<li>Han TS, Feenstra PH, Billington SL, "Simulation of Highly Ductile
Fiber-Reinforced Cement-Based Composite Components Under Cyclic
Loading," ACI Structural Journal, V. 100, No. 6, pp. 749-757.</li>
</ol>
<hr />
<p>Code Developed by: <span style="color:blue">Won Lee,
Stanford</span> and <span style="color:blue">Sara
Billington, Stanford</span></p>
