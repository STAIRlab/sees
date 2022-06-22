#!/usr/bin/env python

#import setuptools
from skbuild import setup

if __name__ == "__main__":
    setup(
        cmake_install_dir="src/opensees/",
        cmake_args=['-DDependencies=Conda'],
        cmake_install_target="OpenSeesRT"
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
