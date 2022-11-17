from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

exts = (cythonize("number_cy.pyx"))
setup(include_dirs=[numpy.get_include()], ext_modules = exts)