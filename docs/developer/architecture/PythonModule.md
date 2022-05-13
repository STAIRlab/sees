# Python Module

Components of the `opensees` Python module are divided into

1. *Build-time* operations, and
2. *Run-time* operations.

Build-time operations have no knowledge of a model's *state*. These
include object constructors. All modeling objects are build-time objects.
In the Python interface, the concept of a build-time is abstracted away
by a library of template-like constructors.


Run-time operations imply a lifetime. They include querying *current*
values of the domain, like *time* and *response quantities*.
All analysis objects are run-time objects, and require knowledge of an
instance of the C++ `G3_Runtime` object.

The Python module consists of bindings that are defined
in the file `python/OpenSeesPyRT.cpp`

