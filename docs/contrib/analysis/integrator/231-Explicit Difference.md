# Explicit Difference

<p>This command is used to construct a Explicit Difference integrator
object.</p>

```tcl
integrator Explicitdifference
```
<hr />

## Examples

<p>integrator Explicitdifference</p>
<hr />
<p>NOTES:</p>
<ol>
<li>When using Rayleigh damping, the damping ratio of high vibration
modes is overrated, and the critical time step size will be much
smaller. Hence Modal damping is more suitable for this method.</li>
<li>There should be no zero element on the diagonal of the mass matrix
when using this method.</li>
<li>Diagonal solver should be used when lumped mass matrix is used
because the equations are uncoupled.</li>
<li>For stability, <embed src="ExplicitDifference_eq1.pdf"
title="ExplicitDifference_eq1.pdf" /></li>
</ol>
<hr />

## Theory

<p>The Explicit Difference Integrator is based on the Leap-frog method.
The basic formula of Leap-frog method is shown as below:</p>
<dl>
<dt></dt>
<dd>
<img src="ExplicitDifference_eq2.png"
title="fig:ExplicitDifference_eq2.png"
alt="ExplicitDifference_eq2.png" />
</dd>
<dd>
<img src="ExplicitDifference_eq3.png"
title="fig:ExplicitDifference_eq3.png"
alt="ExplicitDifference_eq3.png" />
</dd>
<dd>
<img src="ExplicitDifference_eq4.png"
title="fig:ExplicitDifference_eq4.png"
alt="ExplicitDifference_eq4.png" />
</dd>
</dl>
<p>As mass matrix M is a diagonal matrix, the equations can be
uncoupled, then the solution procedure will be very efficient.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Shuhao Zhang,
Tsinghua University, and Prof. Xinzheng Lu, Tsinghua University
</span></p>
