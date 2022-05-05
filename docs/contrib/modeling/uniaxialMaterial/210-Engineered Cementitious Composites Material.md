# Engineered Cementitious Composites Material

<p>This command is used to construct a uniaxial Engineered Cementitious
Composites (ECC)material object based on the ECC material model of Han,
et al. (see references). Reloading in tension and compression is
linear.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>uniaxialMaterial ECC01 $matTag $sigt0 $epst0 $sigt1
$epst1 $epst2 $sigc0 $epsc0 $epsc1 $alphaT1 $alphaT2 $alphaC $alphaCU
$betaT $betaC</strong></p></td>
</tr>
</tbody>
</table>
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
<td><p><strong>$sigt1</strong></p></td>
<td><p>peak tensile stress</p></td>
</tr>
<tr class="odd">
<td><p><strong>$epst1</strong></p></td>
<td><p>strain at peak tensile stress</p></td>
</tr>
<tr class="even">
<td><p><strong>$sigt2</strong></p></td>
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
<td><p><strong>$epsc1</strong></p></td>
<td><p>ultimate compressive strain (see NOTES)</p></td>
</tr>
<tr class="even">
<td><p><strong>$alphaT1</strong></p></td>
<td><p>exponent of the unloading curve in tensile strain hardening
region</p></td>
</tr>
<tr class="odd">
<td><p><strong>$alphaT2</strong></p></td>
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
<img src="ECC01.gif" title="ECC01.gif" alt="ECC01.gif" />
<figcaption aria-hidden="true">ECC01.gif</figcaption>
</figure>
<figure>
<img src="eccTensile.gif" title="eccTensile.gif" alt="eccTensile.gif" />
<figcaption aria-hidden="true">eccTensile.gif</figcaption>
</figure>
<figure>
<img src="eccCompression.gif" title="eccCompression.gif"
alt="eccCompression.gif" />
<figcaption aria-hidden="true">eccCompression.gif</figcaption>
</figure>
<hr />
<p>REFERENCES:</p>
<ol>
<li>Han TS, Feenstra PH, Billington SL, "Simulation of Highly Ductile
Fiber-Reinforced Cement-Based Composite Components Under Cyclic
Loading," ACI Structural Journal, V. 100, No. 6, pp. 749-757.</li>
</ol>
<hr />
<p>Code Developed by: <span style="color:blue">Won Lee,
Stanford</span> and <span style="color:blue">Sara
Billington, Stanford</span></p>
