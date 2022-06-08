---
menu: main
product: AIR SDK
title: Simulation
---

# Table of Contents

* [air\_sdk.simulation](#air_sdk.simulation)
  * [Simulation](#air_sdk.simulation.Simulation)
    * [create\_service](#air_sdk.simulation.Simulation.create_service)
    * [add\_permission](#air_sdk.simulation.Simulation.add_permission)
    * [control](#air_sdk.simulation.Simulation.control)
    * [load](#air_sdk.simulation.Simulation.load)
    * [start](#air_sdk.simulation.Simulation.start)
    * [stop](#air_sdk.simulation.Simulation.stop)
    * [store](#air_sdk.simulation.Simulation.store)
    * [delete](#air_sdk.simulation.Simulation.delete)
  * [SimulationApi](#air_sdk.simulation.SimulationApi)
    * [duplicate](#air_sdk.simulation.SimulationApi.duplicate)
    * [get\_citc\_simulation](#air_sdk.simulation.SimulationApi.get_citc_simulation)
    * [get](#air_sdk.simulation.SimulationApi.get)
    * [list](#air_sdk.simulation.SimulationApi.list)
    * [create](#air_sdk.simulation.SimulationApi.create)

Simulation module

<a name="air_sdk.simulation.Simulation"></a>
## Simulation

Manage a Simulation

### json
Returns a JSON string representation of the simulation

### refresh
Syncs the simulation with all values returned by the API

### update
Update the simulation with the provided data

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.simulation.Simulation.create_service"></a>
### create\_service

Create a new service for this simulation

**Arguments**:

- `name` _str_ - Name of the service
- `interface` _str | `SimulationInterface`_ - Interface that the service should be created
  for. This can be provided in one of the following formats:
  - [`SimulationInterface`](/docs/simulation-interface) object
  - ID of a [`SimulationInterface`](/docs/simulation-interface)
  - String in the format of 'node_name:interface_name'
- `dest_port` _int_ - Service port number
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Service`](/docs/service)
  

**Example**:

```
>>> simulation.create_service('myservice', 'oob-mgmt-server:eth0', 22, service_type='ssh')
<Service myservice cc18d746-4cf0-4dd3-80c0-e7df68bbb782>
>>> simulation.create_service('myservice', simulation_interface, 22, service_type='ssh')
<Service myservice 9603d0d5-5526-4a0f-91b8-a600010d0091>
```

<a name="air_sdk.simulation.Simulation.add_permission"></a>
### add\_permission

Adds permission for a given user to this simulation.

**Arguments**:

- `email` _str_ - Email address of the user being given permission
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Permission`](/docs/permission)
  

**Example**:

```
>>> simulation.add_permission('mrobertson@nvidia.com', write_ok=True)
<Permission 217bea68-7048-4262-9bbc-b98ab16c603e>
```

<a name="air_sdk.simulation.Simulation.control"></a>
### control

Sends a control command to the simulation.

**Arguments**:

- `action` _str_ - Control command
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

- `dict` - Response JSON
  

**Example**:

```
>>> simulation.control(action='destroy')
{'result': 'success'}
```

<a name="air_sdk.simulation.Simulation.load"></a>
### load

Alias for `start()`

<a name="air_sdk.simulation.Simulation.start"></a>
### start

Start/load the simulation

<a name="air_sdk.simulation.Simulation.stop"></a>
### stop

Alias for `store()`

<a name="air_sdk.simulation.Simulation.store"></a>
### store

Store and power off the simulation

<a name="air_sdk.simulation.Simulation.delete"></a>
### delete

Delete the simulation

<a name="air_sdk.simulation.SimulationApi"></a>
## SimulationApi

High-level interface for the Simulation API

<a name="air_sdk.simulation.SimulationApi.duplicate"></a>
### duplicate

Duplicate/clone an existing simulation

**Arguments**:

- `simulation` _str | `Simulation`_ - Simulation or ID of the snapshot to be duplicated
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  ([`Simulation`](/docs/simulation), dict): Newly created simulation and response JSON
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulations.duplicate(simulation=simulation)
<Simulation my_sim 5ff3f0dc-7db8-4938-8257-765c8e48623a>
```

<a name="air_sdk.simulation.SimulationApi.get_citc_simulation"></a>
### get\_citc\_simulation

Get the active CITC reference simulation

**Returns**:

  [`Simulation`](/docs/simulation)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulations.get_citc_simulation()
<Simulation my_sim b9125419-7c6e-41db-bba9-7d647d63943e>
```

<a name="air_sdk.simulation.SimulationApi.get"></a>
### get

Get an existing simulation

**Arguments**:

- `simulation_id` _str_ - Simulation ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Simulation`](/docs/simulation)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulations.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Simulation my_sim 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.simulation.SimulationApi.list"></a>
### list

List existing simulations

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
>>> air.simulations.list()
[<Simulation sim1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <Simulation sim2 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.simulation.SimulationApi.create"></a>
### create

Create a new simulation

**Arguments**:

- `topology` _str | `Topology`_ - `Topology` or ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Simulation`](/docs/simulation)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulations.create(topology=topology, title='my_sim')
<Simulation my_sim 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```

