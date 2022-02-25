PRESENTLY LITTLE IN THE INTERFACE .. THIS MAY CHANGE IF MAKE GENERAL i.e
1D, 2D and 3d PROBLEMS RETURN MATRICES AND VECTORS .. IF CHANGE,
INTERFACE FOR UniaxialMaterial MAY THEN CHANGE.

# Material 

```cpp
#include <material/Material.h>
```



class Material: public TaggedObject, public MovableObject



TaggedObject


MovableObject






Material is an abstract class. The Material class provides the interface
that all Material writers must provide when introducing new Material
subclasses. A Material object is responsible for keeping track of
stress, strain and the constitution for a particular point in the
domain.

// Constructor






// Destructor










To construct a Material whose unique integer among Materials in the
domain is given by *tag*, and whose class identifier is given by
*classTag*. These integers are passed to the TaggedObject and
MovableObject class constructors.




