\
\#include $<$/actor/actor/MovableObject.h$>$\

class MovableObject\

\

MovableObject is an abstract class, i.e. no instances of MovableObject
should exist. MovableObjects are objects which are able to send/receive
themselves to/from Channel objects. With each movable object is
associated a unique class identifier, it is this id which will allow
object brokers in remote processes to create an object of the correct
type. In addition when databases are being used, each MovableObject will
have a unique database tag, it is this integer which will allow the
objects to retrieve their own data from the database.

// Constructor\

\

// Destructor\

\
// Public Methods\

\

\

\

The constructor sets the objects class identifier to *classTag*: this is
a unique id for each class of instantiable movable objects. The
identifier will allow an object broker to recognize the object type to
be instantiated. Sets the objects database tag to *dbTag*: this is a
unique id for identifying the object in a database.

The constructor sets the objects class identifier to *classTag* and sets
the objects database tag to *0*.

\

\
A method which returns the class id, *classTag*, provided in the
constructor.

```{.cpp}
int getDbTag(void) const;
```

A method which returns the database tag, *dbTag*, provided in the
constructor or last set in `setDbTag()`.

```{.cpp}
void setDbTag(int dbTag);
```

A method to set the database tag to be equal to *dbTag*.

```{.cpp}
virtual int sendSelf(int commitTag, Channel &theChannel) =0;
```

This is a pure virtual method, one must be written for each instantiable
subclass of MovableObject. Each object has to send the data needed to be
able to reproduce that object in a remote process. The object uses the
methods provided by *theChannel* object to send the data to another
channel at the remote actor, the address of the channel is set before
this method is called. An object of similar type at the remote actor is
invoked with a `receiveSelf()` to receive the data. Returns $0$ if
successful (successful in that the data got to the channel), or a $-1$
if no data was sent.
*virtual int recvSelf(int commitTag, Channel &theChannel,
FEM_ObjectBroker &theBroker) =0;*\
This is a pure virtual method, one must be written for each instantiable
subclass of MovableObject. Each object has to receive the data needed to
be able to recreate itself in the new process after it has been sent
through *theChannel*. If the object is an aggregation containing other
objects, new objects of the correct type can be constructed using
*theBroker*. To return $0$ if successful or a $-1$ if not.
