---
title: Troubleshooting the support Directory
author: Cumulus Networks
weight: 269
aliases:
 - /display/CL25ESR/Troubleshooting+the+support+Directory
 - /pages/viewpage.action?pageId=5115972
pageID: 5115972
product: Cumulus Linux
imgData: cumulus-linux-25esr
siteSlug: cumulus-linux-25esr
---
The `support` directory is unique in the fact that it is not a copy of
the switch's filesystem. Actually, it is the output from various
commands. For example:

| File            | Equivalent Command               | Description                                                                                                                  |
| --------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| support/ip.addr | `cumulus@switch:~$ ip addr show` | This shows you all the interfaces (including swp front panel ports), IP address information, admin state and physical state. |

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
