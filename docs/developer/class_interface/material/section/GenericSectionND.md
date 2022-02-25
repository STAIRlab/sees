\
# GenericSectionND 

```cpp
#include <material/section/GenericSectionND.h>
```

class GenericSectionND : public SectionForceDeformation\

TaggedObject\
MovableObject\
Material\
SectionForceDeformation\

\
GenericSectionND provides a wrapper around a NDMaterial so that any
NDMaterial may be used to model section response. The design of this
class follows the Object Adapter pattern in *Design Patterns* by Gamma
et al.

// Constructor\

// Destructor\

\
// Public Methods\

\

\

\

\

\

\

// Public Methods for Output\

\

\

Constructs a GenericSectionND whose unique integer tag among
SectionForceDeformation objects in the domain is given by *tag*. Obtains
a copy of the NDMaterial *m* via a call to `getCopy()`. The section code
is set to be *code*.

\
Invokes the destructor of the NDMaterial.

\
Sets the trial section deformation vector, $\esec$, to be *def*, then
invokes `setTrialStrain()` on the NDMaterial.

Returns the trial section deformation vector, $\esec$.

Sets the section resisting force, $\ssec$, to be the result of invoking
`getStress()` on the NDMaterial, then returns $\ssec$.

Returns the section resisting force, $\ssec$, from the previous trial
state.

Sets the section tangent stiffness matrix, $\ksec$, to be the result of
invoking `getTangent()` on the NDMaterial, then returns $\ksec$.

Returns the section tangent stiffness matrix, $\ksec$ from the previous
trial state.

Invokes `commitState()` on the NDMaterial and returns the result of that
invocation.

Invokes `revertToLastCommit()` on the NDMaterial and returns the result
of that invocation.

Invokes `revertToStart()` on the NDMaterial and returns the result of
that invocation.

Returns a pointer to a new instance of GenericSectionND, using the same
tag, NDMaterial reference, and code. It is up to the caller to ensure
that the destructor is invoked.

Returns the section ID code that indicates the type of response
quantities returned by this instance of GenericSectionND.

Returns the result of invoking `getOrder()` on the NDMaterial.

FILL IN.

FILL IN.

Prints to the stream *s* the object's *tag*, then invokes `Print()` on
the NDMaterial using the same values of *s* and *flag*.
