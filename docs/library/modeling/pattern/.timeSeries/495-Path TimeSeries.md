# Path TimeSeries

This command is used to construct a Path TimeSeries object. The
relationship between load factor and time is input by the user as a
series of discrete points in the 2d space (load factor, time). The input
points can come from a file or from a list in the script. When the time
specified does not match any of the input points, linear interpolation
is used between points. There are many ways to specify the load path:

For a load path where the factors are specified in a tcl list with a
constant time interval between points:

  -----------------------------------------------------------------------------------------------------------------------------------------
  **timeSeries Path \$tag -dt \$dt -values {list_of_values} \<-factor \$cFactor\> \<-useLast\> \<-prependZero\> \<-startTime \$tStart\>**
  -----------------------------------------------------------------------------------------------------------------------------------------

For a load path where the factors are specified in a file for a constant
time interval between points:

  -------------------------------------------------------------------------------------------------------------------------------------
  **timeSeries Path \$tag -dt \$dt -filePath \$filePath \<-factor \$cFactor\> \<-useLast\> \<-prependZero\> \<-startTime \$tStart\>**
  -------------------------------------------------------------------------------------------------------------------------------------

For a load path where the values are specified at non-constant time
intervals:

  -------------------------------------------------------------------------------------------------------------
  **timeSeries Path \$tag -time {list_of_times} -values {list_of_values} \<-factor \$cFactor\> \<-useLast\>**
  -------------------------------------------------------------------------------------------------------------

For a load path where both time and values are specified in a list
included in the command

  --------------------------------------------------------------------------------------------------------
  **timeSeries Path \$tag -fileTime \$fileTime -filePath \$filePath \<-factor \$cFactor\> \<-useLast\>**
  --------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

  ----------------------- -----------------------------------------------------------------------------------------------
  **\$tag**               unique tag among TimeSeries objects.
  **\$filePath**          file containing the load factors values
  **\$fileTime**          file containing the time values for corresponding load factors
  **\$dT**                time interval between specified points.
  **{ list_of_times}**    time values in a tcl list
  **{ list_of_values}**   load factor values in a tcl list
  **\$cFactor**           optional, a factor to multiply load factors by (default = 1.0)
  **-useLast**            optional, to use last value after the end of the series (default = 0.0)
  **-prependZero**        optional, to prepend a zero value to the series of load factors (default = false). See NOTES.
  **\$tStart**            optional, to provide a start time for provided load factors (default = 0.0)
  ----------------------- -----------------------------------------------------------------------------------------------

NOTES:

-   Linear interpolation between points.
-   If the specified time is beyond last point (AND WATCH FOR NUMERICAL
    ROUNDOFF), 0.0 is returned. Specify -useLast to use the last data
    point instead of 0.0.
-   The transient integration methods in OpenSees assume zero initial
    conditions. So it is important that any timeSeries that is being
    used in a transient analysis starts from zero (first data point in
    the timeSeries = 0.0). To guarantee that this is the case the
    optional parameter -prependZero can be specified to prepend a zero
    value to the provided timeSeries.

EXAMPLE:

timeSeries Path 1 -dT 0.02 -filePath A-ELC270.AT2 -factor \$G

timeSeries Path 2 -time {0.0 0.2 0.4 1.0} -values {0.0 1.0 2.0 0.0}

------------------------------------------------------------------------

Code Developed by: \<span style=\"color:blue\"\> fmk \</span\>
