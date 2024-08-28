from legalops_commons.utils.bpmn.exclusive_gateway import (
    ExclusiveGateway,
    ExclusiveGatewayElement,
)


def test_exclusive_gateway(root):
    exclusive_gateway = ExclusiveGateway(root)
    assert exclusive_gateway.list == [
        ExclusiveGatewayElement(id='Gateway_09uiyn5', name=None),
        ExclusiveGatewayElement(
            id='Gateway_1431tq3', name='Está atualizado ou tentativas >= 10?'
        ),
        ExclusiveGatewayElement(id='Gateway_04151fm', name=None),
        ExclusiveGatewayElement(
            id='Gateway_0ony4ks', name='Qual a esteira de cadastro?'
        ),
        ExclusiveGatewayElement(id='Gateway_0v0migw', name=None),
        ExclusiveGatewayElement(
            id='Gateway_13p78ag', name='Precisa ser triado manualmente?'
        ),
        ExclusiveGatewayElement(id='Gateway_09tged2', name='Tipo de entrada'),
        ExclusiveGatewayElement(
            id='Gateway_0djd7kh', name='Está atualizado ou tentativas >= 10?'
        ),
        ExclusiveGatewayElement(id='Gateway_07nni2c', name=None),
        ExclusiveGatewayElement(id='Gateway_1mzb26a', name=None),
    ]
