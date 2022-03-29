# Graph Classes

In this work Graphs are used for three purposes:

1.  to provide information on the sparsity of the system of equation to
    the SystemofEqn object,

2.  to provide the connectivity of the DOF_Group objects for determining
    a good mapping between degrees-of-freedom and equation numbers.

3.  to provide information on the connectivity both the Elements and
    Nodes in the Domain, which can be useful for example in
    partitioning.

The classes provided include Graph, Vertex, GraphNumberer and
GraphPartitioner. There is no Edge class provided at present. In current
design each Vertex stores in an ID the tag of all it's adjacent
Vertices, this may change. For graph numbering and partitioning this has
to date proved sufficient.


## Graph

## Vertex

## **GraphNumberer**

### RCM

## **GraphPartitioner**

### Metis
