#!/usr/bin/env python
import sys
from glob import glob
from os.path import basename, splitext

import amoeba
import setuptools

if __name__ == "__main__":
    setuptools.setup(
        cmdclass = {"build_ext": amoeba.BuildExtension},
        ext_modules = [
            amoeba.CMakeExtension(
                name = "rt",
                install_prefix="opensees",
                cmake_configure_options = [
                    "-G", "Unix Makefiles", "-DDependencies=Conda"
                ],
                #cmake_configure_defaults = {}
            )
        ]
    )

    # args = dict(
    #     #package_dir = {"": "src"},
    #     #packages    = ["opensees", "opensees.emit", "opensees.units"],
    #     #packages = find_packages("src"),
    #     # cmake_install_dir="src/opensees",
    #     name="opensees",
    #     cmake_args = [
    #         "-G", "Unix Makefiles",
    #         "-DDependencies=Conda"
    #     ],
    # )
    # args["package_dir"] = {"": "src"}

    # if "develop" == sys.argv[1]:
    #     import amoeba
    #     from amoeba import setup
    #     args["cmake_args"] += [
    #         "-DCMAKE_INSTALL_PREFIX:PATH=/home/claudio/packages/opensees-pypi-test/src/opensees"
    #     ]
    #     try:
    #         setup(**args)

    #     except amoeba.exceptions.SKBuildInstallError:
    #         if "cmake_args" in args: del args["cmake_args"]
    #         del args["package_dir"]
    #         setuptools.setup(**args)



