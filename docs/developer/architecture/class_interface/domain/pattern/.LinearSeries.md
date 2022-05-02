# LinearSeries

```cpp
#include <domain/pattern/LinearSeries.h>

class LinearSeries:
public
  DomainComponent
  MovableObject
  TimeSeries
```

The LinearSeries class is a concrete subclass of TimeSeries. The
relationship between the pseudo time and the load factor is linear for
objects of this class.

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\
The tag `TSERIES_TAG_LinearSeries` is passed to the `TimeSeries`
constructor. Sets the constant factor used in the relation to
`cFactor`.


Does nothing.


Returns the product of `cFactor` and `pseudoTime`.

Creates a vector of size 1 into which it places `cFactor` and invokes
`sendVector()` on the Channel object.

Does the mirror image of `sendSelf()`.

Prints the string `'LinearSeries'` and the factor `cFactor`.
