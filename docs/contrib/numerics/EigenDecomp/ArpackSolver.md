# ArpackSolver

This is the solver that works on the ArpackSOE. It uses the LinearSOE
in the SOE to perform the solve() operation if required.
It uses the ARPACK library to perform the eigenvalue analysis.
ARPACK is an eigen analysis package which was developed by
R.B.Lehoucq, D.C.Sorensen and C.Yang at Rice University. ARPACK is a
collection of FORTRAN77 subroutines designed to solve large scale eigen
problems. ARPACK is capable of solving large scale non-Hermitian standard
and generalized eigen problems. When the matrix <b>K</b> is symmetric,
the method is a variant of the Lanczos process called Implicitly Restarted
Lanczos Method (IRLM).


It is based on previous work of Jun Peng(Stanford)

    Written: fmk
    Created: 05.09
