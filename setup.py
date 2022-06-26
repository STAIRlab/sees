#!/usr/bin/env python
from glob import glob
from os.path import basename, splitext

from skbuild import setup
from setuptools import find_packages

if __name__ == "__main__":
    setup(
        name="opensees",
        cmake_install_dir="src/opensees",
        cmake_args  = ["-DDependencies=Conda"],
        package_dir = {"": "src"},
        packages    = ["opensees", "opensees.emit", "opensees.units"],
        #packages = find_packages("src"),
        py_modules  = [
            splitext(basename(path))[0] for path in glob("src/*.py")
        ] + [
            splitext(basename(path))[0] for path in glob("src/units/*.py")
        ] + [
            splitext(basename(path))[0] for path in glob("src/emit/*.py")
        ]
    )

