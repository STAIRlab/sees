# Elastic Orthotropic Material

<p>This command is used to construct an ElasticOrthotropic material
object.</p>

```tcl
nDMaterial ElasticOrthotropic $matTag $Ex $Ey $Ez $vxy
        $vyz $vzx $Gxy $Gyz $Gzx &lt;$rho&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><strong>$Ex, $Ey, $Ez</strong></p></td>
<td><p>elastic modulii in three mutually perpendicular directions (x, y,
and z)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$vxy, $vyz, $vzx</strong></p></td>
<td><p>Poisson's ratios</p></td>
</tr>
<tr class="even">
<td><p><strong>$Gxy, $Gyz, $Gzx</strong></p></td>
<td><p>shear modulii</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>mass density, optional default = 0.0.</p></td>
</tr>
</tbody>
</table>
<p>The material formulations for the ElasticOrthotropic object are
"ThreeDimensional", "PlaneStrain", "Plane Stress", "AxiSymmetric",
"BeamFiber", and "PlateFiber".</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Micheal Scott,
Oregon State University </span></p>
