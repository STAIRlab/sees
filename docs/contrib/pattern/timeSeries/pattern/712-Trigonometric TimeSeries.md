```{=mediawiki}
{{CommandManualMenu}}
```
This command is used to construct a TimeSeries object in which the load
factor is some trigonemtric function of the time in the domain \<math\>
\\lambda = f(t) = \\begin{cases} \\text{cFactor} \* sin (\\frac{2.0 \\Pi
(t-tStart)}{\\text{period}} + \\text{shift}), &\\text{tStart} \<= t \<=
\\text{tEnd}\\\\ \\text{0.0}, &\\text{otherwise}\\\\ \\end{cases}

\</math\>

  ---------------------------------------------------------------------------------------------
  **timeSeries Trig \$tag \$tStart \$tEnd \$period \<-factor \$cFactor\> \<-shift \$shift\>**
  ---------------------------------------------------------------------------------------------

------------------------------------------------------------------------

  --------------- --------------------------------------------------------------
  **\$tag**       unique tag among TimeSeries objects.
  **\$tStart**    starting time of non-zero load factor
  **\$tEnd**      ending time of non-zero load factor
  **\$period**    characteristic period of sine wave
  **\$shift**     phase shift in radians (optional, default=0.0)
  **\$cFactor**   the load factor amplification factor (optional, default=1.0)
  --------------- --------------------------------------------------------------

![](TrigTimeSeries.gif "TrigTimeSeries.gif")

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> fmk \</span\>
