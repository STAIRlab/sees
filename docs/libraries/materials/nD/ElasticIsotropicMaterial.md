\
# ElasticIsotropicMaterial 

```cpp
#include <material/nD/ElasticIsotropicMaterial.h>
```

class ElasticIsotropicMaterial : public NDMaterial\

TaggedObject\
MovableObject\
Material\
NDMaterial\

\
ElasticIsotropicMaterial is an abstract class. It provides the interface
to which all elastic isotropic material implementations must conform. It
also serves as a prototype for all elastic isotropic material
implementations, as described by the Prototype pattern in *Design
Patterns* by Gamma et al.

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\

\

\
To construct an ElasticIsotropicMaterial whose unique integer tag among
NDMaterials in the domain is given by *tag*, and whose class tag is
given by *classTag*. These tags are passed to the NDMaterial class
constructor.

\
Does nothing.

\
Outputs an error indicating this method is a subclass responsibility.

Outputs an error indicating this method is a subclass responsibility.

Outputs an error indicating this method is a subclass responsibility.

Outputs an error indicating this method is a subclass responsibility.

Outputs an error indicating this method is a subclass responsibility.

Outputs an error indicating this method is a subclass responsibility.

Outputs an error indicating this method is a subclass responsibility.

Returns a specific implementation of an ElasticIsotropicMaterial by
switching on *type*. Outputs an error if *type* is not valid. This is
the prototype method.
