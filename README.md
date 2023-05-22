# OpenSeesRT

<img align="left" src="https://raw.githubusercontent.com/BRACE2/OpenSeesRT/master/docs/figures/peer-black-300.png" width="250px" alt="PEER Logo">

***Idiomatic* and *idempotent* C++ bindings to the OpenSees framework for finite element analysis.**


<br>

--------------------------------------------------------------------

<br>

<div style="align:center">

<!--
[![Latest conda-forge version](https://img.shields.io/conda/vn/conda-forge/opensees?logo=conda-forge&style=for-the-badge)](https://anaconda.org/conda-forge/opensees)
-->

<!-- [![PyPI Downloads][pypi-v-image]][pypi-v-link] -->

[![Latest PyPI version](https://img.shields.io/pypi/v/opensees?logo=pypi&style=for-the-badge)](https://pypi.python.org/pypi/opensees)
[![](https://img.shields.io/conda/v/opensees/opensees?color=%23660505&style=for-the-badge)](https://anaconda.org/opensees/opensees)
[![PyPI Downloads](https://img.shields.io/pypi/dm/opensees?style=for-the-badge)](https://pypi.org/project/opensees)

</div>

--------------------------------------------------------------------

<!--

This library provides direct bindings to the [`libg3`](https://github.com/claudioperez/libg3)
OpenSees *runtime*.  This is a new C++ framework for the core OpenSees classes that eliminates
reliance on static global pointers.

-->



## Installing / Compiling

For Windows, first activate WSL2 and install a Linux distribution.
The simplest way to instal is with `pip`:

```bash
pip install opensees
```

Some alternative installation methods are listed below.

### I. Install with Anaconda

<!--
1. Install `mambaforge`
2. `mamba install -c opensees opensees`

### II. Editable (developer) install

Use this method to compile new C++ components (elements, materials, etc.).

1. Install `mambaforge`
2. `pip install -e .`
3. To recompile : `python setup.py build_ext`

-->

1. Install `mambaforge`, a small Anaconda distribution.
  - Go to [https://github.com/conda-forge/miniforge#mambaforge](https://github.com/conda-forge/miniforge#mambaforge)
  - Click the `Mambaforge-Linux-x86_64` link to download an install script.
  - Run the downloaded script.

  This can all be done at once with the following commands:

  ```bash
  wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
  bash Mambaforge-$(uname)-$(uname -m).sh
  ```

2. Create an environment to run `opensees` and `jupyter-lab` out of
  
  ```bash
  conda create -n opensees -c conda-forge python=3.9 jupyterlab matplotlib numpy scipy pyyaml

  ```

3. Install the `opensees` package.

  ```bash
  pip install -U opensees
  ```

Once this is done, you can run the commands

```bash
conda activate opensees
jupyter-lab
```

from the WSL terminal, and a URL will be printed which you can open in a browser to work in
Jupyter Lab.


<!--

### III. Distribution build

Pre-requisites:

-  Install `conda-build`
-  Clone
    ```
    git clone --recurse-submodules https://github.com/BRACE2/OpenSeesRT
    ```

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

-->



<!-- 
  - Install Jupyterlab

    ```bash
    mamba create -n jupyter jupyterlab 
    mamba activate opensees
    python -m ipykernel install --user --name opensees --display-name "Python (opensees)"
    ```
-->




                           ┌─┐┌─┐┌─┐┌─┐  ┌──┌─┐┌─┐ ┌──
                           └─┘├─┘└──┘ │ ─┘  └──└───┘
           ───────────────────┘Berkeley, California ──────────────────────
                                   © UC Regents



<!-- Badge links -->

[pypi-d-image]: https://img.shields.io/pypi/dm/opensees.svg
[license-badge]: https://img.shields.io/pypi/l/opensees.svg
[pypi-d-link]: https://pypi.org/project/opensees
[pypi-v-image]: https://img.shields.io/pypi/v/opensees.svg
[pypi-v-link]: https://pypi.org/project/opensees

