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
<td><p><strong>$matTag</strong></p></td>
<td><p>unique material object integer tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$E</strong></p></td>
<td><p>initial tangent stiffness</p></td>
</tr>
<tr class="odd">
<td><p><strong>$sigmaY</strong></p></td>
<td><p>yield stress (or force)</p></td>
</tr>
<tr class="even">
<td><p><strong>$Hiso</strong></p></td>
<td><p>isotropic hardening Modulus</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Hkin</strong></p></td>
<td><p>kinematic hardening Modulus</p></td>
</tr>
</tbody>
</table>
<p>Note: For this material class, the sensitivity parameters can be: E,
sigmaY, Hkin, Hiso</p>
<hr />
