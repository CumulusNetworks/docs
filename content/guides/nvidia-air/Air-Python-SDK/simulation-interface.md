---
menu: main
product: AIR SDK
title: Simulation Interface
---

# Table of Contents

* [air\_sdk.simulation\_interface](#air_sdk.simulation_interface)
  * [SimulationInterface](#air_sdk.simulation_interface.SimulationInterface)
  * [SimulationInterfaceApi](#air_sdk.simulation_interface.SimulationInterfaceApi)
    * [get](#air_sdk.simulation_interface.SimulationInterfaceApi.get)
    * [list](#air_sdk.simulation_interface.SimulationInterfaceApi.list)

SimulationInterface module

<a name="air_sdk.simulation_interface.SimulationInterface"></a>
## SimulationInterface

Manage a SimulationInterface

### json
Returns a JSON string representation of the simulation interface

### refresh
Syncs the simulation interface with all values returned by the API

### update
Update the simulation interface with the provided data

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.simulation_interface.SimulationInterfaceApi"></a>
## SimulationInterfaceApi

High-level interface for the SimulationInterface API

<a name="air_sdk.simulation_interface.SimulationInterfaceApi.get"></a>
### get

Get an existing simulation interface

**Arguments**:

- `simulation_interface_id` _str_ - SimulationInterface ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`SimulationInterface`](/docs/simulationinterface)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulation_interfaces.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<SimulationInterface 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.simulation_interface.SimulationInterfaceApi.list"></a>
### list

List existing simulation interfaces

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
>>> air.simulation_interfaces.list()
[<SimulationInterface c51b49b6-94a7-4c93-950c-e7fa4883591>, <SimulationInterface 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

