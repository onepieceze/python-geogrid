from distutils.core import setup, Extension
import os
import numpy as np

def numpy_include():
    try:
        inc = np.get_include()
    except AttributeError:
        inc = np.get_numpy_include()
    return inc

np_inc = numpy_include()

script_root = os.path.dirname(os.path.realpath(__file__))
src_root    = f'{script_root}/geogrid/src/'

extensions = [
      Extension('_python_geogrid', [src_root+'python_geogrid_wrap.c', src_root+'write_geogrid.c', src_root+'read_geogrid.c'], include_dirs=[np_inc])]

setup(name  = 'python_geogrid',
      version = "1.0",
      ext_modules = extensions,
      py_modules = ['python_geogrid'],
      package_dir = {'' : 'geogrid/src'}
     )