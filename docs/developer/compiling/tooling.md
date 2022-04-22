# Tooling {#build-tooling}

This page introduces some basic tools which may be new to users who have
not worked with C/C++. Users that are already comfortable with a C/C++
toolchain can skip this page.

## Source Control {#build-src}

A source control tool is like Google Documents, but for source code. It
allows developers to track changes that have been made to a project, and
easily collaborate by sharing patches. Currently, the industry standard
tool for this purpose is [Git](https://git-scm.com). Just like Google
drive provides a platform for hosting sharing and collaborating on
Google documents, [GitHub](https://github.com) is a platform where
developers can host, share and collaborate on software projects.

The OpenSees project follows a *forking* workflow for accepting
contributions. The following resources explain more on this matter.

-   For a brief outline on forking we suggest the [Atlassians forking
    workflow
    page](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow).
-   For a brief introduction to using your new FORK we suggest the
    [Atlassians saving
    changes](https://www.atlassian.com/git/tutorials/saving-changes).
-   For those interested in programming, you might as well become
    proficient using git so the link to all of [Atlassians git
    tutorial](https://www.atlassian.com/git) will make help.

::: {#build-chain}
Compiler tool-chain \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
:::

A compiler tool-chain is the collection of programs that work together
to build a final executable program. This includes the actual compiler,
a linker, and various other utilities. These programs are typically
bundled together and installed collectively in a single step. Different
operating systems generally favor a particular tool-chain, but the
differences between these can generally be hidden by a *build
automation* tool like CMake.

Building OpenSees requires both a C/C++ and a Fortran compiler. Some
suggested compilers for various platforms are listed in
[table-summary](#table-summary)

## Package management {#build-pkg}

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
## Command line environments

**This section is under development**

## Summary

The following table gives a brief rundown of the most common
configurations for various operating systems.

::: {#table-summary}
+--------------------+------------------+--------------+--------------+
| > Tool             | > Windows        | > MacOS      | > Linux      |
+--------------------+------------------+--------------+--------------+
| Source control     | GitHub Desktop   | GitHub       | Git          |
|                    |                  | Desktop      |              |
+--------------------+------------------+--------------+--------------+
| Build automation   | CMake            | CMake        | CMake        |
+--------------------+------------------+--------------+--------------+
| Compiler \| C++    | Visual Studio    | Clang        | GCC          |
|                    | 2019             |              |              |
+--------------------+------------------+--------------+--------------+
| > | Fortran        | [Intel-Fortr     | GFortran     | GFortran     |
|                    | an](https://soft |              |              |
|                    | ware.intel.com/c |              |              |
|                    | ontent/www/us/en |              |              |
|                    | /develop/tools/o |              |              |
|                    | neapi/hpc-toolki |              |              |
|                    | t/download.html) |              |              |
+--------------------+------------------+--------------+--------------+
| Package management |                  | Homebrew     | *system*     |
+--------------------+------------------+--------------+--------------+
:::
