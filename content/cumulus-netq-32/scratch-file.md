---
title: Scratch
author: Cumulus Networks
weight: 0
draft: true
---

{{< tabs "TabIDxxx" >}}

{{< tab "NetQ UI" >}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

{{< /tab >}}

{{< /tabs >}}

## Switch Card/all alarms

1. Click in the **Global Search** field.

2. Enter the hostname or IP address of a switch.

    The medium Switch card shows the total number of alarms, and a distribution of alarms across three categories. Click **Alarms** to view the count of alarms. Click **Charts** to view a graph of the alarms over the time period on the card (default is 24 hours).

    {{<figure src="/images/netq/dev-switch-medium-alarms-charts-231.png" width="400">}}

3. Change to the full-screen card using the size picker to view a list of all of the individual alarms.

    {{<figure src="/images/netq/dev-switch-fullscr-alarms-tab-310.png" width="700">}}


```
cumulus@switch:~$ netq show resource-util

Matching resource_util records:
Hostname          CPU Utilization      Memory Utilization   Disk Name            Total                Used                 Disk Utilization     Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
exit01            9.2                  48                   /dev/vda4            6170849280           1524920320           26.8                 Wed Feb 12 03:54:10 2020
exit02            9.6                  47.6                 /dev/vda4            6170849280           1539346432           27.1                 Wed Feb 12 03:54:22 2020
leaf01            9.8                  50.5                 /dev/vda4            6170849280           1523818496           26.8                 Wed Feb 12 03:54:25 2020
leaf02            10.9                 49.4                 /dev/vda4            6170849280           1535246336           27                   Wed Feb 12 03:54:11 2020
leaf03            11.4                 49.4                 /dev/vda4            6170849280           1536798720           27                   Wed Feb 12 03:54:10 2020
leaf04            11.4                 49.4                 /dev/vda4            6170849280           1522495488           26.8                 Wed Feb 12 03:54:03 2020
spine01           8.4                  50.3                 /dev/vda4            6170849280           1522249728           26.8                 Wed Feb 12 03:54:19 2020
spine02           9.8                  49                   /dev/vda4            6170849280           1522003968           26.8                 Wed Feb 12 03:54:25 2020
```