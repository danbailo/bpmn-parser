import pytest

from bpmn_parser.task import ExecutionListener
from bpmn_parser.user_task import UserTask, UserTaskElement


@pytest.fixture
def user_task(bpmn_parser):
    return UserTask(bpmn_parser.root)


def test_user_task(bpmn_parser, user_task):
    data_to_assert = [
        UserTaskElement(
            id='Activity_TratativaManual',
            name='v0 - ${_fluxo} - Tratativa manual',
            execution_listeners=[
                ExecutionListener(
                    expression="${execution.setVariable('tarefa_criada_em', dateTime().plusHours(3).toDate())}",
                    event='start',
                )
            ],
            form_key='embedded:deployment:TratativaManualPage.json',
            candidate_groups=None,
            due_date='${dateTime().plusDays(2).toDate()}',
            priority="${execution.getVariable('dg_event_object_data__prioritario') == true || execution.getVariable('triagem__tarefa_prioritaria') == true ? 75 : 50}",
        ),
        UserTaskElement(
            id='Activity_Triagem',
            name='v0 - ${_fluxo} - Triagem',
            execution_listeners=[
                ExecutionListener(
                    expression="${execution.setVariable('tarefa_criada_em', dateTime().plusHours(3).toDate())}",
                    event='start',
                )
            ],
            form_key='embedded:deployment:TriagemPage.json',
            candidate_groups=None,
            due_date='${dateTime().plusDays(2).toDate()}',
            priority="${execution.getVariable('dg_event_object_data__prioritario') == true ? 75 : 50}",
        ),
    ]
    assert user_task.list == data_to_assert
    assert bpmn_parser.user_task.list == data_to_assert


def test_get(user_task):
    element = user_task.get('Activity_Triagem')

    assert element.id == 'Activity_Triagem'
    assert element.name == 'v0 - ${_fluxo} - Triagem'
    assert element.form_key == 'embedded:deployment:TriagemPage.json'
    assert element.candidate_groups == None
    assert element.due_date == '${dateTime().plusDays(2).toDate()}'
    assert (
        element.priority
        == "${execution.getVariable('dg_event_object_data__prioritario') == true ? 75 : 50}"
    )

    execution_listener = ExecutionListener(
        expression="${execution.setVariable('tarefa_criada_em', dateTime().plusHours(3).toDate())}",
        event='start',
    )
    assert element.execution_listeners[0].expression == execution_listener.expression
    assert element.execution_listeners[0].event == execution_listener.event


def test_get_not_found(user_task):
    element = user_task.get('')
    assert element is None
