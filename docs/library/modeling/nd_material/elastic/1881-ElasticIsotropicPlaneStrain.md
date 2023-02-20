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

The material formulations for the `ElasticIsotropic` model are
`"ThreeDimensional"`, `"PlaneStrain"`, `"Plane Stress"`, `"AxiSymmetric"`, and
`"PlateFiber"`.

In plane strain, an isotropic material is governed by the following constitutive relation:

$$
\left[\begin{array}{l}
\sigma_{11} \\
\sigma_{22} \\
\sigma_{12}
\end{array}\right]=\frac{E}{\left(1-\nu^2\right)}\left[\begin{array}{ccc}
1 & \nu & 0 \\
\nu & 1 & 0 \\
0 & 0 & (1-\nu) / 2
\end{array}\right]\left[\begin{array}{c}
\varepsilon_{11} \\
\varepsilon_{22} \\
2 \varepsilon_{12}
\end{array}\right]
$$

<hr />
<p>Code Developed by: <span style="color:blue"> Micheal Scott, Oregon State University </span></p>

