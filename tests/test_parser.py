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
    assert repr(bpmn_parser) == 'BPMNParser(file_path=resources/flow.bpmn)'


@patch('bpmn_parser.parser.parse')
def test_refresh(mocked_parse: MagicMock, bpmn_parser):
    mocked_parse.return_value.getroot.return_value.base = 'resources/flow2.bpmn'
    bpmn_parser.file_path = 'resources/flow2.bpmn'
    bpmn_parser.refresh
    assert repr(bpmn_parser) == 'BPMNParser(file_path=resources/flow2.bpmn)'
    mocked_parse.assert_called_once()
