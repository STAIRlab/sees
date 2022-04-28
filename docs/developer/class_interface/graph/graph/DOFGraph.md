# DOFGraph

```cpp
#include  <DOFGraph.h>

class DOFGraph: public ArrayGraph
```

Graph\
ArrayGraph\

\
DOFGraph is a type of Graph. It is a graph of the DOF connectivity of
the analysis model. It is utilised by a SystemOfEqn object to determine
the sparsity of the system. It is a subtype of ArrayGraph, though it
could just as easily be a subtype of any other type of Graph subclass
that fully implements the graph interface.

\
The constructor is responsible for constructing the graph given
*theModel*. It creates the vertices of the graph, one for every DOF in
the model and adds all edges based on the FE_Element connectivity. For
this reason the model must be fully populated with the DOF_Group and
FE_Element objects before the constructor is called.

\
The superclass ArrayGraph is responsible for destroying the vertices.

\
