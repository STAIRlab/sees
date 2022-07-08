# Analysis Classes

The **Analysis** object is an aggregation of objects of the following types:

1.  [`SolnAlgorithm`](algorithm/SolutionAlgorithm): The solution algorithm object is responsible for
    orchestrating the steps performed in the analysis.

2.  [`AnalysisModel`](model/AnalysisModel): The AnalysisModel object is a container class for
    storing and providing access to the following types of objects:

    1. **DOF_Group**: The **DOF_Group** objects represent the
       degrees-of-freedom at the **Node**s or new degrees-of-freedom
       introduced into the analysis to enforce the constraints.

    2. [`FE_Element`](model/fe_ele): The `FE_Element` objects represent the
       `Elements` in the `Domain` or they are introduced to add
       stiffness and/or load to the system of equations in order to
       enforce the constraints.

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




```plantuml
'package "OpenSees Analysis" #DDDDDD {
abstract class Integrator 
abstract class Analysis 
abstract class SystemOfEqn 
abstract Class ConvergenceTest 
abstract class Algorithm
Analysis o- ConstraintHandler 
Analysis o- Numberer 
Analysis o- Algorithm
Analysis o- ConvergenceTest 
Analysis o- Integrator 
Analysis o- SystemOfEqn 
'}
```
