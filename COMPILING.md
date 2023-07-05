

`OS`/`Deps`/`PyRT`:

- [x] `Unix`/`Unix`/`True?` - use for PyPI

- [ ] `Unix`/`Conda`

  NOTE: with this option, you need to ensure that CMake only
  finds conda compilers; you may need to install the conda-forge packages
  `fortran-compiler`, `cxx-compiler` and `c-compiler`

- [x] `Win32`/`Intel`/`False`
  python3.9 -m cibuildwheel --platform windows --arch AMD64

- [ ] `Win32`/`Conda`/


