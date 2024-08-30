# BPMN Parser

[![Publish to PyPI](https://github.com/danbailo/bpmn-parser/actions/workflows/publish.yaml/badge.svg)](https://github.com/danbailo/bpmn-parser/actions/workflows/publish.yaml) [![Tests and Linting](https://github.com/danbailo/bpmn-parser/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/danbailo/bpmn-parser/actions/workflows/tests.yaml) ![Python Versions](https://img.shields.io/pypi/pyversions/bpmn-parser?color=g) ![PyPI - Version](https://img.shields.io/pypi/v/bpmn-parser?color=%252334D058&label=pypi%20package) ![Coverage Status](./assets/coverage-badge.svg)

A simple BPMN Parser implemented in Python.

Works like an API.

Example:

```python
In [1]: from bpmn_parser import BPMNParser

In [2]: bpmn_parser = BPMNParser('/path/to/bpmn/flow.bpmn')

In [3]: bpmn_parser
Out[3]: BPMNParser(file_path=/path/to/bpmn/flow.bpmn)

In [4]: bpmn_parser.service_task.list
Out[4]: 
[ServiceTaskElement(id='Activity_0psrd5x', name='Example Worker_1', execution_listeners=[], topic_name='example-worker', type='external'),
 ServiceTaskElement(id='Activity_139q5mt', name='Another Worker_1', execution_listeners=[], topic_name='another-worker', type='external'),
 ServiceTaskElement(id='Activity_12xjm8v', name='Example BPMN_1', execution_listeners=[], topic_name=None, type=None)]

In [5]: bpmn_parser.service_task.get('Activity_139q5mt')
Out[5]: ServiceTaskElement(id='Activity_139q5mt', name='Another Worker_1', execution_listeners=[], topic_name='another-worker', type='external'
```

### Installation

To install, just run:

```
pip install bpmn-parser
```

### How to use
...

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

### Install

```bash
make install
```

### Project commands

| Command | Description |
|-|-|
| `make tests` | Runs all unit tests |
| `make format` | Format the code |
| `make lint` | Lint the code |


## To do
- [ ] Create Elements