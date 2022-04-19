\
# BidirectionalMaterial 

```cpp
#include <material/nD/BidirectionalMaterial.h>
```

class BidirectionalMaterial : public NDMaterial\

TaggedObject\
MovableObject\
Material\
NDMaterial\

\
BidirectionalMaterial is an implementation of NDMaterial.
BidirectionalMaterial is a two-dimensional elasto-plastic material model
with combined linear isotropic and kinematic hardening. The yield
surface is circular with a specified radius. A radial return map
algorithm is used in the state determination.

### Constructors

\

### Destructor

\
// Public Methods\

\

\

\

\

// Public Methods for Output\

\

\

Constructs a BidirectionalMaterial whose unique integer among
NDMaterials in the domain is given by *tag*. Sets the elastic modulus to
*E*, initial yield stress to *fy*, and isotropic and kinematic hardening
moduli to *Hiso* and *Hkin*, respectively. Sets all committed history
variables to $0.0$. The integers *tag* and ND_TAG_Bidirectional, defined
in  `<classTags.h>`, are passed to the NDMaterial constructor.

Constructs a BidirectionalMaterial with tag 0. All material parameters
and committed history variables are set to $0.0$. The integers 0 and
ND_TAG_Bidirectional, defined in  `<classTags.h>`, are passed to the
NDMaterial constructor.

\
Does nothing.

\
Sets the trial strain of this material to be *strain*. Returns 0.

Returns the current trial strain of this material.

Returns the current stress computed by the radial return mapping
algorithm. This is the 2d generalization of the 1d algorithm described
in Simo & Hughes (1998), Box $1.5$.

Returns the tangent consistent with the stress computed by the radial
return mapping algorithm in `getStress()`.

Sets the committed history variables to be their corresponding trial
values. Returns 0.

Does nothing. Returns 0.

Sets all committed history variables to $0.0$. Returns 0.

Returns a pointer to a new instance of BidirectionalMaterial with the
same tag, elastic modulus, initial yield stress, and hardening moduli.
Copies the committed history variables to the new object. It is up to
the caller to invoke the destructor.

Returns 0 if successful and a negative number if any of the send
operation fails.

Returns 0 if successful and a negative number if any of the receive
operation fails.

Prints the tag of this object and its elastic modulus, initial yield
stress, and hardening moduli to the stream *s*.
