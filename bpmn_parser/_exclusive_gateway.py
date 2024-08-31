from dataclasses import dataclass

from lxml.etree import _Element

from bpmn_parser._task import BPMNElement, Task


@dataclass
class ExclusiveGatewayElement(BPMNElement):
    """Parse an Exclusive Gateway from BPMN"""

    pass


class ExclusiveGateway(Task):
    """An API from Exclusive Gateway from BPMN. This classes holds `ExclusiveGatewayElement` as elements.

    Attributes:
        root (_Element): root of BPMN loaded as XML.
    """

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
