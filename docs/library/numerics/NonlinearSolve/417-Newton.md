# Newton

<p>This command is used to construct a NewtonRaphson algorithm object
which is uses the Newton-Raphson algorithm to solve the nonlinear
residual equation. The Newton-Raphson method is the most widely used and
most robust method for solving nonlinear algebraic equations. The
command is of the following form:</p>

```tcl
algorithm Newton < -initial > < -initialThenCurrent >
```

<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-flag">-initial</code></p></td>
<td><p>optional flag to indicate to use initial stiffness
iterations</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-flag">-initialThenCurrent</code></p></td>
<td><p>optional flag to indicate to use initial stiffness on first step,
then use current stiffness for subsequent steps</p></td>
</tr>
</tbody>
</table>
<hr />
## References
<p><a href="http://en.wikipedia.org/wiki/Newton%27s_method">Read the
page at Wikipedia</a></p>
<hr />

## Theory

<p>The Newton method used in finite element analysis is identical to
that taught in basic calculus courses. It is just extended for the n
unknown degrees-of-freedom. The method as taught in basic calculus, is a
root-finding algorithm that uses the first few terms of the Taylor
series of a function &lt;math&gt;f(x)\,\!&lt;/math&gt; in the vicinity
of a suspected root &lt;math&gt;x_n\,\!&lt;/math&gt; to find the root
&lt;math&gt;x_{n+1}\,\!&lt;/math&gt;. Newton's method is sometimes also
known as Newton's iteration, although in this work the latter term is
reserved to the application of Newton's method for computing square
roots.</p>
<p>The Taylor series of &lt;math&gt;r(x)\,\!&lt;/math&gt; about the
point &lt;math&gt;x=x_n+\Delta x\,\!&lt;/math&gt; is given by</p>

$$f(x_n+\Delta x) = f(x_n)+r^{'}(x_n)\Delta x + 1/2r^{''}(x_n)
\Delta x^2+....\,\!$$


<p>Keeping terms only to first order,</p>

$$f(x_n+\Delta x) \approx f(x_n)+r^'(x_n)\Delta x = f(x_n)+
\frac{df(x_n)}{dx}\Delta x$$


<p>and since at the root we wish to find  $x_n + \Delta
x$ , the function equates to 0, i.e. &lt;math&gt;f(x_n+\Delta
x) = 0&lt;/math&gt;, we can solve for an approximate &lt;math&gt;\Delta
x&lt;/math&gt;</p>

$$ \Delta x \approx -\frac{f(x_n)}{f^'(x_n)} = -
\frac{df(x_n)}{dx}^{-1}f(x_n)$$


<p>The Newmark method is thus an iterative method in which, starting at
a good initial guess &lt;math&gt;x_0\,\!&lt;/math&gt; we keep iterating
until our convergence criteria is met with the following:</p>

$$ \Delta x = - \frac{df(x_n)}{dx}^{-1}f(x_n)\,\!$$



$$ x_{n+1} = x_n + \Delta x\,\!$$


<p>The method is generalized to n unknowns by replacing the above scalar
equations with matrix ones.</p>

$$R(U_n+\Delta x) = R(U_n)+\frac{\partial R(U_n)}{\partial U}
\Delta U + O(\Delta U ^2) \,\!$$


<p>The matrix &lt;math&gt;\frac{\partial R(U_n)}{\partial
U}\,\!&lt;/math&gt; is called the system Jacobian matrix and will be
denoted K:</p>

$$K = \frac{\partial R(U_n)}{\partial U}\,\!$$


<p>resulting in our iterative procedure where starting from a good
initial guess we iterate until our <a href="Test_Command"
title="wikilink"> convergence criteria</a> is met with the
following:</p>

$$ \Delta U = - K^{-1}R(U_n),\!$$



$$ U_{n+1} = U_n + \Delta U\,\!$$


<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
