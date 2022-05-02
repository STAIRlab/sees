# PathSeries

```{.cpp}
#include <domain/pattern/PathSeries.h>
```

```{.cpp}
class PathSeries:
public
  DomainComponent
  MovableObject
  TimeSeries
```

The PathSeries class is a concrete subclass of TimeSeries. The
relationship between the pseudo time and the load factor follows a user
specified path. The path points are specified at constant time
intervals. For a pseudo time not at a path point, linear interpolation
is performed to determine the load factor. If the time specified is
beyond the last path point a load factor of $0.0$ will be returned.

// Constructors




// Destructor


// Public Methods






Used to construct a `PathSeries` when the data points are specified in a
Vector. The tag `TSERIES_TAG_PathSeries` is passed to the `TimeSeries` The
tag `TSERIES_TAG_PathSeries` is passed to the `TimeSeries` constructor. Sets
the constant factor used in the relation to `cFactor`. Constructs a new
Vector equal to `thePath` containing the data points which are specified
at `dT` time intervals. Prints a warning message if no space is
available for the Vector.

Used to construct a PathSeries when the data points are specified in a
file. The tag `TSERIES_TAG_PathSeries` is passed to the `TimeSeries`
constructor. Sets the constant factor used in the relation to `cFactor`.
Opens the file containing and reads in the data points into a new Vector
which are specified at `dT` time intervals. Prints a warning message if
no space is available for the Vector or if the file could not be found.

For a `FEM_ObjectBroker` to instantiate an empty `PathSeries`, `recvSelf()`
must be invoked on this object. The tag `TSERIES_TAG_PathSeries` is passed
to the TimeSeries constructor.


Invokes the destructor on the Vector created to hold the data points.

Determines the load factor based on the `pseudoTime` and the data
points. Returns $0.0$ if `pseudoTime` is greater than time of last data
point, otherwise returns a linear interpolation of the data points times
the factor `cFactor`.

Creates a vector of size `4` into which it places `cFactor`, `dT`, the
size of `thePath` and another database tag for `thaPath` Vector. Invokes
`sendVector()` on the Channel with this newly created Vector object, and
the `sendVEctor()` on `thePath`.

Does the mirror image of `sendSelf()`.

Prints the string 'PathSeries', the factor`cFactor`, and the time
increment `dT`. If `flag` is equal to $1.0$ the load path Vector is also
printed.

