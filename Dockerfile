FROM quay.io/pypa/manylinux_2_28_x86_64

ADD src/libg3/OTHER /OTHER

RUN yum install -y tcl-devel mysql-devel lapack-devel
RUN for PYBIN in /opt/python/*/bin; do "${PYBIN}/pip" install -U pip ; PIP_ONLY_BINARY=cmake  "${PYBIN}/pip" install cmake'<3.23'; done

# RUN for PYTHON in /opt/python/cp3[7891]*/bin/python; do "${PYTHON}" -m pip install -U pip; done
# RUN for PYTHON in /opt/python/cp3[7891]*/bin/python; do "${PYTHON}" -m pip install -U pybind11; done

