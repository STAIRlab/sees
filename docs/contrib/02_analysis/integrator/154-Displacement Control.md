# Displacement Control

<p>This command is used to construct a DisplacementControl integrator
object. In an analysis step with Displacement Control we seek to
determine the time step that will result in a displacement increment for
a particular degree-of-freedom at a node to be a prescribed value.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>integrator DisplacementControl $node $dof $incr
&lt;$numIter $&lt;math&gt;\Delta U \text{min} &lt;/math&gt;
$&lt;math&gt;\Delta U \text{max}&lt;/math&gt;&gt;</strong></p></td>
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
<td><p>first displacement increment &lt;math&gt;\Delta
U_{\text{dof}}&lt;/math&gt;</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">numIter</code></p></td>
<td><p>the number of iterations the user would like to occur in the
solution algorithm. Optional, default = 1.0.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$&lt;math&gt;\Delta U
\text{min}&lt;/math&gt;</strong></p></td>
<td><p>the min stepsize the user will allow. optional, defualt =
&lt;math&gt;\Delta U_{min} = \Delta U_0&lt;/math&gt;</p></td>
</tr>
<tr class="even">
<td><p><strong>$&lt;math&gt;\Delta U
\text{max}&lt;/math&gt;</strong></p></td>
<td><p>the max stepsize the user will allow. optional, default =
&lt;math&gt;\Delta U_{max} = \Delta U_0&lt;/math&gt;</p></td>
</tr>
</tbody>
</table>
<hr />

## Examples

<p>integrator DisplacementControl 1 2 0.1; # displacement control
algorithm seking constant increment of 0.1 at node 1 at 2'nd dof.</p>
<hr />

## Theory

<p>If we write the governing finite element equation at &lt;math&gt;t +
\Delta t\!&lt;/math&gt;as:</p>

$$ R(U_{t+\Delta t}, \lambda_{t+\Delta t}) = \lambda_{t+\Delta
t} F^{ext} - F(U_{t+\Delta t}) \!$$


<p>where &lt;math&gt;F(U_{t+\Delta t})\!&lt;/math&gt; are the internal
forces which are a function of the displacements &lt;math&gt;U_{t+\Delta
t}\!&lt;/math&gt;, &lt;math&gt;F^{ext}\!&lt;/math&gt; is the set of
reference loads and &lt;math&gt;\lambda\!&lt;/math&gt; is the load
multiplier. Linearizing the equation results in:</p>
<dl>
<dt></dt>
<dd>

$$K_{t+\Delta t}^{*i} \Delta U_{t+\Delta t}^{i+1} = \left (
\lambda^i_{t+\Delta t} + \Delta \lambda^i \right ) F^{ext} -
F(U_{t+\Delta t})$$

</dd>
</dl>
<p>This equation represents n equations in $n+1$
unknowns, and so an additional equation is needed to solve the equation.
For displacement control, we introduce a new constraint equation in
which in each analysis step we set to ensure that the displacement
increment for the degree-of-freedom $\text{dof}$
at the specified node is:</p>

$$ \Delta U_\text{dof} = \text{incr}\!$$


<p>MORE TO COME:</p>
<p>In Displacement Control the
$\Delta_U\text{dof}$ set to &lt;math&gt;t +
\lambda_{t+1}&lt;/math&gt; where,</p>
<dl>
<dt></dt>
<dd>

$$\Delta U_\text{dof}^{t+1} = \max \left ( \Delta U_{min},
\min \left ( \Delta U_\text{max},
\frac{\text{numIter}}{\text{lastNumIter}} \Delta U_\text{dof}^{t} \right
) \right ) $$

</dd>
</dl>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
