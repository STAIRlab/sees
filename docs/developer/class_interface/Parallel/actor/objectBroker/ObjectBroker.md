\

\#include $<$ObjectBroker.h$>$\

class ObjectBroker\

\

ObjectBroker is an abstract class, i.e. no instances of ObjectBroker
should exist. ObjectBrokers are objects in remote processes which create
new objects in the remote process. It has one method


\

\


```{.cpp}
virtual MovableObject \*getNewObject(Channel &channel) =0;
```

This method returns a pointer to an object of the type whose class type
is given by the integer class ID value that is waiting at the Channel.
The method must first instantiate the correct type of object, it then
can invoke `recv(channel)` on this object. To get from a pointer of
MovableObject to one of its descendents type casting must be used.

