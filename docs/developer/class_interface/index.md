
# Class Interface Specification

This document outlines the class interfaces currently provided by G3.
The main categories of classes are:

1.  Matrix Classes: These include the classes Matrix, Vector and ID
    (integer array). These classes are used in the framework for passing
    information between objects in a safe manner, and for small scale
    numerical calculations in element formulation.

2.  [Domain Classes](domain): These classes describe the finite element model and
    store the results of an analysis on the model. The classes include
    `Domain`, `Element`, `Node`, Load, `SP_Constraint`, `MP_Constraint`, and their
    subclasses.

3.  [Analysis Classes](analysis): These classes perform the analysis of the finite
    element model. The classes include the `Analysis`, `ConstraintHandler`,
    `DOF_Numberer`, `SolutionAlgorithm`, `Integrator`, `FE_Element`, `DOF_Group`
    and `AnalysisModel` classes, and their subclasses.

<!--
4.  Modeling Classes: These include the abstract class `ModelBuilder`, and
    concrete subclasses of this class. An analyst will interact with a
    ModelBuilder object, to create the Element, Node, Load and
    Constraint objects that define the model.
-->

5.  Numerical Classes: These include the abstract `SystemOfEquation` and
    `Solver` classes, and subclasses of these classes. These classes are
    provided for the solving of large scale systems of linear and
    eigenvalue equations.

6.  Data Storage These are classes used to store data. There are two
    abstract classes `TaggedObjectStorage` and `FE_Datastore`. Objects of
    type `TaggedObjectStorage` are used as containers to store and provide
    access to the `TaggedObjects` in memory during program execution.
    `FE_Datastore` objects are used to store/retrieve information from
    databases, containers which can permanently hold program data.

7.  Visualization Classes These are classes used to generate images of
    the model for the analyst. These classes include `Renderer`, `ColorMap`,
    and their subclasses.

8.  Graph Classes These are classes used to provide information about
    nodal and elemental connectivity and sparsity of systems of
    equations. The classes include `Graph`, `Vertex`, `GraphNumberer`,
    `GraphPartitioner`, and their subclasses. There is no `Edge` class
    provided at present. In current design each `Vertex` stores in an ID
    the tag of all it's adjacent Vertices. For graph numbering and
    partitioning this has proved sufficient.

9.  Parallel Classes To facilitate the development of parallel
    object-oriented finite element programs, classes are provided for
    parallel programming. The classes in the framework support the
    aggregate programming model. The classes include `Actor`, `Shadow`,
    `Message`, `MachineBroker`, `FEM_ObjectBroker`, `Channel`, and their
    subclasses.

As the design is very modular and most of the classes that are provided
can be subclassed, this allows for the contribution from many
researchers in different areas. The design will allow for contributions
in the fields of:

-   Element and material types.

-   Solution algorithms, integration procedures and constraint handling
    techniques.

-   Model generation.

-   Numerical analysis for solution of linear and eigenvalue problems.

-   Graph theory for numbering and partitioning graphs.

-   Data structures for container classes and database.

-   Graphics.

-   Message passing systems and load balancing in parallel environments.

<center><b>
<!-- Version 0.1 - Preliminary Draft -->
Frank McKenna and Gregory L. Fenves

December 20, 1999
</center></b>

