# SmoothPSConcrete

<p>This command is used to construct a uniaxial smoothed Popovics-Saenz
concrete material object.</p>

```tcl
uniaxialMaterial SmoothPSConcrete $matTag $fc $fu $Ec
        $epso $epsu $eta
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique material object integer tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fc</code></td>
<td><p>concrete compressive strength (positive for compression)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fu</code></td>
<td><p>concrete crushing strength (positive for compression</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Ec</code></td>
<td><p>initial tangent stiffness</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epsco</code></td>
<td><p>concrete strain at maximum strength (positive for
compression)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">epsu</code></td>
<td><p>concrete strain at crushing strength (positive for
compression)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">eta</code></td>
<td><p>smoothing parameter (default value = 0.2).</p></td>
</tr>
</tbody>
</table>
<p>Note: For this material class, the sensitivity parameters can be: fc,
fu, Ec, epsco, epscu, eta</p>
<hr />
