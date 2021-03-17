---
title: Scratch
author: NVIDIA
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

<div style="padding-left: 18px;">text</div>

<div class="notices note"><p>note text</p></div>

<!-- add a horizontal rule -->
- - -

{{< expand "title" >}}

{{< /expand >}}

{{<notice note>}}
When entering a time value in the <code>netq show evpn</code> command, you must include a numeric value <em>and</em> the unit of measure:
<ul>
<li><strong>w</strong>: week(s)</li>
<li><strong>d</strong>: day(s)</li>
<li><strong>h</strong>: hour(s)</li>
<li><strong>m</strong>: minute(s)</li>
<li><strong>s</strong>: second(s)</li>
<li><strong>now</strong>
</ul>

When using the <code>between</code> option, the start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{</notice>}}

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
