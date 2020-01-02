---
title: Facebook Backpack Integration
author: Cumulus Networks
weight: 73
aliases:
 - /display/NETQ110/Facebook+Backpack+Integration
 - /pages/viewpage.action?pageId=7111339
pageID: 7111339
product: Cumulus NetQ
version: 1.1.0
imgData: cumulus-netq-110
siteSlug: cumulus-netq-110
---
NetQ can run within a [Facebook Backpack
chassis](https://cumulusnetworks.com/products/cumulus-express/getting-started/backpack/),
but it is considered to be an [early
access](/version/cumulus-netq-110/Early-Access-Features/) feature.

Keep the following issues in mind if you intend to use NetQ with a
Backpack chassis:

  - You must assign a unique hostname to every node that runs the NetQ
    Agent. By default, all the fabric cards in the chassis have the same
    hostname.

  - The NetQ Agent must be installed on every line card.

  - No information is returned about the ASIC when you run `netq show
    inventory asic`. This is a known issue.

  - Since the chassis sensor information is shared among, every line
    card and fabric card can report the same sensor data. By default,
    sensor data is disabled on a chassis. To enable sensor data on a
    line card, edit `/etc/cts/netq/netq.yml` or
    `/etc/cts/netq/config.d/user.yml` and set the
    `send_chassis_sensor_data` keyword to *true*, then restart the NetQ
    Agent with `netq config agent restart`. This prevents any
    duplication of data in the NetQ database.
    
        cumulus@backpack-lc101:~$ sudo nano /etc/cts/netq/netq.yml
         
        ...
         
        netq-agent:
          send_chassis_sensor_data: true
         
        ...

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
