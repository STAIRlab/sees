# BoucWen

<p>This command is used to construct a uniaxial Bouc-Wen smooth
hysteretic material object. This material model is an extension of the
original Bouc-Wen model that includes stiffness and strength degradation
(Baber and Noori (1985)).</p>

:::{apidoc="opensees.uniaxial.BoucWen"}
```tcl
uniaxialMaterial BoucWen $matTag $alpha $ko $n $gamma
        $beta $Ao $deltaA $deltaNu $deltaEta
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>ratio of post-yield stiffness to the initial elastic stiffenss
(0&lt; $\alpha$ &lt;1)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ko</code></td>
<td><p>initial elastic stiffness</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">n</code></td>
<td><p>parameter that controls transition from linear to nonlinear range
(as n increases the transition becomes sharper; n is usually grater or
equal to 1)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">gamma beta</code></p></td>
<td><p>parameters that control shape of hysteresis loop; depending on
the values of $\gamma$ and
$\beta$ softening, hardening or quasi-linearity
can be simulated (look at the NOTES)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Ao deltaA</code></p></td>
<td><p>parameters that control tangent stiffness</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">deltaNu deltaEta</code></p></td>
<td><p>parameters that control material degradation</p></td>
</tr>
</tbody>
</table>
:::


<p>NOTES:</p>
<ol>
<li>Parameter $\gamma$ is usually in the range
  from -1 to 1 and parameter $\beta$ is usually in
  the range from 0 to 1. Depending on the values of $\gamma$ and $\beta$
  softening, hardening or quasi-linearity can be simulated. The hysteresis
  loop will exhibit <strong>softening</strong> for the following cases:

  1. $\beta + \gamma \gt 0$ and $\beta - \gamma \gt 0$, 
  2. $\beta + \gamma \gt 0$ and $\beta - \gamma \lt 0$, and 
  3. $\beta + \gamma \gt 0$ and $\beta - \gamma = 0$. 
  
  The hysteresis loop will exhibit <strong>hardening</strong> if
  $\beta + \gamma \lt 0$ and $\beta - \gamma \gt 0$, and <strong>quasi-linearity</strong> if
  $\beta + \gamma = 0 and $\beta - \gamma \gt 0$.

</li>
<li>The material can only define stress-strain relationship.</li>
</ol>

## References
<p>Haukaas, T. and Der Kiureghian, A. (2003). "Finite element
reliability and sensitivity methods for performance-based earthquake
engineering." REER report, PEER-2003/14 <a
href="http://peer.berkeley.edu/publications/peer_reports/reports_2003/0314.pdf">1</a>.</p>
<p>Baber, T. T. and Noori, M. N. (1985). "Random vibration of degrading,
pinching systems." Journal of Engineering Mechanics, 111(8),
1010-1026.</p>
<p>Bouc, R. (1971). "Mathematical model for hysteresis." Report to the
Centre de Recherches Physiques, pp16-25, Marseille, France.</p>
<p>Wen, Y.-K. (1976). \Method for random vibration of hysteretic
systems." Journal of Engineering Mechanics Division, 102(EM2),
249-263.</p>
