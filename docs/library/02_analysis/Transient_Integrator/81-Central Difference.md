# Central Difference

<p>This command is used to construct a Central Difference integrator
object.</p>

```tcl
integrator CentralDifference
```
<hr />

## Examples

<p>integrator CentralDifference</p>
<hr />
<p>NOTES:</p>
<ol>
<li>The calculation of $U_{t+\Delta t}$, as shown
below, is based on using the equilibrium equation at time t. For this
reason the method is called an <strong>explicit integration
method</strong>.</li>
<li>If there is no rayleigh damping and the C matrix is 0, for a
diagonal mass matrix a diagonal solver may and should be used.</li>
<li>For stability, &lt;math&gt;\frac{\Delta t}{T_n} &lt;
\frac{1}{\pi}&lt;/math&gt;</li>
</ol>
<hr />
## References
<hr />

## Theory

<p>The Central difference approximations for velocity and
acceleration:</p>
<dl>
<dt></dt>
<dd>

$$v_n = \frac{d_{n+1} - d_{n-1}}{2 \Delta t}$$

</dd>
</dl>
<dl>
<dt></dt>
<dd>

$$a_n = \frac{d_{n+1} - 2 d_n + d_{n-1}}{\Delta
t^2}$$

</dd>
</dl>
<p>In the Central Difference method we determine the displacement
solution at time $t+\delta t$ by considering the
the eqilibrium equation for the finite element system in motion at time
t:</p>
<dl>
<dt></dt>
<dd>

$$M \ddot U_t + C \dot U_t + K U_t = R_t$$

</dd>
</dl>
<p>which when using the above two expressions of becomes:</p>
<dl>
<dt></dt>
<dd>

$$\left ( \frac{1}{\Delta t^2} M + \frac{1}{2 \Delta t} C
\right ) U_{t+\Delta t} = R_t - \left (K - \frac{2}{\Delta t^2}M \right
)U_t - \left (\frac{1}{\Delta t^2}M - \frac{1}{2 \Delta t} C \right)
U_{t-\Delta t} $$

</dd>
</dl>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
