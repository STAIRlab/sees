


# ModelBuilder 

```cpp
#include <modelbuilder/ModelBuilder.h>
```



class ModelBuilder;







The ModelBuilder class is an abstract base class. A subclass of
ModelBuilder is a class which creates the finite element discretization
of a structure: that is it discretizes the structure to be modeled into
Elements, Nodes, Constraints, etc. and adds these components to the
Domain.

// Constructor






// Destructor






// Public Methods






// Protected Methods







All models are associated with a single domain, this constructor sets up
the link between the model and the domain, setting its link to the
Domain object *theDomain*.




Does nothing.




The ModelBuilder will construct the Element, Node, Load and Constraint
objects and add them to the Domain object associated with the
ModelBuilder.




Returns a pointer to the Domain object passed in the constructor. This
method can be used in the subclasses to get a pointer the Domain object
to which to add the domain components.
