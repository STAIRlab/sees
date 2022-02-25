\
# Analysis 

```cpp
#include <analysis/analysis/Analysis.h>
```

class Analysis;\

\

The Analysis class is an abstract base class. Each Analysis object will
be associated with a single Domain, the Domain upon which it will
perform the analysis operations. The base Analysis class holds a pointer
to this Domain and will return this pointer to subclasses.

// Constructors\

\
// Destructor\

\
// Pure Virtual Public Member Functions\

\

// Protected Method\

\

All analysis are associated with a single domain, this constructor sets
up the link between the analysis and the domain.

\
Does nothing. Provided so that the subclasses destructor will be
invoked.

\
Invoked to perform the analysis on the domain, this is a pure virtual
function, i.e. all subclasses or their descendents must implement this
routine. Returns 0 if successful; a negative integer if not; the value
depends on the particular analysis class.

Invoked to inform the analysis that the finite element model has
changed, for example when new elements have been added. It is also a
virtual function. To return $0$ if successful, a negative number if
not.

\
Returns a pointer to the domain that was passed in the constructor.
