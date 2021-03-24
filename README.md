# pfinance
Python financial mathematics library

## TODO list (incomprehensive)
- add content
  - decide what content we actually want in this. Just functions? Models?
- make the tests a thing that actually works
  - need to decide on testing style
- decide on a style guide/best practices for variable names, etc.
- setup a github action
  - versioning and releasing
  - linting (pylint/flake8)
- get this thing actually hosted on PyPI/installable with pip

## Stuff in the venv
- wheel
- setuptools
- twine
- pytest
- pytest-runner

## Building and installing the library
- Clone the repo
- Navigate to the install directory
- Run `python setup.py bdist_wheel`
- Run `pip install ./dist/<wheel file>`
