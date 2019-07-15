---
title: Performing Network Diagnostics
author: Cumulus Networks
weight: 21
aliases:
 - /display/NETQ121/Performing-Network-Diagnostics
 - /pages/viewpage.action?pageId=8356555
pageID: 8356555
product: Cumulus NetQ
version: 1.2.1
imgData: cumulus-netq-121
siteSlug: cumulus-netq-121
---
NetQ provides users with the ability to go back in time to replay the
network state, see fabric-wide event changelogs and root cause state
deviations. The NetQ Telemetry Server maintains data collected by NetQ
agents in a time-series database, making fabric-wide events available
for analysis. This enables you to replay and analyze network-wide events
for better visibility and to correlate patterns. This allows for
root-cause analysis and optimization of network configs for the future.

## <span>Diagnosing an Event after It Occurs</span>

NetQ provides a number of commands to enable you to diagnose past
events.

NetQ Notifier records network events and sends them to `syslog`, or
another third-party service like PagerDuty or Slack. You can use `netq
show changes` to look for any changes made to the runtime configuration
that may have triggered the alert, then use `netq trace` to track the
connection between the nodes.

The `netq trace` command traces the route of an IP or MAC address from
one endpoint to another. It works across bridged, routed and VXLAN
connections, computing the path using available data instead of sending
real traffic — this way, it can be run from anywhere. It performs MTU
and VLAN consistency checks for every link along the path.

For example, say you get an alert about a BGP session failure. You can
quickly run `netq check bgp` to determine what sessions failed:

    cumulus@leaf01:~$ netq check bgp
    Total Nodes: 25, Failed Nodes: 4, Total Sessions: 228 , Failed Sessions: 6, 
    Node        Neighbor    Peer ID     Reason    Time
    ----------  ----------  ----------  --------  -------
    exit01      swp7.2      spine02     Idle      53m ago
    exit01      swp7.3      spine02     Idle      53m ago
    exit02      swp6.4      spine01     Idle      53m ago
    spine01     swp4.4      exit02      Idle      53m ago
    spine02     swp3.2      exit01      Idle      53m ago
    spine02     swp3.3      exit01      Idle      53m ago

You can run a trace from spine01 to leaf02, which has the IP address
10.1.20.252:

    cumulus@leaf01:~$ netq trace 10.1.20.252 from spine01 around 5m
    spine01 -- spine01:swp1 -- leaf01:vlan20
            -- spine01:swp2 -- leaf02:vlan20

Then you can check what's changed on the network to help you identify
the problem. Notice the nodes in a *Failed* state filter to the top of
the list:

    cumulus@leaf01:~$ netq show bgp changes
    Matching BGP Session records are:
    Node             Neighbor                     VRF              ASN        Peer ASN   State  PfxRx        DbState  Last Changed
    ---------------- ---------------------------- ---------------- ---------- ---------- ------ ------------ -------- ------------
    leaf04           swp52(spine02)               default          64516      65000      Estd   6            Add      5h ago
    leaf03           swp52(spine02)               default          64515      65000      Estd   5            Add      5h ago
    leaf01           swp52(spine02)               default          64513      65000      Estd   5            Add      5h ago
    leaf02           swp52(spine02)               default          64514      65000      Estd   6            Add      5h ago
    spine02          swp2(leaf02)                 default          65000      64514      Estd   2            Add      5h ago
    spine02          swp3(leaf03)                 default          65000      64515      Estd   2            Add      5h ago
    spine02          swp1(leaf01)                 default          65000      64513      Estd   2            Add      5h ago
    spine02          swp4(leaf04)                 default          65000      64516      Estd   2            Add      5h ago
    leaf04           swp51(spine01)               default          64516      65000      Estd   6            Add      5h ago
    spine01          swp2(leaf02)                 default          65000      64514      Estd   2            Add      5h ago
    leaf02           swp51(spine01)               default          64514      65000      Estd   6            Add      5h ago
    leaf01           swp51(spine01)               default          64513      65000      Estd   5            Add      5h ago
    spine01          swp1(leaf01)                 default          65000      64513      Estd   2            Add      5h ago
    spine01          swp4(leaf04)                 default          65000      64516      Estd   2            Add      5h ago
    leaf03           swp51(spine01)               default          64515      65000      Estd   5            Add      5h ago
    spine01          swp3(leaf03)                 default          65000      64515      Estd   2            Add      5h ago

## <span id="src-8356555_PerformingNetworkDiagnostics-time_machine" class="confluence-anchor-link"></span><span>Using NetQ as a Time Machine</span>

With NetQ, you can travel back to a specific point in time or a range of
times to help you isolate errors and issues.

For example, if you think you had an issue with your sensors last night,
you can check the sensors on all your nodes around the time you think
the issue occurred:

<div class="confbox panel">

<div class="panel-content">

``` 
cumulus@leaf01:~$ netq check sensors around 12h    
Total Nodes: 25, Failed Nodes: 0, Checked Sensors: 221, Failed Sensors: 0    
```

</div>

</div>

Or you can specify a range of times using the `between` option. The
units of time you can specify are second (*s*), minutes (*m*), hours
(*h*) and days (*d*). Always specify the most recent time first, then
the more distant time. For example, to see the changes made to the
network between the past minute and 5 minutes ago, you'd run:

    cumulus@leaf01:~$ netq show changes between 1m and 5m
    No changes to specified interfaces found
    No changes to interface addresses found
    Matching MAC table records are:
    Origin MAC                  VLAN     Node Name        Egress Port      DbState Last Changed
    ------ -------------------- -------- ---------------- ---------------- ------- --------------
    1      44:38:39:00:00:17    20       leaf02           bond-swp1        Add     3m ago
    1      44:38:39:00:00:17    20       leaf01           bond-swp1        Add     3m ago
    1      44:38:39:00:00:32    20       leaf03           bond-swp2        Add     4m ago
    1      44:38:39:00:00:32    20       leaf04           bond-swp2        Add     4m ago
    1      44:38:39:00:00:15    20       leaf01           bond-swp2        Del     4m ago
    1      44:38:39:00:00:15    20       leaf02           bond-swp2        Del     4m ago
    1      44:38:39:00:00:32    20       leaf03           bond-swp2        Del     4m ago
    1      44:38:39:00:00:32    20       leaf04           bond-swp2        Del     4m ago
    1      44:38:39:00:00:17    20       leaf02           bond-swp1        Del     4m ago
    1      44:38:39:00:00:17    20       leaf01           bond-swp1        Del     4m ago
    Matching IP route records are:
    Origin Table            IP                               Node             Nexthops                 DbState        Last Changed
    ------ ---------------- -------------------------------- ---------------- ------------------------ -------------- ------------
    0      default          ff02::1:ff00:5c/128              spine01          swp1                     Del            3m ago
    0      default          ff02::1:ff00:12/128              leaf02           eth0                     Del            3m ago
    No changes to IP neighbor table found
    No changes to BGP sessions found
    No changes to CLAG session found
    No changes to LNV session found

You can travel back in time 5 minutes and run a trace from spine02 to
exit01, which has the IP address 27.0.0.1:

    cumulus@leaf01:~$ netq trace 27.0.0.1 from spine02 around 5m
    Detected Routing Loop. Node exit01 (now via Local Node exit01 and Ports swp6 <==> Remote  Node/s spine01 and Ports swp3) visited twice.
    Detected Routing Loop. Node spine02 (now via mac:00:02:00:00:00:15) visited twice.
    spine02 -- spine02:swp3 -- exit01:swp6.4 -- exit01:swp3 -- exit01
                            -- spine02:swp7  -- spine02

### <span id="src-8356555_PerformingNetworkDiagnostics-matrix" class="confluence-anchor-link"></span><span>How Far Back in Time Can You Travel?</span>

The NetQ Telemetry Server stores an amount of data limited by a few
factors:

  - The size of the network: The larger the network, the more complex it
    is because of the number of routes and nodes.

  - The amount of memory in the telemetry server. The more memory, the
    more data you can retrieve.

  - The types of nodes you are monitoring with NetQ. You can monitor
    just network switches, or switches and hosts, or switches, hosts and
    containers.

  - The number of changes in the network over time.

In general, you can expect to be able to query to a point back in time
follows:

| Using NetQ to Monitor ...            | Data Point                      | Small Network | Medium Network | Large Network |
| ------------------------------------ | ------------------------------- | ------------- | -------------- | ------------- |
| Switches only                        | Telemetry server memory minimum | 8G            | 16G            | 24G           |
|                                      | Years of data retrievable       | 25.5          | 17.4           | 15.6          |
| Switches and Linux hosts             | Telemetry server memory minimum | 16G           | 32G            | 48G           |
|                                      | Years of data retrievable       | 4.3           | 2.7            | 2.4           |
| Switches, Linux hosts and containers | Telemetry server memory minimum | 32G           | 64G            | 96G           |
|                                      | Years of data retrievable       | 2.9           | 1.5            | 1.2           |

The sizing numbers in this table rely on the following assumptions and
definitions:

  - The types of configuration and operational data being recorded:
    
      - Switches and hosts: Interfaces; MLAG; LLDP-enabled links;
        IPv4/v6 addresses, neighbors and routes; BGP sessions; link
        flaps per day; IPv4/v6 route flaps per day; BGP and MLAG session
        flaps.
    
      - Containers: Exposed ports, networks, container flaps per day.

  - A small network has 20 racks with 40 leaf nodes, 10 spine nodes and
    40 hosts per rack.

  - A medium network has 60 racks with 120 leaf nodes, 30 spine nodes
    and 40 hosts per rack.

  - A large network has 100 racks with 200 leaf nodes, 50 spine nodes
    and 40 hosts per rack.

  - The hosts are dual-attached.

  - The network is oversubscribed 4:1.

  - Adding more memory to the telemetry server allows you to go back
    even further in time, in a near linear fashion. So doubling the
    memory should double the range.

## <span>Using trace in a VRF</span>

The `netq trace` command works with VRFs as well:

    cumulus@leaf01:~$ netq trace 10.1.20.252 from spine01 vrf default around 5m
    spine01 -- spine01:swp1 -- leaf01:vlan20
            -- spine01:swp2 -- leaf02:vlan20

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
