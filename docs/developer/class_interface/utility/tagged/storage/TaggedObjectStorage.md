\
# TaggedObjectStorage 

```cpp
#include <tagged/storage/TaggedObjectStorage.h>
```

class TaggedObjectStorage\

\

TaggedObjectStorage is used as a container object to store and provide
access to objects of type TaggedObject. Each TaggedObject object stored
in a TaggedObjectStorage object must have a unique integer tag to
distinguish it from other the other objects stored. The
TaggedObjectStorage class is an abstract base class, it just defines the
interface all concrete subclasses must provide. The interface defines
methods to add and to remove the components, and methods to obtain
access to the components.

// Constructor\

\
// Destructor\

\
// Pure Virtual Public Methods\

\

\

\

\

\

Does nothing.

\
Does nothing. Provided so that the concrete subclasses destructor will
be invoked. The subclasses destructor is NOT to delete the objects
stored in the object. `clearAll()` can be invoked by the programmer if
this is required.

\
To provide an indication to the container object that *newSize*
components are likely to be added. This is only a hint, it should be
acceptable for more or less objects than *newSize* to be added to the
container.

To add the object *newComponent* to the container. To return *true* if
the object was added to the container, *false* otherwise. The object
should not be added if another object with a similar tag already exists
in the container.

To remove the component whose tag is given by *tag* from the container.
To return a pointer to the removed object if successful, $0$ if not.

To return the number of components currently stored in the container.

To return a pointer to the TaggedObject whose identifier is given by
*tag*. If the object has not been added to the container $0$ is to be
returned.

To return an iter for iterating through the objects that have been added
to the container.

To return an empty copy of the container.

To remove all objects from the container and **to invoke the destructor
on these objects** if *invokeDestructor* is *true*.

To invoke `Print(s,flag)`{.cpp} on all objects which have been added to the
container.
