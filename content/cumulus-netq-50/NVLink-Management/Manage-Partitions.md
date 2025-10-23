---
title: Manage Partitions
author: NVIDIA
weight: 850
toc: 4
bookhidden: true
---

Network partitions refer to logical groupings of GPUs within the same network domain. Partitions can be created based on one of two member types:

- GPU-ID-based: A list of specific GPU identifiers.
- Location-based: A set of objects describing the physical location, including attributes such as domain, chassis, slot, and host.

The member type of a partition is fixed at creation and cannot be modified later. All subsequent operations---such as updates or read requests---must use the same member type. For example, attempting to update a location-based partition using GPU IDs will result in a 409 Conflict error.

## API Endpoints

All asynchronous requests (create, update, and delete) return a 202 Accepted response immediately. This response includes:

- A JSON body:
{
  "operationId": "551137c2f9e1fac808a5f572"
}