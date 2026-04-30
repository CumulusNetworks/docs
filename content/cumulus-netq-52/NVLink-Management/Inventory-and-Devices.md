---
title: Inventory and Devices
author: NVIDIA
weight: 850
toc: 4
---

The NetworkEntity tag groups all endpoints that manage inventory objects in the NVLink fabric: switches, switch nodes, chassis, compute nodes, GPUs, ports, and domains.

<!--need to include info about domain ops-->

## GPU API Endpoints

The `/v1/gpus` endpoint supports the following query parameters. These parameters allow you to scope GPU queries according to a specific chassis, slot, tray, or host without retrieving the entire inventory.

| Parameter | Type | Description | Dependencies |
|-----------|------|-------------|--------------|
| `device-uid` | string | Display a GPU according to its unique device identifier | None |
| `chassis-serial-number` | string | Display GPUs by chassis serial number | None |
| `slot-id` | integer | Display GPUs by slot identifier | Requires `chassis-serial-number` |
| `tray-index` | integer | Display GPUs by tray index | Requires `chassis-serial-number` |
| `host-id` | string | Display GPUs by host identifier | Requires `tray-index` or `slot-id` |
| `domain` | array | Display GPUs by domain UUID(s) | None |
| `pagination` | object | Control result set size with `offset` and `limit` | None |

<!--Avital to update and send
## GPU API Examples

Retrieve all GPUs within a given domain:


Example response:


-->

