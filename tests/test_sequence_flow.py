import pytest

from bpmn_parser._sequence_flow import (
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
            target_ref='Activity_HandleDataManually',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1r8m54y',
            name=None,
            source_ref='Activity_HandleDataManually',
            target_ref='Activity_ValidateData',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1nvrsyh',
            name=None,
            source_ref='Gateway_04151fm',
            target_ref='Activity_QueryData',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_07p3i1y',
            name=None,
            source_ref='Activity_QueryData',
            target_ref='Gateway_1431tq3',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0xokps6',
            name=None,
            source_ref='Gateway_07nni2c',
            target_ref='Activity_PreScreening',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1kwf52v',
            name=None,
            source_ref='Activity_PreScreening',
            target_ref='Gateway_0djd7kh',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1tdfyor',
            name='input 1\ninput 2',
            source_ref='Gateway_InputTypes',
            target_ref='Activity_SomeExternalTask',
            condition_expression=ConditionExpressionElement(
                type='bpmn:tFormalExpression',
                condition="${execution.getVariable('dg_event_event_type') == 'belisarius event'}",
            ),
        ),
        SequenceFlowElement(
            id='Flow_0d7vqji',
            name=None,
            source_ref='Activity_SomeExternalTask',
            target_ref='Gateway_1mzb26a',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0lag6f3',
            name='Yes',
            source_ref='Gateway_1431tq3',
            target_ref='Gateway_09uiyn5',
            condition_expression=ConditionExpressionElement(
                type='bpmn:tFormalExpression',
                condition='${consulta_digesto__is_processo_atualizado == true || consulta_digesto__tentativas_atualizacao >= 10}',
            ),
        ),
        SequenceFlowElement(
            id='Flow_0cqiw0t',
            name='Flow 2',
            source_ref='Gateway_0ony4ks',
            target_ref='Gateway_09uiyn5',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1k0bams',
            name='Not',
            source_ref='Gateway_1431tq3',
            target_ref='Event_WaitToQueryData',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1pwfmlq',
            name=None,
            source_ref='Event_WaitToQueryData',
            target_ref='Gateway_04151fm',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0yljlu7',
            name='Flow 1',
            source_ref='Gateway_0ony4ks',
            target_ref='Gateway_04151fm',
            condition_expression=ConditionExpressionElement(
                type='bpmn:tFormalExpression',
                condition="${execution.getVariable('flow') == 'flow_1' || execution.getVariable('flow') != 'flow_2'}",
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
            source_ref='Activity_ManuallyScreening',
            target_ref='Gateway_0v0migw',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0kt31nl',
            name='Not',
            source_ref='Gateway_13p78ag',
            target_ref='Gateway_0v0migw',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1ab06b8',
            name='Yes',
            source_ref='Gateway_0djd7kh',
            target_ref='Gateway_13p78ag',
            condition_expression=ConditionExpressionElement(
                type='bpmn:tFormalExpression',
                condition='${pre_triagem__is_processo_atualizado == true || pre_triagem__tentativas_atualizacao >= 10}',
            ),
        ),
        SequenceFlowElement(
            id='Flow_07n3h98',
            name='Yes',
            source_ref='Gateway_13p78ag',
            target_ref='Activity_ManuallyScreening',
            condition_expression=ConditionExpressionElement(
                type='bpmn:tFormalExpression',
                condition='${pre_screening_success == false}',
            ),
        ),
        SequenceFlowElement(
            id='Flow_0ij3smu',
            name='input 3\ninput 4\ninput 5',
            source_ref='Gateway_InputTypes',
            target_ref='Gateway_1mzb26a',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_1n8eg7h',
            name=None,
            source_ref='Activity_ValidateData',
            target_ref='Event_0ru28nf',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0dg38wp',
            name='Not',
            source_ref='Gateway_0djd7kh',
            target_ref='Event_WaitToPreScreening',
            condition_expression=None,
        ),
        SequenceFlowElement(
            id='Flow_0ycna54',
            name=None,
            source_ref='Event_WaitToPreScreening',
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
            target_ref='Gateway_InputTypes',
            condition_expression=None,
        ),
    ]
    assert sequence_flow.list == data_to_assert
    assert bpmn_parser.sequence_flow.list == data_to_assert


def test_get(sequence_flow):
    element = sequence_flow.get('Flow_07n3h98')

    assert element.id == 'Flow_07n3h98'
    assert element.name == 'Yes'
    assert element.source_ref == 'Gateway_13p78ag'
    assert element.target_ref == 'Activity_ManuallyScreening'

    condition_expression = ConditionExpressionElement(
        type='bpmn:tFormalExpression',
        condition='${pre_screening_success == false}',
    )
    assert element.condition_expression.type == condition_expression.type
    assert element.condition_expression.condition == condition_expression.condition


def test_get_not_found(sequence_flow):
    element = sequence_flow.get('')
    assert element is None


def test_len(sequence_flow):
    assert len(sequence_flow) == 24


def test_repr(sequence_flow):
    assert repr(sequence_flow) == 'SequenceFlow(items=24)'
