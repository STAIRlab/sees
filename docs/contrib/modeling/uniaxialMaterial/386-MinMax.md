# MinMax

<p>This command is used to construct a MinMax material object. This
stress-strain behaviour for this material is provided by another
material. If however the strain ever falls below or above certain
threshold values, the other material is assumed to have failed. From
that point on, values of 0.0 are returned for the tangent and
stress.</p>

```tcl
uniaxialMaterial MinMax $matTag $otherTag < -min $minStrain > 
        < -max $maxStrain >
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
<td><code class="parameter-table-variable">minStrain</code></td>
<td><p>minimum value of strain. optional default = -1.0e16.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">maxStrain</code></td>
<td><p>max value of strain. optional default = 1.0e16.</p></td>
</tr>
</tbody>
</table>
<hr />
<p>Code Developed by: <span style="color:blue"> Micheal Scott,
Oregon State. </span></p>
