


# TaggedObject 

```cpp
#include <tagged/TaggedObject.h>
```



class TaggedObject











TaggedObject is used as a base class to represent all classes that may
have a integer identifier, a tag, to identify the object. It is used in
the framework as a base class for many classes, for example
DomainComponent and Vertex. The class is provided so that container
classes can be written to store objects and provide access to them. This
saves us rewriting container classes for each type of object. (templates
will be able to provide this functionality when they are provided with
all compilers).

// Constructor






// Destructor






// Public Methods










// Protected Methods







Constructs a TaggedObject with a tag given by *tag*. The tag of a
component is some unique means of identifying the component among like
components, i.e. the tag of a node would be its unique node number.




Does nothing. Provided so the concrete subclasses destructors will be
called.




Returns the tag associated with the object. This function is inlined for
performance.

A pure virtual function. The component is to output itself to the output
stream *s*. The integer *flag* can be used to select just what should be
output, by default $0$ is passed.

Invokes `Print(s)` on the TaggedObject *m*.




Sets the tag of the object to be *newTag*. It is provided so that
MovableObjects can set their tag in `recvSelf()`.
