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

## Releasing
Releases are automatically created and published to PYPI on commits with tags beginning with `v`. Version numbers should follow [semantic versioning guidelines](https://semver.org/). 0.0.x builds indicate alpha versions, and 0.x.x indicate beta versions.

### Publishing a new release
- tag the latest commit with `git tag "v<version>"`, e.g. `git tag "v0.0.7"`
- push the tag to remote `git push origin v<version>`
- allow the actions to run for the release to be created and published
