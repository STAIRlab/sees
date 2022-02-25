


# Solver 

```cpp
#include <system_of_eqn/Solver.h>
```



class Solver: public MovableObject



MovableObject






Solver is an abstract class. A Solver object is responsible for
performing the numerical operations on its associated SystemOfEqn
object.





















The integer *classTag* is passed to the MovableObject classes
constructor.




Does nothing. Provided so the subclasses destructor will be called.




Causes the solver to solve the system of equations. Returns $0$ if
successful , negative number if not; the actual value depending on the
type of Solver.
