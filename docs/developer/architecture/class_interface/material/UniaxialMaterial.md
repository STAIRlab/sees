# UniaxialMaterial

```cpp
#include <material/UniaxialMaterial.h>

class UniaxialMaterial: public Material
```

`UniaxialMaterial` is an abstract class. The `UniaxialMaterial` class
provides the interface that all `UniaxialMaterial` writers must provide
when introducing new `UniaxialMaterial` subclasses. A `UniaxialMaterial`
object is responsible for keeping track of stress, strain and the
constitution for a particular point in the domain.

Implementations of the `UniaxialMaterial` interface are used in several
contexts within the OpenSees modeling framework. Due to their
simplicity, these models can define both stress-strain and
force-deformation relationships. It is up to the calling object, be it
an element object or another material object, to interpret the meaning
appropriately.


### Constructor and Destructor

:::{.admonition}
```cpp
UniaxialMaterial(int tag, int classTag);
```
:::

To construct a `UniaxialMaterial` whose unique integer among
UniaxialMaterials in the domain is given by *tag*, and whose class
identifier is given by *classTag*. These integers are passed to the
`Material` class constructor.

:::{.admonition}
```cpp
~UniaxialMaterial()
```
:::
Does nothing.


### Public Methods

:::{.admonition}
```cpp
virtual int setTrialStrain (double strain) = 0;
virtual int setTrialStrain (double strain, double strainRate =0) =0;
virtual int setTrialStrain (double strain, double temperature, double strainRate);
virtual int setTrial(double strain, double &stress, double &tangent, double strainRate = 0.0);
virtual int setTrial(double strain, double temperature, double &stress, 
                     double &tangent, double &thermalElongation, double strainRate = 0.0);
```
:::

Sets the value of the trial strain, that value used by `getStress()` and
`getTangent()`, to be `strain`. Return $0$ if successful, a negative
number if not.
The `setTrialStrain()` is the method called by an element when a new
strain in the material is to be set. Subsequent calls to `getTangent()`
and `getStress()` are to return the corresponding tangent and stress values
for that strain. `setTrialStrain()` is invoked as the solution algorithm
tries a number of trial solution steps as it goes from one commited
solution to the next on the solution path.


:::{.admonition}
```cpp
virtual double getStrain(void) = 0;
virtual double getStrainRate(void);
```
:::
`getStrain()` and `getStrainRate()` are to return the current strain
and strain rate of the material. The method `getStrain()` is
pure virtual, while `getStrainRate()` is only virtual; by default it
returns $0.0$, but may be overridden in subclasses if needed.

:::{.admonition}
```cpp
virtual double getStress(void) = 0;
```
:::
Return the trial value of stress for the trial strain.
The current stress is typically a function of the
current strain, $\varepsilon$, and the current strain rate,
$\dot{\varepsilon}$,

$$\sigma = \sigma(\varepsilon,\dot{\varepsilon}) \: .$$

:::{.admonition}
```cpp
virtual double getTangent(void) = 0;
```
:::
Return the trial value of the tangent for the trial strain.
The material tangent is the partial derivative of the
material stress with respect to the current strain,

$$E_t = \frac{\partial{\sigma}}{\partial{\varepsilon}} \: .$$

:::{.admonition}
```cpp
virtual double getDampTangent(void);
```
:::
damping tangent, which is the partial derivative of the current stress
with respect to the current strain rate,

$$\eta = \frac{\partial{\sigma}}{\partial{\dot{\varepsilon}}} \: .$$

By default, this method returns $0.0$, and it may be overridden in
subclasses of UniaxialMaterial where there is strain rate dependence.



:::{.admonition}
```cpp
virtual double getInitialTangent(void) = 0;
```
:::
Return the initial tangent.

:::{.admonition}
```cpp
virtual int commitState(void) = 0;
```
:::
Accept the current value of the trial strain as being on the solution
path. Return $0$ if successful, a negative number if not.
The `commitState()` method is invoked when a trial solution has been
determined to be on the solution path. It is the responsibility of the
material to be able to back track to that solution if a
`revertToLastCommit()` is invoked. This will happen if the algorithm fails
to find a solution on the solution path.

:::{.admonition}
```cpp
virtual int revertToLastCommit(void) = 0;
```
:::
To cause the material to revert to the state at the last commit. To
return $0$ if successful, a negative number if not.

:::{.admonition}
```cpp
virtual int revertToStart(void) = 0;
```
:::
Invoked to cause the material to revert to its original state in its
undeformed configuration. To return $0$ if successful, a negative number
if not.

:::{.admonition}
```cpp
virtual UniaxialMaterial *getCopy(void) = 0;
```
:::

Return an exact copy of the material. The `getCopy()` method is typically
invoked by a calling object (e.g. an `Element`, `Fiber`, or another `Material`
object) in its constructor. The material is to return a unique copy of itself
to the element. This way, different elements can use the same material type
with the same properties, with each element having it's own unique copy. A
pointer to the new object is returned by this function, and the calling object
is responsible for deleting this dynamically allocated memory.

:::{.admonition}
```cpp
virtual Response *setResponse(const char **argv, int argc,
                              OPS_Stream &theOutputStream);
virtual int getResponse (int responseID, Information &matInformation);
```
:::
The `setResponse()`/`getResponse()` methods typically do not have to be provided.
These are the methods called by a recorder after a `commit()`. If you are
happy with the existing responses for a `UniaxialMaterial` which responds
to `"stress"`, `"strain"`, `"tangent"`, `"stressANDstrain"` you do not have to
implement these methods. 

:::{.admonition}
```cpp
virtual int sendSelf(int commitTag, Channel &theChannel);
virtual int recvSelf(int commitTag, Channel &theChannel,
             FEM_ObjectBroker &theBroker);
```
:::
The `sendSelf()`/`recvSelf()` methods are used in parallel processing
with OpenSeesSP and when using the `database` command.



