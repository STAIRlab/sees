
# Channel 

```cpp
#include <actor/channel/Channel.h>
```

class Channel\

\

Channel is an abstract class, i.e. no instances of Channel should exist.
A Channel is a point of communication in a program, a mailbox to/from
which data enters/leaves a program. Channels are objects through which
the objects in the current processes address space can interact with
objects in another processes address space. A channel in one process
space is associated with a channel in the address space of another
process space. The interaction is in the form of data sent between the
two processes along the connection line.
### Constructor

\
### Destructor

\
// Public Methods\

\

\

\

\

\

\

\

\

\
Does nothing.

\
Does nothing. Provided so that a subclasses destructor will be invoked.

\
When creating remote actors the channels created in the actor space need
to know how to contact the shadows channels. This information is
provided in the string returned from this method. It is used by the
machine broker when starting the remote process. It places this
information as the last arguments to the program.

A method invoked in the local address space by a shadow object. The
method is to be invoked concurrently with a `setUpShadow()` invocation
on a channel object in all the remote actor processes.

```{.cpp}
virtual int setUpActor(void) =0;
```

A method invoked in the remote address space by the actor. The method is
invoked concurrently with a corresponding `setUpShadow()` invocation on
a channel in a local actor process by the shadow object that created the
running actor process. If the method fails returns a negative number.
For actors with only one Channel this should cause the termination of
the actor.

```{.cpp}
virtual int setNextAddress(ChannelAddress &theNextAddress) =0;
```

A method invoked to set specify the next address that the next messages
to be sent if `sendMessage()` or received if `recvMessage()` is invoked
with a null pointer.

To return the next available database tag, must be an integer value
greater than $0$, $0$ is used my the objects to check if they have yet
been assigned a database tag. The method defined for the Channel base
class always returns $0$, only database channel objects need worry about
assigning unique integer values.

To send the object *theObject* and the commit tag *commitTag* to a
remote Channel whose address is given by *theAddress*. If *theAddress*
is $0$, the Channel sends to the Channel with the address last set in a
*send..()*, *recv..()*, or `setNextAddress()` operation. To return $0$
if successful, a negative number if not.

To receive the object *theObject* with the commit tag *commitTag* from a
remote Channel whose address is given by *theAddress*. If *theAddress*
is $0$, the Channel receives from the Channel with the address last set
in a *send..()*, *recv..()*, or `setNextAddress()` operation. To return
$0$ if successful, a negative number if not.

A method which is invoked to send the data in the Message object
*theMessage* to another Channel object. The object will obtain the data
and size of the data to be sent by invoking `getData()` and `getSize()`
on *theMessage*. The channel object is then responsible for sending that
data to the remote channel address given by *theAddress*. If
*theAddress* is $0$, the Channel sends to the Channel with the address
last set in a *send..()*, *recv..()*, or `setNextAddress()` operation.
To return $0$ if successful, a negative number if not.

A method which is invoked to send the data in the Message object
*theMessage* to another Channel object. The object will obtain the the
size of the data that is being received by invoking `getSize()` on
*theMessage*. The channel object is then responsible for receiving that
amount of data from the channel whose address is given by *theAddress*.
If *theAddress* is $0$, the Channel receives from the Channel with the
address last set in a *send..()*, *recv..()*, or `setNextAddress()`
operation. To return $0$ if successful, a negative number if not.

A method for sending a Matrix *theMatrix* to a remote Channel, whose
address is given by *theAddress*, with the integer identifiers *dbTag*
and *commitTag*. If *theAddress* is $0$, the Channel sends to the
Channel with the address last set in a *send..()*, *recv..()*, or
`setNextAddress()` operation. To return $0$ if successful, a negative
number if not.

A method for receiving a Matrix *theMatrix* from a remote Channel, whose
address is given by *theAddress*, with the integer identifiers *dbTag*
and *commitTag*. If *theAddress* is $0$, the Channel receives from the
Channel at the address last set in a *send..()*, *recv..()*, or
`setNextAddress()` operation. To return $0$ if successful, a negative
number if not.

A method for sending a Vector *theVector* to a remote Channel, whose
address is given by *theAddress*, with the integer identifiers *dbTag*
and *commitTag*. If *theAddress* is $0$, the Channel sends to the
Channel with the address last set in a *send..()*, *recv..()*, or
`setNextAddress()` operation. To return $0$ if successful, a negative
number if not.

A method for receiving a Vector *theVector* from a remote Channel, whose
address is given by *theAddress*, with the integer identifiers *dbTag*
and *commitTag*. If *theAddress* is $0$, the Channel receives from the
Channel at the address last set in a *send..()*, *recv..()*, or
`setNextAddress()` operation. To return $0$ if successful, a negative
number if not.

A method for sending a ID *theID* to a remote Channel, whose address is
given by *theAddress*, with the integer identifiers *dbTag* and
*commitTag*. If *theAddress* is $0$, the Channel sends to the Channel
with the address last set in a *send..()*, *recv..()*, or
`setNextAddress()` operation. To return $0$ if successful, a negative
number if not.

A method for receiving a ID *theID* from a remote Channel, whose address
is given by *theAddress*, with the integer identifiers *dbTag* and
*commitTag*. If *theAddress* is $0$, the Channel receives from the
Channel at the address last set in a *send..()*, *recv..()*, or
`setNextAddress()` operation. To return $0$ if successful, a negative
number if not.
