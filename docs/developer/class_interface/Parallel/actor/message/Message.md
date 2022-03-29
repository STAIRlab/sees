\
# Message 

```cpp
#include <actor/message/Message.h>
```

class Message\

\

Messages are objects that can be sent between Channels. They are
provided to allow data of arbitrary length and type, e.g. structs, to be
sent between processes running on similar machine architectures. WARNING
Sending Messages between machines with different architectures can
result in erroniuos data being received. Each Message object keeps a
pointer to the data it represents and an integer outlining the data
size. There is no copy of the data kept by the Message.

### Constructors

\

\

### Destructor

\
// Public Member Functions\
;\

\

\
To construct an empty message.

To construct a message for sending/receiving an array containing *num*
doubles.

To construct a message for sending/receiving an array containing *num*
ints.

To construct a message for sending/receiving a string of *num*
characters or a struct.

\
Does nothing.

;\
A method which will put the data given by the character pointer
*theData* of size *endLoc -startLoc* into the data array pointed to by
the Message starting at location $startLoc$ in this array. Returns $0$
if successful; an error message is printed and a $-1$ is returned if
not. The routine `bcopy()` is used to copy the data.

```{.cpp}
virtual const char \*getData(void);
```

A method which returns a const char \* pointer to the messages data.

```{.cpp}
virtual int getSize(void);
```

A method to get the size of the array. The unit of size is that of a
character.
