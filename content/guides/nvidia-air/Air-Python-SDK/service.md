---
menu: main
product: AIR SDK
title: Service
---

# Table of Contents

* [air\_sdk.service](#air_sdk.service)
  * [Service](#air_sdk.service.Service)
  * [ServiceApi](#air_sdk.service.ServiceApi)
    * [get](#air_sdk.service.ServiceApi.get)
    * [list](#air_sdk.service.ServiceApi.list)
    * [create](#air_sdk.service.ServiceApi.create)

Service module

<a name="air_sdk.service.Service"></a>
## Service

Manage a Service

### delete
Delete the service. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](/docs/exceptions) when referenced.

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Delete failed
  
  ### json
  Returns a JSON string representation of the service
  
  ### refresh
  Syncs the service with all values returned by the API
  
  ### update
  Update the service with the provided data
  

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.service.ServiceApi"></a>
## ServiceApi

High-level interface for the Service API

<a name="air_sdk.service.ServiceApi.get"></a>
### get

Get an existing service

**Arguments**:

- `service_id` _str_ - Service ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Service`](/docs/service)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.services.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Service SSH 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.service.ServiceApi.list"></a>
### list

List existing services

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
>>> air.services.list()
[<Service SSH c51b49b6-94a7-4c93-950c-e7fa4883591>, <Service HTTP 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.service.ServiceApi.create"></a>
### create

Create a new service

**Arguments**:

- `name` _str_ - Service name
- `interface` _str | `SimulationInterface`_ - Interface that the service should be created
  for. This can be provided in one of the following formats:
  - [`SimulationInterface`](/docs/simulationinterface) object
  - ID of a [`SimulationInterface`](/docs/simulationinterface)
  - String in the format of 'node_name:interface_name'
- `simulation` _str | `Simulation`_ - `Simulation` or ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Service`](/docs/service)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.services.create(name='myservice', interface='oob-mgmt-server:eth0', dest_port=22)
<Service myservice cc18d746-4cf0-4dd3-80c0-e7df68bbb782>
>>> air.services.create(name='myservice', interface=simulation_interface, dest_port=22)
<Service myservice 9603d0d5-5526-4a0f-91b8-a600010d0091>
```

