---
title: Manage Partitions
author: NVIDIA
weight: 850
toc: 4
---

Network partitions represent logical groupings of GPUs that reside within the same network domain. Partitions can be created based on one of two member types:

- GPU-ID-based: A list of unique GPU identifiers.
- Location-based: A set of objects describing each GPU’s physical placement, including attributes such as domain, chassis, slot, and host.

A partition's member type is fixed at creation and cannot be changed or updated. All subsequent operations---such as updates or read requests---must use the same member type. For example, attempting to update a location-based partition using GPU IDs will result in a `409 Conflict` error.

GPUs can only belong to one partition; all GPUs within a partition must belong to the same network domain.

## Partition API Endpoints

Use the `/v1/partitions` endpoint to create, update, view, or delete a partition. Most API responses return an operation ID, which you can use to query the status of the request:

| Endpoint | Description |
| :-- | :-- |
| GET `/nmx/v1/partitions` | Retrieve a list of partitions |
| POST `/nmx/v1/partitions` | Create a partition. The request body must include a partition name and a `members` object, which is either GPU-ID-based or location-based |
| GET `/nmx/v1/partitions/{id}` | Retrieve partition information, including health and metadata |
| PUT `/nmx/v1/partitions/{id}` | Update a partition. Note that the partition name cannot be modified. However, you can update its member list. When performing a PUT operation, the `members` parameter must include all GPUs that will belong to the partition. The system compares the provided list with the current configuration and adds or removes members automatically. |
| DELETE `/nmx/v1/support-packages/{id}` | Delete a partition |

## Monitor Partition Health

<!--is this required?-->

Depending on the resiliency mode for the partition, the partition can enter one of the following health states:

| Resiliency Mode | State | Description |
| :-- | :-- | :-- |
| Full-Bandwidth Mode | HEALTHY | Operates at full bandwidth and full compute capacity. This is the optimal state. |
|  | DEGRADED | Some GPUs may be *parked* with a NO_NVLINK health status. Remaining GPUs operate at full bandwidth; the partition remains operational. |
|  | UNHEALTHY | Internal failures render the partition non-operational.  |
| Adaptive-Bandwidth Mode | HEALTHY | Runs at full bandwidth and full compute capacity. This is the optimal state. |
|  | BANDWIDTH | Some trunk links are unavailable, reducing bandwidth. All GPUs can still communicate; considered operational. |
|  | UNHEALTHY | Internal failures render the partition non-operational.  |
| User-Action-Required Mode | HEALTHY | Operates at full bandwidth and full compute capacity. This is the optimal state. |
|  | DEGRADED_BANDWIDTH | Missing trunk links reduce communication bandwidth. All GPUs can still communicate; considered operational. |
|  | UNHEALTHY | Internal failures render the partition non-operational. |

## Related Information

- {{<exlink url="https://docs.nvidia.com/multi-node-nvlink-systems/partition-guide-v1-2.pdf" text="NVIDIA GB200 NVL Partition User Guide">}}
