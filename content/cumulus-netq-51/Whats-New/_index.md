---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. 

- For a list of open and fixed issues, see the {{<link title="NVIDIA NetQ 5.1 Release Notes" text="release notes">}}.

## What's New in NetQ 5.1


- Check which version of NetQ you are running using the NetQ for NVLink API <!--Swagger link-->
- Performance improvements to the account management page in the UI
- Decreased time to install NetQ
- Added Arm support <!--at risk-->


## Release Considerations



### Upgrade Paths

NetQ 5.1 is available exclusively for on-premises deployments. You can upgrade to 5.1 if your deployment is running version 5.0 or 4.15. First {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}, then concurrently restore your data and upgrade NetQ during a {{<link title="Install the NetQ System" text="new NetQ 5.0 installation">}}.


### Compatible Agent Versions

The NetQ 5.1 server is compatible with NetQ agents 5.1 and 5.0. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.16, 5.15, 5.11.3, 5.9.4
- Ubuntu 24.04, 22.04