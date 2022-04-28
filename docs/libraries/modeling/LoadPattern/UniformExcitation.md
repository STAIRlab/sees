# UniformExcitation 

```cpp
#include <domain/pattern/UniformExcitation.h>

class UniformExcitation: public EarthquakeLoad
```

  TaggedObject\
  MovableObject\
  DomainComponent\
  LoadPattern\
  EarthquakePattern\


A UniformExcitation is an object which adds the loads imposed by a
single ground excitation to the model. For a UniformExcitation this
means that the *R* matrix at each node will have $1$ column and all
entries but those corresponding to the degree of freedom direction will
be set to $0$, the value for the degree of freedom direction will be set
to $1$.
