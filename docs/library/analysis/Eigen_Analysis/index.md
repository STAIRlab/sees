# Eigen Analysis

       eigen numEigenvalues?

To perform a generalized eigenvalue problem to determine the first
numEigenvalues eigenvalues and eigenvectors. The eigenvectors are stored
at the nodes and can be printed out. Currently each invocation of this
command constructs a new EigenvalueAnalysis object, each with new
component objects: a ConstraintHandler of type Plain, an EigenvalueSOE
and solver of type BandArpackSOE and BandArpackSolver and an algorithm
of type FrequencyAlgo. These objects are destroyed when the command has
finished. This will change.
