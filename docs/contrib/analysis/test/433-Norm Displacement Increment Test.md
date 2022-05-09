# Norm Displacement Increment Test

<p>This command is used to construct a convergence test which uses the
norm of the left hand side solution vector of the matrix equation to
determine if convergence has been reached. What the solution vector of
the matrix equation is depends on integrator and constraint handler
chosen. Usually, though not always, it is equal to the displacement
increments that are to be applied to the model. The command to create a
NormDispIncr test is the following:</p>

```tcl
test NormDispIncr $tol $iter &lt;$pFlag&gt;
        &lt;$nType&gt;
```

<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">tol</code></p></td>
<td><p>the tolerance criteria used to check for convergence</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">iter</code></p></td>
<td><p>the max number of iterations to check before returning failure
condition</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">pFlag</code></p></td>
<td><p>optional print flag, default is 0. valid options:</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>0 print nothing</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>1 print information on norms each time test() is invoked</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>2 print information on norms and number of iterations at end of
successful test</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>4 at each step it will print the norms and also the
$\Delta U$ and $R(U)$
vectors.</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>5 if it fails to converge at end of $numIter it will print an
error message BUT RETURN A SUCCESSFUL test</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">nType</code></p></td>
<td><p>optional type of norm, default is 2. (0 = max-norm, 1 = 1-norm, 2
= 2-norm, ...)</p></td>
</tr>
</tbody>
</table>
<hr />
<p>NOTES:</p>
<ul>
<li>When using the Lagrange method to enforce the constraints, the
Lagrange multipliers appear in the solution vector.</li>
</ul>
<hr />

## Theory

<p>If the system of equations formed by the integrator is:</p>

$$K \Delta U^i = R(U^i)\,\!$$


<p>This integrator is testing:</p>

$$\parallel \Delta U^i \parallel &lt; \text{tol}
\!$$


<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
