# Analysis Capabilities
Linear equation solvers, time integration schemes, and solution algorithms are the core of the OpenSees computational framework. The components of a solution strategy are interchangeable, allowing analysts to find sets suited to their particular problem. Outlined here are the available solution strategies. New parts of the solution strategy may be seamlessly plugged in to the existing framework.

### Static Integrators
Determing the next time step for an analysis is done by the following schemes

- [Load Control]() -- Specifies the incremental load factor to be applied to the loads in the domain
- [Displacement Control]() -- Specifies the incremental displacement at a specified DOF in the domain
- [Minimum Unbalanced Displacement Norm](StaticIntegrator/) -- Specifies the incremental load factor such that the residual displacement norm in minimized
- [Arc Length](StaticIntegrator/ArcLength1) -- Specifies the incremental arc-length of the load-displacement path

### Transient Integrators
Determing the next time step for an analysis including inertial effects is done by the following schemes

- [Newmark](TransientIntegrator/Newmark) -- The two parameter time-stepping method developed by Newmark
- [HHT](TransientIntegrator/HHT) -- The three parameter Hilbert-Hughes-Taylor time-stepping method
- [Generalized Alpha](TransientIntegrator/GeneralizedAlpha) -- Generalization of the HHT algorithm with improved numerical damping
- [Central Difference]() -- Approximates velocity and acceleration by centered finite differences of displacement


### Eigenvalue Solvers
The following methods provide the solution of the generalized eigenvalue problem $Kv = MvL$

- [Symmetric Arpack]() -- Arpack solver for symmetric matrices
- [Band Arpack]() -- Arpack solver for banded matrices

