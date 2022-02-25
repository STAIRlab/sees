\
# Graph 

```cpp
#include <graph/graph/Graph.h>
```

class Graph:\

\

Graph is a base class. A Graph is a container class responsible for
holding the vertex set and edge set. The class is responsible for:

1.  providing methods to add vertices and edges.

2.  accessing the vertices and edges.

All the methods for the class are declared as virtual to allow
subclasses to be introduced.

// Constructors\

\

\
// Destructor\

\
// Public Methods\

\

\

\

\

\

To create an empty Graph. Creates an ArrayOfTagged object of initial
size $32$ in which to store the Vertices. The ArrayOfTagged object is
used to store the Vertices.

To create an empty Graph. Creates an ArrayOfTagged object of initial
size *numVertices* in which to store the Vertices. The ArrayOfTagged
object is used to store the Vertices.

To create an empty Graph. The *theVerticesStorage* object is used to
store the Vertices. `clearAll()` is invoked on this object to ensure it
is empty.

\
Invokes `clearAll()` on the storage object used to store the Vertices.
It then invokes delete on the storage object used, which was either
passed or created in the constructor.

\
Causes the graph to add a vertex to the graph. If *checkAdjacency* is
*true*, a check is made to ensure that all the Vertices in the adjacency
list of the Vertex are in the Graph. If a vertex in the adjacency is not
in the Graph the vertex is not added, a warning message is printed and
*false* is returned. If successful, returns the result of invoking
`addComponent()` on the TaggedStorage object used to store the
Vertices.
*virtual int addEdge(int vertexTag, int otherVertexTag);* \
Causes the Graph to add an edge `(vertexTag,otherVertexTag)`{.cpp} to the
Graph. A check is first made to see if vertices with tags given by
*vertexTag* and *otherVertexTag* exist in the graph. If they do not
exist a $-1$ is returned, otherwise the method invokes `addEdge()` on
each of the corresponding vertices in the graph. Increments *numEdge* by
$1$ and returns $0$ if sucessfull, a $1$ if the edge already existed,
and a $-2$ if one `addEdge()` was successful, but the other was not.

```{.cpp}
virtual Vertex \*getVertexPtr(int vertexTag);
```

A method which returns a pointer to the vertex whose tag is given by
*vertexTag*. If no such vertex exists in the graph $0$ is returned.
Invokes `getComponentPtr(vertexTag)` on the vertex storage object and
casts this to a Vertex \* if not null.

```{.cpp}
virtual VertexIter &getVertices(void);
```

A method which returns a reference to the graphs VertexIter. This iter
can be used for iterating through the vertices of the graph.

```{.cpp}
virtual int getNumVertex(void) const;
```

A method to return the number of vertices in the graph. Invokes
`getNumComponents()` on the Vertex storage object.

```{.cpp}
virtual int getNumEdge(void) const;
```

A method to return the number of edges in the graph, returns *numEdge*.

To remove the Vertex from the Graph whose tag is equal to *vertexTag*.
If *removeEdgeFlag* is *true* will also remove the Vertex from the
remaining Vertices adjacency lists. returns a pointer to the removed
Vertex if successful, $0$ if the Vertex was not in the Graph. Invokes
`removeComponent(vertexTag)` on the vertex storage object and casts this
to a Vertex \* if not null. DOES NOT YET DEAL WITH *removeEdgeFlag*.

```{.cpp}
virtual void Print(OPS_Stream &s, int flag =0);
```

A method to print the graph. Invokes `Print(s, flag)`{.cpp} on the vertex
storage object.

Invokes `Print()` on the Graph *G*.
