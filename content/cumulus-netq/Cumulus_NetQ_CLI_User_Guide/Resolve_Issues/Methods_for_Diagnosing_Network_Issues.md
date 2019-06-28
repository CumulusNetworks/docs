---
title: Methods for Diagnosing Network Issues
author: Cumulus Networks
weight: 107
aliases:
 - /display/NETQ/Methods+for+Diagnosing+Network+Issues
 - /pages/viewpage.action?pageId=10456383
pageID: 10456383
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
NetQ provides users with the ability to go back in time to replay the
network state, see fabric-wide event change logs and root cause state
deviations. The NetQ Telemetry Server maintains data collected by NetQ
agents in a time-series database, making fabric-wide events available
for analysis. This enables you to replay and analyze network-wide events
for better visibility and to correlate patterns. This allows for
root-cause analysis and optimization of network configs for the future.

## <span>Diagnose an Event after It Occurs</span>

NetQ provides a number of commands for diagnosing past events.

NetQ records network events and stores them in its database. You can
view the events through a third-party notification application like
PagerDuty or Slack or use `netq show events` to look for any changes
made to the runtime configuration that may have triggered the alert,
then use `netq trace` to track the connection between the nodes.

The `netq trace` command traces the route of an IP or MAC address from
one endpoint to another. It works across bridged, routed and VXLAN
connections, computing the path using available data instead of sending
real traffic — this way, it can be run from anywhere. It performs MTU
and VLAN consistency checks for every link along the path.

For example, say you get an alert about a BGP session failure. You can
quickly run `netq check bgp` to determine what sessions failed:

``` 
cumulus@switch:~$ netq check bgp
Total Nodes: 25, Failed Nodes: 3, Total Sessions: 220 , Failed Sessions: 24, 
Hostname          VRF             Peer Name         Peer Hostname     Reason                                        Last Changed
----------------- --------------- ----------------- ----------------- --------------------------------------------- -------------------------
exit-1            DataVrf1080     swp6.2            firewall-1        BGP session with peer firewall-1 swp6.2: AFI/ 1d:7h:56m:9s
                                                                      SAFI evpn not activated on peer              
exit-1            DataVrf1080     swp7.2            firewall-2        BGP session with peer firewall-2 (swp7.2 vrf  1d:7h:49m:31s
                                                                      DataVrf1080) failed,                         
                                                                      reason: Peer not configured                  
exit-1            DataVrf1081     swp6.3            firewall-1        BGP session with peer firewall-1 swp6.3: AFI/ 1d:7h:56m:9s
                                                                      SAFI evpn not activated on peer              
exit-1            DataVrf1081     swp7.3            firewall-2        BGP session with peer firewall-2 (swp7.3 vrf  1d:7h:49m:31s
                                                                      DataVrf1081) failed,                         
                                                                      reason: Peer not configured       
```

You can run a trace from spine01 to leaf02, which has the IP address
10.1.20.252:

    cumulus@switch:~$ netq trace 10.1.20.252 from spine01 around 5m
    spine01 -- spine01:swp1 -- leaf01:vlan20
            -- spine01:swp2 -- leaf02:vlan20

Then you can check what's changed on the network to help you identify
the problem.

    cumulus@switch:~$ netq show events type bgp
    Matching events records:
    Hostname          Message Type Severity Message                             Timestamp
    ----------------- ------------ -------- ----------------------------------- -------------------------
    leaf21            bgp          info     BGP session with peer spine-1 swp3. 1d:8h:35m:19s
                                            3 vrf DataVrf1081 state changed fro
                                            m failed to Established
    leaf21            bgp          info     BGP session with peer spine-2 swp4. 1d:8h:35m:19s
                                            3 vrf DataVrf1081 state changed fro
                                            m failed to Established
    leaf21            bgp          info     BGP session with peer spine-3 swp5. 1d:8h:35m:19s
                                            3 vrf DataVrf1081 state changed fro
                                            m failed to Established
    leaf21            bgp          info     BGP session with peer spine-1 swp3. 1d:8h:35m:19s
                                            2 vrf DataVrf1080 state changed fro
                                            m failed to Established
    leaf21            bgp          info     BGP session with peer spine-3 swp5. 1d:8h:35m:19s
                                            2 vrf DataVrf1080 state changed fro
                                            m failed to Established
    ...

## <span id="src-10456383_MethodsforDiagnosingNetworkIssues-time_machine" class="confluence-anchor-link"></span><span>Use NetQ as a Time Machine</span>

With NetQ, you can travel back to a specific point in time or a range of
times to help you isolate errors and issues.

For example, if you think you had an issue with your sensors last night,
you can check the sensors on all your nodes around the time you think
the issue occurred:

``` 
cumulus@leaf01:~$ netq check sensors around 12h    
Total Nodes: 25, Failed Nodes: 0, Checked Sensors: 221, Failed Sensors: 0    
```

Or you can specify a range of times using the `between` option. The
units of time you can specify are second (*s*), minutes (*m*), hours
(*h*) and days (*d*). Always specify the most recent time first, then
the more distant time. For example, to see the changes made to the
network between the past minute and 5 minutes ago, you'd run:

    cumulus@switch:/$ netq show events between now and 48h
    Matching events records:
    Hostname          Message Type Severity Message                             Timestamp
    ----------------- ------------ -------- ----------------------------------- -------------------------
    leaf21            configdiff   info     leaf21 config file ptm was modified 1d:8h:38m:6s
    leaf21            configdiff   info     leaf21 config file lldpd was modifi 1d:8h:38m:6s
                                            ed
    leaf21            configdiff   info     leaf21 config file interfaces was m 1d:8h:38m:6s
                                            odified
    leaf21            configdiff   info     leaf21 config file frr was modified 1d:8h:38m:6s
    leaf12            configdiff   info     leaf12 config file ptm was modified 1d:8h:38m:11s
    leaf12            configdiff   info     leaf12 config file lldpd was modifi 1d:8h:38m:11s
                                            ed
    leaf12            configdiff   info     leaf12 config file interfaces was m 1d:8h:38m:11s
                                            odified
    leaf12            configdiff   info     leaf12 config file frr was modified 1d:8h:38m:11s
    leaf11            configdiff   info     leaf11 config file ptm was modified 1d:8h:38m:22s
    ...

You can travel back in time 5 minutes and run a trace from spine02 to
exit01, which has the IP address 27.0.0.1:

    cumulus@leaf01:~$ netq trace 27.0.0.1 from spine02 around 5m
    Detected Routing Loop. Node exit01 (now via Local Node exit01 and Ports swp6 <==> Remote  Node/s spine01 and Ports swp3) visited twice.
    Detected Routing Loop. Node spine02 (now via mac:00:02:00:00:00:15) visited twice.
    spine02 -- spine02:swp3 -- exit01:swp6.4 -- exit01:swp3 -- exit01
                            -- spine02:swp7  -- spine02

### <span>Trace Paths in a VRF</span>

The `netq trace` command works with VRFs as well:

    cumulus@leaf01:~$ netq trace 10.1.20.252 from spine01 vrf default around 5m
    spine01 -- spine01:swp1 -- leaf01:vlan20
            -- spine01:swp2 -- leaf02:vlan20

## <span>Sample Commands for Various Components</span>

NetQ provides network validation for the entire stack, providing
algorithmic answers to many questions, both simple and intractable, that
pertain to your network fabric.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Component</p></th>
<th><p>Problem</p></th>
<th><p>Solution</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Host</p></td>
<td><p>Where is this container located?</p>
<p>Open ports? What image is being used?</p>
<p>Which containers are part of this service? How are they connected?</p></td>
<td><p>netq show docker container</p>
<p>netq show docker container service</p></td>
</tr>
<tr class="even">
<td><p>Overlay</p></td>
<td><p>Is my overlay configured correctly?</p>
<p>Can A reach B?</p></td>
<td><p>netq check|show vxlan</p>
<p>netq check evpn|lnv</p></td>
</tr>
<tr class="odd">
<td><p>L3</p></td>
<td><p>Is OSPF working as expected?</p>
<p>Is BGP working as expected?</p>
<p>Can IP A reach IP B?</p></td>
<td><p>netq check|show ospf</p>
<p>netq check|show bgp</p></td>
</tr>
<tr class="even">
<td><p>L2</p></td>
<td><p>Is MLAG configured correctly?</p>
<p>Is there an STP loop?</p>
<p>Is VLAN or MTU misconfigured?</p>
<p>How does MAC A reach B?</p></td>
<td><p>netq check|show clag</p>
<p>netq show stp</p>
<p>netq check|show vlan</p>
<p>netq check mtu</p></td>
</tr>
<tr class="odd">
<td><p>OS</p></td>
<td><p>Are all switches licensed correctly?</p>
<p>Do all switches have NetQ agents running?</p></td>
<td><p>netq check license</p>
<p>netq check|show agents</p></td>
</tr>
<tr class="even">
<td><p>Interfaces</p></td>
<td><p>Is my link down? Are all bond links up?</p>
<p>What optics am I using? What's the peer for this port?</p>
<p>Which ports are empty? Is there a link mismatch? Are links flapping?</p></td>
<td><p>netq show|check interfaces</p></td>
</tr>
<tr class="odd">
<td><p>Hardware</p></td>
<td><p>Have any components crashed?</p>
<p>What switches do I have in the network?</p></td>
<td><p>netq check sensors</p>
<p>netq show sensors all</p>
<p>netq show inventory brief</p></td>
</tr>
</tbody>
</table>
