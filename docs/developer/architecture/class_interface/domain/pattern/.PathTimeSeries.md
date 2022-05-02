# PathTimeSeries

```{.cpp}
#include <domain/pattern/PathTimeSeries.h>
```

```{.cpp}
class PathTimeSeries: 
public
  DomainComponent
  MovableObject
  TimeSeries
```


The `PathTimeSeries` class is a concrete subclass of TimeSeries. The
relationship between the pseudo time and the load factor follows a user
specified path. The path points are specified at user specified time
values. For a pseudo time not at a path point, linear interpolation is
performed to determine the load factor. If the time specified is beyond
the last path point a load factor of $0.0$ will be returned.

// Constructors




// Destructor


// Public Methods





Used to construct a PathTimeSeries when the data points and time values
are specified in a Vectors. The tag TSERIES_TAG_PathTimeSeries is passed
to the TimeSeries constructor. Sets the constant factor used in the
relation to *cFactor*. Constructs two new Vectors equal to *thePath* and
*time*. Prints a warning message if no space is available for the
Vectors or if the two Vectors are not of the same size.

Used to construct a PathTimeSeries when the data points and time values
are specified in files. The tag TSERIES_TAG_PathTimeSeries is passed to
the TimeSeries constructor. Sets the constant factor used in the
relation to *cFactor*. Opens the two files and counts the number of
entries in each, if different prints a warning message and returns.
Constructs the two vectors for the data and reads the data from the
files into the two vectors. Prints a warning message if no space is
available for the Vectors.

\
For a `FEM_ObjectBroker` to instantiate an empty PathTimeSeries,
`recvSelf()` must be invoked on this object. The tag
`TSERIES_TAG_PathTimeSeries` is passed to the TimeSeries constructor.

\
Invokes the destructor on the two Vectors created to hold the data.


Determines the load factor based on the *pseudoTime* and the data
points. Returns $0.0$ if *pseudoTime* is greater than time of last data
point, otherwise returns a linear interpolation of the data points times
the factor *cFactor*.

Creates a vector of size 4 into which it places *cFactor*, the size of
*thePath* and two database tag for *thaPath* and *time* Vectors. Invokes
`sendVector()` on the Channel with this newly created Vector object, and
then again with the *time* and *thePath* Vectors.

Does the mirror image of `sendSelf()`.

Prints the string 'PathTimeSeries', the factor*cFactor*, and the time
increment *dT*. If *flag* is equal to $1.0$ *thePath* and *time* Vector
are also printed.


