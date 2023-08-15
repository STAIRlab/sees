#!/usr/bin/env python
import os
import sys
from glob import glob
from pathlib import Path
from os.path import basename, splitext

import amoeba
import setuptools

options = {
    "PyPI":  "Unix",
    "Unix":  "Unix",
    "Conda": "",
    "Win32": ""
}

if os.name == "nt":
    EnvArgs = []

elif "CONDA_PREFIX" in os.environ:
    EnvArgs = [
        "-DDependencies=Conda",
        f"-DCMAKE_PREFIX_PATH:FILEPATH={os.environ['CONDA_PREFIX']}",
        f"-DCMAKE_IGNORE_PATH:FILEPATH=/usr/lib/;/lib",
    ]

else:
    EnvArgs = [
        "-DDependencies=Unix",
    ]


try:
    import pybind11
    OpenSeesPyRT_Config = [
        f"-Dpybind11_DIR:FILEPATH={pybind11.get_cmake_dir()}",
        f"-DPYTHON_EXECUTABLE:FILEPATH={sys.executable}"
    ]

except ImportError:
    OpenSeesPyRT_Config = ["-DNoOpenSeesPyRT=True"]

if __name__ == "__main__":
    setuptools.setup(
        data_files=[('bin', [*map(str,Path("win32/").glob("*.*"))]),
        ] if os.name == "nt" else [],
        cmdclass = {"build_ext": amoeba.BuildExtension, 
                    "cmake": amoeba.CMakeCommand},
        ext_modules = [
            amoeba.CMakeExtension(
#               name = "pypa",        # PyPA
                name = "local",
                install_prefix="opensees",
                cmake_configure_options = [
                    "-G", "Unix Makefiles",
                    *EnvArgs,
#                   "-DCMAKE_BUILD_TYPE=DEBUG",
                    "-DCMAKE_BUILD_TYPE=RELEASE",
                    "-DOPENSEESRT_VERSION=0.0.45",
                    "-DProfileBuild:BOOL=TRUE",
                    *OpenSeesPyRT_Config,

                ],
                cmake_build_options=["-j15",
                    "--target", "OpenSeesRT",
                    "--target", "OpenSeesPyRT"
                ]
            )
        ]
    )

