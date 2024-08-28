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
    This will create a `build` directory with a `Makefile` that you can
    use for subsequent builds by running the following:
    ```shell
    make OpenSeesRT -j5
    ```
    where the option `-j5` makes the build faster and can be adjusted
    for your needs and resources (see `make` documentation).

## Dependencies

The primary system dependencies required for compiling are LAPACK/BLAS and Tcl.
Packages providing these libraries are listed below for various package
management ecosystems.
> **NOTE** If you build in an Anaconda environment, you should install 
> everything with `conda` or `mamba`, and preferably from `conda-forge`. 
> See Anaconda below.

**Windows**: Install Intel compilers and Conan


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
compilers.
The following command should install everything you need:

``` shell
conda install -c conda-forge fortran-compiler cxx-compiler c-compiler openblas
```


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
