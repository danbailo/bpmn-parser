::: bpmn_parser._exclusive_gateway.ExclusiveGateway

::: bpmn_parser._exclusive_gateway.ExclusiveGatewayElement

```python linenums="1"
type(bpmn_parser.exclusive_gateway)
```

```python title="Output"
bpmn_parser._exclusive_gateway.ExclusiveGateway
```

### List
List all exclusive gateways elements founded in `.bpmn` file.
```python linenums="1"
bpmn_parser.exclusive_gateway.list
```

```python title="Output"
[
    ExclusiveGatewayElement(
        id='Gateway_04151fm',
        name=None
    ),
    ExclusiveGatewayElement(
        id='Gateway_0ony4ks',
        name='Which flow?'
    ),
    ExclusiveGatewayElement(
        id='Gateway_0v0migw',
        name=None
    ),
]
```

### Get
Get a specific exclusive gateway by your ID.
```python linenums="1"
bpmn_parser.exclusive_gateway.get('Gateway_04151fm')
```

```python title="Output"
ExclusiveGatewayElement(
    id='Gateway_04151fm',
    name=None
),
```