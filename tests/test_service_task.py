import pytest

from bpmn_parser._service_task import ServiceTask, ServiceTaskElement


@pytest.fixture
def service_task(bpmn_parser):
    return ServiceTask(bpmn_parser.root)


def test_service_task(bpmn_parser, service_task):
    data_to_assert = [
        ServiceTaskElement(
            id='Activity_QueryData',
            name='Query Data',
            execution_listeners=[],
            topic_name='query-data',
            type='external',
        ),
        ServiceTaskElement(
            id='Activity_PreScreening',
            name='Pre-Screening',
            execution_listeners=[],
            topic_name='pre-screening',
            type='external',
        ),
        ServiceTaskElement(
            id='Activity_SomeExternalTask',
            name='Some External Task',
            execution_listeners=[],
            topic_name='some-external-task',
            type='external',
        ),
        ServiceTaskElement(
            id='Activity_ValidateData',
            name='Validate Data',
            execution_listeners=[],
            topic_name='validate-data',
            type='external',
        ),
    ]

    assert service_task.list == data_to_assert
    assert bpmn_parser.service_task.list == data_to_assert


def test_get(service_task):
    element = service_task.get('Activity_ValidateData')
    assert element.id == 'Activity_ValidateData'
    assert element.name == 'Validate Data'
    assert element.execution_listeners == []
    assert element.topic_name == 'validate-data'
    assert element.type == 'external'


def test_get_not_found(service_task):
    element = service_task.get('')
    assert element is None
