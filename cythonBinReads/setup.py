from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("binReads", ["binReads.pyx"])]

setup(
  name = 'Bin reads',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)