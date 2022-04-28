


\#include $<\tilde{}$/convergenceTest/ConvergenceTest.h$>$



class ConvergenceTest: public MovableObject



MovableObject






A ConvergenceTest object is an object which can be used in an
algorithmic class to test if convergence has been achieved for an
iteration. The ConvergenceTest class is an abstract class, defining the
interface that all subclasses must provide.

























The integer *classTag* is passed to the MovableObject constructor.




Does nothing.




To set the corresponding EquiSolnAlgo class.

To return a postive number if the convergence criteria defined for the
object has been satisfied, the positibe number equal to the number of
times since *start* that `test()` has been invoked. Otherwise a negative
number is to be returned. A *-2* is returned if the test fails to meet
the criteria and no more tests are to be performed due to limits set,
i.e. the maximum number of iterations, otherwise a *-1* is to be
returned.

This is invoked at the start of each iteration. To return *0* if
sucessfull, i.e that testing can proceed, a negative number if not.
