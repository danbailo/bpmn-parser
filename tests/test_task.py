from unittest.mock import MagicMock, patch

import pytest
from lxml.etree import _Element

from bpmn_parser._task import BPMNTagNotFound, Task


class SomeTask(Task):
    def __init__(self, root: _Element):
        super().__init__(root)

    @property
    def list(self):
        pass

    def get(self):
        pass


@patch('bpmn_parser._task.re.search', return_value=None)
def test_bpmn_tag_not_found(mocked_re_search: MagicMock, bpmn_parser):
    with pytest.raises(BPMNTagNotFound):
        SomeTask(bpmn_parser.root)

    mocked_re_search.assert_called_once()
