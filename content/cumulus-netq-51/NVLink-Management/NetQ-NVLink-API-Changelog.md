---
title: API Changelog
author: NVIDIA
weight: 355
toc: 3
---

For more information, see the NetQ for NVLink Swagger documentation.

## 5.1 NetQ for NVLink REST API Changelog

- Added API methods to download support packages and upgrade NVOS for all switches within an NVLink domain. Switch-level operations receive priority over domain-level operations.
   - Added `GET /domain`
   - Added `GET /domains/count`
   - Added `GET /domains/{id}`
   - Added `profileID` in the response body of the `PATCH /domains/{id}` endpoint
   - Added `profileID` in the response body of the `PUT /switch-nodes/{id}` endpoint
   - Updated `POST /upgrade-switch` to support NVOS upgrades at the domain level
   - Updated `POST /tech-support` to download logs at the domain level
 - Added a fault-tolerance mechanism that allows NVLink switches with at least two out-of-band management ports to maintain connectivity to NMX controller and telemetry services in case one port fails.
    - Added `GET /services/{id}/connection`
    - Added `GET /services/connection`
- Added `GET /version` to get NetQ version