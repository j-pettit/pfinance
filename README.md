# pfinance
Python financial mathematics library.

## Installation
### Using pip

- run `pip install pfinance`

### Building from source

- clone the repo
- run `python setup.py bdist_wheel`

## Publishing to PyPI

Package builds are automatically published to PyPI on each version bump. Version changes should follow standard [semantic versioning guideline](https://semver.org/).

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
