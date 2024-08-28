import pytest

from bpmn_parser.sequence_flow import (
    ConditionExpressionElement,
    SequenceFlow,
    SequenceFlowElement,
)


@pytest.fixture
def sequence_flow(bpmn_parser):
    return SequenceFlow(bpmn_parser.root)


def test_sequence_flow(bpmn_parser, sequence_flow):
    data_to_assert = [
        SequenceFlowElement(
            id='Flow_11qv0wo',
            name=None,
            source_ref='Gateway_09uiyn5',
            target_ref='Activity_TratativaManual',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1r8m54y',
            name=None,
            source_ref='Activity_TratativaManual',
            target_ref='Activity_DefineFluxoSaida',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1nvrsyh',
            name=None,
            source_ref='Gateway_04151fm',
            target_ref='Activity_ConsultaDigesto',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_07p3i1y',
            name=None,
            source_ref='Activity_ConsultaDigesto',
            target_ref='Gateway_1431tq3',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0xokps6',
            name=None,
            source_ref='Gateway_07nni2c',
            target_ref='Activity_PreTriagem',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1kwf52v',
            name=None,
            source_ref='Activity_PreTriagem',
            target_ref='Gateway_0djd7kh',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1tdfyor',
            name='Documento\nE-mail',
            source_ref='Gateway_09tged2',
            target_ref='Activity_OCRPreExtracao',
            condition_expression=ConditionExpressionElement(
                type='bpmn:tFormalExpression',
                condition="${execution.getVariable('dg_event_event_type') == 'belisarius event'}",
            ),
        ),
        SequenceFlowElement(
            id='Flow_0d7vqji',
            name=None,
            source_ref='Activity_OCRPreExtracao',
            target_ref='Gateway_1mzb26a',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0lag6f3',
            name='Sim',
            source_ref='Gateway_1431tq3',
            target_ref='Gateway_09uiyn5',
            condition_expression=ConditionExpressionElement(
                type='bpmn:tFormalExpression',
                condition='${consulta_digesto__is_processo_atualizado == true || consulta_digesto__tentativas_atualizacao >= 10}',
            ),
        ),
        SequenceFlowElement(
            id='Flow_0cqiw0t',
            name='Não Judicial',
            source_ref='Gateway_0ony4ks',
            target_ref='Gateway_09uiyn5',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1k0bams',
            name='Não',
            source_ref='Gateway_1431tq3',
            target_ref='Event_EsperaConsultaDigesto',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1pwfmlq',
            name=None,
            source_ref='Event_EsperaConsultaDigesto',
            target_ref='Gateway_04151fm',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0yljlu7',
            name='Judicial',
            source_ref='Gateway_0ony4ks',
            target_ref='Gateway_04151fm',
            condition_expression=ConditionExpressionElement(
                type='bpmn:tFormalExpression',
                condition="${execution.getVariable('_esteira') == 'Judicial' || execution.getVariable('triagem__tipo_numero_identificador') == 'CNJ'}",
            ),
        ),
        SequenceFlowElement(
            id='Flow_0nyc1g3',
            name=None,
            source_ref='Gateway_0v0migw',
            target_ref='Gateway_0ony4ks',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_12kpqpg',
            name=None,
            source_ref='Activity_Triagem',
            target_ref='Gateway_0v0migw',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0kt31nl',
            name='Não',
            source_ref='Gateway_13p78ag',
            target_ref='Gateway_0v0migw',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1ab06b8',
            name='Sim',
            source_ref='Gateway_0djd7kh',
            target_ref='Gateway_13p78ag',
            condition_expression=ConditionExpressionElement(
                type='bpmn:tFormalExpression',
                condition='${pre_triagem__is_processo_atualizado == true || pre_triagem__tentativas_atualizacao >= 10}',
            ),
        ),
        SequenceFlowElement(
            id='Flow_07n3h98',
            name='Sim',
            source_ref='Gateway_13p78ag',
            target_ref='Activity_Triagem',
            condition_expression=ConditionExpressionElement(
                type='bpmn:tFormalExpression',
                condition='${pre_triagem__sucesso == false}',
            ),
        ),
        SequenceFlowElement(
            id='Flow_0ij3smu',
            name='Distribuição\nIntimação elet.',
            source_ref='Gateway_09tged2',
            target_ref='Gateway_1mzb26a',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1n8eg7h',
            name=None,
            source_ref='Activity_DefineFluxoSaida',
            target_ref='Event_0ru28nf',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0dg38wp',
            name='Não',
            source_ref='Gateway_0djd7kh',
            target_ref='Event_EsperaPreTriagem',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0ycna54',
            name=None,
            source_ref='Event_EsperaPreTriagem',
            target_ref='Gateway_07nni2c',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1dne2mb',
            name=None,
            source_ref='Gateway_1mzb26a',
            target_ref='Gateway_07nni2c',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0csizns',
            name=None,
            source_ref='Event_0i7m04u',
            target_ref='Gateway_09tged2',
            condition_expression=None,
        ),
    ]
    assert sequence_flow.list == data_to_assert
    assert bpmn_parser.sequence_flow.list == data_to_assert


def test_get(sequence_flow):
    element = sequence_flow.get('Flow_07n3h98')

    assert element.id == 'Flow_07n3h98'
    assert element.name == 'Sim'
    assert element.source_ref == 'Gateway_13p78ag'
    assert element.target_ref == 'Activity_Triagem'

    condition_expression = ConditionExpressionElement(
        type='bpmn:tFormalExpression',
        condition='${pre_triagem__sucesso == false}',
    )
    assert element.condition_expression.type == condition_expression.type
    assert element.condition_expression.condition == condition_expression.condition


def test_get_not_found(sequence_flow):
    element = sequence_flow.get('')
    assert element is None
