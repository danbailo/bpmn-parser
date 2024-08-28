import pytest

from legalops_commons.utils.bpmn.parser import (
    BPMNParser,
)


@pytest.fixture
def bpmn_parser():
    return BPMNParser('samples/bpmn_parser/flow.bpmn')


@pytest.fixture
def root(bpmn_parser: BPMNParser):
    return bpmn_parser.root
