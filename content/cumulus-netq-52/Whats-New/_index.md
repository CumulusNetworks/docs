---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a list of open and fixed issues, see the {{<link title="NVIDIA NetQ 5.2 Release Notes" text="release notes">}}.

## What's New in NetQ 5.2.0

- Re-designed the {{<link title="Network Topology" text="network topology dashboard">}} so that you can visualize your network's topology according to the system labels assigned to a device (beta)
- You can now {{<link title="Disaster Recovery Using NFS" text="back up your NetQ data using an NFS server">}} for disaster recovery scenarios (beta)
- NetQ now supports {{<link title="System Events Reference/#correlation-events" text="fault correlation system events">}} which group events linked to the same underlying issue and displays the association between host-based errors and devices within a network’s fabric (beta)
- Added {{<link title="Validation Tests Reference/#adaptive-routing-validation-tests" text="adaptive routing validations">}} that verify configuration consistencies across switches in your network's fabric (beta)
- You can now add nodes to your existing NetQ NVLink + Ethernet combined mode deployments (beta)
- Added {{<link title="Validation Tests Reference/#roce-validation-tests" text="RoCE validations">}} that verify configuration consistencies across the entire network fabric, including switches, host NICs, and DPUs (beta)
- Added support for Arm-based systems
- You can now {{<link title="Create a NetQ Simulation in DSX Air" text="create NetQ simulations">}} using the NVIDIA DSX Air platform
- Updated the {{<link title="Cable Validations" text="Cable Validation Tool">}} to version 1.9
- Added IPv6 support for {{<link title="Switch Management/#switch-discovery" text="switch discovery">}} operations


### NetQ for NVLink API Changes
- Added a `/v1/redfish` endpoint to {{<link title="Sensor Events and Notifications" text="detect and report leak events">}} in liquid-cooling equipment
- Added `/v1/certificates` endpoints that let you use your own certificates instead of the ones that NetQ NVLink automatically generates. To use your own certificates, {{<link title="Install NetQ NVLink" text="install NetQ NVLink">}}, then {{<link title="Upload Custom Certificates" text="upload the certificates">}} using the API.
- Added `/v1/validations/fw-versions` endpoint to validate that all switches within a domain have the same firmware version
- Added ability {{<link title="Upgrade NVOS or Firmware" text="to upgrade firmware">}} using the `/v1/upgrade-switch` endpoint
- Added several `/v1/kpis` endpoints that allow you to {{<link title="Collect KPIs" text="apply KPI filters">}} to view heath metrics for GPUs, switch nodes, compute nodes, partitions, and domains over a range of time
- Added several parameters to the `/v1/gpus` endpoint that allow for filtering based on a device's UUID, chassis serial number, slot ID, tray index, or host ID
- Added parameter that allows you to {{<link title="Manage Partitions" text="manage partitions">}} using a device's unique identifier (UUID) with the `/v1/partitions` endpoints
- Added ability to adjust NMX-T polling frequency using the `/v1/settings` endpoint
- Added recommendation to {{<link title="NVLink Bringup/#switch-profile-endpoints" text="change switch credentials">}} from their default values to dedicated usernames and passwords for each switch
- Added support for NetQ NVLink on the NVIDIA Vera Rubin platform (beta)
- Refer to the {{<link title="NetQ NVLink API Changelog">}} for a comprehensive list of changes
- View the {{<exlink url="http://docs.nvidia.com/networking-ethernet-software/netq-nvlink-api-520/" text="REST API in Swagger">}}

## Release Considerations


- NetQ 5.2 is tested and validated as part of the Spectrum-X reference architecture 2.2 release. For a full compatibility matrix, refer to the {{<exlink url="https://docs.nvidia.com/networking/software/spectrumx-solution-stack/index.html" text="NVIDIA Spectrum-X Validated Solution Stack">}}.
- When your NetQ deployment operates in combined Ethernet and NVLink mode, certain NVLink data is not preserved during the backup and restore process. Information related to network entities such as switches, GPUs, and partitions is not saved. However, data for services, switch profiles, and domains is saved during the backup and restore process.
- The following features have been removed or deprecated:
    - Flow analysis (deprecated)
    - Validations: duplicate IP addresses, agents, VXLAN, MLAG bond VLAN consistency test (deprecated)
    - ECMP without adaptive routing (removed)
    - High-availability scale cluster deployment for Ethernet only (removed). You can upgrade this deployment type using the upgrade instructions for the NVLink + Ethernet combined mode deployment.

## Upgrade Paths

NetQ 5.2 is available exclusively for on-premises deployments. You can upgrade to 5.2 if your deployment is running version 5.1 or 5.0. 

- To upgrade from 5.1 to 5.2, perform an {{<link title="Upgrade NetQ Virtual Machines" text="in-place upgrade">}}. 
- To upgrade from 5.0 to 5.2, {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}, then concurrently restore your data and upgrade NetQ during a {{<link title="Install the NetQ System" text="new NetQ 5.2 installation">}}.


## Compatible Agent Versions

The NetQ 5.2 server is compatible with NetQ agents 5.2 and 5.1. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.16, 5.15, 5.11.3, 5.9.4 <!--need to verify-->
- Ubuntu 24.04, 22.04