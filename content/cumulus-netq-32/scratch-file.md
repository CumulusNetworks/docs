---
title: Scratch
author: Cumulus Networks
weight: 0
bookhidden: true
pdfhidden: true
---

{{< tabs "TabIDxxx" >}}

{{< tab "NetQ UI" >}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

{{< /tab >}}

{{< /tabs >}}

<div style="padding-left: 18px;">

-------------

cumulus@tor-1:mgmt:~$ netq tor-1 show wjh-drop between now and 7d

Matching wjh records:
Drop type          Aggregate Count
------------------ ------------------------------
L1                 560
Buffer             224
Router             144
L2                 0
ACL                0
Tunnel             0
cumulus@tor-1:mgmt:~$ netq tor-1 show wjh-drop details between now and 7d

Matching wjh records:
Drop type          Aggregate Count                Reason
------------------ ------------------------------ ---------------------------------------------
L1                 556                            None
Buffer             196                            WRED
Router             144                            Blackhole route
Buffer             14                             Packet Latency Threshold Crossed
Buffer             14                             Port TC Congestion Threshold
L1                 4                              Oper down
----------

install prep, cloud:
cumulus@ip-10-150-10-10:~$ netq bootstrap reset purge-db
Successfully reset the node. Please bootstrap the node again before continuing.
cumulus@ip-10-150-10-10:~$ netq bootstrap master interface eth0 tarball 's3://netq-archives/latest/netq-bootstrap-'3.2.0-SNAPSHOT.tgz
2020-09-29 15:53:40.295564: master-node-installer: Extracting tarball s3://netq-archives/latest/netq-bootstrap-3.2.0-SNAPSHOT.tgz
2020-09-29 15:55:15.991860: master-node-installer: Checking package requirements
2020-09-29 15:55:16.217339: master-node-installer: Using IP: 10.150.10.10
2020-09-29 15:55:18.300543: master-node-installer: Initializing kubernetes cluster
-----------------------------------------
Successfully bootstrapped the master node
cumulus@ip-10-150-10-10:~$ 


<div style="padding-left: 18px;">When multiple jobs are running, scroll down or use the filters above the jobs to find the jobs of interest:
<ul>
<li><strong>Time Range</strong>: Enter a range of time in which the upgrade job was created, then click <strong>Done</strong>.</li>
<li><strong>All switches</strong>: Search for or select individual switches from the list, then click <strong>Done</strong>.</li>
<li><strong>All switch types</strong>: Search for or select individual switch series, then click <strong>Done</strong>.</li>
<li><strong>All users</strong>: Search for or select individual users who created an upgrade job, then click <strong>Done</strong>.</li>
<li><strong>All filters</strong>: Display all filters at once to apply multiple filters at once. Additional filter options are included here. Click <strong>Done</strong> when satisfied with your filter criteria.</li>
</ul>

By default, filters show <em>all</em> of that items of the given filter type until it is restricted by these settings.
</div>

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