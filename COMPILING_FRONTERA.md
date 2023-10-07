# Compiling on FRONTERA

*Last Update: October 7, 2023*

The following instructions outline the compilation process on the [FRONTERA](https://www.tacc.utexas.edu/systems/frontera/) supercomputer.
`Anaconda` is not involved, to rely exclusively on the optimized libraries available on the cluster and avoid conflicts.

1. Start an interactive session, since we will be compiling with all available cores to save time. See [[1](https://frontera-portal.tacc.utexas.edu/user-guide/conduct/)].
```shell
idev -m 120 # run for 2 hours
```
2. Load the appropriate modules. See [[2]()].
```shell
module load impi
module load python3/3.9.2  # this is currently the latest available python 3
```
3. Obtain the source code
```shell
cd $SCRATCH

git clone --recurse-submodules https://github.com/BRACE2/OpenSeesRT
cd OpenSeesRT

# Pull latest changes in `src/libg3`, soon to be resolved.
# cd src/libg3
# git pull origin master
# cd ../../
```

4. Configure environment variables
```shell
# set compilers with environment variables
export CC=$(which mpicc)
export CXX=$(which mpicxx)
export FC=$(which mpif90)
```

5. Modify `CMakeLists.txt` files:

| File                                              | Action                                          |
| :------------------------------------------------ | :-----------------------------------------------|
| `/src/libg3/CMakeLists.txt`                       | Uncomment `find_package(MKL)`.                  |
| `/src/libg3/SRC/runtime/parallel/CMakeLists.txt`  | Remove the two `/usr/lib/libscalapack.so` lines |

Also modify `setup.py` to specify `"-j52"` towards the end of the file, utilizing all cores for parallel compilation.

6. Install `OpenSeesRT`
```shell
pip3 install --user -e .  # installs to $HOME/.local
```

7. Run

Before running any code that requires `OpenSeesRT`, the environment setup should be configured as follows:
```
module load impi
module load python3/3.9.2
export LD_PRELOAD=/opt/intel/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64_lin/libmkl_def.so:/opt/intel/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64_lin/libmkl_avx2.so:/opt/intel/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64_lin/libmkl_core.so:/opt/intel/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so:/opt/intel/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64_lin/libmkl_intel_thread.so:/opt/intel/compilers_and_libraries_2020.1.217/linux/compiler/lib/intel64_lin/libiomp5.so
```

Use `python3` instead of `python`, and `pip3` instead of `pip` (or create aliases if desired).

---

Optional: Recompile specifying the instruction set.
See [[3](https://frontera-portal.tacc.utexas.edu/user-guide/building/#architecture-specific-flags)].

Edit `src/libg3/CMakeLists.txt` and append the following optimization options:
```
    $<$<CONFIG:RELEASE>:-mkl=cluster>
    $<$<CONFIG:RELEASE>:-xCORE-AVX512>
```

```shell
python3 setup.py cmake
cd build/temp.linux-x86_64-cpython-39_pypa
make OpenSeesRT -j52

export OPENSEESRT_LIB=$SCRATCH/OpenSeesRT/build/temp.linux-x86_64-cpython-39_pypa/src/libg3/SRC/runtime/libOpenSeesRT.so

```


---

Links:\
[[1](https://frontera-portal.tacc.utexas.edu/user-guide/conduct/)] Good Conduct on Frontera\
[[2](https://frontera-portal.tacc.utexas.edu/user-guide/admin/#using-modules-to-manage-your-environment)] Using Modules to Manage your Environment\
[[3](https://frontera-portal.tacc.utexas.edu/user-guide/building/#architecture-specific-flags)] Architecture-Specific Flags
