NEEDS FINISHING.

# UniformExcitation 

```cpp
#include <domain/pattern/UniformExcitation.h>
```

class UniformExcitation: public EarthquakeLoad\

TaggedObject\
MovableObject\
DomainComponent\
LoadPattern\
EarthquakePattern\

\
A UniformExcitation is an object which adds the loads imposed by a
single ground excitation to the model. For a UniformExcitation this
means that the *R* matrix at each node will have $1$ column and all
entries but those corresponding to the degree of freedom direction will
be set to $0$, the value for the degree of freedom direction will be set
to $1$.

// Constructor\

\
// Destructor\

\
// Public Methods\

\

\

\

The integers *LOAD_TAG_UniformExcitation* and *classTag* are passed to
the Load classes constructor.

\
Does nothing.

Checks to see if the number of nodes in the domain has changed, if there
has been a change it invokes `setNumColR(1)`{.cpp} and then *setR(theDof, 0,
1.0)* on each Node. It then invokes the base classes `applyLoad()`
method. THIS SHOULD BE CHANGED TO USE LATEST domainChanged().

Does nothing. NEEDS WORK.

Does nothing. NEEDS WORK.

Does nothing. NEEDS WORK.
