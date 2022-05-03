```{=mediawiki}
{{CommandManualMenu}}
```
This command is used to construct a NewtonRaphson algorithm object which
is uses the Newton-Raphson algorithm to solve the nonlinear residual
equation. The Newton-Raphson method is the most widely used and most
robust method for solving nonlinear algebraic equations. The command is
of the following form:

  -----------------------------------------------------------
  **algorithm Newton \<-initial\> \<-initialThenCurrent\>**
  -----------------------------------------------------------

  ------------------------- -------------------------------------------------------------------------------------------------------------------
  **-initial**              optional flag to indicate to use initial stiffness iterations
  **-initialThenCurrent**   optional flag to indicate to use initial stiffness on first step, then use current stiffness for subsequent steps
  ------------------------- -------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

REFERENCES:

[Read the page at
Wikipedia](http://en.wikipedia.org/wiki/Newton%27s_method)

------------------------------------------------------------------------

THEORY:

The Newton method used in finite element analysis is identical to that
taught in basic calculus courses. It is just extended for the n unknown
degrees-of-freedom. The method as taught in basic calculus, is a
root-finding algorithm that uses the first few terms of the Taylor
series of a function \<math\>f(x)\\,\\!\</math\> in the vicinity of a
suspected root \<math\>x_n\\,\\!\</math\> to find the root
\<math\>x\_{n+1}\\,\\!\</math\>. Newton\'s method is sometimes also
known as Newton\'s iteration, although in this work the latter term is
reserved to the application of Newton\'s method for computing square
roots.

The Taylor series of \<math\>r(x)\\,\\!\</math\> about the point
\<math\>x=x_n+\\Delta x\\,\\!\</math\> is given by

:   \<math\>f(x_n+\\Delta x) = f(x_n)+r\^{\'}(x_n)\\Delta x +
    1/2r\^{\'\'}(x_n) \\Delta x\^2+\....\\,\\!\</math\>

Keeping terms only to first order,

:   \<math\>f(x_n+\\Delta x) \\approx f(x_n)+r\^\'(x_n)\\Delta x =
    f(x_n)+ \\frac{df(x_n)}{dx}\\Delta x\</math\>

and since at the root we wish to find \<math\>x_n + \\Delta x\</math\>,
the function equates to 0, i.e. \<math\>f(x_n+\\Delta x) = 0\</math\>,
we can solve for an approximate \<math\>\\Delta x\</math\>

:   \<math\> \\Delta x \\approx -\\frac{f(x_n)}{f\^\'(x_n)} = -
    \\frac{df(x_n)}{dx}\^{-1}f(x_n)\</math\>

The Newmark method is thus an iterative method in which, starting at a
good initial guess \<math\>x_0\\,\\!\</math\> we keep iterating until
our convergence criteria is met with the following:

:   \<math\> \\Delta x = -
    \\frac{df(x_n)}{dx}\^{-1}f(x_n)\\,\\!\</math\>

```{=html}
<!-- -->
```

:   \<math\> x\_{n+1} = x_n + \\Delta x\\,\\!\</math\>

The method is generalized to n unknowns by replacing the above scalar
equations with matrix ones.

:   \<math\>R(U_n+\\Delta x) = R(U_n)+\\frac{\\partial R(U_n)}{\\partial
    U} \\Delta U + O(\\Delta U \^2) \\,\\!\</math\>

The matrix \<math\>\\frac{\\partial R(U_n)}{\\partial U}\\,\\!\</math\>
is called the system Jacobian matrix and will be denoted K:

:   \<math\>K = \\frac{\\partial R(U_n)}{\\partial U}\\,\\!\</math\>

resulting in our iterative procedure where starting from a good initial
guess we iterate until our [ convergence
criteria](Test_Command "wikilink") is met with the following:

:   \<math\> \\Delta U = - K\^{-1}R(U_n),\\!\</math\>

```{=html}
<!-- -->
```

:   \<math\> U\_{n+1} = U_n + \\Delta U\\,\\!\</math\>

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> fmk \</span\>
