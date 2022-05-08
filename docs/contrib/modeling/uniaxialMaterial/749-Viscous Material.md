# Viscous

<p>This command is used to construct a uniaxial viscous material object.
stress =C(strain-rate)^alpha</p>

```tcl
uniaxialMaterial Viscous $matTag $C
        $alpha
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">C</code></td>
<td><p>damping coeficient</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>power factor (=1 means linear damping)</p></td>
</tr>
</tbody>
</table>
<hr />
<p>NOTES:</p>
<p>1. This material can only be assigned to truss and zeroLength
elements.</p>
<p>2. This material can not be combined in parallel/series with other
materials. When defined in parallel with other materials it is
ignored.</p>
<p>REFERENCES:</p>
<p>See Eqn 9 in G. Pekcan, J.B.Mander abd S.S. Chen, "Fundamental
Considerations for the Design of Non-Linear Viscous Dampers", Earthqauke
Engineering &amp; Structural Dynamics 28,1405-1425 (1999)</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Mehrdad Sasani,
NEU </span></p>
