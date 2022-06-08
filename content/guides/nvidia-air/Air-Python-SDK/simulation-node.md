---
menu: main
product: AIR SDK
title: Simulation Node
---

# Table of Contents

* [air\_sdk.simulation\_node](#air_sdk.simulation_node)
  * [SimulationNode](#air_sdk.simulation_node.SimulationNode)
    * [create\_instructions](#air_sdk.simulation_node.SimulationNode.create_instructions)
    * [list\_instructions](#air_sdk.simulation_node.SimulationNode.list_instructions)
    * [delete\_instructions](#air_sdk.simulation_node.SimulationNode.delete_instructions)
    * [control](#air_sdk.simulation_node.SimulationNode.control)
    * [rebuild](#air_sdk.simulation_node.SimulationNode.rebuild)
    * [reset](#air_sdk.simulation_node.SimulationNode.reset)
  * [SimulationNodeApi](#air_sdk.simulation_node.SimulationNodeApi)
    * [get](#air_sdk.simulation_node.SimulationNodeApi.get)
    * [list](#air_sdk.simulation_node.SimulationNodeApi.list)

SimulationNode module

<a name="air_sdk.simulation_node.SimulationNode"></a>
## SimulationNode

Manage a SimulationNode

### json
Returns a JSON string representation of the simulation node

### refresh
Syncs the simulation node with all values returned by the API

### update
Update the simulation node with the provided data

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.simulation_node.SimulationNode.create_instructions"></a>
### create\_instructions

Create instructions for the `SimulationNode`'s agent to execute

**Arguments**:

- `data` _str | list_ - Instruction data
- `executor` _str_ - Agent executor type
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

- `dict` - Response JSON
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> simulation_node.create_instructions(data='echo foo', executor='shell')
{'id': '67f73552-ffdf-4e5f-9881-aeae227604a3'}
```

<a name="air_sdk.simulation_node.SimulationNode.list_instructions"></a>
### list\_instructions

List all instructions for a `SimulationNode`

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  list
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> simulation_node.instructions.list()
[{'id': '56abc69b-489f-429a-aed9-600f26afc956'}, {'id': '7c9c3449-f071-4bbc-bb42-bef04e44d74e'}]
```

<a name="air_sdk.simulation_node.SimulationNode.delete_instructions"></a>
### delete\_instructions

Delete all instructions for a `SimulationNode`

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Instruction delete failed
  

**Example**:

```
>>> simulation_node.instructions.delete()
```

<a name="air_sdk.simulation_node.SimulationNode.control"></a>
### control

Sends a control command to the `SimulationNode`.

**Arguments**:

- `action` _str_ - Control command
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

- `dict` - Response JSON
  

**Example**:

```
>>> simulation_node.control(action='reset')
{'result': 'success'}
```

<a name="air_sdk.simulation_node.SimulationNode.rebuild"></a>
### rebuild

Rebuild the `SimulationNode` back to it's initial state. **All existing data will be lost!**

<a name="air_sdk.simulation_node.SimulationNode.reset"></a>
### reset

Reset the `SimulationNode`

<a name="air_sdk.simulation_node.SimulationNodeApi"></a>
## SimulationNodeApi

Wrapper for the SimulationNode API

<a name="air_sdk.simulation_node.SimulationNodeApi.get"></a>
### get

Get an existing simulation node

**Arguments**:

- `simulation_node_id` _str_ - SimulationNode ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`SimulationNode`](/docs/simulationnode)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulation_nodes.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<SimulationNode my_sim 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.simulation_node.SimulationNodeApi.list"></a>
### list

List existing simulation nodes

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  list
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulation_nodes.list()
[<SimulationNode sim1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <SimulationNode sim2 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

