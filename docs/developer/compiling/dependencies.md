# Dependencies

Try `cmake ..`; on Unix-like systems, this is often enough.
If a dependency is missing, try one of the following options
and run `cmake ..` again:
  
1. Install the missing dependency with a system package manager (see below), or
2. Install conan and run `conan install .. --build missing` from the build
   directory

If a package was successfully installed but CMake still cannot find it,
you can manually set one of the variables below:


 Dependency     Default   Linker variable       Compiler include
 ------------  --------- --------------------  -------------------
 [BLAS]          `B`      `BLAS_LIBRARIES`
 [LAPACK]
 [ARPACK]        `B`      `ARPACK_LIBRARIES`    `-`
 [Tcl]          `C/S`     `TCL_LIBRARIES`       `TCL_INCLUDE_PATH`
 [SuperLU]       `B`

: `B`: use bundled version, `S`: search operating system ( using CMake's `find_package`)
  `C/S`: uses Conan if it has been run, otherwise searches system. 


    OPS >>> LAPACK:  /usr/lib/liblapack.so.3
    OPS >>> SUPERLU: OTHER/bin/SuperLU_5.1.1/libSUPERLU.a
    OPS >>> ARPACK:  OTHER/bin/ARPACK/libARPACK.a
    OPS >>> UMFPACK: OTHER/bin/UMFPACK/libUMFPACK.a
    OPS >>> CSPARSE: OTHER/bin/CSPARSE/libCSPARSE.a
    OPS >>> TCL:
    OPS >>> AMD:     OTHER//bin/AMD/libAMD.a
    OPS >>> BLAS
    OPS >>> LAPACK
    OPS >>> SUPERLU

```{=html}
<details><summary><a>APT (Ubuntu, Debian Linux)</a></summary>
```
  Dependency    Package
  ------------- ----------------------
  LAPACK        `liblapack-dev`
  BLAS          `libblas-dev`
  SuiteSparse   `suitesparse-dev`
  SuperLU       `superlu-dev`
  MySQL\*       `libmysqlclient-dev`
  Tcl\*         `tcl-dev`

```{=html}
</details>
```
```{=html}
<details><summary><a>Pacman (Arch, Manjaro Linux)</a></summary>
```
The Pacman package manager

  Dependency    Package
  ------------- ---------------
  LAPACK        `lapack`
  BLAS          `blas`
  SuiteSparse   `suitesparse`
  SuperLU       `superlu`
  MySQL\*       `mariadb`
  Tcl\*         `tcl`

```{=html}
</details>
```
```{=html}
<details><summary><a>Anaconda (Mac, Windows, Linux)</a></summary>
```
  Dependency    Package         Channel
  ------------- --------------- ---------------
  LAPACK        `lapack`        
  BLAS          `blas`          
  SuperLU       `superlu`       
  SuiteSparse   `suitesparse`   
  MySQL\*       `mysql`         `conda-forge`

```{=html}
</details>
```

```{=html}
</details>
```
```{=html}
<details><summary><a>Yum (CentOS, Redhat Linux)</a></summary>
```

  Dependency    Package
  ------------- ---------------
  LAPACK        `lapack-devel`
  MySQL\*       `mysql-devel`
  Tcl\*         `tcl-devel`

```{=html}
</details>
```

