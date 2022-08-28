# OpenSees

<img align="left" src="https://github.com/BRACE2/OpenSeesRT/blob/master/etc/images/peer-black.svg" width="250px">

***Idiomatic* and *idempotent* C++ bindings to the OpenSees framework for finite element analysis.**

<!--
raylib is highly inspired by Borland BGI graphics lib and by XNA framework and it's specially well suited for prototyping, tooling, graphical applications, embedded systems and education.

*NOTE for ADVENTURERS: raylib is a programming library to enjoy videogames programming; no fancy interface, no visual helpers, no debug button... just coding in the most pure spartan-programmers way.*

-->

<br>

--------------------------------------------------------------------

<br>

<div style="align:center">

[![PyPI Downloads](https://img.shields.io/pypi/dm/opensees?style=for-the-badge)](https://pypi.org/project/opensees)
[![Latest PyPI version](https://img.shields.io/pypi/v/opensees?logo=pypi&style=for-the-badge)](https://pypi.python.org/pypi/opensees)
[![Latest conda-forge version](https://img.shields.io/conda/vn/conda-forge/opensees?logo=conda-forge&style=for-the-badge)](https://anaconda.org/conda-forge/opensees)
[![](https://img.shields.io/conda/v/opensees/opensees?color=%23660505&style=for-the-badge)](https://anaconda.org/opensees/opensees)

</div>

--------------------------------------------------------------------


## Installing / Compiling

### I. Simple user install

1. Install `mambaforge`
2. `mamba install -c opensees opensees`

### II. Editable (developer) install

1. Install `mambaforge`
2. `pip install -e .`
3. To recompile : `python setup.py build_ext`

### III. Distribution build

Pre-requisites:
1. Install `conda-build`

Steps for `opensees`:
1. `conda-build -c conda-forge etc/conda/ --python 3.7`
2. `anaconda upload <path>`

Steps for `opensees-intel`
1. `conda-build -c intel etc/conda-intel/ --python 3.7`
2. `anaconda upload <path>`

### IV. Python-only build

```
python setup.py [install|develop] --skip-cmake
```

## Build Environment

```shell
  conda create -c conda-forge -n skbuild python==3.8 cmake'>=3.18'  \
    scikit-build pybind11 setuptools
```


