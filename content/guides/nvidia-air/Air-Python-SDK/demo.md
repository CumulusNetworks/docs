---
menu: main
product: AIR SDK
title: Demo
---

# Table of Contents

* [air\_sdk.demo](#air_sdk.demo)
  * [Demo](#air_sdk.demo.Demo)
  * [DemoApi](#air_sdk.demo.DemoApi)
    * [get](#air_sdk.demo.DemoApi.get)
    * [list](#air_sdk.demo.DemoApi.list)

Demo module

<a name="air_sdk.demo.Demo"></a>
## Demo

View Demos
### json
Returns a JSON string representation of the demo

### refresh
Syncs the demo with all values returned by the API

<a name="air_sdk.demo.DemoApi"></a>
## DemoApi

High-level interface for the Demo API

<a name="air_sdk.demo.DemoApi.get"></a>
### get

Get an existing demo

**Arguments**:

- `dmeo_id` _str_ - Demo ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Demo`](/docs/demo)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.demos.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Demo EVPN 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.demo.DemoApi.list"></a>
### list

List existing demos

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
>>> air.demos.list()
[<Demo EVPN c51b49b6-94a7-4c93-950c-e7fa4883591>, <Demo Challenges 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

