# SteelMP

<p>This command is used to construct a uniaxial Menegotto-Pinto steel
material object.</p>

```tcl
uniaxialMaterial SteelMP $matTag $sigmaY $E $b
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique material object integer tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">sigmaY</code></td>
<td><p>yield stress or force</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">E</code></td>
<td><p>initial tangent stiffness</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">b</code></td>
<td><p>strain-hardening ratio (ratio between post-yield tangent and
initial elastic tangent)</p></td>
</tr>
</tbody>
</table>
<p>Note: For this material class, the sensitivity parameters can be:
sigmaY, E, b</p>
<hr />

$$
\begin{aligned}
\sigma^{*}=b \cdot \varepsilon^{*} &+\frac{(1-b) \cdot \varepsilon^{*}}{\left(1+\left|\varepsilon^{*}\right|^{R}\right)^{1 / R}} \\
\varepsilon^{*} &=\frac{\varepsilon-\varepsilon_{r}}{\varepsilon_{y}-\varepsilon_{r}} \\
\sigma^{*} &=\frac{\sigma-\sigma_{r}}{\sigma_{y}-\sigma_{r}}
R &= R_{0}-\frac{a_{1} \cdot \xi}{a_{2}+\xi} \\
\xi &= \dfrac{\max _{\varepsilon}\left|\varepsilon_{\max }-\varepsilon_{y}\right| }{\varepsilon_{y,0}}
\end{aligned}
$$


<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
Reference:
</dd>
<dd>
Barbato M., Conte J.P. (2006). “Finite element structural response
sensitivity and reliability analyses using smooth versus non-smooth
material constitutive models.” International Journal of Reliability and
Safety, 1(1-2):3-39.
</dd>
</dl>
</dd>
</dl>
