# BPMN Parser

[![Publish to PyPI](https://github.com/danbailo/bpmn-parser/actions/workflows/publish.yaml/badge.svg?branch=main)](https://github.com/danbailo/bpmn-parser/actions/workflows/publish.yaml)
[![Tests and Linting](https://github.com/danbailo/bpmn-parser/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/danbailo/bpmn-parser/actions/workflows/tests.yaml) ![PyPI - Version](https://img.shields.io/pypi/v/bpmn-parser?color=%2334D058&label=pypi%20package) ![Coverage Status](./assets/coverage-badge.svg)

Simple structure that I([@danbailo](https://github.com/danbailo)) like use to build projects.

enjoy and... Python 🐍 for everthing 😄

## Make
The project uses a [Makefile](Makefile) to facilitate project installation, lint execution, typing and testing.

### Preparing virtual enviroment

It is highly recommended to use virtual environments when developing Python projects.

### Using poetry

Install [poetry](https://github.com/python-poetry/poetry) then install the project using Make.

```
make install
```

### Using pyenv

Install the [prerequisites](https://github.com/pyenv/pyenv/wiki/Common-build-problems#prerequisites) and then install [pyenv](https://github.com/pyenv/pyenv-installer). After install and configure pyenv, just install the project using Make.

```
make prepare_env_pyenv
```

then

```
make install
```

### Checkers

`make check_format` - Checks code formatting.

`make format` - Automatically formats the code.

`make check_lint` - Checks the code lint.

`make lint` - Formats the code by automatically correcting the lint.

`make check_types` - Checks the typing hinting of the code.

`make tests` - Runs the project's tests.

`make check_all` - Runs all the project's "checkers" and tests signaling when everything is ok. This way, it is certain that the pull-request pipeline will be ready to go to main.

All settings defined in formatting, typing, lint, etc. They are defined in the Python project configuration file - [pyproject.toml](pyproject.toml).
