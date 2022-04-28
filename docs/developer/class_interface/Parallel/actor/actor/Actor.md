
# Actor 

```cpp
#include <actor/actor/Actor.h>
```

class Actor\

\

Actor is meant as an abstract class, i.e. no instances of Actor should
exist. An actor is associated with a shadow object. The shadow acts like
a normal object in the users address space, data and processing that is
done by the shadow may be stored and processed in a remote process, the
actor resides in this remote address space. The actor and the shadow
both have a channel, a communication port. This allows the two to
communicate with each other.

### Constructor

\
### Destructor

\
// Public Methods for Processing Functions\

\

\
// Public Methods for Sending/Receiving Objects\

\

\

\

\

\

\

\

This is called by the remote process upon initialization to construct
the local actor object. It is used to create an Actor object in that
remote address space which will communicate with objects in other
processes through a channel object, *theChannel* and which uses
*theBroker* to receive movable objects sent from other processes. The
subclass will be able to add *numMethods* actor methods using
`addMethod()` call.
The base classes constructor invokes `setUpActor()` on *theChannel*
object. It then sets the Address of the remote shadow object which
created the actor process by invoking `getLastSendersAddress()` on
*theChannel*.

\
Provided so subclass destructor will be called.

\
A method to add as a function to the actor object the function *fp*,
this function is identified by the *tag* value. This function will be
invoked by the actor on invocation of `processMethod()` with *tag* as
the argument. The object checks to see that the *tag* has not been used
previously. If it has not and the number of functions so far added is
less than *numActorMethods* the function is added and $0$ is returned,
otherwise a $-1$ (if *tag* was already used) or $-2$ (if
*numActorMethods* already added) or a $-3$ (if running out of space) is
returned to indicate the function was not added.

```{.cpp}
virtual int getMethod();
```

A method which returns the next integer value sitting in the actors
channel. This int value corresponds to the *tag* of the next method that
the shadow object wants the actor to perform. If an error occurs $-1$
will be returned.

```{.cpp}
virtual int processMethod(int tag);
```

This causes the actor object to invoke the function that was added to
the actor with the *tag* identifier. If no method with *tag* exists a
$-1$ is returned.
*virtual int sendObject(MovableObject &theObject, ChannelAddress
\*theAddress =0);*\
A method which will send *theObject* through the actors channel either
to the address given by *theAddress* or to the address of the shadow
object that created the actor if no address is specified.

Returns the result of invoking *sendObj(0,
theObject,theBroker,theAddress)* on the actors channel object if an
address is specified, otherwise the result of invoking
*sendObj(theMessage,theBroker,this-\>getShadowAdressPtr())* on the
actors channel object is returned.
*virtual int recvObject(MovableObject &theObject, ChannelAddress
\*theAddress =0);*\
A method which will receive *theObject* from the actors channel either
from the address given by *theAddress* or from the address of the shadow
object that created the actor if no address is specified.

Returns the result of invoking *recvObj(0,
theObject,theBroker,theAddress)* on the actors channel object if an
address is specified, otherwise the result of invoking
*recvObj(theMessage,theBroker,this-\>getShadowAdressPtr())* on the
actors channel object is returned.
*virtual int sendMessage(Message &theMessage, ChannelAddress
\*theAddress =0);*\
A method which will send the data in the message *theMessage* through
the actors channel either to the address given by *theAddress* or to the
address of the shadow object that created the actor if no address is
specified.

Returns the result of invoking `sendMsg(0,0,theMessage,theAddress)`{.cpp} on
the actors channel object if an address is specified, otherwise the
result of invoking `sendMsg(theMessage,this-\>getShadowAdressPtr())`{.cpp} on
the actors channel object is returned.

```{.cpp}
virtual int recvMessage(Message &theMessage);
```

A method which will receive the data in the message *theMessage* from
the actors channel either from the address given by *theAddress* or from
the address of the shadow object that created the actor if no address is
specified.

Returns the result of invoking `recvMsg(0,0,theMessage,theAddress)`{.cpp} on
the actors channel object if an address is specified, otherwise the
result of invoking *recvMsg(0,0,theMessage,this-\>getShadowAdressPtr())*
on the actors channel object is returned.
*virtual int sendMatrix(Matrix &theMatrix, ChannelAddress \*theAddress
=0);*\
A method which will send *theMatrix* through the actors channel either
to the address given by *theAddress* or to the address of the shadow
object that created the actor if no address is specified.

Returns the result of invoking `sendMatrix(0,0,theMatrix,theAddress)`{.cpp} on
the actors channel object if an address is specified, otherwise the
result of invoking
*sendMatrix(0,0,theMatrix,this-\>getShadowAdressPtr())* on the actors
channel object is returned.

```{.cpp}
virtual int recvMatrix(Matrix &theMatrix);
```

A method which will receive *theMatrix* from the actors channel either
from the address given by *theAddress* or from the address of the shadow
object that created the actor if no address is specified.

Returns the result of invoking `recvMatrix(0,0,theMatrix,theAddress)`{.cpp} on
the actors channel object if an address is specified, otherwise the
result of invoking
*recvMatrix(0,0,theMatrix,this-\>getShadowAdressPtr())* on the actors
channel object is returned.
*virtual int sendVector(Vector &theVector, ChannelAddress \*theAddress
=0);*\
A method which will send *theVector* through the actors channel either
to the address given by *theAddress* or to the address of the shadow
object that created the actor if no address is specified.

Returns the result of invoking `sendVector(0,0,theVector,theAddress)`{.cpp} on
the actors channel object if an address is specified, otherwise the
result of invoking
*sendVector(0,0,theVector,this-\>getShadowAdressPtr())* on the actors
channel object is returned.

```{.cpp}
virtual int recvVector(Vector &theVector);
```

A method which will receive *theVector* from the actors channel either
from the address given by *theAddress* or from the address of the shadow
object that created the actor if no address is specified.

Returns the result of invoking `recvVector(0,0,theVector,theAddress)`{.cpp} on
the actors channel object if an address is specified, otherwise the
result of invoking
*recvVector(0,0,theVector,this-\>getShadowAdressPtr())* on the actors
channel object is returned.

```{.cpp}
virtual int sendID(ID &theID, ChannelAddress \*theAddress =0);
```

A method which will send *theID* through the actors channel either to
the address given by *theAddress* or to the address of the shadow object
that created the actor if no address is specified.

Returns the result of invoking `sendID(0,0,theID,theAddress)`{.cpp} on the
actors channel object if an address is specified, otherwise the result
of invoking `sendID(0,0,theID,this-\>getShadowAdressPtr())`{.cpp} on the
actors channel object is returned.

```{.cpp}
virtual int recvID(ID &theID);
```

A method which will receive *theID* from the actors channel either from
the address given by *theAddress* or from the address of the shadow
object that created the actor if no address is specified.

Returns the result of invoking `recvID(0,0,theID,theAddress)`{.cpp} on the
actors channel object if an address is specified, otherwise the result
of invoking `recvID(0,0,theID,this-\>getShadowAdressPtr())`{.cpp} on the
actors channel object is returned.

```{.cpp}
void Channel \*getChannelPtr(void) const;
```

A method which returns a pointer to the channel passed in the
constructor.

```{.cpp}
void FEM_ObjectBroker \*getObjectBrokerPtr(void) const;
```

A method which returns a pointer to the FEM_ObjectBroker passed in the
constructor.

```{.cpp}
void ChannelAddress \*getChannelAddressPtr(void) const;
```

A method which returns a pointer to the channel address for the shadow
object that created the actor.
