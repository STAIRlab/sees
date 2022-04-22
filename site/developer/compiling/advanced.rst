
Advanced Configurations with CMake
==================================

**This section is incomplete**


Highly customized versions of OpenSees can be configured and built with 
the help of CMake. In this document, a few special cases are considered:

#. Developing extension libraries for OpenSees.
#. Managing different versions of dependencies like Tcl
#. Linking OpenSees against alternative numerical libraries like BLAS
   and LAPACK.


The CMake build system is primarily composed of 3 files:

- ``/Conf.cmake``: This file is meant to be modified by intermediate to advanced
  users who may wish to use non-default configuration options.

- ``/ETC/cmake/OpenSeesDependencies*.cmake``: This file is used to configure a
  strategy for locating build dependencies. Users should not have to modify
  these files for standard builds on common operating systems; a correct
  strategy should be automatically configured based on the detected OS.

- ``/CMakeLists.txt``: The root-level CMakeLists.txt defines most of the
  logic for generating the OpenSees build system. It is responsible for
  sourcing all other CMake files. Users will not have to modify this file.



