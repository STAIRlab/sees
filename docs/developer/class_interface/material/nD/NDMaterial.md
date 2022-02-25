INTERFACE MAY CHANGE IF MAKE MATERIAL MORE GENERAL.

# NDMaterial 

```cpp
#include <material/nD/NDMaterial.h>
```

class NDMaterial : public Material\

TaggedObject\
MovableObject\
Material\

\
NDMaterial is an abstract class. The NDMaterial class provides the
interface that all NDMaterial writers must provide when introducing new
NDMaterial subclasses. An NDMaterial object is responsible for keeping
track of stress, strain and the constitution for a particular point in
the domain.

// Constructor\

\
// Destructor\

\
// Public Methods\

\

\

\

\

To construct a NDMaterial whose unique integer among NDMaterials in the
domain is given by *tag*, and whose class identifier is given by
*classTag*. These integers are passed to the Material class
constructor.

\
Does nothing.

\
Sets the value of the trial strain vector, that value used by
`getStress()` and `getTangent()`, to be *strain*. To return $0$ if
successful and a negative number if not.

To return the material stress vector at the current trial strain.

To return the material tangent stiffness matrix at the current trial
strain.

To accept the current value of the trial strain vector as being on the
solution path. To return $0$ if successful, a negative number if not.

To cause the material to revert to its last committed state. To return
$0$ if successful, a negative number if not.

Invoked to cause the material to revert to its original state in its
undeformed configuration. To return $0$ if successful, a negative number
if not.

Returns a pointer to a new NDMaterial, which is an exact copy of this
instance. It is up to the caller to ensure that the destructor is
invoked.
