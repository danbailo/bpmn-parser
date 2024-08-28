import pytest

from bpmn_parser.parser import (
    BPMNParser,
)


@pytest.fixture
def bpmn_parser():
    return BPMNParser('resources/flow.bpmn')
