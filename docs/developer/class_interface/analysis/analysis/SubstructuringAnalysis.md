\
\#include $<$/analysis/analysis/SubstructuringAnalysis.h$>$\

class SubstructuringAnalysis: public DomainDecompositionAnalysis;\

MovableObject Analysis\
DomainDecompositionAnalysis\

\
SubstructuringAnalysis is a subclass of DomainDecompositionAnalysis. It
is used when performing an analysis using the substructuring method. It
differs from the DomainDecompositionAnalysis class only in that the
constructor ensures that a SubstructuringSolver is given for the Solver.


\
The constructor is responsible for ensuring a Substructuring solver is
passed in as an argument. The base class does the rest. For this reason
WE WILL FORGET THIS CLASS.

\
Invokes `removeDomainUser(this)` on the domain object.

\
