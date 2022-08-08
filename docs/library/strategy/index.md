# Numeric Libraries

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

- [Plain](Constraint/Plain) -- Removes constrained degrees of freedom from the system of equations
- [Lagrange](Constraint/Lagrange) -- Uses the method of Lagrange multipliers to enforce constraints
- [Penalty](Constraint/Penalty) -- Uses penalty numbers to enforce constraints
- [Transformation](Constraint/Transformation) -- Performs a condensation of constrained degrees of freedom

