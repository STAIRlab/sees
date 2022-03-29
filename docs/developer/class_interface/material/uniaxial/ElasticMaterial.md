\
# ElasticMaterial 

```cpp
#include <material/ElasticMaterial.h>
```

class ElasticMaterial: public MaterialModel\

TaggedObject\
MovableObject\
MaterialModel\
UniaxialMaterial\

\
ElasticMaterial provides the abstraction of an elastic uniaxial
material, i.e. the stress-strain relationship is given by the linear
equation $\sigma = E * \epsilon$.

### Constructor

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

To construct an ElasticMaterial with an integer identifier *tag*, an
elastic tangent modulus of $E$ and a current strain $\epsilon$ of $0.0$.
The integers *tag* and MAT_TAG_ElasticMaterial, defined in
 `<classTags.h>`, are passed to the UniaxialMaterial classes
constructor.

\
Does nothing.

\
Sets the value of the trial strain, $\epsilon$ to be *strain*. Returns
$0$.

Returns the product of $E * \epsilon$, where $\epsilon$ is the current
trial strain.

Returns the value of $E$ passed in the constructor.

Returns $0$.

Returns $0$.

Returns $0$.

returns a pointer to a new ElasticMaterial object, constructed using the
same values of *tag* and $E$. It is up to the caller to ensure that the
destructor is invoked.

Creates a Vector of size $2$ into which it places *tag* and *E*. Invokes
`sendVector()` on *theChannel* using the ElasticMaterialObjects *dbTag*,
the integer *commitTag* and the Vector as arguments. Returns $0$ if
successful, a warning message and a negative number are returned if the
Channel object fails to send the Vector.

Creates a Vector of size $2$. Invokes `recvVector()` on *theChannel*
using the ElasticMaterialObjects *dbTag*, the integer *commitTag* and
the Vector as arguments. Using the data in the Vector to set it's *tag*
and $E$. Returns $0$ if successful, a warning message is printed, *tag*
and $E$ are set to $0.0$, and a negative number is returned if the
Channel object fails to receive the Vector.

Prints to the stream *s* the objects *tag* and $E$ values.
