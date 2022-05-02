
# Data Storage

In this work there are two general types of data storage classes
provided:

1.  Classes which can be used to store and provide access to the
    `TaggedObjects` during program execution. The abstract base class for
    these classes is `TaggedObjectStorage`. The concrete subclasses can
    implement the interface using the traditional CS data storage
    techniques, such as arrays, linked lists, hash tables, etc..

2.  Classes which can be used to store and retrieve information from
    permanent data archives, i.e. databases. The abstract base class
    defining the interface for these classes is [`FE_Datastore`](FE_Datastore).

