 # Hardening

<p>This command is used to construct a uniaxial material object with
combined linear kinematic and isotropic hardening. The model includes
optional visco-plasticity using a Perzyna formulation.</p>

```tcl
uniaxialMaterial Hardening $matTag $E $sigmaY $H_iso
        $H_kin &lt;$eta&gt;
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
<td><p>tangent stiffness</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">sigmaY</code></td>
<td><p>yield stress or force</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">H_iso</code></td>
<td><p>isotropic hardening Modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">H_kin</code></td>
<td><p>kinematic hardening Modulus</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">eta</code></td>
<td><p>visco-plastic coefficient (optional, default=0.0)</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/HardeningMaterial.gif" title="HardeningMaterial.gif"
alt="HardeningMaterial.gif" />
<figcaption aria-hidden="true">HardeningMaterial.gif</figcaption>
</figure>
<hr />
<p>Code Developed by: <span style="color:blue"> Micheal H. Scott,
Oregon State University </span></p>
<p>Image Developed by: <span style="color:blue"> Silvia Mazzoni
</span></p>
