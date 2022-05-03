```{=mediawiki}
{{CommandManualMenu}}
```
This command is used to construct a SecantNewton algorithm object which
uses the two-term update to accelerate the convergence of the modified
newton method. The command is of the following form:

  ---------------------------------------------------------------------------------------------------
  **algorithm SecantNewton \<-iterate \$tangIter\> \<-increment \$tangIncr\> \<-maxDim \$maxDim\>**
  ---------------------------------------------------------------------------------------------------

  ---------------- ------------------------------------------------------------------------------------------------
  **\$tangIter**   tangent to iterate on, options are current, initial, noTangent. default is current.
  **\$tangIncr**   tangent to increment on, options are current, initial, noTangent. default is current
  **\$maxDim**     max number of iterations until the tangent is reformed and acceleration restarts (default = 3)
  ---------------- ------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

NOTES:

The default \"cut-out\" values recommended by Crisfield (R1=3.5, R2=0.3)
are used.

------------------------------------------------------------------------

REFERENCES:

Crisfield, M.A. \"Non-linear Finite Element Analysis of Solids and
Structures\", Vol. 1, Wiley, 1991.

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> Michael Scott, Oregon
State University \</span\>
