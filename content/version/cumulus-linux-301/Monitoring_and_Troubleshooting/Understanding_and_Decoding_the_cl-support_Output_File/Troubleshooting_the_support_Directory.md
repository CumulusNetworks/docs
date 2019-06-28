---
title: Troubleshooting the support Directory
author: Cumulus Networks
weight: 283
aliases:
 - /display/CL30/Troubleshooting+the+support+Directory
 - /pages/viewpage.action?pageId=5118239
pageID: 5118239
product: Cumulus Linux
version: '3.0'
imgData: cumulus-linux-301
siteSlug: cumulus-linux-301
---
The `support` directory is unique in the fact that it is not a copy of
the switch's filesystem. Actually, it is the output from various
commands. For example:

| File            | Equivalent Command               | Description                                                                                                                  |
| --------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| support/ip.addr | `cumulus@switch:~$ ip addr show` | This shows you all the interfaces (including swp front panel ports), IP address information, admin state and physical state. |
