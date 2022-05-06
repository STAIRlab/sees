```{=mediawiki}
{{CommandManualMenu}}
```
This command is used to construct a TimeSeries object in which the load
factor is some pulse function of the time in the domain.

  ------------------------------------------------------------------------------------------------------------------------
  \'\'\'timeSeries Pulse \$tag \$tStart \$tEnd \$period \<-width \$pulseWidth\> \<-shift \$shift\> \<-factor \$cFactor\>
  ------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

  ------------------ -------------------------------------------------------------------
  **\$tag**          unique tag among TimeSeries objects
  **\$tStart**       starting time of non-zero load factor
  **\$tEnd**         ending time of non-zero load factor
  **\$period**       characteristic period of pulse
  **\$pulseWidth**   pulse width as a fraction of the period (optional, default = 0.5)
  **\$shift**        phase shift in seconds (optional, default = 0.0)
  **\$cFactor**      the load amplification factor (optional, default = 1.0)
  ------------------ -------------------------------------------------------------------

![](PulseTimeSeries.png "PulseTimeSeries.png")

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> Andreas Schellenberg,
University of California, Berkeley. \</span\>
