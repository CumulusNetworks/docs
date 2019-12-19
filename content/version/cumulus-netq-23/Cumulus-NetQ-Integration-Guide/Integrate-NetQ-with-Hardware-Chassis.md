---
title: Integrate with Hardware Chassis
author: Cumulus Networks
weight: 204
aliases:
 - /display/NETQ/Integrate+with+Third+party+Software+and+Hardware
 - /pages/viewpage.action?pageId=12320911
pageID: 12320911
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq
siteSlug: cumulus-netq
---

NetQ can run within a [Facebook Backpack
chassis](https://cumulusnetworks.com/products/cumulus-express/getting-started/backpack/),
[Cumulus Express CX-10256-S
chassis](https://cumulusnetworks.com/products/cumulus-express/getting-started/cx10256s-omp800/)
or [Edgecore OMP-800
chassis](https://cumulusnetworks.com/products/cumulus-express/getting-started/cx10256s-omp800/).

Keep the following issues in mind if you intend to use NetQ with a
chassis:

  - You must assign a unique hostname to every node that runs the NetQ
    Agent. By default, all the fabric cards in the chassis have the same
    hostname.
  - The NetQ Agent must be installed on every line card.
  - No information is returned about the ASIC when you run `netq show
    inventory asic`. This is a known issue.
  - Since the chassis sensor information is shared, every line card and
    fabric card can report the same sensor data. By default, sensor data
    is disabled on a chassis to avoid this duplication . To enable
    sensor data on a line card, edit `/etc/netq/netq.yml` or
    `/etc/netq/config.d/user.yml` and set the `send_chassis_sensor_data`
    keyword to *true*, then restart the NetQ Agent with `netq config
    agent restart`. Configuring NetQ in this way prevents any
    duplication of data in the NetQ database.

        cumulus@chassis:~$ sudo nano /etc/netq/netq.yml
         
        ...
        netq-agent:
          send_chassis_sensor_data: true
        ...

