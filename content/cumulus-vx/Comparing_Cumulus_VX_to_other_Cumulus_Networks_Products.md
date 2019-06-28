---
title: Comparing Cumulus VX to other Cumulus Networks Products
author: Cumulus Networks
weight: 13
aliases:
 - /display/VX/Comparing+Cumulus+VX+to+other+Cumulus+Networks+Products
 - /pages/viewpage.action?pageId=5126709
pageID: 5126709
product: Cumulus VX
version: 3.4.0
imgData: cumulus-vx
siteSlug: cumulus-vx
---
Cumulus VX is not a production-ready virtual switch or router. It has
the same foundation as Cumulus Linux and Cumulus RMP, including all the
control plane elements, but without an actual ASIC or NPU for line rate
performance or hardware acceleration.

You can use tools like `jdoo` to monitor the virtual switch. The same
automation, zero touch provisioning, security, and QoS tools are
available.

The following table outlines the similarities and differences between
Cumulus VX and other Cumulus Networks operating systems:

| Feature or Functionality                             | Cumulus VX                                                                                                                                                                                   |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Installation and Upgrade                             | New images available with every GA release.                                                                                                                                                  |
| Hardware acceleration                                | Datapath forwarding is dependent on the choice of hypervisor and VM resources.                                                                                                               |
| Hardware management                                  | None                                                                                                                                                                                         |
| Hardware limitations                                 | None. Dependent on hypervisor and VM resources. Certain features such as route-table-size might accommodate more routes than are supported in hardware (32K routes), given available memory. |
| Production-ready                                     | No                                                                                                                                                                                           |
| Linux extensibility                                  | Yes                                                                                                                                                                                          |
| Layer 2 features                                     | Yes; hypervisor/topology manager dependent.                                                                                                                                                  |
| Layer 3 features                                     | Yes                                                                                                                                                                                          |
| Network virtualization                               | Yes (software forwarding)                                                                                                                                                                    |
| OS management (ZTP, ifupdown2, third party packages) | Yes                                                                                                                                                                                          |
| Automation, monitoring, troubleshooting              | Yes                                                                                                                                                                                          |
| Security                                             | Yes                                                                                                                                                                                          |
| QoS                                                  | Yes                                                                                                                                                                                          |
