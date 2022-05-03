```{=mediawiki}
{{CommandManualMenu}}
```
This command is used to construct a KrylovNewton algorithm object which
uses a Krylov subspace accelerator to accelerate the convergence of the
modified newton method. The command is of the following form:

  ---------------------------------------------------------------------------------------------------
  **algorithm KrylovNewton \<-iterate \$tangIter\> \<-increment \$tangIncr\> \<-maxDim \$maxDim\>**
  ---------------------------------------------------------------------------------------------------

  ---------------- -----------------------------------------------------------------------------------------------------
  **\$tangIter**   tangent to iterate on, options are current, initial, noTangent. default is current.
  **\$tangIncr**   tangent to increment on, options are current, initial, noTangent. default is current
  **\$maxDim**     max number of iterations until the tangent is reformed and the acceleration restarts (default = 3).
  ---------------- -----------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

NOTES:

------------------------------------------------------------------------

REFERENCES:

Scott, M.H. and G.L. Fenves. \"A Krylov Subspace Accelerated Newton
Algorithm: Application to Dynamic Progressive Collapse Simulation of
Frames.\" Journal of Structural Engineering, 136(5), May 2010.
[DOI](http://dx.doi.org/10.1061/(ASCE)ST.1943-541X.0000143)

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> Michael Scott, Oregon
State University \</span\>
