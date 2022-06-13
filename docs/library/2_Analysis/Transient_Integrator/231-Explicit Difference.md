# Explicit Difference

This command is used to construct a Explicit Difference integrator
object.

```tcl
integrator Explicitdifference
```
<hr />

## Examples

```tcl
integrator Explicitdifference
```

<hr />

## Notes

1. When using Rayleigh damping, the damping ratio of high vibration
   modes is overrated, and the critical time step size will be much
   smaller. Hence Modal damping is more suitable for this method.

2. There should be no zero element on the diagonal of the mass matrix
   when using this method.

3. Diagonal solver should be used when lumped mass matrix is used
   because the equations are uncoupled.

4. For stability, $\Delta t \leq\left(\sqrt{\zeta^{2}+1}-\zeta\right) \frac{2}{\omega}$


<hr />

## Theory

<p>The Explicit Difference Integrator is based on the Leap-frog method.
The basic formula of Leap-frog method is shown as below:</p>

$$
\begin{aligned}
&\hat{\ddot{u}}_{t}=M^{-1}\left(F-K u_{t}-C \dot{u}_{t-\frac{1}{2} \Delta t}\right) \\
&\hat{\dot{u}}_{t+\frac{1}{2} \Delta t}=\dot{u}_{t-\frac{1}{2} \Delta t}+\ddot{\hat{u}}_{t} \Delta t \\
&u_{t+\Delta t}=u_{t}+\dot{\hat{u}}_{t+\frac{1}{2} \Delta t} \Delta t
\end{aligned}
$$

<p>As mass matrix M is a diagonal matrix, the equations can be
uncoupled, then the solution procedure will be very efficient.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Shuhao Zhang,
Tsinghua University, and Prof. Xinzheng Lu, Tsinghua University
</span></p>
