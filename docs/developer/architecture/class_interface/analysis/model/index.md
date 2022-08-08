# Analysis Model

The AnalysisModel object is a container class for
storing and providing access to the following types of objects:

1. **DOF_Group**: The **DOF_Group** objects represent the
   degrees-of-freedom at the **Node**s or new degrees-of-freedom
   introduced into the analysis to enforce the constraints.

2. [`FE_Element`](model/fe_ele): The `FE_Element` objects represent the
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

