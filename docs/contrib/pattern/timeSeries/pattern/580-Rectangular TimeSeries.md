```{=mediawiki}
{{CommandManualMenu}}
```
This command is used to construct a TimeSeries object in which the load
factor is constant for a specified period and 0 otherwise, i.e.

\<math\> \\lambda = f(t) = \\begin{cases} \\text{cFactor},
&\\text{tStart} \<= t \<= \\text{tEnd}\\\\ \\text{0.0},
&\\text{otherwise}\\\\ \\end{cases}

\</math\>

  ------------------------------------------------------------------------
  **timeSeries Rectangular \$tag \$tStart \$tEnd \<-factor \$cFactor\>**
  ------------------------------------------------------------------------

------------------------------------------------------------------------

  --------------- -------------------------------------------------
  **\$tag**       unique tag among TimeSeries objects.
  **\$tStart**    starting time of non-zero load factor
  **\$tEnd**      ending time of non-zero load factor
  **\$cFactor**   the load factor applied (optional, default=1.0)
  --------------- -------------------------------------------------

![](RectangularTimeSeries.gif "RectangularTimeSeries.gif")

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> fmk \</span\>
