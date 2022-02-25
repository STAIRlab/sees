


# FE_Datastore 

```cpp
#include <database/FE_Datastore.h>
```



class FE_Datastore: public ModelBuilder, public Channel



ModelBuilder


Channel






FE_Datastore is an abstract class. An FE_Datastore object is used in the
program to store/restore the geometry and state information in the
domain at particular instances. How, where and how the data is stored
depends on the implementation provided by the concrete subclasses.

// Constructor






// Destructor






// Public Methods















// Protected Methods










The Domain object *theDomain* is passed to the ModelBuilder constructor.
A pointer is kept to *theBroker* object.




Does nothing.




To return a unique integer identifier at each call. This identifier will
be used by the objects to store/retrieve their information to/from the
database.

Invoked to store the current state of the domain in the database. The
integer *commitTag* is used to identify the state for subsequent calls
to restore the information from the database. To return $0$ if
successful, a negative number if not.

In the implementation for the FE_Datastore class, the object first
invokes `validateBaseRelationsWrite()` on itself. If this method returns
$0$, the object then loops over all the components of the Domain object
invoking `sendSelf(commitTag, this)`{.cpp} on each of these objects. Returns
$0$ if successful, a negative number if not. For each domain component
that could not send itself a warning message is printed.

Invoked to restore the state of the domain from a database. The state of
the domain at the end of this call is to be the same as the state of the
domain when `commitState(commitTag)` was invoked. To return $0$ if
successful, a negative number if not.

In the implementation for the FE_Datastore class, the object first
invokes `validateBaseRelationsRead()` on itself. If this method returns
$0$, the object then loops over all the components of the Domain object
invoking `recvSelf(commitTag, this)`{.cpp} on each of these objects. Returns
$0$ if successful, a negative number if not. For each domain component
that could not send itself a warning message is printed.

This method is invoked before the information can be sent to the
database. It is required to ensure that:

1.  Each Node, Element, `SP_Constraint`, `MP_Constraint`, NodalLoad and
    ElementalLoad which is to save information in the database has a
    database tag.

2.  That the information in the base tables is up to date so that a
    later call to `validateBaseRelationsRead(commitTag)` will be
    successful.

To return $0$ if the base relations are up to date, to return $1$ if
they are up to date and the component data has been sent to the
database, and a negative number if the method fails.

This method is invoked before the information can be extracted from the
database. It is required to ensure that the Domain has the same type of
DomainComponent objects and that each of these has the same database tag
as when `validateBaseRealationsWrie(commitTag)` was invoked. To return
$0$ if the base relations are up to date, to return $1$ if they are up
to date and the component data has been received from the database, and
a negative number if the method fails.

Returns a pointer to *theBroker* object passed in the constructor.
