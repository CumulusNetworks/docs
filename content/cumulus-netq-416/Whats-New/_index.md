---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. 

- For a list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.16 Release Notes" text="release notes">}}

## What's New in NetQ 4.15

NetQ 4.15.0 includes the following new features:

- The {{<link title="Validate Network Protocol and Service Operations" text="validation summary">}} has been redesigned to let you view all the results from recent validations. You can also re-run validations directly from the summary.
- You can now {{<link title="Integrate NetQ with Grafana" text="integrate NetQ with Grafana">}} and create custom dashboards to view telemetry data. The data is collected using OpenTelemetry and stored in a time-series database that you can also query directly (beta)
- {{<link title="Validate Network Protocol and Service Operations/#topology-validations" text="Topology validations">}} now support topology blueprint files in both JSON and DOT formats

The following features have been removed or deprecated:

- The cloud (OPTA) cluster deployment option is no longer available or supported
- The close button has been removed from the user interface. To navigate to different pages, use the links in the breadcrumb menu.


## Release Considerations

- When you upgrade to NetQ v4.15.0, any pre-existing validation data will be lost. Additionally, NetQ will not retain data related to network services (including BGP, LLDP, EVPN, and MLAG) after upgrading.
- You must upgrade cloud (OPTA) deployments to NetQ 4.15 before initiating a {{<link title="Switch Management/#switch-discovery" text="switch discovery">}}.

### Upgrade Paths

You can upgrade to NetQ 4.15 if your deployment is running version 4.14 or 4.13. For on-premises and cloud deployments, {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}, then concurrently restore your data and upgrade NetQ during a {{<link title="Install the NetQ System" text="new NetQ 4.15 installation">}}


### Compatible Agent Versions

The NetQ 4.15 server is compatible with NetQ agents 4.15 and 4.14. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.13.1, 5.12.1 <!--update to 5.14.0, 5.13.1 when 5.14 is released-->
- Ubuntu 24.04, 22.04

NVIDIA recommends upgrading to the latest agent version. The NetQ agent is not compatible with Broadcom switches. Reach out to your NVIDIA support representative if your networking environment requires Broadcom support.