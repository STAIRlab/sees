#!/usr/bin/env python
import os
import sys
from glob import glob
from os.path import basename, splitext

import amoeba
import setuptools

options = {
    "PyPI":  "Unix",
    "Unix":  "Unix",
    "Conda": "",
    "Win32": ""
}

try:
    import pybind11
    OpenSeesPyRT_Config = [
        f"-Dpybind11_DIR:FILEPATH={pybind11.get_cmake_dir()}",
    ]

except ImportError:
    OpenSeesPyRT_Config = []

if __name__ == "__main__":
    setuptools.setup(
        cmdclass = {"build_ext": amoeba.BuildExtension, "cmake": amoeba.CMakeCommand},
        ext_modules = [
            amoeba.CMakeExtension(
#               name = "rt",        # PyPA
                name = "local",
                install_prefix="opensees",
                cmake_configure_options = [
                    "-G", "Unix Makefiles",

                    f"-DCMAKE_PREFIX_PATH:FILEPATH={os.environ['CONDA_PREFIX']}",
                    f"-DCMAKE_IGNORE_PATH:FILEPATH=/usr/lib/;/lib",
                    f"-DDependencies=Conda",
                    # "-DDependencies=Unix",

                    "-DCMAKE_BUILD_TYPE=DEBUG",
                    # "-DCMAKE_BUILD_TYPE=Release",
                    "-DOPENSEESRT_VERSION=0.0.34",
                    # "-DNoOpenSeesPyRT=True",
                    # "-DCMAKE_CXX_INCLUDE_WHAT_YOU_USE=include-what-you-use",
                    *OpenSeesPyRT_Config,

                    f"-DPYTHON_EXECUTABLE:FILEPATH={sys.executable}"
                ],
                cmake_build_options=["--target", "OpenSeesRT"]
            )
        ]
    )

