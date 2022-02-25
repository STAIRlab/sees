\
\#include $<\tilde{ }$domain/pattern/TimeSeries.h$>$\

class TimeSeries: public DomainComponent\

MovableObject\

\
The TimeSeries class is an abstract base class. A TimeSeries object is
used in a LoadPattern to determine the current load factor to be applied
to the loads and constraints for the time specified.

// Constructor\

\
// Destructor\

\
// Pure Virtual Public Methods\

\

\
The integer *classTag* is passed to the MovableObject classes
constructor.

\
Does nothing.

\
To return the current load factor for the given value of *pseudoTime* to
be applied to the loads and single-point constraints in a LoadPattern
based on the value of *pseudoTime*.

To print to the stream *s* output based on the value of *flag*.
