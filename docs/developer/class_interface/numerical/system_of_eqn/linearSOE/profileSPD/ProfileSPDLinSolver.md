\

\#include $<\tilde{ }$ProfileSPDLinSolver.h$>$\

class ProfileSPDLinSolver: public LinearSOESolver\

Solver\
LinearSOESolver\

\
ProfileSPDLinSolver is an abstract class. The ProfileSPDLinSolver class
provides access for each subclass to the ProfileSPDLinSOE object through
the pointer *theSOE*, which is a protected pointer.

### Constructor

\
### Destructor

\
// Public Methods\

\

The integer *classTag* is passed to the LinearSOESolver classes
constructor.

\
Does nothing, provided so the subclasses destructor will be called.

\
The method sets up the link between the ProfileSPDLinSOE object and the
ProfileSPDLinSolver, that it is sets the pointer the subclasses use.
