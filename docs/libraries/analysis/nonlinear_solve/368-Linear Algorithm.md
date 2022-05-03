```{=mediawiki}
{{CommandManualMenu}}
```
This command is used to construct a Linear algorithm object which takes
one iteration to solve the system of equations.

:   \<math\> \\Delta U = - K\^{-1}R(U),\\!\</math\>

  ---------------------------------------------------
  **algorithm Linear \<-initial\> \<-factorOnce\>**
  ---------------------------------------------------

  ----------------- -----------------------------------------------------------------
  **-secant**       optional flag to indicate to use secant stiffness
  **-initial**      optional flag to indicate to use initial stiffness
  **-factorOnce**   optional flag to indicate to only set up and factor matrix once
  ----------------- -----------------------------------------------------------------

------------------------------------------------------------------------

NOTES 1) as the tangent matrix typically will not change during the
analysis in case of an elastic system it is highly advantageous to use
the -factorOnce option. Do not use this option if you have a nonlinear
system and you want the tangent used to be actual tangent at time of the
analysis step.

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> fmk \</span\>
