# SectionForceDeformation 

```cpp
#include <material/section/SectionForceDeformation.h>

class SectionForceDeformation : public Material
```

  TaggedObject
  MovableObject
  Material


SectionForceDeformation provides the interface which all
SectionForceDeformation models must implement.

### Constructor and Destructor

:::{.admonition}
```cpp
SectionForceDeformation(int tag, int classTag);
```
:::

To construct a SectionForceDeformation object whose unique integer tag
among SectionForceDeformation objects in the domain is given by *tag*,
and whose class identifier is given by *classTag*. These integers are
passed to the Material class constructor.


:::{.admonition}
```cpp
~SectionForceDeformation()
```
:::
Does nothing.

### Public Methods

:::{.admonition}
```cpp
virtual int setTrialSectionDeformation (const Vector &def) = 0;
```
:::
To set the value of the trial section deformation vector, $\esec$ to be
`def`. To return $0$ if successful, a negative number if not.

:::{.admonition}
```cpp
virtual const Vector &getSectionDeformation (void) = 0;
```
:::
To return the trial section deformation vector, $\esec$.

:::{.admonition}
```cpp
virtual const Vector &getStressResultant (void) = 0;
```
:::
To return the section resisting forces, $\ssec$, at the current trial state.

:::{.admonition}
```cpp
virtual const Vector &getPrevStressResultant (void) = 0;
```
:::
To return the section resisting forces, $\ssec$, from the previous trial
state.

:::{.admonition}
```cpp
virtual const Matrix &getSectionTangent (void) = 0;
```
:::
To return the section tangent stiffness matrix, $\ksec$, at the current
trial state.

:::{.admonition}
```cpp
virtual const Matrix &getPrevSectionTangent (void) = 0;
```
:::
To return the section tangent stiffness matrix, $\ksec$, from the
previous trialstate.

:::{.admonition}
```cpp
virtual const Matrix &getSectionFlexibility (void);
```
:::
Obtains the section tangent stiffness matrix, $\ksec$, and returns its
inverse, the section flexibility matrix, $\fsec$, via an explicit matrix
inversion. NOTE: The explicit matrix inversion provides default behavior
and may be overridden in subclasses to suit specific
`SectionForceDeformation` implementations.

:::{.admonition}
```cpp
virtual const Matrix &getPrevSectionFlexibility (void);
```
:::
Returns the section flexibility matrix, $\fsec$, from the previous trial
state. NOTE: This function provides default behavior and may be
overridden in subclasses to suit specific SectionForceDeformation
implementations.

:::{.admonition}
```cpp
virtual int commitState (void) = 0;
```
:::
To commit the section state. Returns $0$ if successful and a negative
number if not.

:::{.admonition}
```cpp
virtual int revertToLastCommit (void) = 0;
```
:::
To revert the section to its last committed state. Returns $0$ if
successful and a negative number if not.

:::{.admonition}
```cpp
virtual int revertToStart (void) = 0;
```
:::
To revert the section to its initial state. Returns $0$ if successful
and a negative number if not.

:::{.admonition}
```cpp
virtual SectionForceDeformation *getCopy(void) = 0;
```
:::
To return a pointer to a new SectionForceDeformation object, which is a
copy of this instance. It is up to the caller to ensure that the
destructor is invoked.

:::{.admonition}
```cpp
virtual const ID &getType (void) = 0;
```
:::
To return the section ID code that indicates the ordering and type of
response quantities returned by the section. Lets the calling object
(e.g. an Element) know how to interpret the quantites returned by this
SectionForceDeformation model.

:::{.admonition}
```cpp
virtual int getOrder(void) = 0;
```
:::
To return the number of response quantities provided by the section.

### Output

:::{.admonition}
```cpp
int sendSelf(int commitTag, Channel &theChannel);
int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker &theBroker);
```
:::
The `sendSelf()`/`recvSelf()` methods are used in parallel processing
with OpenSeesSP and when using the `database` command.



:::{.admonition}
```cpp
void Print(OPS_Stream &s, int flag = 0) = 0;
```
:::
To print section information to the stream `s` based on the value of
`flag`.

