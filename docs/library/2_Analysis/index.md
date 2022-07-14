# Analysis Capabilities

Linear equation solvers, time integration schemes, and solution algorithms are
the core of the OpenSees computational framework. The components of a solution
strategy are interchangeable, allowing analysts to find sets suited to their
particular problem.

### Eigenvalue Solvers
The following methods provide the solution of the generalized eigenvalue problem $Kv = MvL$

- [Symmetric Arpack]() -- Arpack solver for symmetric matrices
- [Band Arpack]() -- Arpack solver for banded matrices

