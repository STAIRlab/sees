\
# EarthquakePattern 

```cpp
#include <domain/pattern/EarthquakePattern.h>
```
NEEDS MODIFICATION TO ALLOW MULTIPLE EARTHQUAKE PATTERNS, SO DON"T HAVE
TO SET R IN NODES EACH APPLYLOAD.

class EarthquakePattern: public LoadPattern\

TaggedObject\
MovableObject\
DomainComponent\
LoadPattern\

\
The EarthquakePattern class is an abstract class. An EarthquakePattern
is an object which adds earthquake loads to models. This abstract class
keeps track of the GroundMotion objects and implements the `applyLoad()`
method. It is up to the concrete subclasses to set the appropriate
values of *R* at each node in the model.

### Constructor

\
### Destructor

\
// Public Methods\

// Protected Methods\

\

\
The integers *tag* and *classTag* are passed to the LoadPattern classes
constructor.

\
Invokes the destructor on all GroundMotions added to the
Earthquakepattern. It then invokes the destructor on the array holding
pointers to the GroundMotion objects.

Obtains from each GroundMotion, the velocity and acceleration for the
time specified. These values are placed in two Vectors of size equal to
the number of GroundMotion objects. For each node in the Domain
`addInertiaLoadToUnbalance()` is invoked with the acceleration Vector
objects. SIMILAR OPERATION WITH VEL and ACCEL NEEDS TO BE INVOKED ON
ELEMENTS .. NEED TO MODIFY ELEMENT INTERFACE\

Adds the GroundMotion, *theMotion* to the list of GroundMotion objects.
