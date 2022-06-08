---
menu: main
product: AIR SDK
title: Link
---

# Table of Contents

* [air\_sdk.link](#air_sdk.link)
  * [Link](#air_sdk.link.Link)
  * [LinkApi](#air_sdk.link.LinkApi)
    * [get](#air_sdk.link.LinkApi.get)
    * [list](#air_sdk.link.LinkApi.list)
    * [create](#air_sdk.link.LinkApi.create)

Link module

<a name="air_sdk.link.Link"></a>
## Link

Manage a Link

### delete
Delete the link. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](/docs/exceptions) when referenced.

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Delete failed
  
  ### json
  Returns a JSON string representation of the link
  
  ### refresh
  Syncs the link with all values returned by the API
  
  ### update
  Update the link with the provided data
  

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.link.LinkApi"></a>
## LinkApi

High-level interface for the Link API

<a name="air_sdk.link.LinkApi.get"></a>
### get

Get an existing link

**Arguments**:

- `link_id` _str_ - Link ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Link`](/docs/link)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.links.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Link 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.link.LinkApi.list"></a>
### list

List existing links

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
>>> air.links.list()
[<Link c51b49b6-94a7-4c93-950c-e7fa4883591>, <Link 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.link.LinkApi.create"></a>
### create

Create a new link

**Arguments**:

- `topology` _str | `Topology`_ - `Topology` or ID
- `interfaces` _list_ - List of `Interface` objects or IDs
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Link`](/docs/link)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.links.create(topology=topology, interfaces=[intf1, 'fd61e3d8-af2f-4735-8b1d-356ee6bf4abe'])
<Link 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```

