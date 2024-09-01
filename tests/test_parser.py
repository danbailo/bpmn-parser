from unittest.mock import MagicMock, patch

import pytest

from bpmn_parser.exceptions import NotBPMNFile
from bpmn_parser.parser import (
    BPMNParser,
)


def test_not_bpmn_file():
    mocked_file = MagicMock()
    mocked_file.suffix = '.foo'
    with pytest.raises(NotBPMNFile):
        BPMNParser(mocked_file)


def test_repr(bpmn_parser):
    assert repr(bpmn_parser) == (
        'BPMNParser('
        'service_task=4, '
        'user_task=2, '
        'sequence_flow=24, '
        'intermediate_catch_event=2, '
        'exclusive_gateway=10, '
        'file_path=resources/flow.bpmn'
        ')'
    )


@patch('bpmn_parser.parser.BPMNParser.exclusive_gateway')
@patch('bpmn_parser.parser.BPMNParser.intermediate_catch_event')
@patch('bpmn_parser.parser.BPMNParser.sequence_flow')
@patch('bpmn_parser.parser.BPMNParser.user_task')
@patch('bpmn_parser.parser.BPMNParser.service_task')
@patch('bpmn_parser.parser.parse')
def test_refresh(
    mocked_parse: MagicMock,
    mocked_service_task: MagicMock,
    mocked_user_task: MagicMock,
    mocked_sequence_flow: MagicMock,
    mocked_intermediate_catch_event: MagicMock,
    mocked_exclusive_gateway: MagicMock,
    bpmn_parser,
):
    mocked_parse.return_value.getroot.return_value.base = 'resources/flow2.bpmn'
    bpmn_parser.file_path = 'resources/flow2.bpmn'
    bpmn_parser.refresh
    assert repr(bpmn_parser) == (
        'BPMNParser('
        'service_task=0, '
        'user_task=0, '
        'sequence_flow=0, '
        'intermediate_catch_event=0, '
        'exclusive_gateway=0, '
        'file_path=resources/flow2.bpmn'
        ')'
    )
