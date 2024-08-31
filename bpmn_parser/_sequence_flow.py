from dataclasses import dataclass
from typing import Union

from lxml.etree import _Element

from bpmn_parser._task import BPMNElement, Task


@dataclass
class ConditionExpressionElement:
    """Parse an Condition Expression from BPMN.

    Attributes:
        type (str): type of expression in BPMN.
        condition (str): condition implemented in BPMN.
    """

    type: str
    condition: str


@dataclass
class SequenceFlowElement(BPMNElement):
    """Parse an Sequence Flow from BPMN.

    Attributes:
        source_ref (str): source reference from this element in BPMN.
        target_ref (str): target reference from this element in BPMN.
        condition_expression (Union[ConditionExpressionElement, None]): a condition
            expression implemented in this element in BPMN.
    """

    source_ref: str
    target_ref: str
    condition_expression: Union[ConditionExpressionElement, None]


class SequenceFlow(Task):
    """An API from Sequence Flow from BPMN. This classes holds `SequenceFlowElement` as elements.

    Attributes:
        root (_Element): root of BPMN loaded as XML.
    """

    def __init__(self, root: _Element):
        super().__init__(root)

    @property
    def list(self):
        items = []
        for sequence_flow in self.root.xpath(
            '//bpmn:sequenceFlow', namespaces={'bpmn': self.bpmn_tag}
        ):
            if condition_expression := sequence_flow.xpath(
                './/bpmn:conditionExpression', namespaces={'bpmn': self.bpmn_tag}
            ):
                condition_expression = ConditionExpressionElement(
                    type=condition_expression[0].get(
                        self._get_xml_schema_attrib('type')
                    ),
                    condition=condition_expression[0].text,
                )
            else:
                condition_expression = None
            items.append(
                SequenceFlowElement(
                    id=sequence_flow.get('id'),
                    name=sequence_flow.get('name'),
                    source_ref=sequence_flow.get('sourceRef'),
                    target_ref=sequence_flow.get('targetRef'),
                    condition_expression=condition_expression,
                )
            )
        return items

    def get(self, id: str):
        return next((item for item in self.list if item.id == id), None)
