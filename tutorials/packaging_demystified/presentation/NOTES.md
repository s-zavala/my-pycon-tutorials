# Shipping and Running Python code on other machines
[gaborbernat/pi-approx](https://github.com/gaborbernat/pi-approx)

Use a script for approximating pi with the Gregory-Leibniz series.
## Make code available - 2 ways
- Developer method: >>> from pi_approx import approximate_pi
    - Make a library
- End-user method: $ python ./pi_approx.py
    - Make an application
## Application requirements
- Python interpreter
- Exact dependencies (obfuscated)
- Source code (obfuscated)
- Entry point
## Library requirements
- Python interpreter
- Compatible dependencies
- Source code
## How to package a library
### Context
Two types of python interpreters are the global/system interpreter and virtual environments (venv, virtualenv).
Virtual environments are isolated.
Users import libraries within either python interpreter.
Not all modules are alike. The types of modules are built-ins, standard library, and site-packages(unique to user or env).
The types of importers are built-in, frozen, third-party.
```
>>> import sys
>>> for importer in sys.meta_path:
        print(repr(importer))
```
Python defines two directories as library locations: platlib and purelib.
```
>>> import sys, sysconfig
>>> sysconfig.get_path('purelib')
>>> sysconfig.get_path('platlib')
```
### Parts of a library
- The source code either as a module or package
- Entry points: console/GUI
- Metadata
### Python project on dev machine
- project
    - pi_approx.py
    - test_pi_approx.py
    - LICENSE
    - README.md
    - github
        - workflows
            - check.yaml
    -pyproject.toml
### Python project on user machine
- pi_approx.py
- pi_approx-1.0.dist-info
    - INSTALLER
    - LICENSE
    - METADATA
    - RECORD
    - REQUESTED
    - WHEEL
### Package types
#### SDIST
- Source distribution is similar to the python project on dev machine.
- project
    - pi_approx.py
    - test_pi_approx.py
    - LICENSE
    - README.md
    - X github
        - X workflows
            - X check.yaml
    -pyproject.toml
#### WHEEL
The wheel is what we want on the target/user machine.
- pi_approx.py
- pi_approx-1.0.dist-info
    - INSTALLER
    - LICENSE
    - METADATA
    - RECORD
    - REQUESTED
    - WHEEL
When you install a package you always install a wheel. If there is a sdist then you build a wheel from it.
## Shipping a library
- Dev source tree
- Build a package
- package
- Upload package
- Central Package Store
## Consume a package
- Centeral Package Store
- package
- Discover & download package
- is wheel
    - no -> build wheel then ->
    - yes -> install wheel
- Target machine
## History of packaging
- 2000 distutils
- 2004 setuptools, problem with build dependencies, would break
- 2014 PEP-427 introduced wheels
- 2015 flit library, uses declarative over dynamic
- 2018 poetry library
## [flit](https://flit.readthedocs.io/en/latest/)
- Add a docstring and `__version__ = "x.x.x"` to your module.
- Run `flit init` inside the module directory to make a pyproject.toml file.
    - Customize pyproject.toml
        - requires-python = ">=3.8" for python version under `[project]`
        - dependencies in requires list under `[build-system]`.
- Run `flit build` to build a wheel and sdist from the package.
- Upload to PyPI with `flit publish`.
- Simple test `>>> python -m pip install <path-to-.tar.gz-file>`
## Speed up with Cython, uses setuptools(instead of flit) and builder
- Install [setuptools](https://setuptools.pypa.io/en/latest/userguide/index.html)
- Add a pyproject.toml file with this format:
```
[build-system]
requires = ["setuptools >= x.x.x", "wheel >= x.x.x"]
build-backend = "setuptools.build_meta"
```
- Add a setup.cfg
```
[metadata]
name = mypackage
version = 0.0.1

[options]
packages = mypackage
install_requires =
    requests
    importlib; python_version == "2.6"
```
- Add a setup.py
```
from setuptools import setup

setup(
    name='mypackage',
    version='0.0.1',
    packages=['mypackage'],
    install_requires=[
        'requests',
        'importlib; python_version == "2.6"',
    ],
)
```
- Run `python -m build` to make a `dist` directory with wheel and sdist.
- Install [Cython](https://cython.readthedocs.io/en/latest/index.html)
- Copy source code .py file and rename copy with .pyx extension (eg. pi_approx.py -> py_approx_cy.pyx)
- Add Cython to pyproject.toml to the requires list:
```
requires = [
    "setuptools >= 41.0.0",
    "wheel >= 0.30.0",
    "cython",
]
```
- Add `ext_modules=cythonize` to setup.py setup() arguments.
`ext_modules=cythonize("pi_approx_cy.pyx")`
- Run `pyproject-build --sdist --wheel` to build package.
- Make a virtualenv, run `python -m pip install <packagename>` to install library.
- Import into python interpreter and use.