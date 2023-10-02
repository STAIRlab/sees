

To clone with submodules:

```shell
git clone --recurse-submodules https://github.com/BRACE2/OpenSeesRT
```



----------------------------------------------------------



`OS`/`Deps`/`PyRT`:


- [ ] `Unix`: Conda



- [ ] **Windows**: Intel and Conan

  ```shell
  python -m pip install -e .
  ```




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

<details><summary><a>Pacman (Arch, Manjaro Linux)</a></summary>

The Pacman package manager

  Dependency    Package
  ------------- ---------------
  LAPACK        `lapack`
  BLAS          `blas`
  SuiteSparse   `suitesparse`
  SuperLU       `superlu`
  MySQL\*       `mariadb`
  Tcl\*         `tcl`


</details>


<details><summary><a>Anaconda (Mac, Windows, Linux)</a></summary>


  When using conda, you need to ensure that CMake only
  finds conda compilers. It is best to install the following packages

  ```shell
  conda install -c conda-forge fortran-compiler cxx-compiler c-compiler openblas
  ```
  Dependency    Package         Channel
  ------------- --------------- ---------------
  LAPACK        `lapack`        
  BLAS          `blas`          
  SuperLU       `superlu`       
  SuiteSparse   `suitesparse`   
  MySQL\*       `mysql`         `conda-forge`


</details>



</details>

<details><summary><a>Yum (CentOS, Redhat Linux)</a></summary>


  Dependency    Package
  ------------- ---------------
  LAPACK        `lapack-devel`
  MySQL\*       `mysql-devel`
  Tcl\*         `tcl-devel`


</details>



## Other

- [x] **Windows** CI build

  ```shell 
  python scripts\win_repair.py win32 wheelhouse\opensees-0.0.47*
  ```

- [x] `Unix`/`Unix` CI build
