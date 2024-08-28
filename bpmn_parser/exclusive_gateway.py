from dataclasses import dataclass

from lxml.etree import _Element

from bpmn_parser.task import BPMNElement, Task


@dataclass
class ExclusiveGatewayElement(BPMNElement):
    pass


class ExclusiveGateway(Task):
    def __init__(self, root: _Element):
        super().__init__(root)

    @property
    def list(self):
        items = []
        for exclusive_gateway in self.root.xpath(
            '//bpmn:exclusiveGateway', namespaces={'bpmn': self.bpmn_tag}
        ):
            items.append(
                ExclusiveGatewayElement(
                    id=exclusive_gateway.get('id'),
                    name=exclusive_gateway.get('name'),
                )
            )
        return items

    def get(self, id: str):
        return next((item for item in self.list if item.id == id), None)
