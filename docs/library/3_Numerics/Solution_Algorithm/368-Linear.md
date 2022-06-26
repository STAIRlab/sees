# Linear

<p>This command is used to construct a Linear algorithm object which
takes one iteration to solve the system of equations.</p>

$$ \Delta U = - K^{-1}R(U),\!$$



```tcl
algorithm Linear < -initial > < -factorOnce >
```

<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-flag">-secant</code></p></td>
<td><p>optional flag to indicate to use secant stiffness</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-flag">-initial</code></p></td>
<td><p>optional flag to indicate to use initial stiffness</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-flag">-factorOnce</code></p></td>
<td><p>optional flag to indicate to only set up and factor matrix
once</p></td>
</tr>
</tbody>
</table>
<hr />
<p>NOTES 1) as the tangent matrix typically will not change during the
analysis in case of an elastic system it is highly advantageous to use
the -factorOnce option. Do not use this option if you have a nonlinear
system and you want the tangent used to be actual tangent at time of the
analysis step.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
