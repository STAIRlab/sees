# DomainUser

```cpp
#include  <DomainUser.h>

class DomainUser;
```

Analysis
Design
DomainDisplay

The DomainUser class is an abstract base class. Its purpose is to define
the interface common among all subclasses. A DomainUser is a user of the
domain, example subtypes being Analysis and Design. The class defines
the pure virtual function `domainChange()`: it is this method that is
invoked by the domain on all domain users once the domain has changed,
i.e. the connectivity has changed.

\
All DomainUser are associated with a single domain, this constructor
sets up the link between the DomainUser and the domain, setting its link
with theDomain. The constructor invokes `addDomainUser(\*this)`{.cpp} on the
domain.

\
All DomainUser are associated with a single domain, the destructor
removes the link in the domain by invoking `removeDomainUser(\*this)`{.cpp} on
the domain.

\
Invoked by the associated domain to inform the domainUser that the
connectivity of the domain has changed.

\
A const method which returns a pointer to the Domain object on which the
DomainUser performs its DomainUser.
