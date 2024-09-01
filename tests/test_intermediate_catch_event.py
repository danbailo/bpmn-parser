import pytest

from bpmn_parser._intermediate_catch_event import (
    IntermediateCatchEvent,
    IntermediateCatchEventElement,
)


@pytest.fixture
def intermediate_catch_event(bpmn_parser):
    return IntermediateCatchEvent(bpmn_parser.root)


def test_intermediate_catch_event(bpmn_parser, intermediate_catch_event):
    data_to_assert = [
        IntermediateCatchEventElement(
            id='Event_WaitToQueryData',
            name='Wait 1h',
            execution_listeners=[],
            time_duration='PT1H',
        ),
        IntermediateCatchEventElement(
            id='Event_WaitToPreScreening',
            name='Wait 30min',
            execution_listeners=[],
            time_duration='PT30M',
        ),
    ]
    assert intermediate_catch_event.list == data_to_assert
    assert bpmn_parser.intermediate_catch_event.list == data_to_assert


def test_get(intermediate_catch_event):
    element = intermediate_catch_event.get('Event_WaitToQueryData')
    assert element.id == 'Event_WaitToQueryData'
    assert element.name == 'Wait 1h'
    assert element.execution_listeners == []
    assert element.time_duration == 'PT1H'


def test_get_not_found(intermediate_catch_event):
    element = intermediate_catch_event.get('')
    assert element is None


def test_len(intermediate_catch_event):
    assert len(intermediate_catch_event) == 2


def test_repr(intermediate_catch_event):
    assert repr(intermediate_catch_event) == 'IntermediateCatchEvent(items=2)'
