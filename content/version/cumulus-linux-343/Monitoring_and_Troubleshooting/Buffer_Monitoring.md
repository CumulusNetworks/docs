---
title: Buffer Monitoring
author: Cumulus Networks
weight: 219
aliases:
 - /display/CL34/Buffer+Monitoring
 - /pages/viewpage.action?pageId=7112383
pageID: 7112383
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
---
Monitoring [packet
buffers](/version/cumulus-linux-343/Interface_Configuration_and_Management/Buffer_and_Queue_Management/)
and their utilization is vital for proper traffic management on a
network. It is quite useful for:

  - Identifying microbursts that result in longer packet latency

  - Giving early warning signs of packet buffer congestion that could
    lead to packet drops

  - Quickly identifying a network problem with a particular switch, port
    or traffic class

You can use buffer utilization monitoring to quickly filter out
non-problematic switches so you can focus on the ones causing trouble on
the network.

The monitoring involves a set of configurable triggers, that, when
triggered can lead to any or all of the following three actions:

  - **Log actions**, which involves writing to `syslog`

  - **Snapshot actions**, which involves writing to a file detailing the
    current state

  - **Collect actions**, where the switch can collect more information

The monitoring is managed by the `asic-monitor` service, which is in
turn managed by `systemd`.

{{%notice warning%}}

Buffer monitoring is supported on Mellanox switches only.

{{%/notice%}}

## <span>Understanding Histograms</span>

The Mellanox Spectrum ASIC provides a mechanism to measure and report
egress queue lengths in *histograms*. You can configure the ASIC to
measure up to 64 egress queues. Each queue is reported through a
histogram with 10 bins, where each bin represents a range of queue
lengths.

You configure the histogram with a minimum size boundary (*Min*) and a
histogram size — the
*monitor.histogram\_pg.histogram.minimum\_bytes\_boundary* and
*monitor.histogram\_pg.histogram.bin\_size\_bytes* settings, which are
described in the table below.

You then derive the maximum size boundary (*Max*) by adding the Min and
the histogram size.

The 10 bins are numbered 0 through 9. Bin 0 represents queue lengths up
to the Min specified, including queue length 0.

Bin 9 represents queue lengths of Max and above.

Bins 1 through 8 represent equal-sized ranges between the Min and Max,
which is determined by dividing the histogram size by 8.

For example, consider the following histogram queue length ranges, in
bytes:

  - Min = 960

  - Histogram size = 12288

  - Max = 13248

  - Range size = 1536

  - Bin 0: 0:959

  - Bin 1: 960:2495

  - Bin 2: 2496:4031

  - Bin 3: 4032:5567

  - Bin 4: 5568:7103

  - Bin 5: 7104:8639

  - Bin 6: 8640:10175

  - Bin 7: 10176:11711

  - Bin 8: 11712:13247

  - Bin 9: 13248:\*

When using the snapshot action, all of this information is captured in
the file specified by the *monitor.histogram\_pg.snapshot.file* setting.

## <span>Configuring Buffer Monitoring</span>

The `asic-monitor` tool has a number of settings you need to configure
before you can start monitoring. They're described in the following
table:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Setting</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>monitor.port_group_list</p></td>
<td><p>A user-defined list of all the port groups in the monitor file. The configuration file contains the following port group names as examples:</p>
<ul>
<li><p>all_packet_pg</p></li>
<li><p>buffers_pg</p></li>
<li><p>discards_pg</p></li>
<li><p>histogram_pg</p></li>
</ul>
<p>You must specify at least one port group. If the port group list is empty, then <code>systemd</code> shuts down the <code>asic-monitor</code> service.</p></td>
</tr>
<tr class="even">
<td><p>monitor.histogram_pg.port_set</p></td>
<td><p>The range of ports for which histograms are configured. This setting can take GLOBs and comma-separated lists, like <em>swp1-swp4,swp8,swp10-swp50</em>.</p></td>
</tr>
<tr class="odd">
<td><p>monitor.histogram_pg.stat_type</p></td>
<td><p>Each port group monitors one kind of hardware state, in this case, a <em>histogram</em>.</p></td>
</tr>
<tr class="even">
<td><p>monitor.histogram_pg.cos_list</p></td>
<td><p>Each CoS (Class of Service) value in the list has its own histogram on each port.</p></td>
</tr>
<tr class="odd">
<td><p>monitor.histogram_pg.trigger_type</p></td>
<td><p>The type of trigger that can initiate state collection. The only valid option is <em>timer</em>. This setting is optional.</p>
<p>If no port group has its trigger type set to <em>timer</em>, the <code>asic-monitor</code> service exits without an error.</p></td>
</tr>
<tr class="even">
<td><p>monitor.histogram_pg.timer</p></td>
<td><p>The frequency at which the histogram triggers; for example, a setting of <em>1s</em> indicates it executes once per second.</p>
<p>The timer can be set to:</p>
<ul>
<li><p>1 to 60 seconds, so <em>1s</em>, <em>2s</em>, and so on up to <em>60s</em></p></li>
<li><p>1 to 60 minutes, so <em>1m</em>, <em>2m</em>, and so on up to <em>60m</em></p></li>
<li><p>1 to 24 hours, so <em>1h</em>, <em>2h</em>, and so on up to <em>24h</em></p></li>
<li><p>1 to 7 days, so <em>1d</em>, <em>2d</em> and so on up to <em>7d</em></p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>monitor.histogram_pg.action_list</p></td>
<td><p>State collection is initiated when triggered by the <code>asic-monitor</code> service. The state collection may result in one or more actions — <em>snapshot</em>, <em>collect</em> and <em>log</em> — in response.</p></td>
</tr>
<tr class="even">
<td><p>monitor.histogram_pg.snapshot.file</p></td>
<td><p>The prefix file name for the snapshot file. All snapshots use this name, with a sequential number appended to it. For example, <em>/var/lib/cumulus/histogram_stats_0</em>.</p></td>
</tr>
<tr class="odd">
<td><p>monitor.histogram_pg.snapshot.file_count</p></td>
<td><p>The number of snapshots that can be created before the first snapshot file is overwritten. While more snapshots can provide you with more data, they can occupy a lot of disk space on the switch. See <a href="#src-7112383_BufferMonitoring-caveats">Caveats and Errata</a> below.</p></td>
</tr>
<tr class="even">
<td><p>monitor.histogram_pg.histogram.minimum_bytes_boundary</p></td>
<td><p>The minimum boundary size for the histogram in bytes. On a Mellanox switch, this number must be a multiple of 96.</p>
<p>Adding this number to the size of the histogram produces the maximum boundary size.</p></td>
</tr>
<tr class="odd">
<td><p>monitor.histogram_pg.histogram.bin_size_bytes</p></td>
<td><p>The size of the histogram in bytes.</p>
<p>Adding this number and the minimum_bytes_boundary value together produces the maximum boundary size.</p></td>
</tr>
<tr class="even">
<td><p>monitor.histogram_pg.histogram.sample_time_ns</p></td>
<td><p>The sampling time of the histogram in nanoseconds.</p></td>
</tr>
<tr class="odd">
<td><p>monitor.histogram_pg.log.queue_bytes</p></td>
<td><p>The length of the queue in bytes before the log action writes a message to <code>syslog</code>.</p></td>
</tr>
<tr class="even">
<td><p>monitor.histogram_pg.collect.queue_bytes</p></td>
<td><p>During state collection, when this queue length (measured in bytes) is reached, the collect action initiates another state collection.</p></td>
</tr>
<tr class="odd">
<td><p>monitor.histogram_pg.collect.port_group_list</p></td>
<td><p>The port groups that get triggered by the histogram_pg collect action.</p></td>
</tr>
</tbody>
</table>

The configuration is stored in the `/etc/cumulus/datapath/monitor.conf`
file. You edit the settings in the file directly with a text editor.
There is no default configuration. Here is a sample configuration:

    cumulus@switch:~$ cat /etc/cumulus/datapath/monitor.conf
     
    monitor.port_group_list = [discards_pg,histogram_pg,all_packet_pg,buffers_pg]
     
    # The queue length histograms are collected every second
    # and the results are written to a snapshot file.
    # Sixty-four snapshot files will be maintained.
    monitor.histogram_pg.port_set = swp1-swp50
    monitor.histogram_pg.stat_type = histogram
    monitor.histogram_pg.cos_list = [0]      
    monitor.histogram_pg.trigger_type = timer
    monitor.histogram_pg.timer = 1s
    monitor.histogram_pg.action_list = [snapshot,collect,log]
    monitor.histogram_pg.snapshot.file = /var/lib/cumulus/histogram_stats
    monitor.histogram_pg.snapshot.file_count = 64
    monitor.histogram_pg.histogram.minimum_bytes_boundary = 1024
    monitor.histogram_pg.histogram.bin_size_bytes = 1024
    monitor.histogram_pg.histogram.sample_time_ns = 1024
    monitor.histogram_pg.log.queue_bytes = 500
    monitor.histogram_pg.collect.queue_bytes = 500                              
    monitor.histogram_pg.collect.port_group_list = [buffers_pg,all_packet_pg]

## <span>Restarting the asic-monitor Service</span>

After you modify the configuration in the `monitor.conf` file, you need
to restart the `asic-monitor` service. This does not disrupt traffic,
nor does it require you to restart `switchd` in order for the changes to
take effect.

    cumulus@switch:~$ sudo systemctl restart asic-monitor.service

The service is enabled by default when you boot the switch and is
restarted whenever you restart `switchd`.

## <span>Understanding Triggers</span>

During state collection, the monitoring service may respond to a
threshold being crossed, which triggers a monitoring action.

At this time, the only type of trigger that initiates state collection
is a *timer*. The timer is the frequency at which the histogram triggers
and reads the ASIC state.

When a monitoring statistic meets a configured threshold, it can trigger
an action. Triggers can include:

  - Queue length, as measured by a histogram

  - Packet drops due to packet buffer congestion

  - Packet drops due to errors

If no trigger is configured for a monitoring action, the action happens
unconditionally and always occurs.

## <span>Understanding Monitoring Actions</span>

Monitoring actions are responses to triggers issued by the
`asic-monitor` service.

There are three types of monitoring actions: *collect*, *log* and
*snapshot*. And any or all three of these actions can be triggered by
one monitoring step.

A *collect* action triggers the collection of additional ASIC state.
Multiple port groups can be daisy chained into a single collect action.
A collect action requires a port group.

A *log* action writes out the state to `syslog`. For example:

    2017-04-26T20:14:41.560840+00:00 cumulus asic-monitor-module INFO: 2017-04-26 20:14:41.559967: Egress queue(s) greater than 500 bytes in monitor port group histogram_pg

A *snapshot* action takes a snapshot of the current state that was
collected and writes it out to a file. You specify the prefix for the
snapshot file name — including the path, like `/var/lib/cumulus/` for
example — and the number of snapshots that can be taken before the
system starts overwriting the earliest snapshot files. For example, if
the snapshot file is called `/var/lib/cumulus/snapshot` and the snapshot
file count is set to 64, then the first snapshot file is named
snapshot\_0 and the 64th snapshot is named snapshot\_63. When the 65th
snapshot has taken, the original snapshot file —
`/var/lib/cumulus/snapshot_0` — is overwritten and the files are
overwritten in sequence..

## <span id="src-7112383_BufferMonitoring-caveats" class="confluence-anchor-link"></span><span>Caveats and Errata</span>

Keep in mind that a lot of overhead is involved in collecting this data,
hitting the CPU and SDK process, which can affect execution of
`switchd`. Snapshots and logging can occupy a lot of disk space if
you’re not limiting the number of files to copy.
