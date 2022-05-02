# Vertex 

```cpp
#include <graph/graph/Vertex.h>

class Vertex: public TaggedObject;
```

Vertex is the abstraction of a vertex in a
graph. It has a color, weight and a temporary integer value associated
with it. Also associated with it is an integer reference, which can be
used to identify an object of some type the vertex is representing and
in integer temporary variable for algorithms which work with graphs.  

// Constructor   

// Destructor   

// Public Methods    .            

Construct a Vertex whose tag, reference, weight and color are as given
by the arguments. The degree of the vertex is set to $0$. The integer
\*tag\* is passed to the TaggedObject classes constructor.   Does
nothing.   To set the weight of the vertex to \*newWeight\* 

```cpp
virtual void setColor(int newColor);
```

To set the color of the vertex to \*newColor\* 

```cpp
virtual void setTmp(int newTmp);
```

To set the temporary variable of the vertex to \*newTmp\* 

```cpp
virtual int getTag(void) const;
```
. Returns the vertices tag. 

```cpp
virtual int getRef(void) const;
```

Returns the vertices integer reference. 

```cpp
virtual double getWeight(void) const;
```

 Returns the vertices weight. 
```cpp
virtual int getColor(void) const;
```

Returns the vertices color. 

```cpp
virtual int getTmp(void) const;
```

Returns the vertices temporary variable. 

```cpp
virtual int addEdge(int otherTag);
```
If the adjacency list for that vertex does not already
contain `otherTag`, `otherTag` is added to the adjacency list and
the degree of the vertex is incremented by $1$. Returns a $0$ if
sucessfull, a $1$ if edge already existed and a negative number if not.
Note that no check is done by the vertex to see that a vertex with
`otherTag` exists in the graph. The adjacency list for a Vertex is
stored in an ID object containing the adjacent Vertices tags. 

A check is made to see if `otherTag` is in this ID using `getLocation()`,
if it needs to be added the \*$$degree$$\* operator is invoked on the ID. 


```cpp
virtual int getDegree(void) const;
```
Returns the vertices degree. 


```cpp
virtual const ID &getAdjacency(void) const;
```

Returns the vertices
adjacency list, this is returned as an ID whose components are tags for
vertices which have been successfully added. 

```cpp
virtual void Print(OPS_Stream &s, int flag=0);
```
Prints the vertex. If the `flag = 0` only the vertex
tag and adjacency list is printed. If the `flag =1` the vertex tag,
weight and adjacency are printed. If the `flag =2` the vertex tag, color
and adjacency are printed. If the `flag =3` the vertex tag, weight, color
and adjacency are printed. 
