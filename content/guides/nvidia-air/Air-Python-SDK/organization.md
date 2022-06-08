---
menu: main
product: AIR SDK
title: Organization
---

# Table of Contents

* [air\_sdk.organization](#air_sdk.organization)
  * [Organization](#air_sdk.organization.Organization)
  * [OrganizationApi](#air_sdk.organization.OrganizationApi)
    * [get](#air_sdk.organization.OrganizationApi.get)
    * [list](#air_sdk.organization.OrganizationApi.list)
    * [create](#air_sdk.organization.OrganizationApi.create)

Organization module

<a name="air_sdk.organization.Organization"></a>
## Organization

Manage an Organization

### delete
Delete the organization. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](/docs/exceptions) when referenced.

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Delete failed
  
  ### json
  Returns a JSON string representation of the organization
  
  ### refresh
  Syncs the organization with all values returned by the API
  
  ### update
  Update the organization with the provided data
  

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.organization.OrganizationApi"></a>
## OrganizationApi

High-level interface for the Organization API

<a name="air_sdk.organization.OrganizationApi.get"></a>
### get

Get an existing organization

**Arguments**:

- `organization_id` _str_ - Organization ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Organization`](/docs/organization)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.organizations.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Organization NVIDIA 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.organization.OrganizationApi.list"></a>
### list

List existing organizations

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
>>> air.organizations.list()
[<Organization NVIDIA c51b49b6-94a7-4c93-950c-e7fa4883591>, <Organization Customer 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.organization.OrganizationApi.create"></a>
### create

Create a new organization

**Arguments**:

- `name` _str_ - Organization name
- `members` _list_ - List of member [`Account`](/docs/account) objects or IDs
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Organization`](/docs/organization)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.organizations.create(name='NVIDIA', members=[account, 'fa42f2ce-8494-4d4d-87fd-d9ebc18831bd'])
<Organization NVIDIA 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```

