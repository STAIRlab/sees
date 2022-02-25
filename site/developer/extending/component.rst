
Simple Components
=================

Inside each module-level ``CMakeLists.txt`` file there is a function call
with the form:

.. code-block:: cmake

   target_sources(OPS_Module 
     PRIVATE 
       <some source files>...
     PUBLIC
       <some header files>...
   )

Simple materials and elements can be added to the CMake build simply by
including them in the relevant CMake ``target_sources`` call.

For example, a new element might be implemented in a file called
``ElasticFoo.cpp`` with header ``ElasticFoo.h`` in the directory
``OpenSees/SRC/element/``. These files would simply need to be
added to the function call ``target_sources(OPS_Element ...)``
in the file ``OpenSees/SRC/element/CMakeLists.txt``.


