```{=mediawiki}
{{CommandManualMenu}}
```
This command is used to construct a NewtonLineSearch algorithm object
which introduces line search to the [
Newton-Raphson](Newton_Algorithm "wikilink") algorithm to solve the
nonlinear residual equation. Line search increases the effectiveness of
the Newton method when convergence is slow due to roughness of the
residual. The command is of the following form:

  ---------------------------------------------------------------------------------------------------------------------------------------
  **algorithm NewtonLineSearch \<-type \$typeSearch\> \<-tol \$tol\> \<-maxIter \$maxIter\> \<-minEta \$minEta\> \<-maxEta \$maxEta\>**
  ---------------------------------------------------------------------------------------------------------------------------------------

  ------------------ --------------------------------------------------------------------------------
  **\$typeSearch**   line search algorithm. optional default is InitialInterpoled. valid types are:
                     Bisection, Secant, RegulaFalsi, InitialInterpolated
  **\$tol**          tolerance for search. optional, defeulat = 0.8
  **\$maxIter**      max num of iterations to try. optional, default = 10
  **\$minEta**       a min \<math\>\\eta\\!\</math\> value. optional, default = 0.1
  **\$maxEta**       a max \<math\>\\eta\\!\</math\> value. optional, default = 10.0
  ------------------ --------------------------------------------------------------------------------

------------------------------------------------------------------------

REFERENCES:

M.A. Crisfield, \"Nonlinear Finite Element Analysis of Solids and
Structures, Volume 1:Essentials\", Wiley, 1991.

------------------------------------------------------------------------

THEORY:

The rationale behin line search is that:

-   the direction \<math\>\\Delta U\\,\\!\</math\> found by the [
    Newton-Raphson method](Newton_Algorithm "wikilink") is often a good
    direction, but the step size \<math\>\\parallel\\Delta
    U\\parallel\</math\> is not.
-   It is cheaper to compute the residual for several points along
    \<math\>\\Delta U\\,\\!\</math\> rather than form and factor a new
    system Jacobian

In NewtonLineSearch the regular [ Newton-Raphson
method](Newton_Algorithm "wikilink") is used to compute the
\<math\>\\Delta U\\,\\!\</math\>, but the update that is used is
modified. The modified update is:

:   \<math\> U\_{n+1} = U_n + \\eta \\Delta U\\,\\!\</math\>

The different line search algorithms use different root finding methods
to obtain \<math\>\\eta\\,\\!\</math\>, a root to the function
\<math\>s(\\eta)\</math\> defined as:

:   \<math\> s(\\eta) = \\Delta U R(U\_{n} + \\eta \\Delta
    U)\\,\\!\</math\>

with

:   \<math\> s_0 = \\Delta U R(U_n),\\!\</math\>

## Interpolated Line Search: {#interpolated_line_search}

while (\<math\>\\frac{s_n}{s_0}\\!\</math\> \> \$tol && count \<
\$maxIter} {

:   \<math\> \\eta\_{n+1} = \\frac{\\eta_n \*s0}{s0 -s\_{n+1}}
    ,\\!\</math\>

}

\_\_NOTOC\_\_

## RegulaFalsi Line Search: {#regulafalsi_line_search}

while (\<math\>\\frac{s_n}{s_0}\\!\</math\> \> \$tol && count \<
\$maxIter} {

:   \<math\> \\eta\_{n+1} = \\eta_U -
    \\frac{s_U\*(\\eta_L-\\eta_U)}{s_L-S_U} ,\\!\</math\>
:   if \<math\> s\_{n+1} \* s_L \< 0 \\Rightarrow \\eta_U =
    \\eta\_{n+1}, s_U = s\_{n+1},\\!\</math\>
:   if \<math\> s\_{n+1} \* s_U \< 0 \\Rightarrow \\eta_L =
    \\eta\_{n+1}, s_L = s\_{n+1},\\!\</math\>

}

## Bisection Line Search: {#bisection_line_search}

while (\<math\>\\frac{s_n}{s_0}\\!\</math\> \> \$tol && count \<
\$maxIter} {

:   \<math\> \\eta\_{n+1} = \\frac{\\eta_L - \\eta_U}{2.0} ,\\!\</math\>
:   if \<math\> s\_{n+1} \* s_L \< 0 \\Rightarrow \\eta_U =
    \\eta\_{n+1}, s_U = s\_{n+1},\\!\</math\>
:   if \<math\> s\_{n+1} \* s_U \< 0 \\Rightarrow \\eta_L =
    \\eta\_{n+1}, s_L = s\_{n+1},\\!\</math\>

}

## Secant Line Search: {#secant_line_search}

while (\<math\>\\frac{s_n}{s_0}\\!\</math\> \> \$tol && count \<
\$maxIter} {

:   \<math\> \\eta\_{n+1} = \\eta_j -
    \\frac{s_j\*(\\eta\_{j-1}-\\eta_j)}{s\_{j-1}-S_j} ,\\!\</math\>
:   if \<math\> s\_{n+1} \* s_L \< 0 \\Rightarrow \\eta_U =
    \\eta\_{n+1}, s_U = s\_{n+1},\\!\</math\>
:   if \<math\> s\_{n+1} \* s_U \< 0 \\Rightarrow \\eta_L =
    \\eta\_{n+1}, s_L = s\_{n+1},\\!\</math\>

}

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> fmk \</span\>
