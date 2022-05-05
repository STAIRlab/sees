# Elastic Uniaxial Material

<p>This command is used to construct an elastic uniaxial material
object.</p>

```tcl
uniaxialMaterial Elastic $matTag $E &lt;$eta&gt;
        &lt;$Eneg&gt;
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
<td><code class="parameter-table-variable">eta</code></td>
<td><p>damping tangent (optional, default=0.0)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Eneg</code></td>
<td><p>tangent in compression (optional, default=E)</p></td>
</tr>
</tbody>
</table>
<p><img src="Elastic.gif" title="Elastic.gif" alt="Elastic.gif" /> <img
src="ElasticPosNeg.png" title="ElasticPosNeg.png"
alt="ElasticPosNeg.png" /></p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
