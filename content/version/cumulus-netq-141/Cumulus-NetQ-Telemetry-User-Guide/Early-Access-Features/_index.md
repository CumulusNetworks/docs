---
title: Early Access Features
author: Cumulus Networks
weight: 73
aliases:
 - /display/NETQ141/Early+Access+Features
 - /pages/viewpage.action?pageId=10453494
pageID: 10453494
---
NetQ has [early access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878-Early-Access-Features-Defined) features that provide advanced access to new functionality before it
becomes generally available. The following features are early access in NetQ 1.4:

- [Collection of interface statistics](/cumulus-netq-141/Cumulus-NetQ-Telemetry-User-Guide/Early-Access-Features/Collect-Interface-Statistics)
- [Custom commands](/cumulus-netq-141/Cumulus-NetQ-Telemetry-User-Guide/Early-Access-Features/Extend-NetQ-with-Custom-Commands/)
- [Database queries](/cumulus-netq-141/Cumulus-NetQ-Telemetry-User-Guide/Early-Access-Features/Query-the-NetQ-Database)

In NetQ 1.4, early access features are bundled into the `netq-apps`
package; there is no specific EA package like there typically is with
Cumulus Linux.

You enable these early access features by running the ` netq config add
experimental  `command. You disable the early access features by running
the `netq config del experimental` command.

Refer to [Configure Optional NetQ Capabilities](/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Configure-Optional-NetQ-Capabilities) to access the Image and Provisioning Management application.
