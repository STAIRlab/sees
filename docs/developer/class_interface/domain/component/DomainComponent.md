\
# DomainComponent 

```cpp
#include <domain/component/DomainComponent.h>
```

class DomainComponent\

TaggedObject\
MovableObject\

Element\
Node\
NodalLoad\
ElementalLoad\
SP_Constraint\
MP_Constraint\

The DomainComponent class is an abstract class, example subclasses
include Element, Node, `SP_Constraint`, `MP_Constraint`, NodalLoad,
ElementalLoad. Each object of these types is a component of an enclosing
Domain object. The DomainComponent class provides methods to set and
retrieve a pointer to the enclosing Domain object.

// Constructor\

\
// Destructor\

\
// Public Methods\

\

\

Constructs a DomainComponent with a tag given by *tag*, whose class tag
is given by *classTag*. The tag of a component is some unique means of
identifying the component among like components, i.e. the tag of a node
would be its unique node number. The *classTag* is a means of
identifying the class of the object. No domain is associated with the
object. The integer *tag* is passed to the TaggedObject constructor and
the integer *classTag* is passed to the MovableObject constructor.

\
Does nothing. Provided so subclasses destructor's will always be
called.

\
Sets the encompassing domain of the component to that given by
*theDomain*. This method is invoked by *theDomain* when the component is
being added to the domain, in an *addDomain..* invocation (see interface
for Domain).

Returns a pointer to the Domain to which the component was added, or $0$
if the `setDomain()` command was never called on the object.

To cause the object to display itself using *theRenderer*. The integer
*displayMode* is used to indicate what is to be displayed and the float
*fact* is used to factor the nodal displacements. To return $0$ if
successful, a negative number if not. This base class simply returns
$0$. Its up to the subclasses to override this method if the objects are
to be rendered.
