import re
from abc import ABC, abstractmethod
from dataclasses import dataclass

from lxml.etree import _Element


@dataclass
class ExecutionListener:
    expression: str
    event: str


@dataclass
class BPMNElement:
    id: str
    name: str


@dataclass
class TaskElement(BPMNElement):
    execution_listeners: list[ExecutionListener]


class BPMNTagNotFound(Exception):
    message = 'BPMN tag not found!'

    def __init__(self):
        super().__init__(self.message)


class Task(ABC):
    def __init__(self, root: _Element):
        self.root = root

        if not (match := re.search(r'{(?P<tag>.+)}', self.root.tag)):
            raise BPMNTagNotFound()

        self.bpmn_tag = match['tag']
        self.camunda_tag = 'http://camunda.org/schema/1.0/bpmn'
        self.xml_schema_tag = 'http://www.w3.org/2001/XMLSchema-instance'

    def _get_xml_schema_attrib(self, name: str):
        return '{' f'{self.xml_schema_tag}' '}' f'{name}'

    def _get_camunda_attrib(self, name: str):
        return '{' f'{self.camunda_tag}' '}' f'{name}'

    def _get_execution_listeners(self, element: _Element):
        return [
            ExecutionListener(
                expression=item.get('expression'),
                event=item.get('event'),
            )
            for item in element.xpath(
                './/camunda:executionListener', namespaces={'camunda': self.camunda_tag}
            )
        ]

    @property
    @abstractmethod
    def list(self):  # pragma: no cover
        pass

    @property
    @abstractmethod
    def get(self):  # pragma: no cover
        pass
