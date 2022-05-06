# Newmark Method

<p>This command is used to construct a Newmark integrator object.</p>

```tcl
integrator Newmark $gamma $beta
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">gamma</code></p></td>
<td><p>$\gamma$ factor</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">beta</code></p></td>
<td><p>$\beta$ factor</p></td>
</tr>
</tbody>
</table>
<hr />

## Examples

<p>integrator Newmark 0.5 0.25</p>
<hr />
<p>NOTES:</p>
<ol>
<li>If the accelerations are chosen as the unknowns and
$\beta$ is chosen as 0, the formulation results
in the fast but conditionally stable explicit Central Difference method.
Otherwise the method is implicit and requires an iterative solution
process.</li>
<li>Two common sets of choices are
<ol>
<li>Average Acceleration Method (&lt;math&gt;\gamma=\tfrac{1}{2}, \beta
= \tfrac{1}{4}&lt;/math&gt;)</li>
<li>Linear Acceleration Method (&lt;math&gt;\gamma=\tfrac{1}{2}, \beta =
\tfrac{1}{6}&lt;/math&gt;)</li>
</ol></li>
<li>$\gamma &gt; \tfrac{1}{2}$ results in
numerical damping proportional to &lt;math&gt; \gamma -
\tfrac{1}{2}&lt;/math&gt;</li>
<li>The method is second order accurate if and only if
&lt;math&gt;\gamma=\tfrac{1}{2}&lt;/math&gt;</li>
<li>The method is conditionally stable for &lt;math&gt; \beta &gt;=
\frac{\gamma}{2} &gt;= \tfrac{1}{4}&lt;/math&gt;</li>
</ol>
<hr />
<p>REFERENCES</p>
<p>Newmark, N.M. "A Method of Computation for Structural Dynamics" ASCE
Journal of Engineering Mechanics Division, Vol 85. No EM3, 1959.</p>
<hr />

## Theory

<p>The Newmark method is a one step implicit method for solving the
transient problem, represented by the residual for the momentum
equation:</p>
<dl>
<dt></dt>
<dd>

$$R_{t + \Delta t} = F_{t+\Delta t}^{ext} - M \ddot U_{t +
\Delta t} - C \dot U_{t + \Delta t} + F(U_{t + \Delta
t})^{int}$$

</dd>
</dl>
<p>Using the Taylor series approximation of &lt;math&gt;U_{t+\Delta
t}&lt;/math&gt; and $\dot U_{t+\Delta t}$:</p>
<dl>
<dt></dt>
<dd>

$$U_{t+\Delta t} = U_t + \Delta t \dot U_t + \tfrac{\Delta
t^2}{2} \ddot U_t + \tfrac{\Delta t^3}{6} \dot \ddot U_t + \cdots
$$

</dd>
</dl>
<dl>
<dt></dt>
<dd>

$$\dot U_{t+\Delta t} = \dot U_t + \Delta t \ddot U_t +
\tfrac{\Delta t^2}{2} \dot \ddot U_t + \cdots $$

</dd>
</dl>
<p>Newton truncated these using the following:</p>
<dl>
<dt></dt>
<dd>

$$U_{t+\Delta t} = u_t + \Delta t \dot U_t + \tfrac{\Delta
t^2}{2} \ddot U + \beta {\Delta t^3} \dot \ddot U $$

</dd>
</dl>
<dl>
<dt></dt>
<dd>

$$\dot U_{t + \Delta t} = \dot U_t + \Delta t \ddot U_t +
\gamma \Delta t^2 \dot \ddot U $$

</dd>
</dl>
<p>in which he assumed linear acceleration within a time step, i.e.</p>
<dl>
<dt></dt>
<dd>

$$\dot \ddot U = \frac{{\ddot U_{t+\Delta t}} - \ddot
U_t}{\Delta t} $$

</dd>
</dl>
<p>which results in the following expressions:</p>
<dl>
<dt></dt>
<dd>

$$U_{t+\Delta t} = U_t + \Delta t \dot U_t + [(0.5 - \beta)
\Delta t^2] \ddot U_t + [\beta \Delta t^2] \ddot U_{t+\Delta
t}$$

</dd>
</dl>
<dl>
<dt></dt>
<dd>

$$\dot U_{t+\Delta t} = \dot U_t + [(1-\gamma)\Delta t] \ddot
U_t + [\gamma \Delta t ] \ddot U_{t+\Delta t} $$

</dd>
</dl>
<p>The variables $\beta$ and
$\gamma$ are numerical parameters that control
both the stability of the method and the amount of numerical damping
introduced into the system by the method. For
$\gamma=\tfrac{1}{2}$ there is no numerical
damping; for $\gamma&gt;=\tfrac{1}{2}$ numerical
damping is introduced. Two well known and commonly used cases are:</p>
<ol>
<li>Average Acceleration Method (&lt;math&gt;\gamma=\tfrac{1}{2}, \beta
= \tfrac{1}{4}&lt;/math&gt;)</li>
<li>Constant Acceleration Method (&lt;math&gt;\gamma=\tfrac{1}{2}, \beta
= \tfrac{1}{6}&lt;/math&gt;)</li>
</ol>
<p>The linearization of the Newmark equations gives:</p>
<dl>
<dt></dt>
<dd>

$$dU_{t+\Delta t}^{i+1} = \beta \Delta t^2 d \ddot U_{t+\Delta
t}^{i+1}$$

</dd>
</dl>
<dl>
<dt></dt>
<dd>

$$d \dot U_{t+\Delta t}^{i+1} = \gamma \Delta t \ddot
U_{t+\Delta t}^{i+1}$$

</dd>
</dl>
<p>which gives the update formula when displacement increment is used as
unknown in the linearized system as:</p>
<dl>
<dt></dt>
<dd>

$$U_{t+\Delta t}^{i+1} = U_{t+\Delta t}^i + dU_{t+\Delta
t}^{i+1}$$

</dd>
</dl>
<dl>
<dt></dt>
<dd>

$$\dot U_{t+\Delta t}^{i+1} = \dot U_{t+\Delta t}^i +
\frac{\gamma}{\beta \Delta t}dU_{t+\Delta t}^{i+1}$$

</dd>
</dl>
<dl>
<dt></dt>
<dd>

$$\ddot U_{t+\Delta t}^{i+1} = \ddot U_{t+\Delta t}^i +
\frac{1}{\beta \Delta t^2}dU_{t+\Delta t}^{i+1}$$

</dd>
</dl>
<p>The linearization of the momentum equation using the displacements as
the unknowns leads to the following linear equation:</p>
<dl>
<dt></dt>
<dd>

$$K_{t+\Delta t}^{*i} \Delta U_{t+\Delta t}^{i+1} =
R_{t+\Delta t}^i$$

</dd>
</dl>
<p>where</p>
<dl>
<dt></dt>
<dd>

$$K_{t+\Delta t}^{*i} = K_t + \frac{\gamma}{\beta \Delta t}
C_t + \frac{1}{\beta \Delta t^2} M$$

</dd>
</dl>
<p>and</p>
<dl>
<dt></dt>
<dd>

$$R_{t+\Delta t}^i = F_{t + \Delta t}^{ext} - F(U_{t + \Delta
t}^{i-1})^{int} - C \dot U_{t+\Delta t}^{i-1} - M \ddot U_{t+ \Delta
t}^{i-1}$$

</dd>
</dl>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
