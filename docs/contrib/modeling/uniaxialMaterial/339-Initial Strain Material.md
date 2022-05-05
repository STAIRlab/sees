# Initial Strain Material

<p>This command is used to construct an Initial Strain material object.
The stress-strain behaviour for this material is defined by another
material. Initial Strain Material enables definition of initial strains
for the material under consideration. The stress that corresponds to the
initial strain will be calculated from the other material.</p>

```tcl
uniaxialMaterial InitStrainMaterial $matTag $otherTag
        $initStrain
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">otherTag</code></td>
<td><p>tag of the other material</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">initStrain</code></td>
<td><p>initial strain</p></td>
</tr>
</tbody>
</table>
