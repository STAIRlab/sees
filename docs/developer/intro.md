# Developer Introduction

An OpenSees application can be decomposed into the following
parts:

- The core framework, as originally presented in @mckenna1998.
  This defines the core components and interfaces.
- Component libraries; these are concrete objects such as elements,
  materials and solvers.
- Runtime (**OpenSeesRT**, **OpenSees.exe**, **OpenSeesPy**). A runtime
  is responsible for providing a mechanism to users for conducting an analysis.
  Runtimes have been implemented using various communication mechanisms.
  The classic OpenSees Tcl interpreters generally invoke
  class methods directly to perform analysis procedures, meanwhile
  **OpenSeesPy** leverages the interpreter framework introduced in
  @mckenna2010


The OpenSeesRT distributioin aims to achieve the following goals:

- *Idempotence*
- *Reliability* In order to prevent the *exensability* of the framework from impacting
  its *reliability*, modularity must be separated from the core framework.

Architecture:

- `libG3` - Core OpenSees framework
- `libOpenSeesRT` - Tcl package linking `libG3` with OpenSees
  component libraries.
- libOpenSeesPyRT  - Python bindings. Exposes direct interface
  to model objects like `Element`, `UniaxialMaterial`, etc.


