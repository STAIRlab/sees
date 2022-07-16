```{=mediawiki}
{{CommandManualMenu}}
```
This command is used to construct a TimeSeries object in which the load
factor is some triangular function of the time in the domain.

  ---------------------------------------------------------------------------------------------------
  \'\'\'timeSeries Triangle \$tag \$tStart \$tEnd \$period \<-shift \$shift\> \<-factor \$cFactor\>
  ---------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

  --------------- ---------------------------------------------------------
  **\$tag**       unique tag among TimeSeries objects
  **\$tStart**    starting time of non-zero load factor
  **\$tEnd**      ending time of non-zero load factor
  **\$period**    characteristic period of triangular wave
  **\$shift**     phase shift in seconds (optional, default = 0.0)
  **\$cFactor**   the load amplification factor (optional, default = 1.0)
  --------------- ---------------------------------------------------------

![](TriangularTimeSeries.png "TriangularTimeSeries.png")

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> Andreas Schellenberg,
University of California, Berkeley. \</span\>
