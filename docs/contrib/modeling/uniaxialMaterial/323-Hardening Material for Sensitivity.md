# Hardening Material for Sensitivity

<p>This command is used to construct a uniaxial material object with
combined linear kinematic and isotropic hardening.</p>

```tcl
uniaxialMaterial Hardening $matTag $E $sigmaY $Hiso
        $Hkin
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
<td><p>yield stress (or force)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Hiso</code></td>
<td><p>isotropic hardening Modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Hkin</code></td>
<td><p>kinematic hardening Modulus</p></td>
</tr>
</tbody>
</table>
<p>Note: For this material class, the sensitivity parameters can be: E,
sigmaY, Hkin, Hiso</p>
<hr />
