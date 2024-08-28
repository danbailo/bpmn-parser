import pytest

from bpmn_parser.service_task import ServiceTask, ServiceTaskElement


@pytest.fixture
def service_task(bpmn_parser):
    return ServiceTask(bpmn_parser.root)


def test_service_task(bpmn_parser, service_task):
    data_to_assert = [
        ServiceTaskElement(
            id='Activity_ConsultaDigesto',
            name='v0 - Consulta Digesto',
            execution_listeners=[],
            topic_name='consulta-digesto',
            type='external',
        ),
        ServiceTaskElement(
            id='Activity_PreTriagem',
            name='v0 - Pré-triagem',
            execution_listeners=[],
            topic_name='pre-triagem',
            type='external',
        ),
        ServiceTaskElement(
            id='Activity_OCRPreExtracao',
            name='v0 - OCR e pré-extração',
            execution_listeners=[],
            topic_name='ocr-pre-extracao',
            type='external',
        ),
        ServiceTaskElement(
            id='Activity_DefineFluxoSaida',
            name='v0 - Define fluxo saída',
            execution_listeners=[],
            topic_name='define-fluxo-saida',
            type='external',
        ),
    ]
    assert service_task.list == data_to_assert
    assert bpmn_parser.service_task.list == data_to_assert


def test_get(service_task):
    element = service_task.get('Activity_DefineFluxoSaida')
    assert element.id == 'Activity_DefineFluxoSaida'
    assert element.name == 'v0 - Define fluxo saída'
    assert element.execution_listeners == []
    assert element.topic_name == 'define-fluxo-saida'
    assert element.type == 'external'


def test_get_not_found(service_task):
    element = service_task.get('')
    assert element is None
