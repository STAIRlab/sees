# OpenSees

*Idiomatic* and *idempotent* C++ bindings to the OpenSees framework.

--------------------------------------------------------------------

<center>

[![Latest PyPI version](https://img.shields.io/pypi/v/opensees?logo=pypi&style=for-the-badge)](https://pypi.python.org/pypi/opensees)
[![Latest conda-forge version](https://img.shields.io/conda/vn/conda-forge/opensees?logo=conda-forge&style=for-the-badge)](https://anaconda.org/conda-forge/opensees)
[![](https://img.shields.io/conda/v/opensees/opensees?color=%23660505&style=for-the-badge)](https://anaconda.org/opensees/opensees)

</center>

--------------------------------------------------------------------


## Installing / Compiling

### Simple install

1. Install `mambaforge`
2. `mamba install -c opensees opensees`

### Editable install

1. Install `mambaforge`
2. `conda develop .` # pip install -e .
3. To recompile : `python -m build`

### Distributing

1. Install `conda-build`
2. `conda-build -c conda-forge etc/conda/`
3. `anaconda upload <path>`

## Build Environment

```shell
  conda create -c conda-forge -n skbuild python==3.8 cmake'>=3.18'  \
    scikit-build pybind11 setuptools
```


