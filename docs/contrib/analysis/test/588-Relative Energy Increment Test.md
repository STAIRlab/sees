# RelativeEnergyIncr

<p>This command is used to construct a convergence test which uses the
dot product of the solution vector and norm of the right hand side of
the matrix equation to determine if convergence has been reached. The
physical meaning of this quantity depends on the integrator and
constraint handler chosen. Usually, though not always, it is equal to
the energy unbalance in the system. The test is relatively to the first
dot product computed for each step. The command to create a EnergyIncr
test is the following:</p>

```tcl
test RelativeEnergyIncr $tol $iter &lt;$pFlag&gt;
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
successfull test</p></td>
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
error message BUT RETURN A SUCEESSFULL test</p></td>
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
<li>When using the Penalty method additional large forces to enforce the
penalty functions exist on the right had side, making</li>
</ul>
<p>convergence using this test usually impossible (even though solution
might have converged).</p>
<ul>
<li>When Lagrange multipliers are used, the solution vector contains the
Lagrange multiplies.</li>
</ul>
<hr />

## Theory

<p>If the system of equations formed by the integrator is:</p>

$$K \Delta U^i = R(U^i)\,\!$$


<p>This integrator is testing:</p>

$$ \frac{\Delta U^i R(U^i)}{\Delta U^0 R(U^0)} &lt; \text{tol}
\!$$


<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
