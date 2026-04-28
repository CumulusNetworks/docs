---
title: Inventory and Devices
author: NVIDIA
weight: 850
toc: 4
---

The NetworkEntity section of the API lets you manage inventory and hardware objects in the NVLink fabric, including switches, chassis, compute nodes, GPUs, ports, and domains.

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
curl -X GET "https://<netq.domain>:443/api/nmx/v1/gpus?deviceUID=GPU-12345678" \
  -H "accept: application/json" \
  -H "Authorization: Basic <auth-token>"
```
{{< expand "Example response" >}}

```
[
  {
    "EntityID": "gpu-uuid-001",
    "DeviceUID": "GPU-12345678",
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
curl -X GET "https://<netq.domain>:443/api/nmx/v1/gpus?chassisSerialNumber=CH-SN-9876543" \
  -H "accept: application/json" \
  -H "Authorization: Basic <auth-token>"
```
{{< expand "Example response" >}}

```
[
  {
    "EntityID": "gpu-uuid-001",
    "DeviceUID": "GPU-12345678",
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
    "DeviceUID": "GPU-12345679",
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
curl -X GET "https://<netq.domain>:443/api/nmx/v1/gpus?chassisSerialNumber=CH-SN-9876543&slot-id=3" \
  -H "accept: application/json" \
  -H "Authorization: Basic <auth-token>"
```

{{< expand "Example response" >}}

```
[
  {
    "EntityID": "gpu-uuid-001",
    "DeviceUID": "GPU-12345678",
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
curl -X GET "https://<netq.domain>:443/api/nmx/v1/gpus?chassisSerialNumber=CH-SN-9876543&tray-index=1&host-id=compute-node-05" \
  -H "accept: application/json" \
  -H "Authorization: Basic <auth-token>"
```
{{< expand "Example response" >}}

```
[
  {
    "EntityID": "gpu-uuid-001",
    "DeviceUID": "GPU-12345678",
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
    "DeviceUID": "GPU-12345679",
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
