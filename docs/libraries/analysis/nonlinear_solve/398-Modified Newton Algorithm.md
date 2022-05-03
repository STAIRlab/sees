```{=mediawiki}
{{CommandManualMenu}}
```
This command is used to construct a ModifiedNewton algorithm object,
which uses the modified newton-raphson algorithm to solve the nonlinear
residual equation. The command is of the following form:

  -------------------------------------------
  **algorithm ModifiedNewton \<-initial\>**
  -------------------------------------------

  -------------- ----------------------------------------------------------------
  **-initial**   optional flag to indicate to use initial stiffness iterations.
  -------------- ----------------------------------------------------------------

------------------------------------------------------------------------

NOTES:

------------------------------------------------------------------------

THEORY:

The theory for the ModifiedNewton method is similar to that for the [
Newton-Raphson method](Newton_Algorithm "wikilink"). The difference is
that the tangent at the initial guess is used in the iterations, instead
of the current tangent. The Modified Newmark method is thus an iterative
method in which, starting at a good initial guess \<math\>U_0\</math\>
we keep iterating until \<math\>\\Delta U\</math\> is small enough using
the following:

:   \<math\> \\Delta U = - K_0\^{-1}R(U_n),\\!\</math\>

```{=html}
<!-- -->
```

:   \<math\> U\_{n+1} = U_n + \\Delta U\\,\\!\</math\>

where:

:   \<math\>K_0 = \\frac{\\partial R(U_0)}{\\partial U}\\,\\!\</math\>

The advantage of this method over the regular Newton method, is that the
system Jacobian is formed only once at the start of the step and
factored only once if a direct solver is used. The drawback of this
method is that it requires more iterations than Newton\'s method.

note: when -initial flag is provided \<math\>K_0\</math\> is Jacobian
from undeformed configuration.

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> fmk \</span\>
