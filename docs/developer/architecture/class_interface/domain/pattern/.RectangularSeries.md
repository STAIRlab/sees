# RectangularSeries

```cpp
#include <domain/pattern/RectangularSeries.h>

class RectangularSeries: public DomainComponent
```

MovableObject\
TimeSeries\

\
The RectangularSeries class is a concrete subclass of TimeSeries. The
relationship between the pseudo time and the load factor is defined by
the simple relationship: factor $=$ cFactor when tStart $<=$ pseudo time
$<=$ tFinish, otherwise factor $=0.0$.

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\
The tag TSERIES_TAG_RectangularSeries is passed to the TimeSeries
constructor. Saves the values *tStart*, *tFinish* and *cfactor*.

\
Does nothing.

\
Returns cFactor if tStart $<=$ pseudo time $<=$ tFinish, otherwise
returns $0.0$.

Creates a vector of size 3 into which it places *tStart*, *tFinish* and
*cFactor*, and it then invokes `sendVector()` on the Channel object.

Does the mirror image of `sendSelf()`.

Prints the string 'RectangularSeries' and the values *tStart*, *tFinish*
and *factor*.
