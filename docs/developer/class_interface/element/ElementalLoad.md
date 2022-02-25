


# ElementalLoad 

```cpp
#include <element/ElementalLoad.h>
```



class ElementalLoad: public Load



TaggedObject


MovableObject


DomainComponent


Load






ElementalLoad is an abstract class, i.e. no instances of ElementalLoad
will exist. The ElementalLoad class provides the interface that all
ElementalLoad writers must provide when introducing new ElementalLoad
classes.

// Constructors







// Destructor






// Public Methods







Provided to allow subclasses to construct an ElementalLoad object
associated with the Element whose unique identifier in the Domain will
be *elementTag*. The integers *tag* and and *classTags* are passed to
the Load constructor.

Provided so that a FEM_ObjectBroker can construct an object. $0$ and
*classTag* are passed to the Load classes constructor. The data for the
object is filled in when `recvSelf()` is invoked on the object.




Does nothing. Provided so that the ElementalLoad subclasses destructor
will be called.




Returns the integer *elementTag* passed in the constructor.
