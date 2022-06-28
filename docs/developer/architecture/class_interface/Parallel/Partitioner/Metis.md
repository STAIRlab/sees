# Metis 

```cpp
#include <graph/partitioner/Metis.h>
```

class GraphPartitioner:\

GraphPartitioner\

\
Metis is a GraphPartitioner. The Metis graph partitioner calls
procedures defined in the METIS library to partition the graph. METIS is
currently being developed by G. Karypis and V. Kumar at the University
of Minnesota. At the present time the Graph to be partitioned MUST have
the vertices labeled $0$ through $numVertex-1$.
The METIS library uses two integer arrays to represent the graph, *xadj*
and *adjncy*. $xadj(i)$ stores the location in *adjncy* of the start of
the $i$'th Vertices adjacent Vertices. *adjncy* contains the tags of all
the adjacent vertices. For example, the graph which is represented by
the following matrix $A$:

$$A =
\left[
\begin{array}{ccccc}
1 & 0 & 1 & 1 & 0  \\
1 & 1 & 0 & 0 & 0  \\
0 & 1 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 \\
1 & 1 & 0 & 0 & 1
\end{array}
\right]$$

is represented by:

$$xadj =
\left[
\begin{array}{cccccccccccccc}
0 & 2 & 3 & 4 & 5 & 7
\end{array}
\right]$$

and

$$adjncy =
\left[
\begin{array}{cccccccccccccc}
2 & 3 & 0 & 1 & 4 & 0 & 1
\end{array}
\right]$$

note that there is no space allocated for the diagonal components.

### Constructors

\

\
### Destructor

\
// Public Methods\

\

\
// Private Method\

\

To construct a Metis object which will use the default settings when
partitioning.

To construct a Metis object which will use the setting passed into the
constructor as options to metis's `PMETIS()` routine. `checkOptions()`
is invoked to ensure the settings are valid.

\

\
This is the method invoked to partition the graph into *numPart*
partitions. On completion of the routine each vertex will be assigned a
color $1$ through *numPart*, the color assigned indicating the partition
to which the vertex belongs.

To partition a number of integer arrays are created, *options\[5$$
*,
*partition\[numVertex+1$$
*, *xadj\[numVertex+1$$
* and
*adjncy\[2\*numEdge$$
* (CURRENTLY ASSUMING GRAPH IS SYMMETRIC - THIS MAY
CHANGE & xadj and partition 1 LARGER THAN REQUIRED). If not enough
memory is available for the arrays, a warning message is printed and
$-2$ is returned. The data for *xadj* and *adjncy* are determined from
the Vertices of the Graph by iterating over each Vertex from $0$ through
*numVertex* $-1$. If default options are specified *options\[0$$
* is set
to $0$, otherwise $1$ with *options\[1:4$$
 = coarsenTo, mType, ipType,
rType*. if *pType* equals $1$ *PMETIS* is called, otherwise *KMETIS* is
called. Both are called with the following arguments: *numVertex,
xadj,adjncy, 0, 0, &weightFlag, options, numPart, &numbering, &edgecut,
partition* The colors of the partitions are then set equal to the color
indicated in *partition*. The integer arrays are destroyed and $0$
returned.

Sets the default options.

Sets the options for the partitioning to those passed as arguments. Then
invokes `checkOptions()` to see if the options are valid. HOW ABOUT
REFERRINGR TO MANUAL TO SEE WHAT OPTIONS MEAN.

If options are not valid sets the default options. EXPAND ON VALID
OPTIONS OR REFER TO METIS MANUAL.
