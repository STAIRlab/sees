


# SystemOfEqn 

```cpp
#include <system_of_eqn/SystemOfEqn.h>
```



class SystemOfEqn: public MovableObject



MovableObject



LinearSOE


EigenSOE



SystemOfEqn is an abstract class. A SystemOfEqn object is responsible
for storing the system of equations it represents. A Solver object,
which is associated with the SystemOfEqn object, is responsible for
performing the numerical operations to solve for the system of
equations.





















The integer *classTag* is provided to the constructor for the
MovableObject.




Does nothing. Declared to allow the subclass destructor to be called.




Invoked to cause the system of equation object to solve itself. To
return $0$ if successful, negative number if not.
