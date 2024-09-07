from pathlib import Path
from typing import Optional, Union

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
        file_path (Union[Path, str]): path of bpmn file.
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

        self._service_task: Optional[ServiceTask] = None
        self._user_task: Optional[UserTask] = None
        self._sequence_flow: Optional[SequenceFlow] = None
        self._intermediate_catch_event: Optional[IntermediateCatchEvent] = None
        self._exclusive_gateway: Optional[ExclusiveGateway] = None

    @property
    def service_task(self):
        """Parse all Service Tasks from this BPMN."""
        if self._service_task is not None:
            return self._service_task

        self._service_task = ServiceTask(self.root)
        return self._service_task

    @property
    def user_task(self):
        """Parse all User Task from this BPMN."""
        if self._user_task is not None:
            return self._user_task

        self._user_task = UserTask(self.root)
        return self._user_task

    @property
    def sequence_flow(self):
        """Parse all Sequence Flow from this BPMN."""
        if self._sequence_flow is not None:
            return self._sequence_flow

        self._sequence_flow = SequenceFlow(self.root)
        return self._sequence_flow

    @property
    def intermediate_catch_event(self):
        """Parse all Intermediate Catch Event from this BPMN."""
        if self._intermediate_catch_event is not None:
            return self._intermediate_catch_event

        self._intermediate_catch_event = IntermediateCatchEvent(self.root)
        return self._intermediate_catch_event

    @property
    def exclusive_gateway(self):
        """Parse all Exclusive Gateway from this BPMN."""
        if self._exclusive_gateway is not None:
            return self._exclusive_gateway

        self._exclusive_gateway = ExclusiveGateway(self.root)
        return self._exclusive_gateway

    @property
    def refresh(self):
        """Refresh the BPMN if the file get some modify."""
        self.tree = parse(self.file_path, self.xml_parser)
        self.root = self.tree.getroot()

        del self._service_task
        self._service_task = None

        del self._user_task
        self._user_task = None

        del self._sequence_flow
        self._sequence_flow = None

        del self._intermediate_catch_event
        self._intermediate_catch_event = None

        del self._exclusive_gateway
        self._exclusive_gateway = None

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}('
            f'service_task={len(self.service_task)}, '
            f'user_task={len(self.user_task)}, '
            f'sequence_flow={len(self.sequence_flow)}, '
            f'intermediate_catch_event={len(self.intermediate_catch_event)}, '
            f'exclusive_gateway={len(self.exclusive_gateway)}, '
            f'file_path={self.root.base}'
            ')'
        )
