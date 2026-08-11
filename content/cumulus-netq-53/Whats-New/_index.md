---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a list of open and fixed issues, see the {{<link title="NVIDIA NetQ 5.3 Release Notes" text="release notes">}}.

## What's New in NetQ 5.3.0

### NetQ for NVLink API Changes

- Added ability to replace the CA, server, or switch P12 certificates in-place, without reinstalling NetQ NVLink. See {{<link title="Upload Custom Certificates/#rotate-certificates" text="Rotate Certificates">}} for step-by-step workflows.
- Added {{<link title="Inventory and Devices/#delete-entities" text="delete endpoints">}} for compute nodes, switch nodes, chassis, and domains
- Refer to the {{<link title="NetQ NVLink API Changelog">}} for a comprehensive list of changes
- View the {{<exlink url="http://docs.nvidia.com/networking-ethernet-software/netq-nvlink-api-530/" text="REST API in Swagger">}}


## Upgrade Paths

NetQ 5.3 is available exclusively for on-premises deployments. You can upgrade to 5.3 if your deployment is running version 5.2 or 5.1. 

- To upgrade to NetQ 5.3, perform an {{<link title="Upgrade NetQ Virtual Machines" text="in-place upgrade">}}. 

## Compatible Agent Versions

The NetQ 5.3 server is compatible with NetQ agents 5.3 and 5.2. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.18, 5.17, 5.16, 5.15, 5.11
- Ubuntu 24.04, 22.04