from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("pi_approx_cy.pyx"),
)

