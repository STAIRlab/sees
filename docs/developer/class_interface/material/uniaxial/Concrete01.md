UNDER CONSTRUCTION.

# Concrete01 

```cpp
#include <material/Concrete01.h>
```

class Concrete01: public MaterialModel\

TaggedObject\
MovableObject\
MaterialModel\
UniaxialMaterial\

\
Provides a uniaxial Kent-Scott-Park concrete model with linear
unloading/reloading according to the work of Karsan-Jirsa and no
strength in tension. The model contains a compressive strength of fpc, a
strain at the compressive strength of epsc0, a crushing strength of
fpcu, and a strain at the crushing strength of epscu. Compressive
concrete parameters should be input as negative numeric values for this
model to behave properly. Specification of minimum and maximum failure
strains through the -min and -max switches is optional. The argument
matTag is used to uniquely identify the material object among material
objects in the BasicBuilder object.

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

