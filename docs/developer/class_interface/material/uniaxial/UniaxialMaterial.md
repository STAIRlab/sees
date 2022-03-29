INTERFACE MAY CHANGE IF MAKE MATERIAL MORE GENERAL.

# UniaxialMaterial 

```cpp
#include <material/UniaxialMaterial.h>
```

class UniaxialMaterial: public Material\

TaggedObject\
MovableObject\
Material\

\
UniaxialMaterial is an abstract class. The UniaxialMaterial class
provides the interface that all UniaxialMaterial writers must provide
when introducing new UniaxialMaterial subclasses. A UniaxialMaterial
object is responsible for keeping track of stress, strain and the
constitution for a particular point in the domain.

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\

\

To construct a UniaxialMaterial whose unique integer among
UniaxialMaterials in the domain is given by *tag*, and whose class
identifier is given by *classTag*. These integers are passed to the
Material class constructor.

\
Does nothing.

\
Sets the value of the trial strain, that value used by `getStress()` and
`getTangent()`, to be *strain*. To return $0$ if successful, a negative
number if not.

To return the current value of stress for the trial strain.

To return the current value of the tangent for the trial strain.

To accept the current value of the trial strain as being on the solution
path. To return $0$ if successful, a negative number if not.

To cause the material to revert to the state at the last commit. To
return $0$ if successful, a negative number if not.

Invoked to cause the material to revert to its original state in its
undeformed configuration. To return $0$ if successful, a negative number
if not.

To return an exact copy of the material.
