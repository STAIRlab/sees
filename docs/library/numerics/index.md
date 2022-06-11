# Numeric Libraries

### Linear Equation Solvers
The following methods provide the solution of the linear system of equations $Ku = P$. Each solver is tailored to a specific matrix topology.

- [Profile SPD]() -- Direct profile solver for symmetric positive definite matrices
- [Band General]() -- Direct solver for banded unsymmetric matrices
- [Band SPD]() -- Direct solver for banded symmetric positive definite matrices
- [Sparse General]() -- Direct solver for unsymmetric sparse matrices
- [Sparse Symmetric]() -- Direct solver for symmetric sparse matrices
- [UmfPack General]() -- Direct UmfPack solver for unsymmetric matrices
- [Full General]() -- Direct solver for unsymmetric dense matrices
- [Conjugate Gradient]() -- Iterative solver using the preconditioned conjugate gradient method

### Eigenvalue Solvers
The following methods provide the solution of the generalized eigenvalue problem $Kv = MvL$

- [Symmetric Arpack]() -- Arpack solver for symmetric matrices
- [Band Arpack]() -- Arpack solver for banded matrices

### DOF Numberers
The numbering of the degrees of freedom in the domain is done by the following methods

- Plain -- Uses the numbering provided by the user
- RCM -- Renumbers the DOF to minimize the matrix band-width using the Reverse Cuthill-McKee algorithm

