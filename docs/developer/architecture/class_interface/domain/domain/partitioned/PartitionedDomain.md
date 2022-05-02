UNDER CONSTRUCTION


\#include  `</domain/domain/partitioned/PartitionedDomain.h>`\

class PartitionedDomain: public Domain\

Domain\

\
PartitionedDomain is an extension of Domain. A partitioned domain is an
aggregation of subdomains. All elements, nodes, loadcases are added to
the PartitionedDomain. The components can be moved among subdomains
(keeping in mind that subdomains are themselves subclasses of domain and
therefore must obey the requirements for adding and removing elements
specified in the interface for Domain) by invoking the *remove..()* and
*add\...()* methods on the subdomain.

### Constructors

\

### Destructor

\
// Public Member Functions - which extend the Domain class\

\

\

\

\
// Public Member Functions - inherited from Domain but rewritten\

\

\

\

\

\

\

\

\

\

\

\

\

\
// Protected Methods\

*virtual int buildEleGraph(Graph &theEleGraph)*\

\
Constructs an empty PartitionedDomain. A link with the domain
partitioner *thePartitioner* is set up. The *thePartitioner* is used by
the domain to partition and load balance the partitioned domain.

Constructs an empty PartitionedDomain, storage is allocated for the
components that are to be added using the estimated number of components
passed as arguments. A link with the domain partitioner *thePartitioner*
is set up. The *thePartitioner* is used by the domain to partition and
load balance the partitioned domain.

\
Deletes the storage components.

\
Method which first checks that subdomains with tags 1 through
*numPartitions* exist in the PartitionedDomain. Then it invokes
*setPartitionedDomain(\*this)* on the DomainPartitioner and finally it
returns the result of invoking *partition(numPartitions* on the
DomainPartitioner, which will return 0 if successful, a negative number
if not.

```{.cpp}
virtual bool addSubdomain(Subdomain \*theSubdomainPtr);
```

Adds the subdomain pointed to by theSubdomainPtr to the domain. The
domain is responsible for checking that no other subdomain with a
similar tag, has been previously added to the domain. If successful the
domain is responsible for invoking `setDomain(this)` on the Subdomain.
The domain is also responsible for invoking `domainChange()`. The call
returns *false* if the subdomain was not added, otherwise *true* is
returned.

```{.cpp}
virtual int getNumSubdomains(void);
```

Method which returns the number of Subdomains (partitions).

```{.cpp}
virtual Subdomain \*getSubdomainPtr(int tag);
```

Returns the Subdomain whose tag is given by *tag*.

```{.cpp}
virtual SubdomainIter &getSubdomains(void);
```

Returns an iter for the Subdomains of the PartitionedDomain.
*Node \*removeExternalNode(int tag);* \
A method to remove a Node whose tag is given by *tag* from the
PartitionedDomain, but will not remove the Node from any Subdomains.
*Graph &getSubdomainGraph(void);* \
This will create a new graph each time it is invoked; deleting the old
graph. THIS WILL BE CHANGED. A vertex is created for each Subdomain,
with an edge to each Subdomain the Subdomain is connected to, a tag
equal to the Subdomain tag, and a weight equal to the result of invoking
`getCost()` on the Subdomain.

\
To add the element pointed to by theElementPtr to the domain. If *check*
is *true* the domain is responsible for checking to see that: 1) no
other element with a similar tag, element number, exists in any of the
subdomains. If check is successful the partitioned domain attempts to
add the element to the storage arrey. The call returns *false* if the
element was not added, otherwise *true* is returned.

```{.cpp}
virtual bool addNode(Node \*theNodePtr, bool check = false);
```

Adds the node pointed to by theNodePtr to the domain. If *check* is
*true* the domain is responsible for checking that no other node with a
similar tag, node number, exists in any of the subdomains. If successful
the partition domain attempts to add the node by invoking
*Domain::addNode*. The call returns *false* if the node was not added,
otherwise *true* is returned.
*virtual bool addSP_Constraint(SP_Constraint \*theSPptr, bool check =
false);*\
Adds the single point constraint pointed to by theSPptr to the domain.
The domain performs some checks is *check* is true. If successful the
domain adds the constraint using *Domain::addSP_Constraint()*. The call
returns *false* if the constraint was not added, otherwise *true* is
returned.

```{.cpp}
virtual bool addMP(MP_Constraint \*theMPptr, bool check = false);
```

Adds the multiple point constraint pointed to by theMPptr, to the
domain. The domain performs some checks is *check* is true. If
successful the domain adds the constraint using
*Domain::addMP_Constraint()*. The call returns *false* if the constraint
was not added, otherwise *true* is returned.

```{.cpp}
virtual bool addLoadCase(LoadCase \*theLCptr);
```


\

It returns an *PartionedDomEleIter* for the elements of the domain. This
is an iter which goes through all the subdomains, invoking
`getElements()` on the subdomain to get an ElementIter. The
PartitionedDomEleIter uses this iter to go through the elements of the
subdomain until it begins returning $0$; at which point it goes on to
the next subdomain.

```{.cpp}
virtual Element \*getElement(int tag) const;
```

Returns a pointer to the element whose tag is given by *tag*. If no such
element exists $0$ is returned. This is done by invoking
`getElement(tag)` on the subdomains until the element is found or no
more subdomains exist; in which case a $0$ is returned.

```{.cpp}
virtual Node \*getNode(int tag) const;
```

Returns a pointer to the node whose tag is given by *tag*. If no such
node exists $0$ is returned. This is done by invoking `getNode(tag)` on
the subdomains until the element is found or no more subdomains exist;
in which case a $0$ is returned.

```{.cpp}
virtual LoadCase \*getLoadCasePtr(int tag) const;
```

Returns a pointer to the element whose tag is given by *tag*. If no such
load case exists $0$ is returned.

Sets the current load case of the domain to be that whose tag is given
by LCtag. It iterates through all the subdomains invoking the same
operation on them. Returns *false* if no such load case exists,
otherwise returns *true*.

Sets the current load case of the domain to be that whose tag is given
by *newTime*. It iterates through all the subdomains invoking the same
operation on them.

```{.cpp}
virtual void applyLoad(double time = 0.0, double loadFactor = 1.0);
```

The partitioned domain iterates through all the subdomains invoking
*applyLoad(double timeStamp)* on them.

```{.cpp}
virtual void linearize(void);
```

The partitioned domain iterates through all the subdomains invoking
`linearize()` on them.

```{.cpp}
virtual void commit(void);
```

The partitioned domain iterates through all the subdomains invoking
`commit()` on them.

\
Returns the tag of the current load case set for the domain. If no load
case is set $-1$ is returned.

Returns the currentTime set for the domain. If no load case is set $0$
is returned.

\
Returns the number of elements in the domain. This number is obtained by
summing the contributions from each subdomain.

```{.cpp}
virtual int getNumNodes(void) const = 0;
```

Returns the number of nodes in the domain. This number is obtained by
summing the contributions from each subdomain.

```{.cpp}
virtual int getNumSPs(void) const;
```

Returns the number of SP_Constraints in the domain. This number is
obtained by summing the contributions from each subdomain.

```{.cpp}
virtual int getNumMPs(void) const;
```

Returns the number of MP_Constraints in the domain. This number is
obtained by summing the contributions from each subdomain.

```{.cpp}
virtual int getNumLCs(void) const;
```

Returns the number of LoadCases in the domain.  This number is obtained
by summing the contributions from each subdomain.

```{.cpp}
virtual Domain \*getEmptyDomainCopy(void);
```

Returns an empty copy of the actual domain.

```{.cpp}
virtual Element \*removeElement(int tag);
```

To remove the element whose tag is given by *tag* from the domain. The
method Returns $0$ if no such element exists in the domain. Otherwise
the domain invokes `setDomain(0)`{.cpp} on the element and
*setDomainChange(true,true,false)* on itself before a pointer to the
element is returned.

```{.cpp}
virtual Node \*removeNode(int tag, bool checkNeeded = true);
```

To remove the node whose tag is given by *tag* from the domain. Returns
$0$ if no such node exists in the domain. Otherwise if the *checkNeeded*
is *true* before the node is removed a check is made to see that the
node is not referenced by any element, constraint or load. If it is
referenced the Node will not be removed and $0$ is returned. If the node
is to be removed the domain invokes `setDomain(0)`{.cpp} on the node and
*setDomainChange(true,false,true)* on itself before a pointer to the
Node is returned.

```{.cpp}
virtual LoadCase \*removeLoadCase(int tag);
```

To remove the load case whose tag is given by *tag* from the domain.
Returns $0$ if the load case was not in the domain, otherwise returns a
pointer to the load case that was removed. Invokes `setDomain(0)`{.cpp} on the
load case before it is returned.

```{.cpp}
virtual SP_Constraint \*removeSP_Constraint(int tag);
```

To remove the SP_Constraint whose tag is given by *tag* from the domain.
Returns $0$ if the constraint was not in the domain, otherwise the
domain invokes `setDomain(0)`{.cpp} on the constraint and
*setDomainChange(true,false,false)* on itself before a pointer to the
constraint is returned.

```{.cpp}
virtual `MP_Constraint` \*removeMP_Constraint(int tag);
```

To remove the `MP_Constraint` whose tag is given by *tag* from the domain.
Returns $0$ if the constraint was not in the domain, otherwise the
domain invokes `setDomain(0)`{.cpp} on the constraint and
*setDomainChange(true,false,false)* on itself before a pointer to the
constraint is returned.

\
Will return a pointer to the DomainPartitioner object associated with
the PartitionedDomain.
*virtual int buildEleGraph(Graph &theEleGraph)*\
A method which will cause the domain to discard the current element
graph and build a new one based on the element connectivity. Returns $0$
if successful otherwise $-1$ is returned along with an error message to
opserr.
