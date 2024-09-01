::: bpmn_parser._service_task.ServiceTask

::: bpmn_parser._service_task.ServiceTaskElement

```python linenums="1"
type(bpmn_parser.service_task)
```

```python title="Output"
bpmn_parser._service_task.ServiceTask
```

---

```python linenums="1"
bpmn_parser.service_task
```

```python title="Output"
ServiceTask(items=4)
```

### List
List all intermedicate catch events elements founded in `.bpmn` file.
```python linenums="1"
bpmn_parser.service_task.list
```

```python title="Output"
[
    ServiceTaskElement(
        id='Activity_QueryData',
        name='Query Data',
        execution_listeners=[],
        topic_name='query-data',
        type='external'
    ),
    ServiceTaskElement(
        id='Activity_PreScreening',
        name='Pre-Screening',
        execution_listeners=[],
        topic_name='pre-screening',
        type='external'
    ),
    ServiceTaskElement(
        id='Activity_SomeExternalTask',
        name='Some External Task',
        execution_listeners=[],
        topic_name='some-external-task',
        type='external'
    ),
    ServiceTaskElement(
        id='Activity_ValidateData',
        name='Validate Data',
        execution_listeners=[],
        topic_name='validate-data',
        type='external')
]
```

### Get
Get a specific exclusive gateway by your ID.
```python linenums="1"
bpmn_parser.service_task.get('Activity_QueryData')
```

```python title="Output"
ServiceTaskElement(
    id='Activity_QueryData',
    name='Query Data',
    execution_listeners=[],
    topic_name='query-data',
    type='external'
)
```