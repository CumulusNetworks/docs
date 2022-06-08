---
menu: main
product: AIR SDK
title: Topology
---

# Table of Contents

* [air\_sdk.topology](#air_sdk.topology)
  * [Topology](#air_sdk.topology.Topology)
    * [add\_permission](#air_sdk.topology.Topology.add_permission)
  * [TopologyApi](#air_sdk.topology.TopologyApi)
    * [get](#air_sdk.topology.TopologyApi.get)
    * [list](#air_sdk.topology.TopologyApi.list)
    * [create](#air_sdk.topology.TopologyApi.create)

Topology module

<a name="air_sdk.topology.Topology"></a>
## Topology

Manage a Topology

### delete
Delete the topology. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](/docs/exceptions) when referenced.

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Delete failed
  
  ### json
  Returns a JSON string representation of the topology
  
  ### refresh
  Syncs the topology with all values returned by the API
  
  ### update
  Update the topology with the provided data
  

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.topology.Topology.add_permission"></a>
### add\_permission

Adds permission for a given user to this topology.

**Arguments**:

- `email` _str_ - Email address of the user being given permission
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Permission`](/docs/permission)
  

**Example**:

```
>>> topology.add_permission('mrobertson@nvidia.com', write_ok=True)
<Permission 217bea68-7048-4262-9bbc-b98ab16c603e>
```

<a name="air_sdk.topology.TopologyApi"></a>
## TopologyApi

High-level interface for the Topology API

<a name="air_sdk.topology.TopologyApi.get"></a>
### get

Get an existing topology

**Arguments**:

- `topology_id` _str_ - Topology ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Topology`](/docs/topology)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.topologies.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Topology my_network 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.topology.TopologyApi.list"></a>
### list

List existing topologies

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
>>> air.topologies.list()
[<Topology my_network1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <Topology my_network2 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.topology.TopologyApi.create"></a>
### create

Create a new topology. The caller must provide either `dot` (recommended) or `json`.

**Arguments**:

- `dot` _str | fd, optional_ - Topology in DOT format. This can be passed as a string
  containing the raw DOT data, a path to the DOT file on your local disk,
  or as a file descriptor for a local file
- `json` _dict, optional_ - Topology in JSON format
  

**Returns**:

  [`Topology`](/docs/topology)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.topologies.create(dot='/tmp/my_net.dot')
<Topology my_net 01298e0c-4ef1-43ec-9675-93160eb29d9f>
>>> air.topologies.create(dot='graph "my sim" { "server1" [ function="server" os="generic/ubuntu1804"] }')
<Topology my_net 6256baa8-f54b-4190-85c8-1cc574590080>
>>> air.topologies.create(dot=open('/tmp/my_net.dot', 'r'))
<Topology my_net a3d09f12-56ff-4889-8e03-3b714d32c3e5>
```

