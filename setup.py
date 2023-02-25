#!/usr/bin/env python
import sys
from glob import glob
from os.path import basename, splitext

import amoeba
import setuptools

if __name__ == "__main__":
    setuptools.setup(
        cmdclass = {"build_ext": amoeba.BuildExtension, "cmake": amoeba.CMakeCommand},
        ext_modules = [
            amoeba.CMakeExtension(
                name = "rt",
                install_prefix="opensees",
                cmake_configure_options = [
                    "-G", "Unix Makefiles", # 
                    "-DDependencies=Conda",
                    "-DCMAKE_BUILD_TYPE=DEBUG",
                    "-DNoOpenSeesPyRT=True",
                    # "-DCMAKE_CXX_INCLUDE_WHAT_YOU_USE=include-what-you-use",
                    # '-DCMAKE_C_FLAGS_DEBUG="-g -O0"',
                    # '-DCMAKE_CXX_FLAGS_DEBUG="-g -O0"',
                    # "-DDependencies=Unix",

                    f"-DPYTHON_EXECUTABLE:FILEPATH={sys.executable}"
                ],
            )
        ]
    )

