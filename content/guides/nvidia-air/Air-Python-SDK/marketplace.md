---
menu: main
product: AIR SDK
title: Marketplace
---

# Table of Contents

* [air\_sdk.marketplace](#air_sdk.marketplace)
  * [Marketplace](#air_sdk.marketplace.Marketplace)
  * [MarketplaceApi](#air_sdk.marketplace.MarketplaceApi)
    * [get](#air_sdk.marketplace.MarketplaceApi.get)
    * [list](#air_sdk.marketplace.MarketplaceApi.list)

Marketplace module

<a name="air_sdk.marketplace.Marketplace"></a>
## Marketplace

View Marketplace Demos
### json
Returns a JSON string representation of the marketplace demo

### refresh
Syncs the marketplace demo with all values returned by the API

<a name="air_sdk.Marketplace.MarketplaceApi"></a>
## MarketplaceApi

High-level interface for the Marketplace API

<a name="air_sdk.marketplace.MarketplaceApi.get"></a>
### get

Get an existing Marketplace Demo

**Arguments**:

- `demo_id` _str_ - Marketplace Demo ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Marketplace`](/docs/marketplace)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.Marketplace.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Marketplace Demo EVPN 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.marketplace.MarketplaceApi.list"></a>
### list

List existing Marketplace demos

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
>>> air.marketplace.list()
[<Marketplace Demo EVPN c51b49b6-94a7-4c93-950c-e7fa4883591>, <Marketplace Demo Challenges 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

