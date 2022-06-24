#!/usr/bin/env python

#import setuptools
from skbuild import setup#, find_packages

if __name__ == "__main__":
    setup(
        cmake_install_dir="src/opensees/",
        cmake_args=['-DDependencies=Conda', "-DCMAKE_JOB_POOLS=8"],
        cmake_install_target="OpenSeesPyRT",

        package_dir = {
            "": "src"
        },
        packages=["opensees"]

        #package = find_packages(where="src"),#["opensees"]

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
