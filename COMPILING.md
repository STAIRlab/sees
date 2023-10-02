# Compiling

1. Clone with submodules:

   ``` shell
   git clone --recurse-submodules https://github.com/BRACE2/OpenSeesRT
   ```

2. Install dependencies (see below)


3. To compile the first time, run

    ``` shell
    python -m pip install -e .
    ```

## Dependencies



- [ ] **Windows**: Intel and Conan


<details><summary><b>APT (Ubuntu, Debian Linux)</b></summary>

| Dependency  | Package              |
|:------------|:---------------------|
| LAPACK      | `liblapack-dev`      |
| BLAS        | `libblas-dev`        |
| Tcl\*       | `tcl-dev`            |

</details>
<details>
<summary>
<b>Pacman (Arch, Manjaro Linux)</b>
</summary>

The Pacman package manager

| Dependency  | Package       |
|:------------|:--------------|
| LAPACK      | `lapack`      |
| BLAS        | `blas`        |
| Tcl\*       | `tcl`         |

</details>
<details>
<summary>
<b>Anaconda (Mac, Windows, Linux)</b>
</summary>

When using conda, you need to ensure that CMake only finds conda
compilers. It is best to install the following packages

``` shell
conda install -c conda-forge fortran-compiler cxx-compiler c-compiler openblas
```

| Dependency  | Package       | Channel       |
|:------------|:--------------|:--------------|
| LAPACK      | `lapack`      |               |
| BLAS        | `blas`        |               |

</details>
</details>
<details>
<summary>
<b>Yum (CentOS, Redhat Linux)</b>
</summary>

| Dependency | Package        |
|------------|----------------|
| LAPACK     | `lapack-devel` |
| Tcl\*      | `tcl-devel`    |

</details>

## Other

- [x] **Windows** CI build

  ``` shell
  python scripts\win_repair.py win32 wheelhouse\opensees-*
  ```
