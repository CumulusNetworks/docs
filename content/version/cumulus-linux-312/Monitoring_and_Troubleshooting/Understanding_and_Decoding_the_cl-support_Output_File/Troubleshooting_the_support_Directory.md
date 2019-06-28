---
title: Troubleshooting the support Directory
author: Cumulus Networks
weight: 321
aliases:
 - /display/CL31/Troubleshooting+the+support+Directory
 - /pages/viewpage.action?pageId=5121959
pageID: 5121959
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
The `support` directory is unique in the fact that it is not a copy of
the switch's filesystem. Actually, it is the output from various
commands. For example:

| File            | Equivalent Command               | Description                                                                                                                  |
| --------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| support/ip.addr | `cumulus@switch:~$ ip addr show` | This shows you all the interfaces (including swp front panel ports), IP address information, admin state and physical state. |
