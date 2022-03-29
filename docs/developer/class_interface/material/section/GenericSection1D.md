\
# GenericSection1D 

```cpp
#include <material/section/GenericSection1D.h>
```

class GenericSection1D : public SectionForceDeformation\

TaggedObject\
MovableObject\
Material\
SectionForceDeformation\

\
GenericSection1D provides a wrapper around a UniaxialMaterial so that
any UniaxialMaterial may be used to model section response. The design
of this class follows the Object Adapter pattern in *Design Patterns* by
Gamma et al.

### Constructor

### Destructor

\
// Public Methods\

\

\

\

\

\

\

\

// Public Methods for Output\

\

\

Constructs a GenericSection1D whose unique integer tag among
SectionForceDeformation objects in the domain is given by *tag*. Obtains
a copy of the UniaxialMaterial *m* via a call to `getCopy()`. The
section code is set to be *code*.

\
Invokes the destructor of the UniaxialMaterial.

\
Sets the trial section deformation vector, $\esec$, to be *def*, then
invokes `setTrialStrain()` on the UniaxialMaterial.

Returns the trial section deformation vector, $\esec$.

Sets the section resisting force, $\ssec$, to be the result of invoking
`getStress()` on the UniaxialMaterial, then returns $\ssec$.

Returns the section resisting force, $\ssec$, from the previous trial
state.

Sets the section tangent stiffness matrix, $\ksec$, to be the result of
invoking `getTangent()` on the UniaxialMaterial, then returns $\ksec$.

Returns the section tangent stiffness matrix, $\ksec$ from the previous
trial state.

Sets the section flexibility matrix, $\fsec$, to be the inverse of the
result of invoking `getTangent()` on the UniaxialMaterial, then returns
$\fsec$. This function overrides the base class implementation.

Returns the section flexibility matrix, $\fsec$, from the previous trial
state.
This function overrides the base class implementation.

Invokes `commitState()` on the UniaxialMaterial and returns the result
of that invocation.

Invokes `revertToLastCommit()` on the UniaxialMaterial and returns the
result of that invocation.

Invokes `revertToStart()` on the UniaxialMaterial and returns the result
of that invocation.

Returns a pointer to a new instance of GenericSection1D, using the same
tag, UniaxialMaterial reference, and code. It is up to the caller to
ensure that the destructor is invoked.

Returns the section ID code that indicates the type of response quantity
returned by this instance of GenericSection1D.

Returns 1.

FILL IN.

FILL IN.

Prints to the stream *s* the object's *tag*, then invokes `Print()` on
the UniaxialMaterial using the same values of *s* and *flag*.
