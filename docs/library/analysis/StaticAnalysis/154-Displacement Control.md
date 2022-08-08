# Displacement Control

This command is used to construct a DisplacementControl integrator
object. In an analysis step with Displacement Control we seek to
determine the time step that will result in a displacement increment for
a particular degree-of-freedom at a node to be a prescribed value.

<table>
<tbody>
<tr class="odd">
<td><p><strong>integrator DisplacementControl \$node \$dof \$incr
&lt; \$numIter \$$\Delta U \text{min}$ \$$\Delta U \text{max}$</p></td>
</tr>
</tbody>
</table>

<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">node</code></p></td>
<td><p>node whose response controls solution</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">dof</code></p></td>
<td><p>degree of freedom at the node, valid options: 1 through ndf at
node.</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">incr</code></p></td>
<td><p>first displacement increment <math>\Delta
U_{\text{dof}}</math></p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">numIter</code></p></td>
<td><p>the number of iterations the user would like to occur in the
solution algorithm. Optional, default = 1.0.</p></td>
</tr>
<tr class="odd">
<td><p>$\Delta U\text{min}$</td>
<td><p>the min stepsize the user will allow. optional, defualt = $\Delta U_{min} = \Delta U_0$</p></td>
</tr>
<tr class="even">
<td><p>$\Delta U \text{max}$</p></td>
<td><p>the max stepsize the user will allow. optional, default = $\Delta U_{max} = \Delta U_0$</p></td>
</tr>
</tbody>
</table>

<hr />

## Examples

displacement control algorithm seking constant increment of 0.1 at node 1 at 2'nd dof.

```tcl
integrator DisplacementControl 1 2 0.1; 
```

```python
{"integrator": ["DisplacementControl", 1, 2, 0.1]}
```

<hr />

## Theory

<p>If we write the governing finite element equation at <math>t +
\Delta t\!</math>as:</p>

$$ R(U_{t+\Delta t}, \lambda_{t+\Delta t}) = \lambda_{t+\Delta
t} F^{ext} - F(U_{t+\Delta t}) \!$$


<p>where <math>F(U_{t+\Delta t})\!</math> are the internal
forces which are a function of the displacements <math>U_{t+\Delta
t}\!</math>, <math>F^{ext}\!</math> is the set of
reference loads and <math>\lambda\!</math> is the load
multiplier. Linearizing the equation results in:</p>


$$K_{t+\Delta t}^{*i} \Delta U_{t+\Delta t}^{i+1} = \left(
\lambda^i_{t+\Delta t} + \Delta \lambda^i \right) F^{ext} -
F(U_{t+\Delta t})$$


This equation represents $n$ equations in $n+1$
unknowns, and so an additional equation is needed to solve the equation.
For displacement control, we introduce a new constraint equation in
which in each analysis step we set to ensure that the displacement
increment for the degree-of-freedom $\text{dof}$
at the specified node is:

$$ \Delta U_\text{dof} = \text{incr}\!$$


<p>MORE TO COME:</p>
<p>In Displacement Control the
$\Delta_U\text{dof}$ set to $t + \lambda_{t+1}$ where,</p>


$$\Delta U_\text{dof}^{t+1} = \max \left( \Delta U_{min},
\min \left( \Delta U_\text{max},
\frac{\text{numIter}}{\text{lastNumIter}} \Delta U_\text{dof}^{t} \right) \right) $$


<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
