::: bpmn_parser._intermediate_catch_event.IntermediateCatchEvent

::: bpmn_parser._intermediate_catch_event.IntermediateCatchEventElement

```python linenums="1"
type(bpmn_parser.intermediate_catch_event)
```

```python title="Output"
bpmn_parser._intermediate_catch_event.IntermediateCatchEvent
```

### List
List all intermedicate catch events elements founded in `.bpmn` file.
```python linenums="1"
bpmn_parser.intermediate_catch_event.list
```

```python title="Output"
[
    IntermediateCatchEventElement(
        id='Event_WaitToQueryData',
        name='Wait 1h',
        execution_listeners=[],
        time_duration='PT1H'
    ),
    IntermediateCatchEventElement(
        id='Event_WaitToPreScreening',
        name='Wait 30min',
        execution_listeners=[],
        time_duration='PT30M'
    )
]
```

### Get
Get a specific exclusive gateway by your ID.
```python linenums="1"
bpmn_parser.intermediate_catch_event.get('Event_WaitToQueryData')
```

```python title="Output"
IntermediateCatchEventElement(
    id='Event_WaitToQueryData',
    name='Wait 1h',
    execution_listeners=[],
    time_duration='PT1H'
)
```