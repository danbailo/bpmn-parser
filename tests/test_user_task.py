from bpmn_parser.base import ExecutionListener
from bpmn_parser.user_task import UserTask, UserTaskElement


def test_user_task(root):
    user_task = UserTask(root)
    assert user_task.list == [
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
