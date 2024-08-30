import pytest

from bpmn_parser._exclusive_gateway import (
    ExclusiveGateway,
    ExclusiveGatewayElement,
)


@pytest.fixture
def exclusive_gateway(bpmn_parser):
    return ExclusiveGateway(bpmn_parser.root)


def test_exclusive_gateway(bpmn_parser, exclusive_gateway):
    data_to_assert = [
        ExclusiveGatewayElement(id='Gateway_09uiyn5', name=None),
        ExclusiveGatewayElement(id='Gateway_1431tq3', name='Need to query data again?'),
        ExclusiveGatewayElement(id='Gateway_04151fm', name=None),
        ExclusiveGatewayElement(id='Gateway_0ony4ks', name='Which flow?'),
        ExclusiveGatewayElement(id='Gateway_0v0migw', name=None),
        ExclusiveGatewayElement(
            id='Gateway_13p78ag', name='Need to be screening manually?'
        ),
        ExclusiveGatewayElement(
            id='Gateway_0djd7kh', name='Need to pre-screening again?'
        ),
        ExclusiveGatewayElement(id='Gateway_07nni2c', name=None),
        ExclusiveGatewayElement(id='Gateway_1mzb26a', name=None),
        ExclusiveGatewayElement(id='Gateway_InputTypes', name='Input types'),
    ]
    assert bpmn_parser.exclusive_gateway.list == data_to_assert
    assert exclusive_gateway.list == data_to_assert


def test_get(exclusive_gateway):
    element = exclusive_gateway.get('Gateway_1431tq3')
    assert element.id == 'Gateway_1431tq3'
    assert element.name == 'Need to query data again?'


def test_get_not_found(exclusive_gateway):
    element = exclusive_gateway.get('')
    assert element is None
