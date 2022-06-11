# Hilber-Hughes-Taylor Method

<p>This command is used to construct a Hilber-Hughes-Taylor (HHT)
integration object. This is an implicit method that allows for energy
dissipation and second order accuracy (which is not possible with the
regular Newmark method). Depending on choices of input parameters, the
method can be unconditionally stable.</p>

```tcl
integrator HHT $alpha &lt;$gamma
        $beta&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">alpha</code></p></td>
<td><p>$\alpha$ factor</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">gamma</code></p></td>
<td><p>$\gamma$ factor</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">beta</code></p></td>
<td><p>$\beta$ factor</p></td>
</tr>
</tbody>
</table>
<hr />

## Examples

<p>integrator HHT 0.9</p>
<p>NOTES: $\alpha$ is defined differently that in
the paper, we use $\alpha = (\alpha_{HHT} - 1})$
where $\alpha_{HHT}$ is that used in the
paper.</p>
<ol>
<li>Like Newmark and all the implicit schemes, the unconditional
stability of this method applies to linear problems. There are no
results showing stability of this method over the wide range of
nonlinear problems that potentially exist. Experience indicates that the
time step for implicit schemes in nonlinear situations can be much
greater than those for explicit schemes.</li>
<li>$\alpha = 1.0$ corresponds to the Newmark
method.</li>
<li>$\alpha$ should be between 0.67 and 1.0. The
smaller the $\alpha$ the greater the numerical
damping.</li>
<li>$\gamma$ and $\beta$
are optional. The default values ensure the method is second order
accurate and unconditionally stable when $\alpha$
is $\tfrac{2}{3} &lt;= \alpha &lt;= 1.0$. The
defaults are:</li>
</ol>
<dl>
<dt></dt>
<dd>

$$\beta = \frac{(2 - \alpha)^2}{4}$$

</dd>
</dl>
<p>and</p>
<dl>
<dt></dt>
<dd>

$$\gamma = \frac{3}{2} - \alpha$$

</dd>
</dl>
<p>REFERENCES</p>
<p>Hilber, H.M, Hughes,T.J.R and Talor, R.L. "Improved Numerical
Dissipation for Time Integration Algorithms in Structural Dynamics"
Earthquake Engineering and Structural Dynamics, 5:282-292, 1977.</p>
<hr />

## Theory

<p>The HHT method (sometimes called the $\alpha$
method) is a one step implicit method for solving the transient problem
which attempts to increase the amount of numerical damping present
without degrading the order of accuracy. In the HHT method, the same
Newmark approximations are used:</p>
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
<p>but the time-discrete momentum equation is modified:</p>

$$
R_{t + \alpha \Delta t} = F_{t+\Delta t}^{ext} - M \ddot
U_{t + \Delta t} - C \dot U_{t+\alpha \Delta t} - F^{int}(U_{t + \alpha \Delta t})
$$

<p>where the displacements and velocities at the intermediate point are
given by:</p>
<dl>
<dt></dt>
<dd>

$$U_{t+ \alpha \Delta t} = (1 - \alpha) U_t + \alpha U_{t +
\Delta t}$$

</dd>
</dl>
<dl>
<dt></dt>
<dd>

$$\dot U_{t+\alpha \Delta t} = (1-\alpha) \dot U_t + \alpha
\dot U_{t + \Delta t}$$

</dd>
</dl>
<p>Following the methods outlined for Newmarks method, loinearization of
the nonlinear momentum equation results in the following linear
equations:</p>
<dl>
<dt></dt>
<dd>

$$K_{t+\Delta t}^{*i} d U_{t+\Delta t}^{i+1} = R_{t+\Delta
t}^i$$

</dd>
</dl>
<p>where</p>
<dl>
<dt></dt>
<dd>

$$K_{t+\Delta t}^{*i} = \alpha K_t + \frac{\alpha
\gamma}{\beta \Delta t} C_t + \frac{1}{\beta \Delta t^2} M$$

</dd>
</dl>
<p>and</p>
<dl>
<dt></dt>
<dd>

$$R_{t+\Delta t}^i = F_{t + \Delta t}^{ext} - F(U_{t + \alpha
\Delta t}^{i-1})^{int} - C \dot U_{t+\alpha \Delta t}^{i-1} - M \ddot
U_{t+ \Delta t}^{i-1}$$

</dd>
</dl>
<p>The linear equations are used to solve for $U_{t+\alpha
\Delta t}, \dot U_{t + \alpha \Delta t} \ddot U_{t+\Delta
t}$. Once convergence has been achieved the displacements
and velocities at time $t + \Delta t$ can be
computed.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
