# Elastic Material

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
<td><p><strong>$matTag</strong></p></td>
<td><p>unique material object integer tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$E</strong></p></td>
<td><p>elastic stiffness</p></td>
</tr>
<tr class="odd">
<td><p><strong>$eta</strong></p></td>
<td><p>damping stiffness (optional, default=0.0)</p></td>
</tr>
</tbody>
</table>
<p>Note: For this material class, the sensitivity parameters can be: E,
eta</p>
<hr />
