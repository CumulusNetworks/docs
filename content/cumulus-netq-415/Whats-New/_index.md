---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. 

- For a list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.15 Release Notes" text="release notes">}}.
- To upgrade to NetQ 4.15, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrade-NetQ">}}.

## What's New in NetQ 4.15

NetQ 4.15.0 includes the following new features:

- The {{<link title="Validate Network Protocol and Service Operations" text="validation summary">}} has been re-designed to let you view all the results from recent validations and re-run validations directly from the summary
- {{<link title="Integrate NetQ with Grafana">}} and create custom dashboards to view telemetry data from switches, NICs, and GPUs
- Run {{<link title="Validate Network Protocol and Service Operations/#topology-validations" text="topology validations">}} using JSON blueprints
- New UI behavior: removed Close, use breadcrumb navigation to go back
- The cloud (OPTA) cluster deployment option is no longer available or supported


## Release Considerations

- When the NetQ agent is active and What Just Happened (WJH) is enabled, the Cumulus Linux 5.14 packet trimming feature will not work as expected. To enable packet trimming, you must disable NetQ What Just Happened with the `netq config del agent wjh` command, then apply the changes with `netq config restart agent`.
- The NetQ agent is not compatible with Broadcom switches. Reach out to your NVIDIA support representative if your environment requires NetQ compatibility with Broadcom switches.

### Upgrade Paths

For deployments running:



### Compatible Agent Versions

The NetQ 4.15 server is compatible with NetQ agents 4.15 and 4.14. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.13.1, 5.12.1
- Ubuntu 24.04, 22.04

NVIDIA recommends upgrading to the latest agent version.