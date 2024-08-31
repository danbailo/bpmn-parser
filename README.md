<p align="center">
    <em>BPMN Parser, read .bpmn files as Python.</em>
</p>
<p align="center">
<a href="https://github.com/danbailo/bpmn-parser/actions/workflows/publish.yaml" target="_blank">
    <img src="https://github.com/danbailo/bpmn-parser/actions/workflows/publish.yaml/badge.svg" alt="Test">
</a>
<a href="https://github.com/danbailo/bpmn-parser/actions/workflows/tests.yaml?query=branch=main" target="_blank">
    <img src="https://github.com/danbailo/bpmn-parser/actions/workflows/tests.yaml/badge.svg?branch=main" alt="Tests">
</a>
<a href="https://github.com/danbailo/bpmn-parser/actions/workflows/tests.yaml?query=branch=main" target="_blank">
    <img src="https://codecov.io/gh/danbailo/bpmn-parser/branch/main/graph/badge.svg" alt="Coverage">
<a href="https://pypi.org/project/bpmn-parser" target="_blank">
    <img src="https://img.shields.io/pypi/v/bpmn-parser?color=%252334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/bpmn-parser" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/bpmn-parser?color=g" alt="Python Versions">
</a>
</p>

---

**Documentation**: <a href="https://danbailo.github.io/bpmn-parser/" target="_blank">https://danbailo.github.io/bpmn-parser/</a>

**Source Code**: <a href="https://github.com/danbailo/bpmn-parser" target="_blank">https://github.com/danbailo/bpmn-parser</a>

---

BPMN Parser is a library to read and parse `.bpmn` files with Python. With this, you can create another things related with BPMN, such as linters, tests, validate BPMN flows, etc.

The key features are:

* **Easy to use**: It's easy to use for the final users.
* **Start simple**: Just import and use!
* **Support to build other applications**: This library allow and helps to build another applications, such linters, tests, validators, etc.

## Installation

Create and activate a virtual environment and then install **BPMN Parser**:

<div class="termy">

```console
$ pip install bpmn-parser
---> 100%
Successfully installed bpmn-parser
```

</div>

## Example

* Create a file `main.py` with:

```python
# Import BPMN Parser
from bpmn_parser import BPMNParser

# Instance it
bpmn_parser = BPMNParser('/path/to/bpmn/flow.bpmn')

# Listing service tasks
for service_task in bpmn_parser.service_task.list:
    print(service_task)

# Getting service task
print(bpmn_parser.service_task.get('Activity_139q5mt'))
```

## Development

### Using pyenv

Install the [prerequisites](https://github.com/pyenv/pyenv/wiki/Common-build-problems#prerequisites) and then install [pyenv](https://github.com/pyenv/pyenv-installer). After install and configure pyenv, just install the project using Make.

```bash
make prepare_env_pyenv
```

### Using poetry

```bash
pip install poetry
```

#### Then, just install the project

```bash
make install
```

### Project commands

| Command | Description |
|-|-|
| `make install` | Install project as dev |
| `make check_format` | Check code format |
| `make format` | Format the code |
| `make check_lint` | Check code lint |
| `make lint` | Lint the code |
| `make check_types` | Check code types |
| `make tests` | Run tests |
| `make check_all` | Run all checkers of project |
| `make prepare_env_pyenv` | Prepare an enviroment with [pyenv](https://github.com/pyenv/pyenv) |