# Elastic Orthotropic Material

This command is used to construct an ElasticOrthotropic material
object.

```tcl
nDMaterial ElasticOrthotropic $matTag $Ex $Ey $Ez $vxy
        $vyz $vzx $Gxy $Gyz $Gzx < $rho >
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><code>Ex, Ey, Ez</code></p></td>
<td><p>elastic modulii in three mutually perpendicular directions ($x$, $y$,
and $z$)</p></td>
</tr>
<tr class="odd">
<td><p><code>vxy, vyz, vzx</code></p></td>
<td><p>Poisson's ratios</p></td>
</tr>
<tr class="even">
<td><p><code>Gxy, Gyz, Gzx</code></p></td>
<td><p>shear modulii</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>mass density, optional default = 0.0.</p></td>
</tr>
</tbody>
</table>

The material formulations for the ElasticOrthotropic object are
- `ThreeDimensional`, 
- `PlaneStrain`, 
- `Plane Stress`, 
- `AxiSymmetric`,
- `BeamFiber`, and 
- `PlateFiber`.

<hr />
<p>Code Developed by: <span style="color:blue"> Micheal Scott,
Oregon State University </span></p>

