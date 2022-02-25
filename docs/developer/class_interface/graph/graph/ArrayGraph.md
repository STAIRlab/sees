UNDER CONSTRUCTION - removeVertex & printSpecial NEED TO BE ADDED.

# ArrayGraph 

```cpp
#include <graph/graph/ArrayGraph.h>
```

class ArrayGraph: public Graph\

Graph\

\
ArrayGraph is a subtype of Graph. The vertices for this type of graph
are held in a simple array data structure whose initial size is
specified at construction. This size can increase if needed. The array
storage scheme is more efficient than a List storage scheme in terms of
accessing the vertices; in very large problems where memory is limited
this type of scheme may have problems getting enough contiguous meory in
which case a List might be a better choice. **There is a question as to
whether or not the public methods should be declared as virtual. Good
OOP programming would have all methods declared as virtual, however as
subclasses cannot gain access to the private member data there does not
seem to be much point in declaring them, except for the destructor,
virtual in this instance.**\

// Constructors\

\
// Destructor\

\
// Public Methods\

\

\

\

\
// Protected Methods\

\

To construct an empty ArrayGraph. Creates a Vertex \*\* array,
*theVertices* of size *arraySize* and sets the number of vertices,
*numVertex*, and number of edges *numEdge* to $0$. If it fails to get an
array of appropriate size it sets its *arraySize* to $0$; subclasses can
check if successfull construction by invoking the protected member
function `getArraySize()`.

\
Goes through *theVertices* and anywhere it finds a non-zero pointer,
invokes the vertex destructor on that pointer. It then invokes the
destructor on theVertices array.

\
Method to add a vertex to the graph. If the adjacency list of the vertex
is not empty the graph will first check to see all vertices in the the
the vertices adjacency list exist in the graph before the vertex is
added. It then checks if it neeeds a new array and if so creates one,
i.e. if the *arraySize* $=$ *numVertex* it creates a new array, whose
size is double the original and copies the pointers to the vertices,
before invoking `delete()` on the old array. It now tries to add the
vertex in the array at location *vertexTag*. If this fails it adds at
the first empty location it comes to. Returns a 0 if successfull
addition, a $-1$ otherwise and a message to opserr explaining the
problem.
*virtual int addEdge(int vertexTag, int otherVertexTag);* \
Causes the Graph to add an edge `(vertexTag,otherVertexTag)`{.cpp} to the
Graph. A check is first made to see if vertices with tags given by
*vertexTag* and *otherVertexTag* exist in the graph. If they do not
exist a $-1$ is returned, otherwise the method invokes `addEdge()` on
each of the corresponding vertices in the graph. Returns $0$ or a
positive integer if sucessfull (positive if edge has already been
added), a negative number if not.

```{.cpp}
virtual Vertex \*getVertexPtr(int vertexTag);
```

A method which returns a pointer to the vertex whose tag is given by
*vertexTag*. The method first looks at location *vertexTag* for the
vertex, otherwise it must search through the array until it finds the
vertex it is looking for. If no such vertex exists in the graph $0$ is
returned.

```{.cpp}
virtual VertexIter &getVertices(void);
```

A method which first invokes `reset()` on the graphs ArrayVertexIter and
then returns a reference to this iter.

```{.cpp}
virtual int getNumVertex(void) const;
```

A method to return the number of vertices in the graph, returns
numVertex.

```{.cpp}
virtual int getNumEdge(void) const;
```

A method to return the number of edges in the graph, returns numEdge.

```{.cpp}
virtual void Print(OPS_Stream &s) const =0;
```

A method to print the graph. It first prints out numVertex and numEdge
and then on each newline prints the vertexTag and the edges for that
vertex. It does this by going through theVertices array and invoking
`Print()` on each non-zero pointer.

\
A method to return the size of the graphs array.
