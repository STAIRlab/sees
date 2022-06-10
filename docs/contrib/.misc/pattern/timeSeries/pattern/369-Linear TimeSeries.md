```{=mediawiki}
{{CommandManualMenu}}
```
This command is used to construct a TimeSeries object in which the load
factor applied is linearly proportional to the time in the domain, i.e.

\<math\> \\lambda = f(t) = cFactor\*t\</math\>

  ---------------------------------------------------
  **timeSeries Linear \$tag \<-factor \$cFactor\>**
  ---------------------------------------------------

------------------------------------------------------------------------

  --------------- -------------------------------------------
  **\$tag**       unique tag among TimeSeries objects.
  **\$cFactor**   the linear factor (optional, default=1.0)
  --------------- -------------------------------------------

![](LinearTimeSeries.gif "LinearTimeSeries.gif")

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> fmk \</span\>
