# Elastic Isotropic Material

This command is used to construct an ElasticIsotropic material
object.

```tcl
nDMaterial ElasticIsotropic $matTag $E $v < $rho >
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">E</code></td>
<td><p>elastic Modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">v</code></td>
<td><p>Poisson's ratio</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>mass density, optional default = 0.0.</p></td>
</tr>
</tbody>
</table>
<p>The material formulations for the ElasticIsotropic object are
`"ThreeDimensional"`, `"PlaneStrain"`, "Plane Stress," "AxiSymmetric," and
"PlateFiber."</p>

<hr />
<p>Code Developed by: <span style="color:blue"> Micheal Scott, Oregon State University </span></p>

