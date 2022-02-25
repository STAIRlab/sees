\
# SectionForceDeformation 

```cpp
#include <material/section/SectionForceDeformation.h>
```

class SectionForceDeformation : public Material\

TaggedObject\
MovableObject\
Material\

\
SectionForceDeformation provides the interface which all
SectionForceDeformation models must implement.

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

\

// Public Methods for Output\

\

\

To construct a SectionForceDeformation object whose unique integer tag
among SectionForceDeformation objects in the domain is given by *tag*,
and whose class identifier is given by *classTag*. These integers are
passed to the Material class constructor.

\
Does nothing.

\
To set the value of the trial section deformation vector, $\esec$ to be
*def*. To return $0$ if successful, a negative number if not.

To return the trial section deformation vector, $\esec$.

To return the section resisting forces, $\ssec$, at the current trial
state.

To return the section resisting forces, $\ssec$, from the previous trial
state.

To return the section tangent stiffness matrix, $\ksec$, at the current
trial state.

To return the section tangent stiffness matrix, $\ksec$, from the
previous trialstate.

Obtains the section tangent stiffness matrix, $\ksec$, and returns its
inverse, the section flexibility matrix, $\fsec$, via an explicit matrix
inversion. NOTE: The explicit matrix inversion provides default behavior
and may be overridden in subclasses to suit specific
SectionForceDeformation implementations.

Returns the section flexibility matrix, $\fsec$, from the previous trial
state. NOTE: This function provides default behavior and may be
overridden in subclasses to suit specific SectionForceDeformation
implementations.

To commit the section state. Returns $0$ if successful and a negative
number if not.

To revert the section to its last committed state. Returns $0$ if
successful and a negative number if not.

To revert the section to its initial state. Returns $0$ if successful
and a negative number if not.

To return a pointer to a new SectionForceDeformation object, which is a
copy of this instance. It is up to the caller to ensure that the
destructor is invoked.

To return the section ID code that indicates the ordering and type of
response quantities returned by the section. Lets the calling object
(e.g. an Element) know how to interpret the quantites returned by this
SectionForceDeformation model.

To return the number of response quantities provided by the section.

FILL IN.

FILL IN.

To print section information to the stream *s* based on the value of
*flag*.
