# Arc-Length Control

This command is used to construct an ArcLength integrator object. In
an analysis step with ArcLength we seek to determine the time step that
will result in our constraint equation being satisfied.

```tcl
integrator ArcLength $s $alpha
```

<hr />

<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">s</code></p></td>
<td><p>$s$ the arcLength.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">alpha</code></p></td>
<td><p>$\alpha$ a scaling factor on the reference
loads.</p></td>
</tr>
</tbody>
</table>

<hr />

## Examples

```{.tcl .example}
integrator ArcLength 1.0 0.1;
```

```{.py .example}
{"integrator": ["ArcLength", 1.0, 0.1]}
```
<hr />

## Theory

<p>If we write the governing finite element equation at $t + \Delta t\!$as:</p>

$$ R(U_{t+\Delta t}, \lambda_{t+\Delta t}) = \lambda_{t+\Delta
t} F^{ext} - F(U_{t+\Delta t}) \!$$


where $F(U_{t+\Delta t})\!$ are the internal
forces which are a function of the displacements $U_{t+\Delta t}\!$, 
$F^{ext}\!$ is the set of reference loads and $\lambda\!$ is the load
multiplier. Linearizing the equation results in:

<dl>
<dt></dt>
<dd>

$$K_{t+\Delta t}^{*i} \Delta U_{t+\Delta t}^{i+1} = \left (
\lambda^i_{t+\Delta t} + \Delta \lambda^i \right ) F^{ext} -
F(U_{t+\Delta t})$$

</dd>
</dl>

This equation represents $n$ equations in $n+1$
unknowns, and so an additional equation is needed to solve the equation.
For displacement control, we introduce a new constraint equation in
which in each analysis step we set to ensure that the displacement
increment for the degree-of-freedom $\text{dof}$
at the specified node is:

$$ \!$$


<p>MORE TO COME:</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk</span></p>

