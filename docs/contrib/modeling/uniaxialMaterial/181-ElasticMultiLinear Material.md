 # ElasticMultiLinear

<p>This command is used to construct a multi-linear elastic uniaxial
material object. The nonlinear stress-strain relationship is given by a
multi-linear curve that is define by a set of points. The behavior is
nonlinear but it is elastic. This means that the material loads and
unloads along the same curve, and no energy is dissipated. The slope
given by the last two specified points on the positive strain axis is
extrapolated to infinite positive strain. Similarly, the slope given by
the last two specified points on the negative strain axis is
extrapolated to infinite negative strain. The number of provided strain
points needs to be equal to the number of provided stress points.</p>

```tcl
uniaxialMaterial ElasticMultiLinear $matTag &lt;$eta&gt;
        -strain $strainPoints -stress $stressPoints
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">eta</code></td>
<td><p>damping tangent (optional, default=0.0)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">strainPoints</code></td>
<td><p>array of strain points along stress-strain curve</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">stressPoints</code></td>
<td><p>array of stress points along stress-strain curve</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/ElasticMultiLinear.png" title="ElasticMultiLinear.png"
alt="ElasticMultiLinear.png" />
<figcaption aria-hidden="true">ElasticMultiLinear.png</figcaption>
</figure>
<hr />
<p>EXAMPLE:</p>
<p>uniaxialMaterial ElasticMultiLinear 1 -strain -0.045 -0.04 -0.02 0.0
0.02 0.04 0.045 -stress 10 -100 -10 0 50 55 100</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Andreas
Schellenberg, University of California, Berkeley. </span></p>
