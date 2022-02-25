UNDER CONSTRUCTION.

# Steel01 

```cpp
#include <material/Steel01.h>
```

class Steel01 : public MaterialModel\

TaggedObject\
MovableObject\
MaterialModel\
UniaxialMaterial\

\
Steel01 provides the abstraction of a bilinear steel model with
isotropic hardening. The model contains a yield strength of fy, an
initial elastic tangent of E0, and a hardening ratio of b. The optional
parameters a1, a2, a3, and a4 control the amount of isotropic hardening
(default values are provided). Specification of minimum and maximum
failure strains through the -min and -max switches is optional and must
appear after the specification of the hardening parameters, if present.
The argument matTag is used to uniquely identify the material object
among material objects in the BasicBuilder object.


// Constructor\

\
// Destructor\

\
// Public Methods\

\

\

\

\
// Public Methods for Output\

\

// Private Methods\

\

\

\

Does nothing.

\
