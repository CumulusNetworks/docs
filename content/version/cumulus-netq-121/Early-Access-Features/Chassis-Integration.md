---
title: Chassis Integration
author: Cumulus Networks
weight: 73
aliases:
 - /display/NETQ121/Chassis+Integration
 - /pages/viewpage.action?pageId=8356590
pageID: 8356590
product: Cumulus NetQ
version: 1.2.1
imgData: cumulus-netq-121
siteSlug: cumulus-netq-121
---
NetQ can run within a [Facebook Backpack
chassis](https://cumulusnetworks.com/products/cumulus-express/getting-started/backpack/),
[Cumulus Express CX-10256-S
chassis](https://cumulusnetworks.com/products/cumulus-express/getting-started/cx10256s-omp800/)
or [Edgecore OMP-800
chassis](https://cumulusnetworks.com/products/cumulus-express/getting-started/cx10256s-omp800/),
but it is considered to be an [early
access](/version/cumulus-netq-121/Early-Access-Features/) feature.

Keep the following issues in mind if you intend to use NetQ with a
chassis:

  - You must assign a unique hostname to every node that runs the NetQ
    Agent. By default, all the fabric cards in the chassis have the same
    hostname.

  - The NetQ Agent must be installed on every line card.

  - No information is returned about the ASIC when you run `netq show
    inventory asic`. This is a known issue.

  - Since the chassis sensor information is shared among, every line
    card and fabric card can report the same sensor data. By default,
    sensor data is disabled on a chassis. To enable sensor data on a
    line card, edit `/etc/netq/netq.yml` or
    `/etc/netq/config.d/user.yml` and set the `send_chassis_sensor_data`
    keyword to *true*, then restart the NetQ Agent with `netq config
    agent restart`. This prevents any duplication of data in the NetQ
    database.
    
        cumulus@chassis-lc101:~$ sudo nano /etc/netq/netq.yml
         
        ...
         
        netq-agent:
          send_chassis_sensor_data: true
         
        ...

