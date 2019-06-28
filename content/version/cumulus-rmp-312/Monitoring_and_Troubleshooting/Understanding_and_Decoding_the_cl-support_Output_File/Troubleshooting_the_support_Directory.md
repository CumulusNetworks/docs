---
title: Troubleshooting the support Directory
author: Cumulus Networks
weight: 179
aliases:
 - /display/RMP31/Troubleshooting+the+support+Directory
 - /pages/viewpage.action?pageId=5122759
pageID: 5122759
product: Cumulus RMP
version: 3.1.2
imgData: cumulus-rmp-312
siteSlug: cumulus-rmp-312
---
The `support` directory is unique in the fact that it is not a copy of
the switch's filesystem. Actually, it is the output from various
commands. For example:

| File            | Equivalent Command               | Description                                                                                                                  |
| --------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| support/ip.addr | `cumulus@switch:~$ ip addr show` | This shows you all the interfaces (including swp front panel ports), IP address information, admin state and physical state. |
