# Parallel Classes

To facilitate the development of parallel object-oriented finite element
programs, a new framework is presented in this section. The classes in
the framework support the aggregate programming model. The new classes
are:

-   **Shadow** - A Shadow object represents a remote actor object in the
    local actor process.

-   **Actor** - An Actor object is a local object in the remote actor
    process. It performs the operations requested of it by the Shadow
    object. The actor objects in an aggregation collectively perform the
    analysis operations by communicating between themselves.

-   **Channel** - The Shadow and Actor objects communicate with each
    other through Channel objects. A Channel object represents a point
    in a local actor process through which a local object can send and
    receive information.

-   **Address** - An Address object represents the location of a Channel
    object in the machine space. Channel objects send information to
    other Channel objects, whose locations are given by an Address
    object. Channel objects also receive information from other Channel
    objects, whose locations are given by an Address object.

-   **MovableObject** - A MovableObject is an object which can send its
    state from one actor process to another.

-   **ObjectBroker** - An ObjectBroker is an object in a local actor
    process for creating new objects.

-   **MachineBroker** - A MachineBroker is an object in a local actor
    process that is responsible for creating remote actor processes at
    the request of Shadow objects in the same local process.


::: {.center}
**Frank McKenna and Gregory L. Fenves**

**Version 0.1 - Preliminary Draft**

**December 20, 1999**


**PEER, University of California at Berkeley**
:::

