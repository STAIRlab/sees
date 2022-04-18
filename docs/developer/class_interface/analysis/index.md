# Analysis Classes

The **Analysis** object is an aggregation of objects of the following types:

1.  [`SolnAlgorithm`](algorithm/SolutionAlgorithm): The solution algorithm object is responsible for
    orchestrating the steps performed in the analysis.

2.  [`AnalysisModel`](algorithm/AnalysisModel): The AnalysisModel object is a container class for
    storing and providing access to the following types of objects:

    1. **DOF_Group**: The **DOF_Group** objects represent the
       degrees-of-freedom at the **Node**s or new degrees-of-freedom
       introduced into the analysis to enforce the constraints.

    2. [`FE_Element`](fe_ele): The `FE_Element` objects represent the
       `Elements` in the `Domain` or they are introduced to add
       stiffness and/or load to the system of equations in order to
       enforce the constraints.

    The `FE_Element`s and `DOF_Group`s are important to the design
    because:

    1. They remove from the `Node` and `Element` objects the need
       to worry about the mapping between degrees-of-freedoms and
       equation numbers.

    2. They also remove from the `Node` and `Element` class
       interfaces methods for forming tangent and residual vectors,
       that are used to form the system of equations.

    3. The subclasses of `FE_Element` and `DOF_Group` are
       responsible for handling the constraints. This removes from the
       rest of the objects the analysis aggregation the need to deal
       with the constraints.

3.  [`Integrator`](integrator/Integrator): The `Integrator` object is responsible for
    defining the contributions of the `FE_Element`s and `DOF_Group`s
    to the system of equations and for updating the response quantities
    at the `DOF_Group`s with the appropriate values given the solution
    to the system of equations.

4.  **ConstraintHandler**: The **ConstraintHandler** object is
    responsible for handling the constraints. It does this by creating
    **FE_Element**s and **DOF_Group**s of the correct type.

5.  **DOF_Numberer**: The **DOF_Numberer** object is responsible for
    mapping equation numbers in the system of equations to the
    degrees-of-freedom in the **DOF_Group**s.


