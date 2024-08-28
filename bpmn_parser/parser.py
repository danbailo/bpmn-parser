from pathlib import Path

from lxml.etree import XMLParser, _Element, _ElementTree, parse

from bpmn_parser.exclusive_gateway import ExclusiveGateway
from bpmn_parser.intermediate_catch_event import IntermediateCatchEvent
from bpmn_parser.sequence_flow import SequenceFlow
from bpmn_parser.service_task import ServiceTask
from bpmn_parser.user_task import UserTask


class BPMNParser:
    def __init__(self, path: Path):
        xml_parser = XMLParser(remove_blank_text=True)
        self.tree: _ElementTree = parse(path, xml_parser)
        self.root: _Element = self.tree.getroot()

    @property
    def service_task(self):
        return ServiceTask(self.root)

    @property
    def user_task(self):
        return UserTask(self.root)

    @property
    def sequence_flow(self):
        return SequenceFlow(self.root)

    @property
    def intermediate_catch_event(self):
        return IntermediateCatchEvent(self.root)

    @property
    def exclusive_gateway(self):
        return ExclusiveGateway(self.root)
