# Steel01 Material for Sensitivity

<p>This command is used to construct a uniaxial bilinear steel material
object with kinematic hardening and optional isotropic hardening
described by a non-linear evolution equation (refer to <a
href="http://peer.berkeley.edu">http://peer.berkeley.edu</a>).</p>

```tcl
uniaxialMaterial Steel01 $matTag $sigmaY $E $b &lt;$a1
        $a2 $a3 $a4&gt;
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
<td><p>initial tangent stiffness</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">sigmaY</code></td>
<td><p>yield strength</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">b</code></td>
<td><p>strain-hardening ratio (ratio between post-yield tangent and
initial elastic tangent stiffness)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">a1 a2 a3 a4</code></p></td>
<td><p>isotropic hardening parameters: (optional, default: no isotropic
hardening)</p></td>
</tr>
</tbody>
</table>
<p>Note: For this material class, the sensitivity parameters can be: E,
sigmaY, b, a1, a2, a3, a4</p>
<hr />
