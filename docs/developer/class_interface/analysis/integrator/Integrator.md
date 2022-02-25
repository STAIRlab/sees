\
# Integrator 

```cpp
#include <analysis/integrator/Integrator.h>
```

class Integrator: public MovableObject;\

MovableObject\

\
The Integrator class is an abstract base class. Its purpose is to define
the interface common among all subclasses. An integrator method is
responsible for defining how the system of equations are set up (this it
does by specifying how the FE_Element and DOF_Group objects of the
analysis model construct the vectors and matrices asked of them by the
Analysis). It is also responsible for updating the response quantities
at the DOFs with the appropriate values; the values are determined from
the solution to the system of equations.

// Constructor\

\
// Destructor\

\
// Public Methods\

\

\

\
// Public Method added for Domain Decomposition\

\
// Public Method added for Output\

\

*classTag* is passed to the MovableObject classes constructor.

\
Does nothing. Provided so the subclass destructors will be invoked.

\
Is called by the Analysis object. Refer to the Analysis classes to see
when it is invoked. To return $0$ if successful, a negative number if
not. This base class returns $0$.

Called upon to determine the FE_Element *theEle*s matrix contribution to
the SystemOfEqn object. To return $0$ if successful, a negative number
otherwise.

Called upon to determine the DOF_Group *theDof*s matrix contribution to
the SystemOfEqn object. To return $0$ if successful, a negative number
otherwise.

Called upon to determine the FE_Element *theEle*s vector contribution to
the SystemOfEqn object. To return $0$ if successful, a negative number
otherwise.

Called upon to determine the DOF_Group *theDof*s vector contribution to
the SystemOfEqn object. To return $0$ if successful, a negative number
otherwise.

```{.cpp}
virtual int getLastResponse(Vector &result, const ID &id) =0;
```

Called upon to get the result quantities for the components specified in
the ID *id* and to place them in the Vector *result*. This is provided
for domain decomposition methods. To return $0$ if successful, a
negative number otherwise.

The Integrator is to send information to the stream based on the integer
*flag*.
