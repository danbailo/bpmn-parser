from pathlib import Path
from typing import Union

from lxml.etree import XMLParser, _Element, _ElementTree, parse

from bpmn_parser._exclusive_gateway import ExclusiveGateway
from bpmn_parser._intermediate_catch_event import IntermediateCatchEvent
from bpmn_parser._sequence_flow import SequenceFlow
from bpmn_parser._service_task import ServiceTask
from bpmn_parser._user_task import UserTask
from bpmn_parser.exceptions import NotBPMNFile


class BPMNParser:
    """Implement a Python API to a BPMN. With this, is possible to get and list some
    attributes of BPMN, such as: service tasks, user tasks, sequence flows, etc.


    Args:
        file_path (Path): path of bpmn file.
    """

    def __init__(self, file_path: Union[Path, str]):
        if isinstance(file_path, str):
            file_path = Path(file_path)

        if file_path.suffix != '.bpmn':
            raise NotBPMNFile()

        self.file_path = file_path
        self.xml_parser = XMLParser(remove_blank_text=True)
        self.tree: _ElementTree = parse(file_path, self.xml_parser)
        self.root: _Element = self.tree.getroot()

    @property
    def service_task(self):
        """Parse all Service Tasks from this BPMN."""
        return ServiceTask(self.root)

    @property
    def user_task(self):
        """Parse all User Task from this BPMN."""
        return UserTask(self.root)

    @property
    def sequence_flow(self):
        """Parse all Sequence Flow from this BPMN."""
        return SequenceFlow(self.root)

    @property
    def intermediate_catch_event(self):
        """Parse all Intermediate Catch Event from this BPMN."""
        return IntermediateCatchEvent(self.root)

    @property
    def exclusive_gateway(self):
        """Parse all Exclusive Gateway from this BPMN."""
        return ExclusiveGateway(self.root)

    @property
    def refresh(self):
        """Refresh the BPMN if the file get some modify."""
        self.tree = parse(self.file_path, self.xml_parser)
        self.root = self.tree.getroot()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(file_path={self.root.base})'
