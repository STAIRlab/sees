#!/usr/bin/env python
from glob import glob
from os.path import basename, splitext

#import setuptools
from skbuild import setup#, find_packages
from setuptools import find_packages

if __name__ == "__main__":
    setup(
        name="opensees",
        cmake_install_dir="src/opensees",
        cmake_args=['-DDependencies=Conda', "-DCMAKE_JOB_POOLS=8"],
        # cmake_install_target="OpenSeesPyRT",

         package_dir = {
             "": "src",
             #"units": "./src/opensees/units"
         },
        packages=["opensees"],

        #packages = find_packages("src"),
        py_modules = [splitext(basename(path))[0] for path in glob("src/*.py")]
        #packages = find_packages(where="src", include=["opensees", "opensees.*"], 
        #    exclude=[
        #        "build*",
        #        "dist*",
        #        "docs*",
        #        "tests*",
        #        "site*"
        #    ]),#["opensees"]

            # ext_modules=[
            #     setuptools.Extension(
            #         name='opensees.libOpenSeesRT',
            #         sources=[]
            #     ),
            #     setuptools.Extension(
            #         name='opensees.libOpenSeesPyRT',
            #         sources=[]
            #     )
            # ]
    )
