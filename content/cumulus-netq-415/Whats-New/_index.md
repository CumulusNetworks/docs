---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. 



## What's New in NetQ 4.15

NetQ 4.15.0 includes the following new features:


The following features have been removed or deprecated:

- The cloud (OPTA) cluster deployment option is no longer available or supported
- The close button has been removed from the user interface. To navigate to different pages, use the links in the breadcrumb menu.


## Release Considerations

- When you upgrade to NetQ v4.15.0, any pre-existing validation data will be lost. Additionally, NetQ will not retain data related to network services (including BGP, LLDP, EVPN, and MLAG) after upgrading.

### Upgrade Paths




### Compatible Agent Versions

The NetQ 4.15 server is compatible with NetQ agents 4.15 and 4.14. You can install NetQ agents on switches and servers running:

- Cumulus Linux 5.13.1, 5.12.1 <!--update to 5.14.0, 5.13.1 when 5.14 is released-->
- Ubuntu 24.04, 22.04

NVIDIA recommends upgrading to the latest agent version. The NetQ agent is not compatible with Broadcom switches. Reach out to your NVIDIA support representative if your networking environment requires Broadcom support.