mkdir src/libg3/cbin
mkdir src/libg3/OTHER/cbin

cd src/libg3/OTHER/cbin
cmake .. && make -j8

cd ../../cbin/
cmake .. \
  -DDependencies=Conda \
  -Dpybind11_ROOT="$(python3 -m pybind11 --cmakedir)" \
  -DNoOpenSeesPyRT=1 \
  -DCONDA_PREFIX="$CONDA_PREFIX"


cmake --build . --target OpenSeesRT -j5

