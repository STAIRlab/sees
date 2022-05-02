# DummyNode

```cpp
#include  <DummyNode.h>

class DummyNode: public DomainComponent
```

DomainComponent

\
DummyNodes are a type of node created and used by Subdomains for their
exterior nodes. They reference a real node and most methods invoked on
them are in turn invoked by the dummy node on the real node. The calls
asking the real node to change its current state are ignored. The calls
involving `DOF_Group` are handled by the dummy node.

\
To construct a dummy node which is associated with the node pointed to
by *theRealNode*.

\

\
Each DummyNode, when involved with a StaticCondensationAnalysis
analysis, will be associated with a `DOF_Group` object. It is the
DOF_Group that contains the ID of equation numbers. When invoked this
method sets that link for the DummyNode object.

```{.cpp}
virtual `DOF_Group` \*getDOF_GroupPtr(void);
```

Method which returns a pointer to the `DOF_Group` object that was set
using *setDOF_GroupPtr*. If no pointer has been set a $0$ is returned.

```{.cpp}
virtual int getNumberDOF(void) const;
```

Returns the result of invoking `getNumberDOF()` on its associated Node
object.

```{.cpp}
virtual Vector &getMass(void) const;
```

Returns the result of invoking `getMass()` on its associated Node
object.

```{.cpp}
virtual void setMass(Vector &mass);
```

Invokes `getNumberDOF()` on its associated Node object.

```{.cpp}
virtual const Vector &getCrds(void) const;
```

Returns the result of invoking `getCrds()` on its associated Node
object.

```{.cpp}
virtual const Vector &getDisp(void) const;
```

Returns the result of invoking `getDisp()` on its associated Node
object.

```{.cpp}
virtual const Vector &getVel(void) const;
```

Returns the result of invoking `getVel()` on its associated Node
object.

```{.cpp}
virtual const Vector &getAccel(void) const;
```

Returns the result of invoking `getAccel()` on its associated Node
object.

```{.cpp}
virtual const Vector &getTrialDisp(void) const;
```

Returns the result of invoking `getTrialDisp()` on its associated Node
object.

```{.cpp}
virtual const Vector &getTrialVel(void) const;
```

Returns the result of invoking `getTrialVel()` on its associated Node
object.

```{.cpp}
virtual const Vector &getTrialAccel(void) const;
```

Returns the result of invoking `getTrialAccel()` on its associated Node
object.

```{.cpp}
void addUnbalancedLoad(const Vector &additionalLoad);
```

Returns the result of invoking `addUnbalancedLoad()` on its associated
Node object.

```{.cpp}
virtual const Vector &getUnbalancedLoad(void) const;
```

Returns the result of invoking `getUnbalancedLoad()` on its associated
Node object.
The following commands do nothing, they just return.

\

\

\

\
