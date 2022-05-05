# ConcreteD

<p>This command is used to construct a concrete material based on the
Chinese design code.</p>

```tcl
uniaxialMaterial ConcreteD $matTag $fc $epsc $ft $epst
        $Ec $alphac $alphat &lt;$cesp&gt; &lt;$etap&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fc</code></td>
<td><p>concrete compressive strength *</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epsc</code></td>
<td><p>concrete strain at corresponding to compressive
strength*</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ft</code></td>
<td><p>concrete tensile strength *</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epst</code></td>
<td><p>concrete strain at corresponding to tensile strength*</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Ec</code></td>
<td><p>concrete initial Elastic modulus*</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">alphac</code></td>
<td><p>compressive descending parameter*</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alphat</code></td>
<td><p>tensile descending parameter*</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">cesp</code></td>
<td><p>plastic parameter, recommended values: 0.2~0.3*</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">etap</code></td>
<td><p>plastic parameter, recommended values: 1.0~1.3*</p></td>
</tr>
</tbody>
</table>
<hr />
<p><strong>NOTES</strong>:</p>
<ul>
<li>Concrete compressive strength and the corresponding strain should be
input as</li>
</ul>
<p>negative values.</p>
<ul>
<li>The value $fc/$epsc and $ft/$epst should be smaller than $Ec.</li>
<li>The default value for $cesp and $etap are 0.25 and 1.15,
respectively.</li>
</ul>
<hr />
<p><strong>EXAMPLE</strong>:</p>
<p>Example 1: Simulation of compressive test in Karson and Jirsa
(1969).</p>
<p>uniaxialMaterial ConcreteD 1 -27.6 -0.002 3 0.0001 35000 1.0 0.1 0.25
1.15</p>
<hr />
<p><strong>REFERENCES</strong>:</p>
<ul>
<li>Karsan, I. D., and Jirsa, J. O. (1969). “Behavior of concrete under
compressive loadings.” Journal of the Structural Division, 95(12),
2535-2563.</li>
<li>Ministry of Housing and Urban-Rural Development of the People’s
Republic of China. (2010). “Code for design of concrete structures.”
GB50010-2010, Beijing, China.</li>
<li>Ren, X. D. (2010). Multi-scale based stochastic damage constitutive
theory for concrete. Doctoral dissertation, Tongji University, Shanghai.
(in Chinese)</li>
<li>Wu, J. Y., Li, J., and Faria, R. (2006). “An energy release
rate-based plastic-damage model for concrete.” International Journal of
Solids and Structures, 43(3), 583-612.</li>
<li>Zeng, S. J. (2012). Dynamic Experimental Research and Stochastic
Damage Constitutive Model for Concrete. Doctoral dissertation, Tongji
University, Shanghai. (in Chinese)</li>
</ul>
<hr />
<p><strong>Code Developed By</strong>:</p>
<p>Zengyong Wan, Decheng Feng, Xiaodan Ren, Jie Li, College of Civil
Engineering, Tongji University,</p>
