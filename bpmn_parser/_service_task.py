from dataclasses import dataclass
from typing import Optional

from lxml.etree import _Element

from bpmn_parser._task import Task, TaskElement


@dataclass
class ServiceTaskElement(TaskElement):
    """Parse an Service Task from BPMN.

    Attributes:
        topic_name (str): topic name of element in BPMN.
        type (str): type of element in BPMN.
    """

    topic_name: str
    type: str


class ServiceTask(Task):
    """An API from Service Task from BPMN. This classes holds `ServiceTaskElement` as elements.

    Attributes:
        root (_Element): root of BPMN loaded as XML.
    """

    def __init__(self, root: _Element):
        super().__init__(root)
        self._items: Optional[list[ServiceTaskElement]] = None

    @property
    def list(self):
        if self._items is not None:
            return self._items

        self._items = []
        for service_task in self.root.xpath(
            '//bpmn:serviceTask', namespaces={'bpmn': self.bpmn_tag}
        ):
            self._items.append(
                ServiceTaskElement(
                    id=service_task.get('id'),
                    name=service_task.get('name'),
                    topic_name=service_task.get(self._build_camunda_attrib('topic')),
                    type=service_task.get(self._build_camunda_attrib('type')),
                    execution_listeners=self._get_execution_listeners(service_task),
                )
            )
        return self._items
