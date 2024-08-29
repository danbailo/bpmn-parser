from unittest.mock import MagicMock

import pytest

from bpmn_parser.exceptions import NotBPMNFile
from bpmn_parser.parser import (
    BPMNParser,
)


def test_bpmn_parser_not_bpmn_file():
    mocked_file = MagicMock()
    mocked_file.suffix = '.foo'
    with pytest.raises(NotBPMNFile):
        BPMNParser(mocked_file)


def test_bpmn_parser_repr(bpmn_parser):
    assert repr(bpmn_parser) == 'BPMNParser(file_path=resources/flow.bpmn)'
