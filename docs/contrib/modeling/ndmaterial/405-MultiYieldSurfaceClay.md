# MultiYieldSurfaceClay

<p>The ‘MultiYieldSurfaceClay’ is an elastic-plastic material in which
plasticity exhibits only in the deviatoric stress-strain response. The
volumetric stress-strain response is linear-elastic and is independent
of the deviatoric response. This material is implemented to simulate
monotonic or cyclic response of materials whose shear behavior is
pressure independent. Such materials include, for example, organic soils
or clay under fast (undrained) loading conditions.</p>
<p>This material is available for sensitivity computation in both 2-D
and 3-D models. It is another version of PressureIndependMultiYield
material. However there are three differences between this model and
PressureIndependMultiYield:</p>
<p>1. This model uses the consistent tangent modulus instead of the
continuum tangent modulus.</p>
<p>2. This model does not support the ‘updateMaterialStage’ command.</p>
<p>3. This model does not support further discretization of the strain
increment in each iteration.</p>

```tcl
nDmaterial MultiYieldSurfaceClay $matTag $nd $rho $G $K
        $cohesion $peakShearStrain
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique material object integer tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">nd</code></td>
<td><p>number of dimensions, 2 for 2-D analysis (plane-strain), and 3
for 3-D analysis</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>saturated soil mass density</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">G</code></td>
<td><p>reference low-strain shear modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">K</code></td>
<td><p>reference bulk modulus</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">cohesion</code></td>
<td><p>peak shear (apparent cohesion at zero effective
confinement)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">peakShearStrain</code></td>
<td><p>strain at peak shear, i.e., the octahedral shear strain at which
the maximum shear strength is reached</p></td>
</tr>
</tbody>
</table>
<p>Note: For this material class, the sensitivity parameters can be: G,
K, cohesion.</p>
<hr />
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
Reference:
</dd>
<dd>
Gu Q., Conte J.P., Elgamal A., Yang Z. (2009). “Finite element response
sensitivity analysis of multi-yield-surface J2 plasticity model by
direct differentiation method.” Computer Methods in Applied Mechanics
and Engineering, 198(30-32):2272-2285.
</dd>
</dl>
</dd>
</dl>
