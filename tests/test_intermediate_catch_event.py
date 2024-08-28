from legalops_commons.utils.bpmn.intermediate_catch_event import (
    IntermediateCatchEvent,
    IntermediateCatchEventElement,
)


def test_intermediate_catch_event(root):
    intermediate_catch_event = IntermediateCatchEvent(root)
    assert intermediate_catch_event.list == [
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
