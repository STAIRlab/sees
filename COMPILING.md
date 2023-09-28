

To clone with submodules:

```shell
git clone --recurse-submodules https://github.com/BRACE2/OpenSeesRT
```



----------------------------------------------------------



`OS`/`Deps`/`PyRT`:


- [ ] `Unix`: Conda

  When using conda, you need to ensure that CMake only
  finds conda compilers. It is best to install the following packages

  ```shell
  conda install -c conda-forge fortran-compiler cxx-compiler c-compiler openblas
  ```


- [ ] **Windows**: Intel and Conan

  ```shell
  python -m pip install -e .
  ```



## Other

- [x] **Windows** CI build

  ```shell
  python3.9 -m cibuildwheel --platform windows --arch AMD64
  
  python scripts\win_repair.py win32 wheelhouse\opensees-0.0.47*
  ```


- [x] `Unix`/`Unix` CI build

