---
menu: main
product: AIR SDK
title: Capacity
---

# Table of Contents

* [air\_sdk.capacity](#air_sdk.capacity)
  * [Capacity](#air_sdk.capacity.Capacity)
  * [CapacityApi](#air_sdk.capacity.CapacityApi)
    * [get](#air_sdk.capacity.CapacityApi.get)

Capacity module

<a name="air_sdk.capacity.Capacity"></a>
## Capacity

View platform capacity

### json
Returns a JSON string representation of the capacity

### refresh
Syncs the capacity with all values returned by the API

<a name="air_sdk.capacity.CapacityApi"></a>
## CapacityApi

High-level interface for the Simulation API

<a name="air_sdk.capacity.CapacityApi.get"></a>
### get

Get current platform capacity for a [`Simulation`](/docs/simulation)

**Arguments**:

- `simulation_id` _str | `Simulation`_ - Simulation or ID
  

**Returns**:

  [`Capacity`](/docs/capacity)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.capacity.get(simulation)
<Capacity 30>
```

