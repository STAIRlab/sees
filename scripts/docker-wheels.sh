#!/bin/bash
yum install tcl-devel msql-devel lapack-devel ninja-build

function fix_cmake {
	if [ -n "$IS_OSX" ]; then
		brew update
		brew upgrade cmake || brew install cmake
	else
		# Fix cmake installation linking the appropriate binary
		# pip install cmake
		# rm `python -c 'import sys; print(sys.executable[:-6])'`cmake
		CMAKE_BIN=`${PYBIN}/python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`/cmake/data/bin/cmake
		ln -sf ${CMAKE_BIN} /usr/local/bin/cmake
	fi
}


# following, roughly, https://github.com/pypa/python-manylinux-demo/blob/master/travis/build-wheels.sh
for PYBIN in /opt/python/cp3[789]*/bin; do
  echo "${PYBIN}"
  "${PYBIN}/pip" install -U pip 
  "${PYBIN}/pip" install -U build 'cmake<3.23' ninja pybind11
  CMAKE_BIN=`${PYBIN}/python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`/cmake/data/bin/cmake
  ln -sf ${CMAKE_BIN} /usr/local/bin/cmake
  "${PYBIN}/pip" wheel /io/ -w wheelhouse/
done
cp wheelhouse/*.whl /io/wheelhouse/

