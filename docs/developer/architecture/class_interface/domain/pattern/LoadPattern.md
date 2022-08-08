# LoadPattern

```cpp
#include <domain/pattern/LoadPattern.h>

class LoadPattern: public DomainComponent
```

```plantuml
abstract class ElementLoad 
abstract class TimeSeries
LoadPattern o- "one" TimeSeries 
LoadPattern o- ElementLoad 
LoadPattern o- NodalLoad 
LoadPattern o- SP_Constraint 
```

The `LoadPattern` class is a concrete base class. A `LoadPattern` is a
container class for Load and `SP_Constraint` objects. Each `LoadPattern`
object is associated with a `TimeSeries` object which, for a given pseudo
time, will return the appropriate load factor to be applied to the load
in the LoadPattern.

// Constructors



// Destructor


// Public Methods



The integer `tag` is passed to the `DomainComponent` classes constructor.
Creates three `ArrayOftaggedObjects` objects to store pointers to the
`NodalLoad`, `ElementalLoad` and `SP_Constraints` and three iters. If not
enough memory is available for these objects an error message is printed
and the program is terminated.

This is the constructor provided for subclasses to use. The integers
`tag` and `classTag` are passed to the DomainComponent classes
constructor.

Invokes the destructor on the `TimeSeries` object. Also invokes the
destructor on any objects created in the constructor for storage of the
pointers and for iters. It does not invoke the destructor on these
objects, the Domain object is responsible for doing this.


If a `TimeSeries` object is associated with the pattern, the destructor is
invoked on that `TimeSeries` object. It then sets the `TimeSeries` object
associated with the `LoadPattern` to `theSeries`.

If any loads or constraint objects exist in the `LoadPattern`, the
LoadPattern will invoke `setDomain()` on those objects. Finally invokes
the DomainComponent classes `setDomain()` method.

Adds the NodalLoad object pointed to by `theLoad` to the `LoadPattern`. If
the `LoadPattern` could add the pointer to its storage object for nodal
loads, it will invoke `setDomain()` and `setLoadPattern()` on the load
object if a Domain has been set.

Adds the ElementalLoad pointed to by `theLoad` to the LoadPattern. If
the LoadPattern could add the pointer to its storage object for
elemental loads, it will invoke `setDomain()` and `setLoadPattern()` on
the load object if a Domain has been set.

Adds the SP_Constraint pointed to by `theSp` to the LoadPattern. If the
LoadPattern could add the pointer to its storage object for single-point
constraints, it will invoke `setDomain()` and `setLoadPattern()` on the
constraint object if a Domain has been set.

Returns an iter to the nodal loads in the LoadPattern.

Returns an iter to the elemental loads in the LoadPattern.

Returns an iter to the single-point constraints in the LoadPattern.

To remove the nodal load whose identifier is given by `tag` from the
LoadPattern and sets the loads associated Domain object to `0`. Returns
a pointer to the load if successfully removed, otherwise `0` is
returned.

To remove the elemental load whose identifier is given by `tag` from the
LoadPattern and set the loads associated Domain object to `0`. Returns a
pointer to the load if successfully removed, otherwise `0` is returned.

To remove the single-point constraint whose identifier is given by `tag`
from the LoadPattern and st its associated Domain object to `0`. Returns
a pointer to the load if successfully removed, otherwise `0` is
returned.

To apply the load for the pseudo time `pseudoTime`. From the associated
TimeSeries object the LoadPattern will obtain a current load factor for
the pseudo time. It will then invoke `applyLoad(load factor)`{.cpp} on the
loads and `applyConstraint(load factor)`{.cpp} on the single-point constraints
in the LoadPattern. If `setLoadConstant()` has been invoked, the saved
load factor is used and no call is made to the TimeSeries object. If no
TimeSeries is associated with the object a load factor of `0.0` is
used.

Marks the `LoadPattern` as being constant. Subsequent calls to
`applyLoad()` will use the current load factor.

Creates a vector of size 4 into which it places the current load factor,
the mark indicating whether LoadPattern is constant, and the database
tag and class tag of the TimeSeris object. Invokes `sendVector()` on the
Channel object and `sendSelf()` on the TimeSeries object.

Does the mirror image of `sendSelf()`.

Invokes `Print(s, flag)`{.cpp} on the TimeSeries, NodalLoads, ElementalLoads
and SP_Constraints.

