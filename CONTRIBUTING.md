# Contributing Guidelines
Thank you for your interest in contributing to pfinance! Below are some general guidelines to make contributions to the repo easier and more streamlined.

## Issue Tracking
Issues should be created and tracked through GitHub.

## Testing and Linting
Tests are written using pytest. Linting uses flake8 with some minor modifications. Tests and linting can be run using nox.

### Running tests and linting
- navigate to the root directory of the project
- run `nox` to run all sessions
- run `nox -s <session>` to run only a single session, e.g. `nox -s lint`
