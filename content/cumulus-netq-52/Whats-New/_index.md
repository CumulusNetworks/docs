---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a list of open and fixed issues, see the {{<link title="NVIDIA NetQ 5.2 Release Notes" text="release notes">}}.

## What's New in NetQ 5.2


### NetQ for NVLink API Changes

- Refer to the {{<link title="NetQ NVLink API Changelog">}} for a comprehensive list of changes.
- View the {{<exlink url="http://docs.nvidia.com/networking-ethernet-software/netq-nvlink-api-510/" text="REST API in Swagger">}}.

## Release Considerations

- If your NetQ deployment uses combined Ethernet and NVLink mode, only your Ethernet data can be backed up and restored. NVLink data is excluded from the backup and restoration process. <!--need to verify-->
- NetQ 5.2 is tested and validated as part of the Spectrum-X reference architecture 2.2 release. For a full compatibility matrix, refer to the {{<exlink url="https://docs.nvidia.com/networking/software/spectrumx-solution-stack/index.html" text="NVIDIA Spectrum-X Validated Solution Stack">}}.
- The following features have been removed or deprecated:
    - Flow analysis (deprecated)
    - Validations: duplicate IP addresses, agents, VXLAN, MLAG bond VLAN consistency (deprecated)
    - ECMP without adaptive routing (removed) 

## Upgrade Paths

NetQ 5.1 is available exclusively for on-premises deployments. You can upgrade to 5.1 if your deployment is running version 5.0 or 4.15. First {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}, then concurrently restore your data and upgrade NetQ during a {{<link title="Install the NetQ System" text="new NetQ 5.1 installation">}}.


## Compatible Agent Versions

The NetQ 5.2 server is compatible with NetQ agents 5.2 and 5.1. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.16, 5.15, 5.11.3, 5.9.4 <!--need to verify-->
- Ubuntu 24.04, 22.04