# J2 Plasticity Material

<p>This command is used to construct an multi dimensional material
object that has a von Mises (J2) yield criterium and isotropic
hardening.</p>

```tcl
nDMaterial J2Plasticity $matTag $K $G $sig0 $sigInf
        $delta $H
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
<p>The material formulations for the J2 object are "ThreeDimensional,"
"PlaneStrain," "Plane Stress," "AxiSymmetric," and "PlateFiber."</p>
<hr />

## Theory

<p>The theory for the non hardening case can be found <a
href="http://en.wikipedia.org/wiki/Von_Mises_yield_criterion"
title="wikilink">http://en.wikipedia.org/wiki/Von_Mises_yield_criterion</a></p>
<p>J2 isotropic hardening material class</p>
<p>Elastic Model</p>
<p>&lt;math&gt; \sigma = K*trace(\epsilon_e) +
(2*G)*dev(\epsilon_e)&lt;/math&gt;</p>
<p>Yield Function</p>
<p>&lt;math&gt; \phi(\sigma,q) = || dev(\sigma) || -
\sqrt(\tfrac{2}{3}*q(xi)&lt;/math&gt;</p>
<p>Saturation Isotropic Hardening with linear term</p>
<p>&lt;math&gt; q(xi) = \sigma_0 + (\sigma_\inf -
\sigma_0)*exp(-delta*\xi) + H*\xi &lt;/math&gt;</p>
<p>Flow Rules</p>
<p>&lt;math&gt; \dot {\epsilon_p} = \gamma * \frac{\partial
\phi}{\partial \sigma} &lt;/math&gt;</p>
<p>&lt;math&gt; \dot \xi = -\gamma * \frac{\partial \phi}{\partial q}
&lt;/math&gt;</p>
<p>Linear Viscosity</p>
<p>&lt;math&gt;\gamma = \frac{\phi}{\eta} &lt;/math&gt; ( if
&lt;math&gt; \phi &gt; 0&lt;/math&gt; )</p>
<p>Backward Euler Integration Routine Yield condition enforced at time
n+1</p>
<p>set $\eta = 0 $ for rate independent case</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Ed Love
</span></p>
