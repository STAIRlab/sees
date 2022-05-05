# MinMax Material

<p>This command is used to construct a MinMax material object. This
stress-strain behaviour for this material is provided by another
material. If however the strain ever falls below or above certain
threshold values, the other material is assumed to have failed. From
that point on, values of 0.0 are returned for the tangent and
stress.</p>

```tcl
uniaxialMaterial MinMax $matTag $otherTag &lt;-min
        $minStrain&gt; &lt;-max $maxStrain&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><strong>$otherTag</strong></p></td>
<td><p>tag of the other material</p></td>
</tr>
<tr class="odd">
<td><p><strong>$minStrain</strong></p></td>
<td><p>minimum value of strain. optional default = -1.0e16.</p></td>
</tr>
<tr class="even">
<td><p><strong>$maxStrain</strong></p></td>
<td><p>max value of strain. optional default = 1.0e16.</p></td>
</tr>
</tbody>
</table>
<hr />
<p>Code Developed by: <span style="color:blue"> Micheal Scott,
Oregon State. </span></p>
