---
menu: main
product: AIR SDK
title: Permission
---

# Table of Contents

* [air\_sdk.permission](#air_sdk.permission)
  * [Permission](#air_sdk.permission.Permission)
  * [PermissionApi](#air_sdk.permission.PermissionApi)
    * [create](#air_sdk.permission.PermissionApi.create)
    * [get](#air_sdk.permission.PermissionApi.get)
    * [list](#air_sdk.permission.PermissionApi.list)

Permission module

<a name="air_sdk.permission.Permission"></a>
## Permission

Manage a Permission

### delete
Delete the permission. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](/docs/exceptions) when referenced.

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Delete failed
  
  ### json
  Returns a JSON string representation of the permission
  
  ### refresh
  Syncs the permission with all values returned by the API
  
  ### update
  Update the permission with the provided data
  

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.permission.PermissionApi"></a>
## PermissionApi

High-level interface for the Permission API

<a name="air_sdk.permission.PermissionApi.create"></a>
### create

Create a new permission. The caller MUST provide `simulation`, `topology`, or `subject_id`

**Arguments**:

- `email` _str_ - Email address for the user being granted permission
- `simulation` _str | `Simulation`, optional_ - `Simulation` or ID
- `topology` _str | `Topology`, optional_ - `Topology` or ID
- `subject_id` _str | `AirModel`, optional_ - `AirModel` instance or ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Permission`](/docs/permission)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.permissions.create(email='mrobertson@nvidia.com', topology=topology, write_ok=True)
<Permission 01298e0c-4ef1-43ec-9675-93160eb29d9f>
>>> air.permissions.create(email='mrobertson@nvidia.com',
... subject_id='80cf922a-7b80-4795-8cc5-550833ab1cec', subject_model='simulation.image')
<Permission 8a09ea66-51f9-4ddd-8416-62c266cd959e>
```

<a name="air_sdk.permission.PermissionApi.get"></a>
### get

Get an existing permission

**Arguments**:

- `permission_id` _str_ - Permission ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Permission`](/docs/permission)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.permissions.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Permission 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.permission.PermissionApi.list"></a>
### list

List existing permissions

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
>>> air.permissions.list()
[<Permission c51b49b6-94a7-4c93-950c-e7fa4883591>, <Permission 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

