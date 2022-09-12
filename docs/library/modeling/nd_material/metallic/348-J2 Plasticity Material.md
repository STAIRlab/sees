# J2 Plasticity Material

This command is used to construct an multi dimensional material
object that has a von Mises (J2) yield criterium and isotropic
hardening.

```tcl
nDMaterial J2Plasticity $matTag $K $G $sig0 $sigInf $delta $H
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">K</code></td>
<td><p>bulk modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">G</code></td>
<td><p>shear modulus</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">sig0</code></td>
<td><p>initial yield stress</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">sigInf</code></td>
<td><p>final saturation yield stress</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">delta</code></td>
<td><p>exponential hardening parameter</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">H</code></td>
<td><p>linear hardening parameter</p></td>
</tr>
</tbody>
</table>

The material formulations for the J2 object are `"ThreeDimensional"`,
`"PlaneStrain"`, `"Plane Stress"`, `"AxiSymmetric"` and `"PlateFiber"`.

<hr />

## Theory

<p>The theory for the non hardening case can be found <a
href="http://en.wikipedia.org/wiki/Von_Mises_yield_criterion"
title="wikilink">http://en.wikipedia.org/wiki/Von_Mises_yield_criterion</a></p>

$J_2$ isotropic hardening material

- Elastic Model
  $$\sigma = K \operatorname{tr}(\epsilon_e) + 2G \operatorname{dev}(\epsilon_e)$$

- Yield Function
  $$\phi(\sigma, q) = \| \operatorname{dev}(\sigma) \| - \sqrt{\tfrac{2}{3}} q(\xi)$$

- Saturation Isotropic Hardening with linear term</p>
  $$q(\xi) = \sigma_0 + (\sigma_\inf - \sigma_0) \exp(-delta \xi) + H \xi $$

- Flow Rules
  $$\dot {\epsilon_p} = \gamma \frac{\partial \phi}{\partial \sigma} $$
  
  $$\dot \xi = -\gamma \frac{\partial \phi}{\partial q}$$

- Linear Viscosity ( if $\phi \gt  0$ )

  $$\gamma = \frac{\phi}{\eta}$$ 



Backward Euler Integration Routine Yield condition enforced at time $n+1$

- set $\eta = 0$ for rate independent case

<hr />

<p>Code developed by: <span style="color:blue"> Ed Love</span></p>

