::: bpmn_parser._user_task.UserTask

::: bpmn_parser._user_task.UserTaskElement

```python linenums="1"
type(bpmn_parser.user_task)
```

```python title="Output"
bpmn_parser._user_task.UserTask
```

---

```python linenums="1"
bpmn_parser.user_task
```

```python title="Output"
UserTask(items=2)
```

### List
List all intermedicate catch events elements founded in `.bpmn` file.
```python linenums="1"
bpmn_parser.user_task.list
```

```python title="Output"
[
    UserTaskElement(
        id='Activity_HandleDataManually',
        name='Handle Data Manually',
        execution_listeners=[
            ExecutionListener(
                expression="${execution.setVariable('task_created_at', dateTime().plusHours(3).toDate())}",
                event='start'
            )
        ],
        form_key='embedded:deployment:HandleDataManually.json',
        candidate_groups='some-group',
        due_date='${dateTime().plusDays(2).toDate()}',
        priority="${execution.getVariable('is_priority') == true ? 75 : 50}"
    ),
    UserTaskElement(
        id='Activity_ManuallyScreening',
        name='Manually Screening',
        execution_listeners=[
            ExecutionListener(
                expression="${execution.setVariable('task_created_at', dateTime().plusHours(3).toDate())}",
                event='start'
            )
        ],
        form_key='embedded:deployment:ManuallyScreening.json',
        candidate_groups='some-group',
        due_date='${dateTime().plusDays(2).toDate()}',
        priority="${execution.getVariable('is_priority') == true ? 75 : 50}")
]
```

### Get
Get a specific exclusive gateway by your ID.
```python linenums="1"
bpmn_parser.user_task.get('Activity_QueryData')
```

```python title="Output"
UserTaskElement(
    id='Activity_HandleDataManually',
    name='Handle Data Manually',
    execution_listeners=[
        ExecutionListener(
            expression="${execution.setVariable('task_created_at', dateTime().plusHours(3).toDate())}",
            event='start'
        )
    ],
    form_key='embedded:deployment:HandleDataManually.json',
    candidate_groups='some-group',
    due_date='${dateTime().plusDays(2).toDate()}',
    priority="${execution.getVariable('is_priority') == true ? 75 : 50}"
)
```