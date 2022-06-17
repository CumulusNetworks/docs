---
product: NVIDIA Air
title: Air Python SDK
author: NVIDIA
weight: 999
type: nojsscroll
---

This project provides a Python SDK for interacting with the NVIDIA Air API (https://air.nvidia.com/api/).


# Prerequisite

The SDK requires python 3.7 or later. The safest way to install the SDK is to set up a virtual environment in python3.7:

```
apt-get install python3.7
```

```
python3.7 -m pip install virtualenv
```

```
python3.7 -m virtualenv venv37
```

```
. venv37/bin/activate
```

# Installation

To install the SDK, use pip. Choose the command that fits your context.

If using the modernized python3 method:

```
python3.7 -m pip install git+https://gitlab.com/cumulus-consulting/air/cumulus_air_sdk.git
```

If using the pip3 method:

```
pip3 install git+https://gitlab.com/cumulus-consulting/air/cumulus_air_sdk.git
```


# Usage

```
>>> from air_sdk import AirApi
>>> air = AirApi(username='<user>', password='<password>')
```

# Authentication Options

Using the API requires the use of either an API token, a username/password, or a bearer token.

## API token

To use an API token, one must first be generated. The easiest way to do this is via the [Air UI](https://air.nvidia.com/settings/api-tokens).

Once a token is generated:

```
>>> air = AirApi(username='<username>', password='<api_token>')
```

## Username/Password

To use a username/password, an administrator of NVIDIA Air must provision a service account. Once the administrator provides the username and password:

```
>>> air = AirApi(username='<username>', password='<password>')
```

## Bearer token

Generally, it's recommended to use an [API Token](#api-token) over a bearer token. However, a bearer token might be used for testing or quick-and-dirty operations that might not need a long term API token. To use a bearer token, the calling user must have a nvidia.com account and have previously approved access for NVIDIA Air. Once a token is obtained:

```
>>> air = AirApi(bearer_token='<bearer_token>')
```

## Interacting with the API

The SDK provides various helper methods for interacting with the API. For example:

```
>>> air.simulations.list()
[<Simulation sim1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <Simulation sim2 3134711d-015e-49fb-a6ca-68248a8d4aff>]
>>> sim1 = air.simulations.get('c51b49b6-94a7-4c93-950c-e7fa4883591')
>>> sim1.title = 'My Sim'
>>> sim1.store()
```

# Developing

Contributions to the SDK are very welcome. All code must pass linting and unit testing before it will be merged.

## Requirements

```
pip3 install -r requirements-dev.txt
```

## Linting

```
pylint **/*.py
```

## Unit testing

```
./unit_test.sh
```

## Generating docs

```
pydoc-markdown
```

# SDK Reference Guide

## Account
Manage an account
### json
Returns a JSON string representation of the account

### refresh
Syncs the account with all values returned by the API

<a name="air_sdk.account.AccountApi"></a>
## AccountApi

High-level interface for the Account API

<a name="air_sdk.account.AccountApi.get"></a>
### get

Get an existing account

**Arguments**:

- `account_id` _str_ - Account ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Account`](/docs/account)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.accounts.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Account mrobertson@nvidia.com 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.account.AccountApi.list"></a>
### list

List existing accounts

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
>>> air.accounts.list()
[<Account mrobertson@nvidia.com c51b49b6-94a7-4c93-950c-e7fa4883591>, <Account nmitchell@nvidia.com 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

Cumulus AIR API module

## AirSession

Wrapper around requests.Session

<a name="air_sdk.air_api.AirSession.rebuild_auth"></a>
### rebuild\_auth

Allow credential sharing between nvidia.com and cumulusnetworks.com only

<a name="air_sdk.air_api.AirApi"></a>
## AirApi

Main interface for an API client instance

<a name="air_sdk.air_api.AirApi.__init__"></a>
### \_\_init\_\_

Create a new API client instance. The caller MUST provide either `username` and `password`
or a `bearer_token`. The `password` argument may either be an API token or a service account
password.

**Arguments**:

- `username` _str, optional_ - Username
- `password` _str, optional_ - Password or API token
- `bearer_token` _str, optional_ - Pre-generated bearer token
- `api_url` _str, optional_ - Default = https://air.nvidia.com/api/
- `api_version` _str_ - Default = v1

<a name="air_sdk.air_api.AirApi.authorize"></a>
### authorize

Authorizes the API client using either a pre-generated API token, a service account
username/password, or a pre-generated bearer token.
Callers MUST pass either a valid `bearer_token` or a `username` and `password`.
The `password` argument may either be an API token or a service account
password. After successfully authorizing, all subsequent API calls will include the
authorization token provided by the AIR API. **Note:** This is called once automatically
when an AirApi object is instantiated.

**Arguments**:

- `bearer_token` _str, optional_ - Pre-generated bearer token
- `username` _str, optional_ - Username
- `password` _str, optional_ - Password or API token
  

**Raises**:

  ValueError - Caller did not pass either a token or a username/password

<a name="air_sdk.air_api.AirApi.get_token"></a>
### get\_token

Gets a new bearer token for a given username and password

**Arguments**:

- `username` _str_ - Username
- `password` _str_ - Password
  

**Returns**:

- `str` - Bearer token
  

**Raises**:

  - [`AirAuthorizationError`](/docs/exceptions) - API did not return a token
  - `JSONDecodeError` - API's response is not a valid JSON object

<a name="air_sdk.air_api.AirApi.get"></a>
### get

Wrapper method for GET requests

<a name="air_sdk.air_api.AirApi.post"></a>
### post

Wrapper method for POST requests

<a name="air_sdk.air_api.AirApi.put"></a>
### put

Wrapper method for PUT requests

<a name="air_sdk.air_api.AirApi.patch"></a>
### patch

Wrapper method for PATCH requests

<a name="air_sdk.air_api.AirApi.delete"></a>
### delete

Wrapper method for DELETE requests

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

## Demo
View demos

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

Custom exceptions for the AIR SDK

## AirError

Base exception class. All custom exceptions should inherit from this class.

<a name="air_sdk.exceptions.AirAuthorizationError"></a>
## AirAuthorizationError

Raised when authorization with the API fails.

<a name="air_sdk.exceptions.AirUnexpectedResponse"></a>
## AirUnexpectedResponse

Raised when the API returns an unexpected response.

<a name="air_sdk.exceptions.AirForbiddenError"></a>
## AirForbiddenError

Raised when an API call returns a 403 Forbidden error

<a name="air_sdk.exceptions.AirObjectDeleted"></a>
## AirObjectDeleted

Raised when accessing a previously instantiated object that has since been deleted

## Image
Manage an image

### delete
Delete the image. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](/docs/exceptions) when referenced.

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Delete failed
  
  ### json
  Returns a JSON string representation of the image
  
  ### refresh
  Syncs the image with all values returned by the API
  
  ### update
  Update the image with the provided data
  

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.image.Image.upload"></a>
### upload

Upload an image file

**Arguments**:

- `filename` _str_ - Absolute path to the local image
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Upload failed

<a name="air_sdk.image.ImageApi"></a>
## ImageApi

High-level interface for the Image API

<a name="air_sdk.image.ImageApi.get"></a>
### get

Get an existing image

**Arguments**:

- `image_id` _str_ - Image ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Image`](/docs/image)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.images.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Image cumulus-vx-4.2.1 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.image.ImageApi.list"></a>
### list

List existing images

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
>>> air.images.list()
[<Image cumulus-vx-4.2.1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <Image generic/ubuntu18.04 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.image.ImageApi.create"></a>
### create

Create a new image

**Arguments**:

- `name` _str_ - Image name
- `organization` _str | `Organization`_ - `Organization` or ID
- `filename` _str, optional_ - Absolute path to the local file which should be uploaded
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Image`](/docs/image)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.images.create(name='my_image', filename='/tmp/my_image.qcow2', agent_enabled=False)
<Image my_image 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```


<a name="air_sdk.interface.Interface"></a>
## Interface

View an interface

### json
Returns a JSON string representation of the interface

### refresh
Syncs the interface with all values returned by the API

<a name="air_sdk.interface.InterfaceApi"></a>
## InterfaceApi

High-level interface for the Interface API

<a name="air_sdk.interface.InterfaceApi.get"></a>
### get

Get an existing interface

**Arguments**:

- `interface_id` _str_ - Interface ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Interface`](/docs/interface)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.interfaces.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Interface eth0 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.interface.InterfaceApi.list"></a>
### list

List existing interfaces

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
>>> air.interfaces.list()
[<Interface eth0 c51b49b6-94a7-4c93-950c-e7fa4883591>, <Interface eth1 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

SimulationInterface module

<a name="air_sdk.simulation_interface.SimulationInterface"></a>
## SimulationInterface

Manage a simulation interface

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



<a name="air_sdk.job.Job"></a>
## Job

Manage a Job

### json
Returns a JSON string representation of the job

### refresh
Syncs the job with all values returned by the API

### update
Update the job with the provided data

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.job.JobApi"></a>
## JobApi

High-level interface for the Job API

<a name="air_sdk.job.JobApi.get"></a>
### get

Get an existing job

**Arguments**:

- `job_id` _str_ - Job ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Job`](/docs/job)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.jobs.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Job START 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.job.JobApi.list"></a>
### list

List existing jobs

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
>>> air.jobs.list()
[<Job START c51b49b6-94a7-4c93-950c-e7fa4883591>, <Job STOP 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```



## Link

Manage a link

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


## Login

View login information

### json
Returns a JSON string representation of the login info

### refresh
Syncs the login info with all values returned by the API

<a name="air_sdk.login.LoginApi"></a>
## LoginApi

High-level interface for the Login API

<a name="air_sdk.login.LoginApi.get"></a>
### get

Get login information or start an OAuth request. This is equivalent to `login.list()`.

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Login`](/docs/login)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.login.get()
<Login>
```

<a name="air_sdk.login.LoginApi.list"></a>
### list

Get login information or start an OAuth request. This is equivalent to `login.get()`.

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Login`](/docs/login)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.login.get()
<Login>
```


## Marketplace

View marketplace demos
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


## Node

Manage a node

### delete
Delete the node. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](/docs/exceptions) when referenced.

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Delete failed
  
  ### json
  Returns a JSON string representation of the node
  
  ### refresh
  Syncs the node with all values returned by the API
  
  ### update
  Update the node with the provided data
  

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.node.NodeApi"></a>
## NodeApi

High-level interface for the Node API

<a name="air_sdk.node.NodeApi.get"></a>
### get

Get an existing node

**Arguments**:

- `node_id` _str_ - Node ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Node`](/docs/node)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.nodes.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Node server 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.node.NodeApi.list"></a>
### list

List existing nodes

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
>>> air.nodes.list()
[<Node server c51b49b6-94a7-4c93-950c-e7fa4883591>, <Node switch 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.node.NodeApi.create"></a>
### create

Create a new node

**Arguments**:

- `name` _str_ - Node name
- `topology` _str | `Topology`_ - `Topology` or ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Node`](/docs/node)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.nodes.create(name='server', topology=topology)
<Node server 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```

<a name="air_sdk.simulation_node.SimulationNode"></a>
## SimulationNode

Manage a SimulationNode

### json
Returns a JSON string representation of the simulation node

### refresh
Syncs the simulation node with all values returned by the API

### update
Update the simulation node with the provided data

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.simulation_node.SimulationNode.create_instructions"></a>
### create\_instructions

Create instructions for the `SimulationNode`'s agent to execute

**Arguments**:

- `data` _str | list_ - Instruction data
- `executor` _str_ - Agent executor type
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

- `dict` - Response JSON
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> simulation_node.create_instructions(data='echo foo', executor='shell')
{'id': '67f73552-ffdf-4e5f-9881-aeae227604a3'}
```

<a name="air_sdk.simulation_node.SimulationNode.list_instructions"></a>
### list\_instructions

List all instructions for a `SimulationNode`

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
>>> simulation_node.instructions.list()
[{'id': '56abc69b-489f-429a-aed9-600f26afc956'}, {'id': '7c9c3449-f071-4bbc-bb42-bef04e44d74e'}]
```

<a name="air_sdk.simulation_node.SimulationNode.delete_instructions"></a>
### delete\_instructions

Delete all instructions for a `SimulationNode`

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Instruction delete failed
  

**Example**:

```
>>> simulation_node.instructions.delete()
```

<a name="air_sdk.simulation_node.SimulationNode.control"></a>
### control

Sends a control command to the `SimulationNode`.

**Arguments**:

- `action` _str_ - Control command
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

- `dict` - Response JSON
  

**Example**:

```
>>> simulation_node.control(action='reset')
{'result': 'success'}
```

<a name="air_sdk.simulation_node.SimulationNode.rebuild"></a>
### rebuild

Rebuild the `SimulationNode` back to its initial state. **All existing data will be lost.**

<a name="air_sdk.simulation_node.SimulationNode.reset"></a>
### reset

Reset the `SimulationNode`

<a name="air_sdk.simulation_node.SimulationNodeApi"></a>
## SimulationNodeApi

Wrapper for the SimulationNode API

<a name="air_sdk.simulation_node.SimulationNodeApi.get"></a>
### get

Get an existing simulation node

**Arguments**:

- `simulation_node_id` _str_ - SimulationNode ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`SimulationNode`](/docs/simulationnode)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulation_nodes.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<SimulationNode my_sim 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.simulation_node.SimulationNodeApi.list"></a>
### list

List existing simulation nodes

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
>>> air.simulation_nodes.list()
[<SimulationNode sim1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <SimulationNode sim2 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```


## Organization

Manage an organization

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


## Permission

Manage a permission

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


## Service

Manage a service

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


## Simulation

Manage a simulation

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


## SimulationInterface

Manage a simulation interface

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


## SimulationNode

Manage a simulation node

### json
Returns a JSON string representation of the simulation node

### refresh
Syncs the simulation node with all values returned by the API

### update
Update the simulation node with the provided data

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.simulation_node.SimulationNode.create_instructions"></a>
### create\_instructions

Create instructions for the `SimulationNode`'s agent to execute

**Arguments**:

- `data` _str | list_ - Instruction data
- `executor` _str_ - Agent executor type
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

- `dict` - Response JSON
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> simulation_node.create_instructions(data='echo foo', executor='shell')
{'id': '67f73552-ffdf-4e5f-9881-aeae227604a3'}
```

<a name="air_sdk.simulation_node.SimulationNode.list_instructions"></a>
### list\_instructions

List all instructions for a `SimulationNode`

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
>>> simulation_node.instructions.list()
[{'id': '56abc69b-489f-429a-aed9-600f26afc956'}, {'id': '7c9c3449-f071-4bbc-bb42-bef04e44d74e'}]
```

<a name="air_sdk.simulation_node.SimulationNode.delete_instructions"></a>
### delete\_instructions

Delete all instructions for a `SimulationNode`

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Instruction delete failed
  

**Example**:

```
>>> simulation_node.instructions.delete()
```

<a name="air_sdk.simulation_node.SimulationNode.control"></a>
### control

Sends a control command to the `SimulationNode`.

**Arguments**:

- `action` _str_ - Control command
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

- `dict` - Response JSON
  

**Example**:

```
>>> simulation_node.control(action='reset')
{'result': 'success'}
```

<a name="air_sdk.simulation_node.SimulationNode.rebuild"></a>
### rebuild

Rebuild the `SimulationNode` back to its initial state. **All existing data will be lost.**

<a name="air_sdk.simulation_node.SimulationNode.reset"></a>
### reset

Reset the `SimulationNode`

<a name="air_sdk.simulation_node.SimulationNodeApi"></a>
## SimulationNodeApi

Wrapper for the SimulationNode API

<a name="air_sdk.simulation_node.SimulationNodeApi.get"></a>
### get

Get an existing simulation node

**Arguments**:

- `simulation_node_id` _str_ - SimulationNode ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`SimulationNode`](/docs/simulationnode)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulation_nodes.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<SimulationNode my_sim 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.simulation_node.SimulationNodeApi.list"></a>
### list

List existing simulation nodes

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
>>> air.simulation_nodes.list()
[<SimulationNode sim1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <SimulationNode sim2 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```


## SSHKey

Manage an SSH key

### delete
Delete the key. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](/docs/exceptions) when referenced.

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Delete failed
  
  ### json
  Returns a JSON string representation of the key
  
  ### refresh
  Syncs the key with all values returned by the API

<a name="air_sdk.ssh_key.SSHKeyApi"></a>
## SSHKeyApi

High-level interface for the SSHKey API

<a name="air_sdk.ssh_key.SSHKeyApi.list"></a>
### list

List existing keys

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
>>> air.ssh_keys.list()
[<SSHKey mykey c51b49b6-94a7-4c93-950c-e7fa4883591>, <SSHKey test_key 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.ssh_key.SSHKeyApi.create"></a>
### create

Add a new public key to your account

**Arguments**:

- `name` _str_ - Descriptive name for the public key
- `public_key` _str_ - Public key
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`SSHKey`](/docs/sshkey)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.ssh_keys.create(name='my_pub_key', public_key='<key_string>')
<SSHKey my_pub_key 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```



## Token

Manage an API token

<a name="air_sdk.api_token.TokenApi"></a>
## TokenApi

High-level interface for the Token API

<a name="air_sdk.api_token.TokenApi.list"></a>
### list

List existing tokens

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  list
  

**Raises**:

  [`AirUnexpectedResponse`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.api_tokens.list()
[<Token mytoken c51b49b6-94a7-4c93-950c-e7fa4883591>, <Token test_token 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.api_token.TokenApi.create"></a>
### create

Add a new api token to your account

**Arguments**:

- `name` _str_ - Descriptive name for the public key
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Token`](/docs/token)
  

**Raises**:

  [`AirUnexpectedResponse`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.api_tokens.create(name='my_api_token')
<Token my_api_token 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```

<a name="air_sdk.api_token.TokenApi.delete"></a>
### delete

Delete the token

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  string
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Received an unexpected response 
  from the Cumulus AIR API (404): {"detail":"Not found."}
  

**Example**:

```
>>> air.api_tokens.delete()
'SUCCESS'
```


## Topology

Manage a topology

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


## Worker

Manage a worker

### json
Returns a JSON string representation of the worker

### refresh
Syncs the worker with all values returned by the API

### update
Update the worker with the provided data

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.worker.Worker.set_available"></a>
### set\_available

Sets a worker's `available` value in AIR

**Arguments**:

  available (bool)

<a name="air_sdk.worker.WorkerApi"></a>
## WorkerApi

High-level interface for the Worker API

<a name="air_sdk.worker.WorkerApi.get"></a>
### get

Get an existing worker

**Arguments**:

- `worker_id` _str_ - Worker ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Worker`](/docs/worker)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.workers.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Worker worker01 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.worker.WorkerApi.list"></a>
### list

List existing workers

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
>>> air.workers.list()
[<Worker worker01 c51b49b6-94a7-4c93-950c-e7fa4883591>, <Worker worker02 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.worker.WorkerApi.create"></a>
### create

Create a new worker

**Arguments**:

- `cpu` _int_ - Number of vCPUs the worker can support
- `memory` _int_ - Amount of memory (in MB) a worker can support
- `storage` _int_ - Amount of storage (in GB) a worker can support
- `ip_address` _str_ - Internal IP address
- `port_range` _str_ - Range of ports available on the worker
- `username` _str_ - Worker username for API access
- `password` _str_ - Worker password for API access
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Worker`](/docs/worker)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.workers.create(cpu=100, memory=200000, storage=1000, ip_address='10.1.1.1', port_range='10000-30000', username='worker01', password='secret')
<Worker my_sim 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```

