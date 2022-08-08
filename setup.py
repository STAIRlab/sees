#!/usr/bin/env python
import sys
from glob import glob
from os.path import basename, splitext

import setuptools
#from setuptools import find_packages#, setup

if __name__ == "__main__":
    args = dict(
        #package_dir = {"": "src"},
        #packages    = ["opensees", "opensees.emit", "opensees.units"],
        #packages = find_packages("src"),
        # cmake_install_dir="src/opensees",
        # cmake_args  = ["-DDependencies=Conda"],
        name="opensees",
        cmake_args = ["-G", "Unix Makefiles"]
    )

    if "develop" == sys.argv[1]:
        import amoeba
        from amoeba import setup
        args["package_dir"] = {"opensees": "src/opensees"}
        args["cmake_args"] += [
            "-DCMAKE_INSTALL_PREFIX:PATH=/home/claudio/packages/opensees-pypi-test/src/opensees"
        ]
        try:
            setup(**args)

        except amoeba.exceptions.SKBuildInstallError:
            if "cmake_args" in args: del args["cmake_args"]
            del args["package_dir"]
            setuptools.setup(**args)

    else:
        from skbuild import setup
        setup(**args)


