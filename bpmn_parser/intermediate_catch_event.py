from dataclasses import dataclass

from lxml.etree import _Element

from bpmn_parser.task import Task, TaskElement


@dataclass
class IntermediateCatchEventElement(TaskElement):
    time_duration: str


class IntermediateCatchEvent(Task):
    def __init__(self, root: _Element):
        super().__init__(root)

    @property
    def list(self):
        items = []
        for intermediate_catch_event in self.root.xpath(
            '//bpmn:intermediateCatchEvent', namespaces={'bpmn': self.bpmn_tag}
        ):
            time_duration = intermediate_catch_event.xpath(
                './/bpmn:timeDuration', namespaces={'bpmn': self.bpmn_tag}
            )
            items.append(
                IntermediateCatchEventElement(
                    id=intermediate_catch_event.get('id'),
                    name=intermediate_catch_event.get('name'),
                    time_duration=time_duration[0].text,
                    execution_listeners=self._get_execution_listeners(
                        intermediate_catch_event
                    ),
                )
            )
        return items

    def get(self, id: str):
        return next((item for item in self.list if item.id == id), None)
