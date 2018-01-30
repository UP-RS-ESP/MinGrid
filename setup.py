from distutils.core import setup, Extension
import numpy

mod = Extension('MinGrid',
    include_dirs = [numpy.get_include()],
    sources = ['MinGrid.c'],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-lgomp']
)

setup (name = 'MinGrid',
    author = 'Aljoscha Rheinwalt',
    author_email = 'aljoscha.rheinwalt@uni-potsdam.de',
    ext_modules = [mod]
)
