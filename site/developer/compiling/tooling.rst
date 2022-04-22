.. _build-tooling:

Tooling
=======

This page introduces some basic tools which may be new to users who have
not worked with C/C++. Users that are already comfortable with a C/C++
toolchain can skip this page.



.. _build-src:

Source Control
--------------

A source control tool is like Google Documents, but for source code.
It allows developers to track changes that have been made to
a project, and easily collaborate by sharing patches.
Currently, the industry standard tool for this purpose is
`Git <https://git-scm.com>`_. 
Just like Google drive provides a platform for hosting sharing and collaborating on
Google documents, `GitHub <https://github.com>`_ is a platform
where developers can host, share and collaborate on software projects.

The OpenSees project follows a *forking* workflow for accepting contributions.
The following resources explain more on this matter.

* For a brief outline on forking we suggest the `Atlassians forking workflow page <https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow>`_.

* For a brief introduction to using your new FORK we suggest the `Atlassians saving changes <https://www.atlassian.com/git/tutorials/saving-changes>`_.

* For those interested in programming, you might as well become proficient using git so the link to all of `Atlassians git tutorial <https://www.atlassian.com/git>`_ will make help.



.. _build-chain:

Compiler tool-chain
------------------

A compiler tool-chain is the collection of programs that work together
to build a final executable program. This includes the actual
compiler, a linker, and various other utilities.  These programs
are typically bundled together and installed collectively in a single
step. Different operating systems generally favor a particular tool-chain, but
the differences between these can generally be hidden by a *build automation*
tool like CMake.

..
  - https://pabloariasal.github.io/2018/02/19/its-time-to-do-cmake-right/


Building OpenSees requires both a C/C++ and a Fortran compiler. Some suggested
compilers for various platforms are listed in table-summary_

.. 
  - Windows: `Intel <OneAPI https://software.intel.com/content/www/us/en/develop/tools/oneapi/hpc-toolkit/download.html>`_


.. _build-pkg:

Package management
------------------



.. raw:: html
   
   <details><summary><a>APT (Ubuntu, Debian Linux)</a></summary>

.. csv-table::
   :header: "Dependency", "Package"

   LAPACK,      ``liblapack-dev``
   BLAS,        ``libblas-dev``
   SuiteSparse, ``suitesparse-dev``
   SuperLU,     ``superlu-dev``
   MySQL*,      ``libmysqlclient-dev``
   Tcl*,        ``tcl-dev``


.. raw:: html
   
   </details>

.. raw:: html
   
   <details><summary><a>Pacman (Arch, Manjaro Linux)</a></summary>

The Pacman package manager 

.. csv-table::
   :header: "Dependency", "Package"

   LAPACK,      ``lapack``
   BLAS,        ``blas``
   SuiteSparse, ``suitesparse``
   SuperLU,     ``superlu``
   MySQL*,      ``mariadb``
   Tcl*,        ``tcl``


.. raw:: html
   
   </details>


.. raw:: html
   
   <details><summary><a>Anaconda (Mac, Windows, Linux)</a></summary>

.. csv-table::
   :header: "Dependency", "Package", "Channel"

   LAPACK,      ``lapack``
   BLAS,        ``blas``
   SuperLU,     ``superlu``
   SuiteSparse, ``suitesparse``
   MySQL*,      ``mysql``, ``conda-forge``


.. raw:: html
   
   </details>

..
    The final tool in a developer's toolbox is a *package manager*.

    Windows

    - chocolatey
    - anaconda/miniconda
    - Conan


    MacOS

    - homebrew
    - anaconda/miniconda
    - Conan

    Linux

    - system package manager
    - anaconda/miniconda
    - Conan


Command line environments
-------------------------

**This section is under development**


Summary
-------

The following table gives a brief rundown of the most common configurations for
various operating systems.

.. _table-summary:

+-----------------------+--------------------+----------------+---------------+
|          Tool         |       Windows      |      MacOS     |     Linux     |
+-----------------------+--------------------+----------------+---------------+
| Source control        | GitHub Desktop     | GitHub Desktop | Git           |
+-----------------------+--------------------+----------------+---------------+
| Build automation [1]_ | CMake              | CMake          | CMake         |
+------------+----------+--------------------+----------------+---------------+
| Compiler   | C++      | Visual Studio 2019 | Clang          | GCC           |
+------------+----------+--------------------+----------------+---------------+
|            | Fortran  | Intel-Fortran_     | GFortran       | GFortran      |
+------------+----------+--------------------+----------------+---------------+
| Package management    |                    | Homebrew       | *system* [2]_ |
+-----------------------+--------------------+----------------+---------------+

.. _Intel-Fortran: https://software.intel.com/content/www/us/en/develop/tools/oneapi/hpc-toolkit/download.html
