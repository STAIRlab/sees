# OpenSees Analysis Capabilities
Linear equation solvers, time integration schemes, and solution algorithms are the core of the OpenSees computational framework. The components of a solution strategy are interchangeable, allowing analysts to find sets suited to their particular problem. Outlined here are the available solution strategies. New parts of the solution strategy may be seamlessly plugged in to the existing framework.

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
The following methods provide the solution of the generalized eigenvalue problem Kv = MvL

- [Symmetric Arpack]() -- Arpack solver for symmetric matrices
- [Band Arpack]() -- Arpack solver for banded matrices

### DOF Numberers
The numbering of the degrees of freedom in the domain is done by the following methods

- Plain -- Uses the numbering provided by the user
- RCM -- Renumbers the DOF to minimize the matrix band-width using the Reverse Cuthill-McKee algorithm

### Static Integrators
Determing the next time step for an analysis is done by the following schemes

- [Load Control]() -- Specifies the incremental load factor to be applied to the loads in the domain
- [Displacement Control]() -- Specifies the incremental displacement at a specified DOF in the domain
- [Minimum Unbalanced Displacement Norm]() -- Specifies the incremental load factor such that the residual displacement norm in minimized
- [Arc Length]() -- Specifies the incremental arc-length of the load-displacement path

### Transient Integrators
Determing the next time step for an analysis including inertial effects is done by the following schemes

- [Newmark]() -- The two parameter time-stepping method developed by Newmark
- [HHT]() -- The three parameter Hilbert-Hughes-Taylor time-stepping method
- [Generalized Alpha]() -- Generalization of the HHT algorithm with improved numerical damping
- [Central Difference]() -- Approximates velocity and acceleration by centered finite differences of displacement

### Solution Algorithms
Iteration from the last time step to the current is done by the following methods

- [Linear]() -- Uses the solution at the first iteration and continues
- [Newton]() -- Uses the tangent at the current iteration to iterate to convergence
- [Modified Newton]() -- Uses the tangent at the first iteration to iterate to convergence

### Convergence Tests
Accepting the current state of the domain as being on the converged solution path is accomplished by the following tests

- [Norm Unbalance]() -- Specifies a tolerance on the norm of the unbalanced load at the current iteration
- [Norm Displacement Increment]() -- Specifies a tolerance on the norm of the displacement increments at the current iteration
- [Energy Increment]() -- Specifies a tolerance on the inner product of the unbalanced load and displacement increments at the current iteration

### Constraint Handlers
The constraints defined on the domain can be handled by the following methods

- [Plain]() -- Removes constrained degrees of freedom from the system of equations
- [Lagrange]() -- Uses the method of Lagrange multipliers to enforce constraints
- [Penalty]() -- Uses penalty numbers to enforce constraints
- [Transformation]() -- Performs a condensation of constrained degrees of freedom

