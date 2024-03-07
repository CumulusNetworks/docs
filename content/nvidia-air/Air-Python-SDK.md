---
product: NVIDIA Air
title: Air API & Python SDK
author: NVIDIA
weight: 999
type: nojsscroll
---

This project provides a Python SDK for interacting with the [NVIDIA Air API](https://air.nvidia.com/api/).

## SDK Usage
### Prerequisite for the SDK

The SDK requires Python 3.7 or later. The safest way to install the SDK is to set up a virtual environment in Python 3.7. For example:

```
$ apt-get install python3.7
$ python3.7 -m pip install virtualenv
$ python3.7 -m virtualenv venv37
$ . venv37/bin/activate
```

### Installation of the SDK

To install the SDK, use pip:

```
$ python3 -m pip install air-sdk
```

## Authentication Options

Authentication requires an API token, a username/password, or a bearer token.

### API token

The easiest way to generate an API token is with the [Air UI](https://air.nvidia.com/settings/api-tokens).

After a token is generated:

{{< tabs "TabID5555 ">}}
{{< tab "SDK ">}}

```
>>> air = AirApi(username='<username>', password='<api_token>')
```

{{< /tab >}}
{{< tab "cURL">}}
The API requires the use of the API Token to generate a bearer token:
```
curl --request POST 'https://air.nvidia.com/api/v1/login/' --form 'username="<user>"' --form 'password="<api_token>"'
```
The bearer token that is returned is used for authentication going forward:
```
curl --location --request <http_request>' \
--header 'Authorization: Bearer <bearer_token>'
```
{{< /tab >}}
{{< /tabs >}}


<details>
  <summary>Other Authentication Options</summary> 

### Username/Password

Username/password authentication is only valid for Air Service Accounts, which can only be created by NVIDIA Air administrators. After the administrator provides the username and password:

```
>>> air = AirApi(username='<username>', password='<password>')
```

### Bearer token

For SDK use, NVIDIA recommends using an [API token](#api-token) over a bearer token. However, a bearer token can be used for testing and performing operations that do not require a long term API token. To use a bearer token, the calling user must have an nvidia.com account and have previously approved access for NVIDIA Air. After you have obtained the token:

{{< tabs "TabID5593 ">}}
{{< tab "SDK ">}}
```
>>> air = AirApi(bearer_token='<bearer_token>')
```
{{< /tab >}}
{{< tab "cURL ">}}
Authenticate using the bearer token and get a list of all simulations:
```
curl --location --request GET 'https://air.nvidia.com/api/v1/simulation/' \
--header 'Authorization: Bearer <bearer_token>'
```
{{< /tab >}}
{{< /tabs >}}

### Service account

Internal NVIDIA users can use an SSA client ID to authenticate as a service account. First, a valid bearer token must be generated.

```
curl --user "$CLIENT_ID:$CLIENT_SECRET" --request POST $AIR_TOKEN_URL --header "Content-Type: application/x-www-form-urlencoded" --data-urlencode "grant_type=client_credentials" --data-urlencode "scope=api-access"
{"access_token":"eyJraWQ...","token_type":"bearer","expires_in":900,"scope":"api-access"}
```

Replace $CLIENT_ID, $CLIENT_SECRET, and $AIR_TOKEN_URL with values generated during your client registration. For more detail, please refer to internal documentation on using service accounts.

Once you have a bearer token, it can be used in the same way as an [Air bearer token](#bearer-token)

</details>

## Examples

### List all Simulations

The SDK provides various helper methods for interacting with the API. The example below shows how to list all simulations with the SDK and with the API using cURL:


{{< tabs "TabID5463 ">}}
{{< tab "SDK ">}}

```
>>> air.simulations.list()
[<Simulation sim1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <Simulation sim2 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

{{< /tab >}}
{{< tab "cURL">}}

```
curl --request GET 'https://air.nvidia.com/api/v1/simulation/' \
--header 'Authorization: Bearer <bearer_token>' 
```

{{< /tab >}}
{{< /tabs >}}

### Get a Specific Simulation 

To get a simulation with ID c51b49b6-94a7-4c93-950c-e7fa4883591:

{{< tabs "TabID5388 ">}}
{{< tab "SDK ">}}

```
>>> sim1 = air.simulations.get('c51b49b6-94a7-4c93-950c-e7fa4883591')
>>> print(sim1.title)
My Sim
```

{{< /tab >}}
{{< tab "cURL">}}

```
curl --request GET 'https://air.nvidia.com/api/v1/simulation/?id=c51b49b6-94a7-4c93-950c-e7fa4883591' \
--header 'Authorization: Bearer <bearer_token>'
```

{{< /tab >}}
{{< /tabs >}}

### Create a Simulation 
Create a simulation using a custom topology and custom organization.

Example topology.dot file:
```
graph "sample_topology" {
  "cumulus0" [ memory="1024" os="cumulus-vx-4.4.0" cpu="1"]
  "cumulus1" [ memory="1024" os="cumulus-vx-4.4.0" cpu="1"]
    "cumulus0":"swp1" -- "cumulus1":"swp1"
    "cumulus0":"swp2" -- "cumulus1":"swp2"
}
```
Create the organization, then create and start the simulation:

{{<notice note>}}
Organization creation is currently only supported for NVIDIA users.
{{</notice>}}

{{< tabs "TabID55113 ">}}
{{< tab "SDK ">}}

```
>>> from air_sdk import AirApi
>>> user = 'user@nvidia.com'
>>> api_token = 'fake_api_token'
>>> air = AirApi(username=user, password=api_token)
>>> dot_file_path = '/tmp/topology.dot'
>>> org_name = 'My Organization'
>>> org = air.organizations.create(name=org_name, members=[{'username': f'{user}', 'roles': ['Organization Admin']}])
>>> simulation = air.simulations.create(topology_data=dot_file_path, organization=org)
```
{{< /tab >}}
{{< tab "cURL ">}}


Create the organization:
```
curl --location --request POST 'https://air.nvidia.com/api/v1/organization/' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <bearer_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "My Organization",
  "members": [
    {
        "username": "user@nvidia.com"
    }
  ]
}'
```

Create and start the simulation:
```
curl --location --request POST 'https://air.nvidia.com/api/v2/simulation/' \
--header 'Authorization: Bearer <bearer_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "topology_data": "graph \"My Simulation\" {\n  \"cumulus0\" [ memory=\"1024\" os=\"cumulus-vx-5.7.0\" cpu=\"1\" ]\n  \"cumulus1\" [ memory=\"1024\" os=\"cumulus-vx-5.7.0\" cpu=\"1\"]\n    \"cumulus0\":\"swp1\" -- \"cumulus1\":\"swp1\"\n    \"cumulus0\":\"swp2\" -- \"cumulus1\":\"swp2\"\n}\n",
  "organization": "<organization_uuid>"
}'
```
{{< /tab >}}
{{< /tabs >}}

### Delete a Simulation
{{< tabs "TabID55289 ">}}
{{< tab "SDK ">}}

```
>>> from air_sdk import AirApi
>>> air = AirApi(username='<user>', password='<api_token>')
>>> simulation = air.simulations.get('<simulation_uuid>')
>>> simulation.delete()
```

{{< /tab >}}
{{< tab "cURL">}}

Find the simulation:
```
curl --request GET 'https://air.nvidia.com/api/v1/simulation/?id=<simulation_uuid>' \
--header 'Authorization: Bearer <bearer_token>'
```
Delete the simulation:
```
curl --request POST 'https://air.nvidia.com/api/v1/simulation/<simulation_uuid>/control/' \
--header 'Authorization: Bearer <bearer_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "action": "destroy",
}'
```

{{< /tab >}}
{{< /tabs >}}

### Enable SSH Service
Wake up a sleeping simulation and enable SSH to the oob-mgmt-server

Find and load the simulation:
{{< tabs "TabID55195 ">}}
{{< tab "SDK ">}}

```
>>> from air_sdk import AirApi
>>> air = AirApi(username='<user>', password='<api_token>')
>>> simulation = air.simulations.get('<simulation_uuid>')
>>> simulation.load()
```

{{< /tab >}}
{{< tab "cURL">}}
Load the simulation:
```
curl --request POST 'https://air.nvidia.com/api/v1/simulation/<simulation_id>/control/' \
--header 'Authorization: Bearer <bearer_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "action": "load",
  "start": true
}'
```
Note that the simulation ID will be used again later. 

{{< /tab >}}
{{< /tabs >}}

Enable ssh to the oob-mgmt-server's management port and print the command to ssh to the device:
{{< tabs "TabID55217 ">}}
{{< tab "SDK ">}}

```
>>> service_name = 'oob-mgmt-server SSH'
>>> interface = 'oob-mgmt-server:eth0'
>>> dest_port = 22
>>> service = air.services.create(name=service_name, interface=interface, simulation=simulation, dest_port=dest_port)
>>> print(f'ssh -p {service.src_port} {service.os_default_username}@{service.host}')
ssh -p 15738 ubuntu@worker.air.nvidia.com
```

{{< /tab >}}
{{< tab "cURL">}}

To enable SSH to a node's interface, the API requires the specific simulation-interface object's uuid or resource url. In this example, the simulation_id is 47c91cdd-93d2-42b7-9c94-1580a9e49a88 and the simulation-interface is eth0 on the oob-mgmt-server node.

To find the simulation interface uuid, first find the node object:
```
curl --request GET 'https://air.nvidia.com/api/v1/node/?name=oob-mgmt-server&simulation=47c91cdd-93d2-42b7-9c94-1580a9e49a88' \
--header 'Authorization: Bearer <bearer_token>' 
```
This will return a list containing one node. The node will have a list of interfaces:
```
[{
    "url": "https://air.nvidia.com/api/v1/node/f2b54dc7-2ec0-40de-b04f-8a2b8655814a/",
    "id": "f2b54dc7-2ec0-40de-b04f-8a2b8655814a",
    "name": "oob-mgmt-server",
    "os": "https://air.nvidia.com/api/v1/image/40000000-0000-0000-8050-000000000001/",
    "interfaces": [
        {
            "url": "https://air.nvidia.com/api/v1/interface/fc92eb67-0abb-4a36-8458-2ecf5cc8ec75/",
            "id": "fc92eb67-0abb-4a36-8458-2ecf5cc8ec75", <--------
            "name": "eth0",
            "mac_address": "04:ca:04:5a:6c:17",
            "outbound": true,
            "index": 5
        }
    ],
    "topology": "https://air.nvidia.com/api/v1/topology/0fbdfdef-c284-4287-85aa-1499fef18a3b/"
}]
```
Find the interface ID and use it to resolve the simulation-interface:
```
curl --request GET 'https://air.nvidia.com/api/v1/simulation-interface/?original=fc92eb67-0abb-4a36-8458-2ecf5cc8ec75' \
--header 'Authorization: Bearer <bearer_token>'
```
```
[{
    "url": "https://air.nvidia.com/api/v1/simulation-interface/bc084dc3-b009-430e-a49a-0699362f955a/",
    "id": "bc084dc3-b009-430e-a49a-0699362f955a", <--------
    "node": "https://air.nvidia.com/api/v1/simulation-node/fbfe474d-44ba-4ff5-b933-658a33857c96/",
    "original": "https://air.nvidia.com/api/v1/interface/fc92eb67-0abb-4a36-8458-2ecf5cc8ec75/",
    "link_up": false,
    "services": [
        "https://air.nvidia.com/api/v1/service/af474fff-4bc9-4590-9f68-0cd3c3b021da/"
    ],
    ...
}]
```

Finally, use the simulation-interface's ID in the interface param and the simulation ID to create the ssh service:
```
curl --request POST 'https://air.nvidia.com/api/v1/service/' \
--header 'Authorization: Bearer <bearer_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "oob-mgmt-server SSH",
  "simulation": "47c91cdd-93d2-42b7-9c94-1580a9e49a88",
  "interface": "bc084dc3-b009-430e-a49a-0699362f955a",
  "dest_port": 22
}'
```
The response will resemble the following:
```{
    "url": "https://air.nvidia.com/api/v1/service/af474fff-4bc9-4590-9f68-0cd3c3b021da/",
    "id": "af474fff-4bc9-4590-9f68-0cd3c3b021da",
    "name": "oob-mgmt-server SSH",
    "simulation": "https://air.nvidia.com/api/v1/simulation/47c91cdd-93d2-42b7-9c94-1580a9e49a88/",
    "interface": "https://air.nvidia.com/api/v1/simulation-interface/bc084dc3-b009-430e-a49a-0699362f955a/",
    "dest_port": 22,
    "src_port": 15502, <--------
    "link": "",
    "service_type": "other",
    "node_name": "oob-mgmt-server",
    "interface_name": "eth0",
    "host": "worker.air.nvidia.com", <--------
    "os_default_username": "ubuntu" <--------
}
```
The SSH command can be generated using the following template: 
```
ssh -p <src_port> <os_default_username>@<host>
```
Which produces a command similar to:
```
ssh -p 15502 ubuntu@worker.air.nvidia.com
```

{{< /tab >}}
{{< /tabs >}}

Use the oob-mgmt-server as a jump host, and ssh through the oob-mgmt-server to another node in the simulation:
```
>>> ssh -J ubuntu@worker.air.nvidia.com:15738 user@hostname
```

### Upload an Image and Create a Topology
Upload a custom image and create a topology using that image.

{{<notice note>}}
Image upload is currently only supported for NVIDIA users. 
{{</notice>}}

Upload and create the image object:
{{< tabs "TabID55242 ">}}
{{< tab "SDK ">}}

```
>>> from air_sdk import AirApi
>>> user = 'user@nvidia.com'
>>> api_token = 'fake_api_token'
>>> air = AirApi(username=user, password=api_token)
>>> image_name = 'My Image'
>>> filename = '/Users/user/my_image.qcow2'
>>> # Is the air-agent enabled in the Image by default?
>>> agent_enabled = False
>>> # Should the image be published and accessible to all users? 
>>> base = False
>>> default_username = 'admin'
>>> default_password = 'admin'
>>> organization = '<organization_uuid>'
>>> image = air.images.create(name=image_name, base=base, filename=filename, agent_enabled=agent_enabled, default_username=default_username, default_password=default_password, organization=organization)
```

{{< /tab >}}
{{< tab "cURL">}}

Create the image object:
```
curl --request POST 'https://air.nvidia.com/api/v1/image/' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <bearer_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "<image_name>",
  "base": "false",
  "agent_enabled": "false",
  "cpu_arch": "x86",
  "default_username": "admin",
  "organization": "<organization_id>",
  "simx": "false",
  "provider": "VM"
}'
```
The response will contain an image upload URL:
```
{
    "url": "https://air.nvidia.co,/api/v1/image/3d9a34e6-fd64-47bc-a65d-8a30f9f3ddc7/",
    "id": "3d9a34e6-fd64-47bc-a65d-8a30f9f3ddc7",
    ...
    "upload_url": "https://air.nvidia.com/api/v1/image/3d9a34e6-fd64-47bc-a65d-8a30f9f3ddc7/upload/", <--------
    ...
}
```
Use the provided upload_url to upload a local image file to Air:
```
curl --request PUT 'https://air.nvidia.com/api/v1/image/3d9a34e6-fd64-47bc-a65d-8a30f9f3ddc7/upload/' -F filename='@/Users/admin/fake_image.qcow2' \
--header 'Authorization: Bearer <bearer_token>'
```


{{< /tab >}}
{{< /tabs >}}


Use the image you created in a custom topology:
{{< tabs "TabID55269 ">}}
{{< tab "SDK ">}}

```
>>> topology_name = 'My Topology'
>>> node_name = 'server01'
>>> dot_graph = f'graph \"{topology_name}\" {{ \"{node_name}\" [ os=\"{image_name}\"] }}'
>>> simulation = air.simulations.create(topology_data=dot_graph)
```

{{< /tab >}}
{{< tab "cURL">}}

```
curl --request POST 'https://air.nvidia.com/api/v2/simulation/' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <bearer_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "topology_data": "graph \"My Topology\" {\n  \"cumulus0\" [ memory=\"1024\" os=\"<image_uuid>\" cpu=\"1\" ]\n  \"cumulus1\" [ memory=\"1024\" os=\"<image_uuid>\" cpu=\"1\" ]\n    \"cumulus0\":\"swp1\" -- \"cumulus1\":\"swp1\"\n    \"cumulus0\":\"swp2\" -- \"cumulus1\":\"swp2"\n}\n"
  }'
```

{{< /tab >}}
{{< /tabs >}}

### Using Node Instructions
Simulation nodes that have the Air agent installed can be configured via the API using node instructions. The Air agent is present in simulation nodes that use images where the agent_enabled flag is set to true.

After creating (but not starting) a simulation, get the ID of the simulation node that you want to configure: 

{{< tabs "TabID55000 ">}}
{{< tab "SDK ">}}

Find the simulation nodes for the simulation, and get the specific simulation node to be configured. In this example the node is named *sample-node*:
```
>>> simnodes = air.simulation_nodes.list(simulation=simulation)
>>> for simnode in simnodes:
>>>    if 'sample-node' == simnode.name:
>>>        sample_node = simnode
```

Edit /etc/network/interfaces on the sample-node and apply config with ifreload:

```
>>> eni_contents = '<string_containing_desired_etc_network_interfaces_content>''
>>> post_cmd = 'ifreload -a'
>>> data = {'/etc/network/interfaces': eni_contents, 'post_cmd': post_cmd}
>>> sample_node.create_instructions(data=json.dumps(data), executor='file')
```

Edit frr.conf on the sample-node and restart frr:
```
>>> frr_contents = '<frr_conf_config_here>'
>>> post_cmd = 'systemctl restart frr'
>>> data = {'/etc/frr/frr.conf': frr_contents, 'post_cmd':post_cmd}
>>> sample_node.create_instructions(data=json.dumps(data), executor='file')
```

To execute a command instead of populating the contents of a file, use the `shell` executor instead of `file`:
```
>>> data = 'ip link set swp1 ip address 192.168.100.2/24'
>>> sample_node.create_instructions(data=data, executor='shell')
```

Add a ZTP script to the node called oob-mgmt-server:
```
>>> oob_mgmt_server = air.simulation_nodes.list(simulation=simulation, name='oob-mgmt-server')[0]
>>> ztp_contents = '<ztp_script_content_here>'
>>> data = {'/var/www/html/cumulus-ztp': ztp_contents}
>>> oob_mgmt_server.create_instructions(data=json.dumps(data), executor='file')
```

Finally, start the simulation:
```
>>> simulation.start()
```
{{< /tab >}}
{{< tab "cURL">}}

Find the simulation's simulation nodes:
```
curl --request GET 'https://air.nvidia.com/api/v1/simulation-node/?simulation=<simulation_id>' \
--header 'Authorization: Bearer <bearer_token>'
```

Create and send the node instruction:
```
curl --request POST 'https://air.nvidia.com/api/v1/simulation-node/<simulation_node_id>/instructions/' \
--header 'Authorization: Bearer <bearer_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "executor": "file",
    "data": "{'\''/etc/frr/frr.conf'\'': '\''<frr.conf contents>'\'', '\''post_cmd'\'':,'\''systemctl restart frr'\''}"
}'
```
Alternately, use the shell executor instead of file to run a command:

```
curl --request POST 'https://air.nvidia.com/api/v1/simulation-node/<simulation_node_id>/instructions/' \
--header 'Authorization: <bearer_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "executor": "shell",
    "data": "ip link set swp1 ip address 192.168.100.2/24"
}'
```

{{< /tab >}}
{{< /tabs >}}

{{<notice info>}}
To avoid a race condition on Cumulus Linux nodes running a version prior to 5.0.0, schedule the node instructions prior to starting the simulation. If you do not perform the steps in this order, the instructions might fail to complete. 
{{</notice>}}

## Developing

Contributions to the SDK are very welcome. All code must pass linting and unit testing before it will be merged.

#### Requirements

```
python3 -m pip install -r requirements-dev.txt
```

#### Linting

```
pylint **/*.py
```

#### Unit testing

```
./unit_test.sh
```

#### Generating docs

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

  [`Account`](#account)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.accounts.list()
[<Account mrobertson@nvidia.com c51b49b6-94a7-4c93-950c-e7fa4883591>, <Account nmitchell@nvidia.com 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.account.AccountApi.preferences"></a>
### Preferences

Get account preferences

**Returns**:

- `dict` - Response JSON

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON

**Example**:

```
>>> air.accounts.preferences()
{"baz": true, "foo": false}
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

  - [`AirAuthorizationError`](#airerror) - API did not return a token
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

Get current platform capacity for a [`Simulation`](#simulation)

**Arguments**:

- `simulation_id` _str | `Simulation`_ - Simulation or ID
  

**Returns**:

  [`Capacity`](#capacity)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Demo`](#demo)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

### copy
Copy an image into another organization.

**Arguments**:

  - `organization` _str | `Organization`_ - Organization where the image should be copied

**Returns**:

  [`Image`](#image)

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Copy failed

### delete
Delete the image. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](#airerror) when referenced.

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Delete failed
  
  ### json
  Returns a JSON string representation of the image
  
  ### refresh
  Syncs the image with all values returned by the API
  
  ### update
  Update the image with the provided data
  

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

### publish
Publish an image for public use

**Arguments**:

  - `contact` _str_ - The email address for the contact person associated with this image.

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Publish failed

### unpublish
Unpublish the image from public use

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Unpublish failed

<a name="air_sdk.image.Image.upload"></a>
### upload

Upload an image file

**Arguments**:

- `filename` _str_ - Absolute path to the local image
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Upload failed

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

  [`Image`](#image)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Image`](#image)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> image = air.images.create(name='my_image', filename='/tmp/my_image.qcow2', agent_enabled=False)
>>> image
<Image my_image 01298e0c-4ef1-43ec-9675-93160eb29d9f>
>>> image.upload_status
'COMPLETE'
>>> alt_img = air.images.create(name='my_alt_img', filename='/tmp/alt_img.qcow2', agent_enabled=False)
>>> alt_img.upload_status
'FAILED'
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

  [`Interface`](#interface)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`SimulationInterface`](#simulationinterface)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Job`](#job)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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
[`AirDeletedObject`](#airerror) when referenced.

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Delete failed
  
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

  [`Link`](#link)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Link`](#link)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Login`](#login)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Login`](#login)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Marketplace`](#marketplace)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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
[`AirDeletedObject`](#airerror) when referenced.

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Delete failed
  
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

  [`Node`](#node)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Node`](#node)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> simulation_node.list_instructions()
[{'id': '56abc69b-489f-429a-aed9-600f26afc956'}, {'id': '7c9c3449-f071-4bbc-bb42-bef04e44d74e'}]
```

<a name="air_sdk.simulation_node.SimulationNode.delete_instructions"></a>
### delete\_instructions

Delete all instructions for a `SimulationNode`

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Instruction delete failed
  

**Example**:

```
>>> simulation_node.delete_instructions()
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

  [`SimulationNode`](#simulationnode)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulation_nodes.list()
[<SimulationNode sim1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <SimulationNode sim2 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.organization.Organization"></a>
## Organization

Manage an organization

<a name="air_sdk.organization.Organization.delete"></a>
### delete
Delete the organization. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](#airerror) when referenced.

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Delete failed

<a name="air_sdk.organization.Organization.json"></a>  
### json
Returns a JSON string representation of the organization

<a name="air_sdk.organization.Organization.refresh"></a>
### refresh
Syncs the organization with all values returned by the API

<a name="air_sdk.organization.Organization.update"></a>
### update
Update the organization with the provided data

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.organization.Organization.add_member"></a>
### add_member
Add a new member to the organization

**Arguments**:
- `username` _str_ - The email address of the user to add
- `roles` _list, optional_ - A list of roles to assign the user. Valid values are
  'Organization Admin' or 'Organization Member'. If no roles list is provided,
  'Organization Member' is used as the default role.

**Example**:

```
>>> organization.add_member('user1@nvidia.com')
>>> organization.add_member('user2@nvidia.com', roles=['Organization Admin'])
```

<a name="air_sdk.organization.Organization.add_members"></a>
### add_members
Add new members to the organization

**Arguments**:
- `members` _list_ - List of organization membership dicts in the format of
  {'username': <email_address>, 'roles': [<role>]}.
  'roles' is optional and defaults to ['Organization Member']
  <role> can be a value of 'Organization Admin' or 'Organization Member'.

**Example**:

```
>>> organization.add_members([{'username': 'user1@nvidia.com', 'roles': ['Organization Admin']}, {'username': 'user2@nvidia.com'}])
```

<a name="air_sdk.organization.Organization.remove_member"></a>
### remove_member
Remove a member from the organization

**Arguments**:
- `username` _str_ - The email address of the user to remove

**Example**:

```
>>> organization.remove_member('user1@nvidia.com')
```

<a name="air_sdk.organization.Organization.remove_members"></a>
### remove_members
Remove multiple members from the organization

**Arguments**:
- `members` _list_ - Email addresses of the users to remove

**Example**:

```
>>> organization.remove_members(['user1@nvidia.com', 'user2@nvidia.com'])
```

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

  [`Organization`](#organization)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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
- `members` _list, optional_ - List of organization membership dicts in the format of
  {'username': <email_address>, 'roles': [<role>]}.
  'roles' is optional and defaults to ['Organization Member']
  <role> can be a value of 'Organization Admin' or 'Organization Member'.
  If no member list is provided, the calling user's account will be set as the organization admin by default.
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Organization`](#organization)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.organizations.create(name='NVIDIA', members=[{'username': 'user1@nvidia.com', 'roles': ['Organization Admin']}, {'username': 'user2@nvidia.com'}])
<Organization NVIDIA 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```


## Permission

Manage a permission

### delete
Delete the permission. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](#airerror) when referenced.

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Delete failed
  
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

  [`Permission`](#permission)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Permission`](#permission)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.permissions.list()
[<Permission c51b49b6-94a7-4c93-950c-e7fa4883591>, <Permission 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```


## ResourceBudget

Manage a ResourceBudget

### json
Returns a JSON string representation of the budget

### refresh
Syncs the budget with all values returned by the API

### update
Update the budget with the provided data

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value pairs in the request's JSON payload

<a name="air_sdk.resource_budget.ResourceBudgetApi"></a>
## ResourceBudgetApi

High-level interface for the ResourceBudget API

<a name="air_sdk.resource_budget.ResourceBudgetApi.get"></a>
### get

Get an existing budget

**Arguments**:

- `budget_id` _str_ - ResourceBudget ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters

**Returns**:

  [`ResourceBudget`](#resource_budget)

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.resource_budgets.get('c604c262-396a-48a0-a8f6-31708c0cff82')
<ResourceBudget c604c262-396a-48a0-a8f6-31708c0cff82>
```

<a name="air_sdk.resource_budget.ResourceBudgetApi.list"></a>
### list

List existing budgets

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters

**Returns**:

  list

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON

**Example**:

```
>>> air.resource_budgets.list()
[<ResourceBudget c604c262-396a-48a0-a8f6-31708c0cff82>, <ResourceBudget 906675f7-8b8d-4f52-b59d-52847af2f0ef>]
```


## Service

Manage a service

### delete
Delete the service. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](#airerror) when referenced.

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Delete failed
  
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

  [`Service`](#service)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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
  - [`SimulationInterface`](#simulationinterface) object
  - ID of a [`SimulationInterface`](#simulationinterface)
  - String in the format of 'node_name:interface_name'
- `simulation` _str | `Simulation`_ - `Simulation` or ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Service`](#service)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

### preferences
Returns a JSON string representation of the simulation preferences

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
  - [`SimulationInterface`](#simulation-interface) object
  - ID of a [`SimulationInterface`](#simulation-interface)
  - String in the format of 'node_name:interface_name'
- `dest_port` _int_ - Service port number
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Service`](#service)
  

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

  [`Permission`](#permission)
  

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

  ([`Simulation`](#simulation), dict): Newly created simulation and response JSON
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Simulation`](#simulation)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Simulation`](#simulation)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulations.list()
[<Simulation sim1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <Simulation sim2 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.simulation.SimulationApi.create"></a>
### create

Create a new simulation. The caller must provide either `topology` or `topology_data`.

**Arguments**:

- `topology` _str | `Topology`, optional_ - `Topology` or ID
- `topology_data` _str | fd, optional_ - Topology in DOT format.
  This can be passed as a string containing the raw DOT data, a path to the DOT file on your local disk, or as a file descriptor for a local file
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Simulation`](#simulation)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.simulations.create(topology=topology, title='my_sim')
<Simulation my_sim 01298e0c-4ef1-43ec-9675-93160eb29d9f>
>>> air.simulations.create(topology_data='/tmp/my_net.dot', organization=my_org)
<Simulation my_sim c0a4c018-0b85-4439-979d-9814166aaeac>
>>> air.simulations.create(topology_data='graph "my_sim" { "server1" [ function="server" os="generic/ubuntu2204"] }', organization=my_org)
<Simulation my_sim b9c0c68e-d4bd-4e9e-8a49-9faf41efaf70>
>>> air.simulations.create(topology_data=open('/tmp/my_net.dot', 'r', encoding='utf-8')), organization=my_org)
<Simulation my_sim 86162934-baa7-4d9a-a826-5863f92b03ef>
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

  [`SimulationInterface`](#simulationinterface)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - Instruction delete failed
  

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

  [`SimulationNode`](#simulationnode)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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
[`AirDeletedObject`](#airerror) when referenced.

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Delete failed
  
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`SSHKey`](#sshkey)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedResponse`](#airerror) - API did not return a 200 OK
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

  [`Token`](#token)
  

**Raises**:

  [`AirUnexpectedResponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - Received an unexpected response 
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
[`AirDeletedObject`](#airerror) when referenced.

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - Delete failed
  
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

  [`Permission`](#permission)
  

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

  [`Topology`](#topology)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Topology`](#topology)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Worker`](#worker)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
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

  [`Worker`](#worker)
  

**Raises**:

  [`AirUnexpectedresponse`](#airerror) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.workers.create(cpu=100, memory=200000, storage=1000, ip_address='10.1.1.1', port_range='10000-30000', username='worker01', password='secret')
<Worker my_sim 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```

