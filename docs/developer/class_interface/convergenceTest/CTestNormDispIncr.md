


\#include $<\tilde{}$/convergenceTest/CTestNormDispIncr.h$>$



class CTestNormDispIncr: public ConvergenceTest



MovableObject


ConvergenceTest






A CTestNormDispIncr object is an object which can be used in an
algorithmic class to test if convergence has been achieved. The
CTestNormDispIncr class tests using the norm of the solution Vector of a
LinearSOE object and a user specified tolerance value.

































The integer *CLASS_TAGS_CTestNormDispIncr*, defined in
$<$classTags.h$>$, is passed to the ConvergenceTest constructor. Sets
the tolerance used in `test()` to be *tol*, the max number of iterations
to be performed to *maxNumIter* and the print flag used to determine
what, if anything, is printed on each test to *printFlag*.

To be used by the FEM_ObjectBroker object in parallel programs. The
integer *CLASS_TAGS_CTestNormDispIncr*, defined in $<$classTags.h$>$, is
passed to the ConvergenceTest constructor. Sets the tolerance used in
`test()` to be *0.0* and *maxNumIter* to be $0$. These will be set when
`recvSelf()` is invoked on the object.




Does nothing.




Sets the tolerance used in `test()` to be *newTol*.

It sets a pointer to *theAlgo*'s LinearSOE object. Returns $0$ if
successful, a $-1$ is returned and an error message printed if no
LinearSOE object has been set in *theAlgo*.

Sets an integer indicating the current number of iterations,
*currentNumIter* to $1$. Returns $0$ if successfull, an error message
and $-1$ are returned if no LinearSOE object has been set.

Returns currentNumIter if if the two norm of the LinearSOE objects X
Vector is less than the tolerance *tol*. If no LinearSOE has been set
$-2$ is returned. If the *currentNumIter* $>=$ *maxNumIter* an error
message is printed and $-2$ is returned. If none of these conditions is
met, the *currentnumIter* is incremented and $-1$ is returned. If the
print flag is $0$ nothing is printed to opserr during the method, if $1$
the current iteration and norm are printed to opserr, and if $2$ the
norm and number of iterations to convergence are printed to opserr.

Creates a Vector of size 3, puts the tolerance value *tol*, *numIncr*
and *printFlag* in this, and then invokes `sendVector()` on
*theChannel*. Returns $0$ if successful. A warning message is printed
and a negative number if the Channel object fails to send the Vector.

Creates a Vector of size 3, invokes `recvVector()` on *theChannel*, and
sets the values of *tol*, *numIncr* and *printFlag*. Returns $0$ if
successful. If the Channel object fails to receive the Vector, *tol* is
set to $1.0e-8$, *numIter* to $25$, a warning message is printed, and a
negative number returned.
