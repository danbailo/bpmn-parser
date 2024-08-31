::: bpmn_parser._sequence_flow.SequenceFlow

::: bpmn_parser._sequence_flow.SequenceFlowElement

```python linenums="1"
type(bpmn_parser.sequence_flow)
```

```python title="Output"
bpmn_parser._sequence_flow_.SequenceFlow
```

### List
List all intermedicate catch events elements founded in `.bpmn` file.
```python linenums="1"
bpmn_parser.sequence_flow.list
```

```python title="Output"
[
    SequenceFlowElement(
        id='Flow_12kpqpg',
        name=None,
        source_ref='Activity_ManuallyScreening',
        target_ref='Gateway_0v0migw',
        condition_expression=None),
    SequenceFlowElement(
        id='Flow_0kt31nl',
        name='Not',
        source_ref='Gateway_13p78ag',
        target_ref='Gateway_0v0migw',
        condition_expression=None),
    SequenceFlowElement(
        id='Flow_1ab06b8',
        name='Yes',
        source_ref='Gateway_0djd7kh',
        target_ref='Gateway_13p78ag',
        condition_expression=ConditionExpressionElement(
            type='bpmn:tFormalExpression',
            condition='${pre_triagem__is_processo_atualizado == true || pre_triagem__tentativas_atualizacao >= 10}')
        ),
    SequenceFlowElement(
        id='Flow_07n3h98',
        name='Yes',
        source_ref='Gateway_13p78ag',
        target_ref='Activity_ManuallyScreening',
        condition_expression=ConditionExpressionElement(
            type='bpmn:tFormalExpression',
            condition='${pre_screening_success == false}')
        ),
]
```

### Get
Get a specific exclusive gateway by your ID.
```python linenums="1"
bpmn_parser.sequence_flow.get('Flow_1ab06b8')
```

```python title="Output"
SequenceFlowElement(
    id='Flow_1ab06b8',
    name='Yes',
    source_ref='Gateway_0djd7kh',
    target_ref='Gateway_13p78ag',
    condition_expression=ConditionExpressionElement(
        type='bpmn:tFormalExpression',
        condition='${pre_triagem__is_processo_atualizado == true || pre_triagem__tentativas_atualizacao >= 10}'
    )
)
```