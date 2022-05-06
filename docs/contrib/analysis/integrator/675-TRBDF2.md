# TRBDF2

<p>This command is used to construct a TRBDF2 integrator object. The
TRBDF2 integrator is a composite scheme that alternates between the
Trapezoidal scheme and a 3 point backward Euler scheme. It does this in
an attempt to conserve energy and momentum, something newmark does not
always do.</p>

```tcl
integrator TRBDF2
```
<hr />
<p>NOTES:</p>
<ol>
<li>As opposed to dividing the time-step in 2 as outlined in the papers,
we just switch alternate between the 2 integration strategies,i.e. the
time step in our implementation is double that described in the
papers.</li>
</ol>
<hr />

## Examples

<p>integrator TRBDF2</p>
<hr />
<p>REFERENCES</p>
<p>Bank, R.E., Coughran W.M., Fichter W., Grosse E.H., Rose, D.J., and
Smith R.K. "Transient Simulations of Silicon Devices and Circuits", IEE
Trans CAD, Vol(4), 436-451, 1985.</p>
<p>Bathe, K.J. "Conserving Energy and Momentum in Nonlinear Dynamics: A
Simple Impicit Time Integration Scheme", Computers and Structures,
Vol(85), 437-445, 2007. <a
href="doi:10.1016/j.compstruc.2006.09.004">doi:10.1016/j.compstruc.2006.09.004</a></p>
<hr />

## Theory

<p>COMING SOON. LOOK AT BATHE'S PAPER FOR NOW.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
