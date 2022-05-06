# Arc-Length Control

<p>This command is used to construct an ArcLength integrator object. In
an analysis step with ArcLength we seek to determine the time step that
will result in our constraint equation being satisfied.</p>

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

<p>integrator ArcLength 1.0 0.1;</p>
<hr />

## Theory

<p>If we write the governing finite element equation at &lt;math&gt;t +
\Delta t\!&lt;/math&gt;as:</p>
<dl>
<dt></dt>
<dd>
&lt;math&gt; R(U_{t+\Delta t}, \lambda_{t+\Delta t}) = \lambda_{t+\Delta
t} F^{ext} - F(U_{t+\Delta t}) \!&lt;/math&gt;
</dd>
</dl>
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
<dl>
<dt></dt>
<dd>
&lt;math&gt; \!&lt;/math&gt;
</dd>
</dl>
<p>MORE TO COME:</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
