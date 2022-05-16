# Concrete01

<p>This command is used to construct a uniaxial Kent-Scott-Park concrete
material object with degraded linear unloading/reloading stiffness
according to the work of Karsan-Jirsa and no tensile strength (refer to
<a href="http://peer.berkeley.edu">http://peer.berkeley.edu</a>).</p>

```tcl
uniaxialMaterial Concrete01 $matTag $fc $epsco $fcu $epscu
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
<td><p>concrete compressive strength (with positive value)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epsco</code></td>
<td><p>concrete strain at maximum strength (with positive
value)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fcu</code></td>
<td><p>concrete crushing strength (with positive value)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epscu</code></td>
<td><p>concrete strain at crushing strength (with positive
value)</p></td>
</tr>
</tbody>
</table>
<p>Note: For this material class, the sensitivity parameters can be: fc,
epsco, fcu, epscu</p>
<hr />
