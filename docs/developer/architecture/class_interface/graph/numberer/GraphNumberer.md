# GraphNumberer 

```cpp
#include <graph/numberer/GraphNumberer.h>

class GraphNumberer: public MovableObject;
```

- [RCM]()
- [MinDegree]()

GraphNumberer is an abstract class. The GraphNumberer class defines the
interface that all programmers must provide when introducing new
GraphNumberer subclasses. A GraphNumberer is an algorithmic class for
numbering the Vertices of a Graph; that is assigning a unique integer
value ($0$ through *numVertex* $-1$) to each Vertex (uses *tmp* variable
of Vertex) of the Graph.

### Constructor

### Destructor

\
// Public Methods\

\

\
The integer *classTag* is passed to the MovableObject classes
constructor.

\
Does nothing.

\
This is the method invoked to perform the graph numbering, that is to
assign a unique integer $1$ through *numVertex*, to each Vertex in the
Graph. Returns an ordered ID containing the vertex references in the
order of the numbering, i.e. $ID(0)$ contains the integer reference for
the vertex assigned the number 1, $ID(1)$ contains the integer reference
for the vertex assigned the number 2 and so on. A side effect of the
numbering is that the *Tmp* variable of each vertex is set to the number
assigned to that vertex. If *lastVertex* is not $-1$ the Vertex whose
tag is given by *lastVertex* should be numbered last (it does not have
to be though THIS MAY CHANGE).

This is the method invoked to perform the graph numbering, that is to
assign a unique integer $1$ through *numVertex*, to each Vertex in the
Graph. Returns an ordered ID containing the vertex references in the
order of the numbering, i.e. $ID(0)$ contains the integer reference for
the vertex assigned the number 1, $ID(1)$ contains the integer reference
for the vertex assigned the number 2 and so on. A side effect of the
numbering is that the *Tmp* variable of each vertex is set to the number
assigned to that vertex. *lastVertices* is used as a hint to indicate
that these Vertices should be numbered last (they do not have to be
though THIS MAY CHANGE).
