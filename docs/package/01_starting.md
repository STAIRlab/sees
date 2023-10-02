# Getting Started

A simulation with `opensees` is generally configured in the following steps:

1.  **Modeling**: This consists of defining a collection of mathematical
    abstractions and their relationships with the objective of representing
    some phenomenon. This generally includes creating
    `Element`, `Node`, `LoadPattern` and `Constraint` objects that define the
    model. 

2.  **Analysis**: Once a model is defined, the next step is to create
    an Analysis. Some common analysis routines are the following:

    - [Static Analysis]() Load or displacement controlled
    - [Spectral Decomposition]()
    - [Transient Direct Integration]()
    - [Transient Modal Integration]()
    - [Moment-Curvature Analysis]()
    - [Ultimate N-M Surface Analysis]()

    These routines are configured and refined in terms of analysis 
    abstractions which generally may include an `Integrator`, 
    `SolutionAlgorithm`, and `ConstraintHandler` strategy.

3.  **Post-processing**: Once the model and analysis have been
    defined, the user has the option of specifying what is to be
    monitored during the analysis. This, for example, could be the
    displacement history at a node or internal state of an element in a
    transient analysis or the entire state of the model at each step in
    the solution procedure. Several Recorder objects are created to
    store what the user wants to examine.

4.  **Runtime and Numerics**: When working on advanced problems, fine-grained
    control over details such as the analysis runtime, parallelization, and
    numeric strategies becomes important.

  -  *Numerics*: when the computational cost of an analysis
     becomes prohibitive, selecting the right numeric strategy can be important.
     Refinements typically consist of choosing an appropriate linear or eigenvalue 
     solver which appropriatly accounts for the structure of a linear system.
     Parallelization may also be considered.

