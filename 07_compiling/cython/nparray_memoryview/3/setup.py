#!/usr/bin/env python
# -*- coding: utf8 -*-

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
import os


os.environ["CC"] = "gcc-7"

# for notes on compiler flags e.g. using
# export CFLAGS=-O2
# so gcc has -O2 passed (even though it doesn't make the code faster!)
# http://docs.python.org/install/index.html

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("calculate", ["cython_np.pyx"],
                           include_dirs=[np.get_include(), '/'.join(np.get_include().split('/')[:-1])])]
)
