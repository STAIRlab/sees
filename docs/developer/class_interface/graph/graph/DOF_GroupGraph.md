\

\#include  `<DOF_GroupGraph.h>`\

class DOF_GroupGraph: public ArrayGraph\

Graph\
ArrayGraph\

\
DOF_GroupGraph is a type of Graph. It is a graph of the DOF_Group
connectivity of the analysis model. It is utilised by the DOF_Numberer
to assign equation numbers to the individual DOFs in the DOF_Groups of
the model. It is a subtype of ArrayGraph, though it could just as easily
be a subtype of any other type of Graph subclass that fully implements
the graph interface.

\
The constructor is responsible for constructing the graph given
*theModel*. It creates the vertices of the graph, one for every equation
(each DOF that has not been constrained out by the constraint handler)
in the model and adds all edges based on the FE_Element connectivity.
For this reason the model must be fully populated with the
DOF_Group_Group and FE_Element objects before the constructor is
called.

\
The superclass ArrayGraph is responsible for destroying the vertices.

\
