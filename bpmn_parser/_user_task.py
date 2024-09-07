from dataclasses import dataclass
from typing import Optional

from lxml.etree import _Element

from bpmn_parser._task import Task, TaskElement


@dataclass
class UserTaskElement(TaskElement):
    """Parse an Service Task from BPMN.

    Attributes:
        form_key (str): form key of element in BPMN.
        candidate_groups (str): candidate groups of element in BPMN.
        due_date (str): due date of element in BPMN.
        priority (str): priority of element in BPMN.
    """

    form_key: str
    candidate_groups: str
    due_date: str
    priority: str


class UserTask(Task):
    """An API from Service Task from BPMN. This classes holds `UserTaskElement` as elements.

    Attributes:
        root (_Element): root of BPMN loaded as XML.
    """

    def __init__(self, root: _Element):
        super().__init__(root)
        self._items: Optional[list[UserTaskElement]] = None

    @property
    def list(self):
        if self._items is not None:
            return self._items

        self._items = []
        for user_task in self.root.xpath(
            '//bpmn:userTask', namespaces={'bpmn': self.bpmn_tag}
        ):
            self._items.append(
                UserTaskElement(
                    id=user_task.get('id'),
                    name=user_task.get('name'),
                    form_key=user_task.get(self._build_camunda_attrib('formKey')),
                    candidate_groups=user_task.get(
                        self._build_camunda_attrib('candidateGroups')
                    ),
                    due_date=user_task.get(self._build_camunda_attrib('dueDate')),
                    priority=user_task.get(self._build_camunda_attrib('priority')),
                    execution_listeners=self._get_execution_listeners(user_task),
                )
            )
        return self._items
