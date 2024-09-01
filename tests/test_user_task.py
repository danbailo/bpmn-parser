import pytest

from bpmn_parser._task import ExecutionListener
from bpmn_parser._user_task import UserTask, UserTaskElement


@pytest.fixture
def user_task(bpmn_parser):
    return UserTask(bpmn_parser.root)


def test_user_task(bpmn_parser, user_task):
    data_to_assert = [
        UserTaskElement(
            id='Activity_HandleDataManually',
            name='Handle Data Manually',
            execution_listeners=[
                ExecutionListener(
                    expression="${execution.setVariable('task_created_at', dateTime().plusHours(3).toDate())}",
                    event='start',
                )
            ],
            form_key='embedded:deployment:HandleDataManually.json',
            candidate_groups='some-group',
            due_date='${dateTime().plusDays(2).toDate()}',
            priority="${execution.getVariable('is_priority') == true ? 75 : 50}",
        ),
        UserTaskElement(
            id='Activity_ManuallyScreening',
            name='Manually Screening',
            execution_listeners=[
                ExecutionListener(
                    expression="${execution.setVariable('task_created_at', dateTime().plusHours(3).toDate())}",
                    event='start',
                )
            ],
            form_key='embedded:deployment:ManuallyScreening.json',
            candidate_groups='some-group',
            due_date='${dateTime().plusDays(2).toDate()}',
            priority="${execution.getVariable('is_priority') == true ? 75 : 50}",
        ),
    ]
    assert user_task.list == data_to_assert
    assert bpmn_parser.user_task.list == data_to_assert


def test_get(user_task):
    element = user_task.get('Activity_ManuallyScreening')

    assert element.id == 'Activity_ManuallyScreening'
    assert element.name == 'Manually Screening'
    assert element.form_key == 'embedded:deployment:ManuallyScreening.json'
    assert element.candidate_groups == 'some-group'
    assert element.due_date == '${dateTime().plusDays(2).toDate()}'
    assert (
        element.priority == "${execution.getVariable('is_priority') == true ? 75 : 50}"
    )

    execution_listener = ExecutionListener(
        expression="${execution.setVariable('task_created_at', dateTime().plusHours(3).toDate())}",
        event='start',
    )
    assert element.execution_listeners[0].expression == execution_listener.expression
    assert element.execution_listeners[0].event == execution_listener.event


def test_get_not_found(user_task):
    element = user_task.get('')
    assert element is None


def test_len(user_task):
    assert len(user_task) == 2


def test_repr(user_task):
    assert repr(user_task) == 'UserTask(items=2)'
