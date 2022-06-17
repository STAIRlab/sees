#!/usr/bin/env python

#import setuptools
from skbuild import setup

if __name__ == "__main__":
    setup(
        cmake_install_dir="src/opensees/"
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
