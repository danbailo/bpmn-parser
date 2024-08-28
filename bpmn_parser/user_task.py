from dataclasses import dataclass

from lxml.etree import _Element

from bpmn_parser.task import Task, TaskElement


@dataclass
class UserTaskElement(TaskElement):
    form_key: str
    candidate_groups: str
    due_date: str
    priority: str


class UserTask(Task):
    def __init__(self, root: _Element):
        super().__init__(root)

    @property
    def list(self):
        items = []
        for user_task in self.root.xpath(
            '//bpmn:userTask', namespaces={'bpmn': self.bpmn_tag}
        ):
            items.append(
                UserTaskElement(
                    id=user_task.get('id'),
                    name=user_task.get('name'),
                    form_key=user_task.get(self._get_camunda_attrib('formKey')),
                    candidate_groups=user_task.get(
                        self._get_camunda_attrib('candidateGroups')
                    ),
                    due_date=user_task.get(self._get_camunda_attrib('dueDate')),
                    priority=user_task.get(self._get_camunda_attrib('priority')),
                    execution_listeners=self._get_execution_listeners(user_task),
                )
            )
        return items

    def get(self, id: str):
        return next((item for item in self.list if item.id == id), None)
