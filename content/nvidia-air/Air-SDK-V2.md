---
product: NVIDIA Air
title: Air SDK V2
author: NVIDIA
weight: 999
type: nojsscroll
---

The NVIDIA Air SDK V2 provides a Python SDK for interacting with most [NVIDIA Air API V2 endpoints](https://air.nvidia.com/api/#/v2).

## API V1 and API V2 Overview

The Air API V2 endpoints offer robust methods for creating and managing simulations. You can initiate simulations through JSON file uploads or by sequentially using RESTful CRUD operations: first by creating a simulation, followed by adding nodes, defining interfaces for each node, and finally linking these interfaces. This structured approach allows for flexible and precise simulation design.

In the Air API V1 endpoints, simulations are structured through a combination of “topology” and “simulation” instances. A simulation comprises a “topology” instance along with a “simulation” instance that references this topology.

Individual nodes within the simulation are represented by “node” instances (which reference the topology) and “simulation_node” instances (which reference the simulation). The interfaces for each node are represented by “interface” instances (linked to “node” instances) and “simulation_interface” instances (linked to “simulation_node” instances).

With the Air API V2, these representations are streamlined for the client. A simulation directly contains “nodes,” which in turn contain “interfaces” that connect to one another. The separate concept of a “topology” is *almost* completely removed, providing a more straightforward structure.

<details>
<summary>Legacy references to topology</summary>
Although most API V2 endpoints make no reference to a topology, there are a few exceptions that are included in the API V2 that were created before the implementation and enforcement of the new convention.

- Topology file: https://air.nvidia.com/api/#/v2/v2_topology_file_list
- Topology patch: https://air.nvidia.com/api/#/v2/v2_topology_partial_update
- Topology put: https://air.nvidia.com/api/#/v2/v2_topology_partial_update
</details>

### Core Endpoints

- [Simulations](https://air.nvidia.com/api/#/v2/v2_simulations_list)
- [Nodes](https://air.nvidia.com/api/#/v2/v2_simulations_nodes_list)
- [Interfaces](https://air.nvidia.com/api/#/v2/v2_simulations_nodes_interfaces_list)
- [Links](https://air.nvidia.com/api/#/v2/v2_simulations_nodes_interfaces_links_list)

## Key Differences Between V1 and V2

### Separate Import Path

The V2 implementation of the SDK has a separate import from the [air_sdk](https://pypi.org/project/air-sdk/) package:

```python
from air_sdk import AirApi as AirApiV1  # Imports the original SDK
from air_sdk.v2 import AirApi  # Imports the V2 SDK

api = AirApi(username=..., password=...)
```

### Iterators Versus Lists

Because most API V2 endpoints that list data are [paginated](https://www.django-rest-framework.org/api-guide/pagination/#limitoffsetpagination), V2 SDK methods often return iterators (for example, api.simulations.list()) which improve performance but require iteration. Convert iterators to lists when indexing is required:

```python
from air_sdk.v2 import AirApi

api = AirApi(username=..., password=...)

simulation_list = list(api.simulations.list())  # Returns a list of simulation objects

simulation_iterator = api.simulations.list()  # Returns an Iterator

for simulation in simulation_iterator:  # The SDK will walk through the pagination to obtain all objects, potentially across multiple requests
    do_something(simulation)
```
The SDK uses a default page size of 200. You can adjust the page size to make fewer or more requests by calling `list` on the iterator:

```python
from air_sdk.v2 import AirApi

api = AirApi(username=..., password=...)
api.set_page_size(10000000)  # Set the page size to be arbitarily large to obtain all objects in one request
sims = list(api.simulations.list())  # will most likely only make 1 call to the Air API
```

### Type Hints and Checks

Most of the SDK V2 comes with type hints that provides assistance and validation when creating or updating objects:

```python
>>> from typing import get_type_hints
>>> for key, value in get_type_hints(air.simulations.create).items():
...    print(key, ':', value)
...
title : <class 'str'>
documentation : typing.Union[str, NoneType]
expires : typing.Union[bool, NoneType]
expires_at : typing.Union[datetime.datetime, NoneType]
metadata : typing.Union[str, NoneType]
organization : typing.Union[air_sdk.v2.endpoints.organizations.Organization, str, uuid.UUID, NoneType]
owner : typing.Union[str, NoneType]
preferred_worker : typing.Union[air_sdk.v2.endpoints.workers.Worker, str, uuid.UUID, NoneType]
sleep : typing.Union[bool, NoneType]
sleep_at : typing.Union[datetime.datetime, NoneType]
return : <class 'air_sdk.v2.endpoints.simulations.Simulation'>
```

### Set Custom Connection Timeouts

Clients can set a custom connection timeout for the SDK V2:

```python
from datetime import timedelta
from air_sdk.v2 import AirApi

api = AirApi(...)

api.set_connect_timeout(timedelta(minutes=2))
```
A custom read timeout may be set separately:
``` 
api.set_read_timeout(timedelta(minutes=2))
```

### Additional Authentication Support

The initialization process for the original and the V2 SDK is nearly identical:

```python
from air_sdk import AirApi as AirApiV1
from air_sdk.v2 import AirApi as AirApiV2

air_v1 = AirApiV1(
    api_url=...,
    username=...,
    password=...,
)
air_v2 = AirApiV2(
    api_url=...,
    username=...,
    password=...,
)
```

There is an additional option to skip authentication during the initialization of the SDK V2 and provide authentication credentials at a later time:

```python
from air_sdk.v2 import AirApi
api = AirApi(api_url=..., authenticate=False)
api.client.authenticate(username=..., password=...)
```

You can also use this method to switch which client is authenticated.

## Interact with Dataclass Objects

SDK V2 introduces dataclasses for representing various objects like simulations, nodes, images, and organizations in Python.

```python
>>> sim
Simulation(id='95bbbf37-a6d4-42b2-ab62-0234cc86370d', title='2k links', state='NEW', documentation=None, write_ok=True, metadata=None)
>>> sim.id
'95bbbf37-a6d4-42b2-ab62-0234cc86370d'
>>> sim.title
'2k links'
>>> sim.created
datetime.datetime(2024, 10, 18, 16, 11, 12, 659424, tzinfo=datetime.timezone.utc)
```
You can easily convert these objects to native Python dictionaries using the `.dict()` method:
```python
>>> sim.dict()
{'id': '95bbbf37-a6d4-42b2-ab62-0234cc86370d', 'title': '2k links', 'state': 'NEW', 'sleep': True, 'owner': 'tiparker@nvidia.com', 'cloned': False, 'expires': False, 'created': datetime.datetime(2024, 10, 18, 16, 11, 12, 659424, tzinfo=datetime.timezone.utc), 'modified': datetime.datetime(2024, 10, 31, 17, 50, 28, 905146, tzinfo=datetime.timezone.utc), 'sleep_at': datetime.datetime(2024, 10, 19, 4, 11, 12, 649304, tzinfo=datetime.timezone.utc), 'expires_at': datetime.datetime(2024, 11, 1, 16, 11, 12, 649000, tzinfo=datetime.timezone.utc), 'organization': '3b7c20c9-e525-46ac-96e3-a9a332aef774', 'preferred_worker': None, 'documentation': None, 'write_ok': True, 'metadata': None}
```

To convert to a JSON string, use the `.json()` method:

```python
>>> sim.json()
'{"id":"95bbbf37-a6d4-42b2-ab62-0234cc86370d","title":"2k links","state":"NEW","sleep":true,"owner":"tiparker@nvidia.com","cloned":false,"expires":false,"created":"2024-10-18T16:11:12.659424Z","modified":"2024-10-31T17:50:28.905146Z","sleep_at":"2024-10-19T04:11:12.649304Z","expires_at":"2024-11-01T16:11:12.649000Z","organization":"3b7c20c9-e525-46ac-96e3-a9a332aef774","preferred_worker":null,"documentation":null,"write_ok":true,"metadata":null}'
```

To synchronize an object’s data with the latest API state, use the `.refresh()` method:

```python
>>> sim.title
'2k links'
>>> sim.title = 'New Name'
>>> sim.title
'New Name'
>>> sim.refresh() # Refreshes the data from the API
>>> sim.title
'2k links'
```

### Directly Access Related Objects

As seen when calling `.json()` or `.dict()` above, `Simulation` instances might reference an associated `organization`.

It is often possible to directly access related objects. For example:

```python
>>> sim.organization
Organization(id='3b7c20c9-e525-46ac-96e3-a9a332aef774', name='Tim test org', member_count=8)
```

These related objects are created lazily, meaning the `Organization` object is fetched on-demand when accessed for the first time. This allows seamless traversal of relationships between connected objects:

```python
>>> sim
Simulation(id='95bbbf37-a6d4-42b2-ab62-0234cc86370d', title='2k links', state='NEW', documentation=None, write_ok=True, metadata=None)
>>> sim.organization
Organization(id='3b7c20c9-e525-46ac-96e3-a9a332aef774', name='Tim test org', member_count=8)
>>> sim.organization.dict()
{
    'id': '3b7c20c9-e525-46ac-96e3-a9a332aef774',
    'name': 'Tim test org',
    'member_count': 8,
    'resource_budget': 'b0c2a464-f6c5-4a9c-a65c-d8645d6fa01f'
}
>>> sim.organization.resource_budget
ResourceBudget(id='b0c2a464-f6c5-4a9c-a65c-d8645d6fa01f')
>>> sim.organization.resource_budget.dict()
{
    'id': 'b0c2a464-f6c5-4a9c-a65c-d8645d6fa01f',
    'cpu': 300,
    'cpu_used': 0,
    'image_uploads': 10000000000,
    'image_uploads_used': 111804416,
    'memory': 300000,
    'memory_used': 0,
    'simulations': 15,
    'simulations_used': 0,
    'storage': 3000,
    'storage_used': 0,
    'userconfigs': 10,
    'userconfigs_used': 0
}
```

When comparing objects accessed by different processes, you should compare the object's `id` (or other primary key):

```python
>>> id(sim) == id(node.simulation)  # Different objects in Python
False
>>> sim == node.simulation
False
>>> sim.id == node.simulation.id
True
```

## Query for Related Objects

In Air, simulations are structured with multiple nodes, and each node can contain several interfaces. In the SDK V2, these 'many-to-one' relationships—where a simulation contains many nodes, and a node contains multiple interfaces—must be explicitly queried to access all related entities. For example:

```python
from air_sdk.v2 import AirApi

air = AirApi(username=..., password=...)

```python
>>> sim = air.simulations.get('1ebf9958-a01e-4396-88f6-946e93299cf2')
>>> hasattr(sim, 'nodes')
False
```
Iterate through a list of nodes for a sim:
```python
>>> for node in air.nodes.list(simulation=sim):
...    print(node.name)
... 
oob-mgmt-switch
node7
node2
node3
node4
node1
node6
node10
oob-mgmt-server
node8
node5
node9
```
Alternatively, obtain a list of nodes by calling `list`:
```python
>>> nodes = list(air.nodes.list(simulation=sim))
>>> len(nodes)
12
```
Interfaces can be filtered by individual nodes or by simulations:
```python
>>> sim = air.simulations.get('<simulation-id>')
>>> node = next(air.nodes.list(simulation=sim))
>>> node_interfaces = list(air.interfaces.list(node=node))
>>> len(node_interfaces)
1
>>> sim_interfaces = list(air.interfaces.list(simulation=node.simulation))
>>> len(sim_interfaces)
29
```

## Create a Simulation

There are two paths for creating simulations using the SDK V2:
- File import
- Blank simulation creation

### File Import

You can create entire simulations efficiently and reliably by importing a file. This process is similar to the DOT file upload process supported by the original SDK and mirrors the [simulation import](https://air.nvidia.com/api/#/v2/v2_simulations_import_create) endpoint.

<!--
More details can be found in the [import instructions section](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Quick-Start/#import-a-topology) of the quick start guide.
-->
```python
from air_sdk.v2 import AirApi

air = AirApi(username=..., password=...)

simulation = air.simulations.create_from(
    'my-simulation',  # The Title
    'JSON',  # The format of the content. Only JSON is supported currently.
    {
        'nodes': {
            'node-1': {
                'os': 'generic/ubuntu2204',
            },
            'node-2': {
                'os': 'generic/ubuntu2204',
            },
        },
        'links': [
            [{'node': 'node-1', 'interface': 'eth1'}, {'node': 'node-2', 'interface': 'eth1'}]
        ]
    },
)
```

### Create a Blank Simulation

A blank simulation (that is, a simulation with no nodes) may be created via the basic [create simulation](https://air.nvidia.com/api/#/v2/v2_simulations_create) endpoint.

```python
from air_sdk.v2 import AirApi

air = AirApi(username=..., password=...)

personal_sim = air.simulations.create(title="Blank Simulation for myself")

org = next(air.organizations.list(search="My Favorite Organization"))
sim_for_my_org = air.simulations.create(
    title="Blank Simulation for my Favorite Org",
    organization=org,
)
```

Most fields specified by the [create simulation](https://air.nvidia.com/api/#/v2/v2_simulations_create) endpoint can be passed into the `air.simulations.create` method.

## Modify a Simulation

You can customize existing simulations by adjusting their fields, adding or removing nodes, and updating node interfaces. You can add or remove new interfaces from nodes and connect them as needed.

### Adjust the Fields on a Simulation Object

#### Select an Existing Simulation

You can retrieve an existing simulation with its ID:

```python
from air_sdk.v2 import AirApi

air = AirApi(username=..., password=...)

simulation = air.simulations.get('<simulation-id>')
```

Alternatively, you can query a simulation by the [list simulations](https://air.nvidia.com/api/#/v2/v2_simulations_list) endpoint:

```python
simulation = next(air.simulations.list(title="My Simulation Title"))  # using `next` gets the first result
```

You can query simulations by any of the values specified in [list simulations](https://air.nvidia.com/api/#/v2/v2_simulations_list).

```python
my_favorite_org = next(air.organizations.list(search="My Favorite Org"))  # using `next` returns the first result
simulation = next(air.simulations.list(title="My Simulation's Title", organization=my_favorite_org))
```

#### Update an Existing Simulation

Update specific fields by calling `.update`:

```
>>> sim = air.simulations.get('1ebf9958-a01e-4396-88f6-946e93299cf2')
>>> sim.title
'Sam Personal 10 w OOB'
>>> sim.update(title="Sam's Personal 10 node sim with OOB")
>>> sim.title
"Sam's Personal 10 node sim with OOB"
```

Calling `.update` on a simulation object corresponds to [PATCH simulation V2](https://air.nvidia.com/api/#/v2/v2_simulations_partial_update).

There is also a `.full_update` method on the simulation that updates all fields on the simulation:

```python
sim.full_update(
    title='New Title',
    documentation=sim.documentation,
    expires=sim.expires,
    expires_at=sim.expires_at,
    metadata=sim.metadata,
    preferred_worker=sim.preferred_worker,
    sleep=sim.sleep,
    sleep_at=sim.sleep_at,
)
```

`Node` and `Interface` objects have similar `.update` and `.full_update` methods for modifying their data.

#### Add New Nodes to a Simulation

```python
>>> image = next(air.images.list(name='generic/ubuntu2204'))  # Obtain an image for the node
>>> image
Image(name='generic/ubuntu2204', version='22.04', organization_name=None)
>>> new_node = air.nodes.create(simulation=sim, name='node13', os=image)
>>> new_node.os.id == image.id
True
>>> new_node.simulation.id == sim.id
True
```

## Export a Simulation

You can [export](https://air.nvidia.com/api/#/v2/v2_simulations_export_retrieve) existing simulations into a JSON representation, which you can share and [re-import](#file-import) into Air.

```python
from air_sdk.v2 import AirApi

air = AirApi(username=..., password=...)

sim_export_json = air.simulations.export(
    simulation='<simulation-id>',
    format='JSON',
    image_ids=True,  # defaults to False
)

# Or call `export` on a simulation object
simulation = air.simulations.get('<simulation-id>')

sim_export_json = simulation.export(format="JSON")
```
<!--
For more information, refer to the [export instructions](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Quick-Start/#export-a-topology) section in the quick start guide.
-->