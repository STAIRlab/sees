#!/bin/bash
# set -e -u -x
PLAT="$1"

repair_wheel() {
    wheel="$1"
    if ! auditwheel show "$wheel"; then
        echo "Skipping non-platform wheel $wheel"
    else
        auditwheel repair "$wheel" --plat "$PLAT" -w /io/wheelhouse/
    fi
}

# mkdir  /io/src/libg3/OTHER/dbin
# cmake -S /io/src/libg3/OTHER/ -B /io/src/libg3/OTHER/dbin
# cmake --build /io/src/libg3/OTHER/dbin

for PYBIN in /opt/python/cp3[1987]*/bin; do
  echo "Python: $(${PYBIN}/python --version)"
  echo "CMake:  $(cmake --version)"

  "${PYBIN}/python" -m pip install -U pip
  "${PYBIN}/python" -m pip install -U pybind11 #amoeba-build pybind11
  export pybind11_DIR=$("${PYBIN}/python" -m pybind11 --cmakedir)
  export PATH="${PYBIN}:${PATH}"
  MAKEFLAGS=-j9 "${PYBIN}/python" -m pip wheel /io/ -w wheelhouse/
  if [[ $? != 0 ]] 
  then 
    exit -1
  fi
done

# find -name libOpenSeesRT.so
# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
  cpxx="$(sed 's/.*-cp\(3[0-9]*\).*/\1/g' <<< $whl)"
  apath="/io/build/lib.linux-x86_64-cpython-${cpxx}/opensees/"
  ls $apath
  #LD_LIBRARY_PATH="$apath:${LD_LIBRARY_PATH}" repair_wheel "$whl"
  LD_LIBRARY_PATH="$apath" repair_wheel "$whl"
done


cp wheelhouse/*.whl /io/wheelhouse/

