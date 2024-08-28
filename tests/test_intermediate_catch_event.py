import pytest

from bpmn_parser.intermediate_catch_event import (
    IntermediateCatchEvent,
    IntermediateCatchEventElement,
)


@pytest.fixture
def intermediate_catch_event(bpmn_parser):
    return IntermediateCatchEvent(bpmn_parser.root)


def test_intermediate_catch_event(bpmn_parser, intermediate_catch_event):
    data_to_assert = [
        IntermediateCatchEventElement(
            id='Event_EsperaConsultaDigesto',
            name='Espera 1h',
            execution_listeners=[],
            time_duration='PT1H',
        ),
        IntermediateCatchEventElement(
            id='Event_EsperaPreTriagem',
            name='Espera 1h',
            execution_listeners=[],
            time_duration='PT1H',
        ),
    ]
    assert intermediate_catch_event.list == data_to_assert
    assert bpmn_parser.intermediate_catch_event.list == data_to_assert


def test_get(intermediate_catch_event):
    element = intermediate_catch_event.get('Event_EsperaConsultaDigesto')
    assert element.id == 'Event_EsperaConsultaDigesto'
    assert element.name == 'Espera 1h'
    assert element.execution_listeners == []
    assert element.time_duration == 'PT1H'


def test_get_not_found(intermediate_catch_event):
    element = intermediate_catch_event.get('')
    assert element is None
