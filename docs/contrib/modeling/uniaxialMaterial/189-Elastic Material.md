 # Elastic

<p>This command is used to construct a linear elastic uniaxial material
object (with optional material damping)</p>

```tcl
uniaxialMaterial Elastic $matTag $E
        &lt;$eta&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique material object integer tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">E</code></td>
<td><p>elastic stiffness</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">eta</code></td>
<td><p>damping stiffness (optional, default=0.0)</p></td>
</tr>
</tbody>
</table>
<p>Note: For this material class, the sensitivity parameters can be: E,
eta</p>
<hr />
