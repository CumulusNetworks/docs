---
title: Inventory and Devices
author: NVIDIA
weight: 850
toc: 4
---

The NetworkEntity section of the API lets you manage inventory and hardware objects in the NVLink fabric, including switches, chassis, compute nodes, GPUs, ports, and domains. You can also delete entities from the fabric directly through the API.

## GPU API Endpoints

The `/v1/gpus` endpoint supports the following query parameters. These parameters allow you to scope GPU queries according to a specific chassis, slot, tray, or host without retrieving the entire inventory.

| Parameter | Type | Description | Dependencies |
|-----------|------|-------------|--------------|
| `deviceUID` | string | Display a GPU according to its unique device identifier | None |
| `chassisSerialNumber` | string | Display GPUs by chassis serial number | None |
| `slotID` | integer | Display GPUs by slot identifier | Requires `chassisSerialNumber`|
| `trayIndex` | integer | Display GPUs by tray index | Requires `chassisSerialNumber`|
| `hostID` | string | Display GPUs by host identifier | Requires `trayIndex` or `slotID` |
| `domain` | array | Display GPUs by domain UUID(s) | None |


## GPU API Examples

Retrieve a specific GPU using its unique device identifier:

```
curl -X GET "https://<ip_address>/nmx/v1/gpus?deviceUID=12345678" \
  -H "accept: application/json" \
  -H "Authorization: Basic <auth-token>"
```
{{< expand "Example response" >}}

```
[
  {
    "EntityID": "gpu-uuid-001",
    "DeviceUID": "12345678",
    "LocationInfo": {
      "ChassisID": "CH-SN-9876543",
      "SlotID": 3,
      "TrayIndex": 1,
      "HostID": "compute-node-05"
    },
    "State": "active",
    "GPUModel": "H100",
    "Memory": 80
  }
]
```
{{< /expand >}}
<br>
Retrieve all GPUs in a specific chassis:

```
curl -X GET "https://<ip_address>/nmx/v1/gpus?chassisSerialNumber=CH-SN-9876543" \
  -H "accept: application/json" \
  -H "Authorization: Basic <auth-token>"
```
{{< expand "Example response" >}}

```
[
  {
    "EntityID": "gpu-uuid-001",
    "DeviceUID": "12345678",
    "LocationInfo": {
      "ChassisID": "CH-SN-9876543",
      "SlotID": 3,
      "TrayIndex": 1,
      "HostID": "compute-node-05"
    },
    ...
  },
  {
    "EntityID": "gpu-uuid-002",
    "DeviceUID": "12345679",
    "LocationInfo": {
      "ChassisID": "CH-SN-9876543",
      "SlotID": 4,
      "TrayIndex": 1,
      "HostID": "compute-node-05"
    },
    ...
  }
]
```
{{< /expand >}}
<br>
Retrieve GPUs from a specific slot within a chassis:

```
curl -X GET "https://<ip_address>/nmx/v1/gpus?chassisSerialNumber=CH-SN-9876543&slotID=3" \
  -H "accept: application/json" \
  -H "Authorization: Basic <auth-token>"
```

{{< expand "Example response" >}}

```
[
  {
    "EntityID": "gpu-uuid-001",
    "DeviceUID": "12345678",
    "LocationInfo": {
      "ChassisID": "CH-SN-9876543",
      "SlotID": 3,
      "TrayIndex": 1,
      "HostID": "compute-node-05"
    },
    "State": "active",
    "GPUModel": "H100",
    "Memory": 80
  }
]
```
{{< /expand >}}
<br>
Retrieve GPUs from a specific tray and host combination:

```
curl -X GET "https://<ip_address>/nmx/v1/gpus?chassisSerialNumber=CH-SN-9876543&trayIndex=1&hostID=1" \
  -H "accept: application/json" \
  -H "Authorization: Basic <auth-token>"
```
{{< expand "Example response" >}}

```
[
  {
    "EntityID": "gpu-uuid-001",
    "DeviceUID": "12345678",
    "LocationInfo": {
      "ChassisID": "CH-SN-9876543",
      "SlotID": 3,
      "TrayIndex": 1,
      "HostID": "compute-node-05"
    },
    ...
  },
  {
    "EntityID": "gpu-uuid-002",
    "DeviceUID": "12345679",
    "LocationInfo": {
      "ChassisID": "CH-SN-9876543",
      "SlotID": 4,
      "TrayIndex": 1,
      "HostID": "compute-node-05"
    },
    ...
  }
]
```
{{< /expand >}}

## Delete Entities

Use the `DELETE` endpoints for chassis, compute nodes, switch nodes, and domains. Deletions cascade automatically to child entities so you do not need to delete them individually beforehand.

{{< notice note >}}
Deletion operations do not require a request body. Pass only the entity ID in the path.
{{< /notice >}}

### Delete a Chassis

`DELETE /v1/chassis/{id}` is a synchronous operation. It deletes the chassis and cascades to all child entities (compute nodes, switch nodes, switches, GPUs, ports, and partitions) in a single transaction. Returns `204` on success.

```
curl -X DELETE "https://<ip_address>/nmx/v1/chassis/<chassis-id>" \
  -H "Authorization: Basic <auth-token>"
```

### Delete a Compute Node

`DELETE /v1/compute-nodes/{id}` is a synchronous operation. It deletes the compute node and its associated GPUs and ports in a single transaction. Returns `204` on success. If any of the compute node's GPUs is a member of an active partition, the request returns `409 Conflict`. Detach or delete the partition before retrying.


```
curl -X DELETE "https://<ip_address>/nmx/v1/compute-nodes/<compute-node-id>" \
  -H "Authorization: Basic <auth-token>"
```

### Delete a Switch Node

`DELETE /v1/switch-nodes/{id}` is a synchronous operation. It deletes the switch node and its switches and ports in a single transaction. Returns `204` on success.

```
curl -X DELETE "https://<ip_address>/nmx/v1/switch-nodes/<switch-node-id>" \
  -H "Authorization: Basic <auth-token>"
```

### Delete a Domain

`DELETE /v1/domains/{id}` is an asynchronous operation. Unlike the other delete endpoints, it returns `202 Accepted` immediately and runs in the background. It deletes the domain and all related entities: chassis, switch nodes, compute nodes, switches, GPUs, ports, partitions, and associated NMX services.

When a domain is being deleted, it enters a draining state that rejects all new operations until the deletion operation completes.

```
curl -X DELETE "https://<ip_address>/nmx/v1/domains/<domain-id>" \
  -H "accept: application/json" \
  -H "Authorization: Basic <auth-token>"
```
Use the returned `operationId` to track progress:

```
curl -X GET "https://<ip_address>/nmx/v1/operations/551137c2f9e1fac808a5f572" \
  -H "accept: application/json" \
  -H "Authorization: Basic <auth-token>"
```
