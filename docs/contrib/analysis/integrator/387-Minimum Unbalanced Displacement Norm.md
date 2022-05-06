# Minimum Unbalanced Displacement Norm

<p>This command is used to construct a StaticIntegrator object of type
MinUnbalDispNorm.</p>

```tcl
integrator MinUnbalDispNorm $dlambda1 &lt;$Jd $minLambda
        $maxLambda&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">dlambda1</code></p></td>
<td><p>first load increment (pseudo-time step) at the first iteration in
the next invocation of the <a href="Analysis_Command"
title="wikilink">analysis</a> command.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Jd</code></p></td>
<td><p>factor relating first load increment at subsequent time steps
(optional, default: 1.0)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$minLambda, $maxLambda</strong></p></td>
<td><p>arguments used to bound the load increment (optional, default:
$dLambda1 for both)</p></td>
</tr>
</tbody>
</table>
<hr />

## Examples

<p>integrator MinUnbalDispNorm 0.1;</p>
<hr />

## Theory

<p>The load increment at iteration i,
&lt;math&gt;d\lambda_{1,i}&lt;/math&gt;, is related to the load
increment at (i-1), $d\lambda_{1,i-1}$, and the
number of iterations at (i-1), $J_{i-1}$, by the
following:</p>
<dl>
<dt></dt>
<dd>

$$d\lambda_{1,i} =
d\lambda_{1,i-1}\frac{J_d}{J_{i-1}}$$

</dd>
</dl>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
