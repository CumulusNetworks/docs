---
title: Monitor Overall Network Health
author: Cumulus Networks
weight: 55
aliases:
 - /display/NETQ141/Monitor+Overall+Network+Health
 - /pages/viewpage.action?pageId=10453519
pageID: 10453519
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
NetQ provides the information you need to monitor the health of your
network fabric, devices, and interfaces. You are able to easily validate
the operation and view the configuration across the entire network from
switches to hosts to containers. For example, you can monitor the
operation of routing protocols and virtual network configurations, the
status of NetQ Agents and hardware components, and the operation and
efficiency of interfaces. When issues are present, NetQ makes it easy to
identify and resolve them. You can also see when changes have occurred
to the network, devices, and interfaces by viewing their operation,
configuration, and status at earlier points in time.

## Validate Network Health

NetQ `check` commands validate the various elements of your network
fabric, looking for inconsistencies in configuration across your fabric,
connectivity faults, missing configuration, and so forth, and then and
display the results for your assessment. They can be run from any node
in the network. Most check commands can be run for a specific device or
for the entire network fabric.

### Validate the Network Fabric

You can validate the following network fabric elements:

  - BGP and OSPF routing protocols
  - VLAN, VXLAN, CLAG, and EVPN virtual constructs
  - MTU setting
  - NetQ Agents

For example, to determine the status of BGP running on your network:

    cumulus@switch:~$ netq check bgp
    Total Nodes: 15, Failed Nodes: 0, Total Sessions: 16, Failed Sessions: 0

You can see from this output that NetQ has validated the connectivity
and configuration of BGP across all of the nodes in the network and
found them all to be operating properly. If there were issues with any
of the nodes, NetQ would provide information about each node to aid in
resolving the issues.

There is a check command for each of the supported routing protocols,
virtual constructs, MTU setting and NetQ Agents. They all behave in a
similar manner, checking for connectivity, configuration, and other
problems, indicating the number of nodes that they have checked and
indicating the number that have failed.

Some additional examples—

Validate that EVPN is running correctly on all nodes:

    cumulus@switch:~$ netq check evpn
    Total Nodes: 15, Failed Nodes: 0, Total Sessions: 0, Failed Sessions: 0, Total VNIs: 0

Confirm all monitored nodes are running the NetQ Agent:

    cumulus@switch:~$ netq check agents
    Checked nodes: 25, Rotten nodes: 0

Validate that all corresponding interface links have matching MTUs:

    cumulus@switch:~$ netq check mtu
    Checked Nodes: 15, Checked Links: 138, Failed Nodes: 0, Failed Links: 0
    No MTU Mismatch found

Validate that VXLANs are configured and operating properly:

    cumulus@switch:~$ netq check vxlan 
    Checked Nodes: 6, Warning Nodes: 0, Failed Nodes: 6
    Nodes with error
    Hostname         Reason
    ---------------- ----------------------------------------------------------------
    exit01           inconsistent replication list for vni 104001                    
    exit02           inconsistent replication list for vni 104001                    
    leaf01           inconsistent replication list for vni 104001                    
    leaf02           inconsistent replication list for vni 104001                    
    leaf03           inconsistent replication list for vni 104001                    
    leaf04           inconsistent replication list for vni 104001                    

{{%notice tip%}}

With NetQ 1.4 both asymmetric and symmetric VXLAN configurations are
validated with this command.

{{%/notice%}}

You can be more granular in your validation as well, using the
additional options available for each of the check commands. For
example, validate BGP operation for nodes with VRF:

    cumulus@switch:~$ netq check bgp vrf DataVrf1081
    Total Nodes: 25, Failed Nodes: 1, Total Sessions: 52 , Failed Sessions: 0

Each of the check commands provides a starting point for troubleshooting
configuration and connectivity issues within your network in real time.
They provide an additional option of viewing the network state at an
earlier time, using the `around` option.

For example, if you were notified of an issue on your VLANs that appears
to have occurred about 10 minutes ago, you could run:

    cumulus@switch:~$ netq check vlan around 10m
    Checked Nodes: 15, Checked Links: 138, Failed Nodes: 0, Failed Links: 0
    No VLAN or PVID Mismatch found

### Validate Device Status and Configuration

You can validate the following device elements:

  - NTP
  - Sensors
  - License

It is always important to have your devices in time synchronization to
ensure configuration and management events can be tracked and
correlations can be made between events. To validate time
synchronization, run:

    cumulus@switch:~$ netq check ntp
    Total Nodes: 15, Checked Nodes: 15, Rotten Nodes: 0, Unknown Nodes: 0, failed NTP Nodes: 8
    Hostname          NTP Sync Connect Time
    ----------------- -------- -------------------------
    exit01            no       2018-09-12 16:30:39      
    exit02            no       2018-09-12 16:30:45      
    leaf01            no       2018-09-12 16:30:43      
    leaf02            no       2018-09-12 16:30:36      
    leaf03            no       2018-09-12 16:30:36      
    leaf04            no       2018-09-12 16:30:34      
    spine01           no       2018-09-12 16:30:44      
    spine02           no       2018-09-12 16:30:40      

This example shows eight nodes that are not in time synchronization. You
can now continue to investigate these nodes, validating that the NetQ
Agents are active, whether an NTP server has become unreachable, and so
forth.

Hardware platforms have a number sensors to provide environmental data
about the switches. Knowing these are all within range is a good check
point for maintenance. For example, if you had a temporary HVAC failure
and you are concerned that some of your nodes are beginning to overheat,
you can run:

    cumulus@switch:~$ netq check sensors
    Total Nodes: 25, Failed Nodes: 0, Checked Sensors: 221, Failed Sensors: 0

You can also check for any nodes that have invalid licenses without
going to each node. Because switches do not operate correctly without a
valid license you might want to verify that your Cumulus Linux licenses
on a regular basis:

    cumulus@switch:~$ netq check license
    Total Nodes: 15, Failed Nodes: 0, Checked Licenses: 10, Failed Licenses: 0

{{%notice tip%}}

This command checks every node, meaning every switch and host in the
network. Hosts do not require a Cumulus Linux license, so the number of
licenses checked is likely to be smaller than the total number of nodes
checked.

{{%/notice%}}

### Validate Interface Status and Configuration

As with other netq check commands, you can validate the proper operation
of your interfaces across the network:

    cumulus@switch:~$ netq check interfaces 
    Checked Nodes: 15, Failed Nodes: 8
    Checked Ports: 118, Failed Ports: 8, Unverified Ports: 94
    Hostname          Interface                 Peer Hostname     Peer Interface            Message
    ----------------- ------------------------- ----------------- ------------------------- -----------------------------------
    leaf01            swp1                      server01          eth1                      Autoneg mismatch (off, on)         
    leaf02            swp2                      server02          eth2                      Autoneg mismatch (off, on)         
    leaf03            swp1                      server03          eth1                      Autoneg mismatch (off, on)         
    leaf04            swp2                      server04          eth2                      Autoneg mismatch (off, on)         
    server01          eth1                      leaf01            swp1                      Autoneg mismatch (on, off)         
    server02          eth2                      leaf02            swp2                      Autoneg mismatch (on, off)         
    server03          eth1                      leaf03            swp1                      Autoneg mismatch (on, off)         
    server04          eth2                      leaf04            swp2                      Autoneg mismatch (on, off)         

When failures are seen, additional information is provided to start your
investigation. In this example, some reconfiguration is required for
auto-negotiation with peer interfaces.

## View Network Details

The `netq show` commands display a wide variety of content about the
network and its various elements. You can show content for the
following:

    cumulus@switch:~$ netq show
        agents      :  Netq agent
        bgp         :  BGP info
        changes     :  How this infomation has changed with time (default '1h')
        clag        :  Cumulus Multi-chassis LAG
        docker      :  Docker Info
        evpn        :  EVPN
        interfaces  :  network interface port
        inventory   :  Inventory information
        ip          :  IPv4 related info
        ipv6        :  IPv6 related info
        kubernetes  :  Kubernetes Information
        lldp        :  LLDP based neighbor info
        lnv         :  Lightweight Network Virtualization info
        macs        :  Mac table or MAC address info
        ntp         :  NTP
        ospf        :  OSPF info
        sensors     :  Temperature/Fan/PSU sensors
        services    :  System services
        vlan        :  VLAN
        vxlan       :  VXLAN data path

For example, to validate the the status of the NetQ agents running in
the fabric, run `netq show agents`. A *Fresh* status indicates the Agent
is running as expected. The Agent sends a heartbeat every 30 seconds,
and if three consecutive heartbeats are missed, its status changes to
*Rotten*.

    cumulus@leaf01:~$ netq show agents
     
    Node             Status    Sys Uptime    Agent Uptime
    ---------------  --------  ------------  --------------
    leaf01           Fresh     2h ago        2h ago
    leaf02           Fresh     2h ago        2h ago
    leaf03           Fresh     2h ago        2h ago
    leaf04           Fresh     2h ago        2h ago
    oob-mgmt-server  Fresh     2h ago        2h ago
    server01         Fresh     2h ago        2h ago
    server02         Fresh     2h ago        2h ago
    server03         Fresh     2h ago        2h ago
    server04         Fresh     2h ago        2h ago
    spine01          Fresh     2h ago        2h ago
    spine02          Fresh     2h ago        2h ago

Some additional examples--

View the status of BGP:

    cumulus@switch:~$ netq show bgp
    Matching bgp records:
    Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
    ----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
    exit01            swp44(internet)              vrf1            65041      25253      2/-/-        5d:1h:8m:59s
    exit01            swp51(spine01)               default         65041      65020      8/-/42       5d:1h:8m:59s
    exit01            swp52(spine02)               default         65041      65020      8/-/42       5d:1h:8m:58s
    exit02            swp44(internet)              vrf1            65042      25253      2/-/-        5d:1h:9m:3s
    exit02            swp51(spine01)               default         65042      65020      8/-/42       5d:1h:9m:4s
    exit02            swp52(spine02)               default         65042      65020      8/-/42       5d:1h:9m:3s
    internet          swp1(exit01)                 default         25253      65041      0/-/-        5d:1h:8m:58s
    internet          swp2(exit02)                 default         25253      65042      0/-/-        5d:1h:9m:3s
    leaf01            swp51(spine01)               default         65011      65020      7/-/24       5d:1h:9m:0s
    leaf01            swp52(spine02)               default         65011      65020      7/-/24       5d:1h:8m:59s
    leaf02            swp51(spine01)               default         65012      65020      8/-/24       5d:1h:9m:0s
    leaf02            swp52(spine02)               default         65012      65020      8/-/24       5d:1h:8m:59s
    leaf03            swp51(spine01)               default         65013      65020      7/-/24       5d:1h:9m:0s
    leaf03            swp52(spine02)               default         65013      65020      7/-/24       5d:1h:8m:59s
    leaf04            swp51(spine01)               default         65014      65020      8/-/24       5d:1h:9m:0s
    leaf04            swp52(spine02)               default         65014      65020      8/-/24       5d:1h:8m:59s
    spine01           swp1(leaf01)                 default         65020      65011      2/-/10       5d:1h:9m:0s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       5d:1h:9m:0s
    spine01           swp29(exit02)                default         65020      65042      1/-/2        5d:1h:9m:4s
    spine01           swp3(leaf03)                 default         65020      65013      2/-/10       5d:1h:9m:0s
    spine01           swp30(exit01)                default         65020      65041      1/-/2        5d:1h:8m:59s
    spine01           swp4(leaf04)                 default         65020      65014      2/-/10       5d:1h:9m:0s
    spine02           swp1(leaf01)                 default         65020      65011      2/-/10       5d:1h:8m:59s
    spine02           swp2(leaf02)                 default         65020      65012      2/-/10       5d:1h:8m:59s
    spine02           swp29(exit02)                default         65020      65042      1/-/2        5d:1h:9m:4s
    spine02           swp3(leaf03)                 default         65020      65013      2/-/10       5d:1h:8m:59s
    spine02           swp30(exit01)                default         65020      65041      1/-/2        5d:1h:8m:58s
    spine02           swp4(leaf04)                 default         65020      65014      2/-/10       5d:1h:8m:58s

View the status of your VLANs:

    cumulus@switch:~$ netq show vlan
    Matching vlan records:
    Hostname          VLANs                     SVIs                      Last Changed
    ----------------- ------------------------- ------------------------- -------------------------
    exit01            4001                      4001                      4d:20h:10m:21s
    exit02            4001                      4001                      4d:20h:9m:57s
    leaf01            1,13,24,4001              13 24 4001                4d:21h:3m:21s
    leaf02            1,13,24,4001              13 24 4001                4d:20h:16m:42s
    leaf03            1,13,24,4001              13 24 4001                4d:20h:15m:52s
    leaf04            1,13,24,4001              13 24 4001                4d:20h:12m:32s

View the status of the hardware sensors:

    cumulus@switch:~$ netq show sensors all
    Matching sensors records:
    Hostname          Name            Description                         State      Message                             Last Changed
    ----------------- --------------- ----------------------------------- ---------- ----------------------------------- -------------------------
    exit01            fan1            fan tray 1, fan 1                   ok                                             4d:20h:11m:54s
    exit01            fan2            fan tray 1, fan 2                   ok                                             4d:20h:11m:54s
    exit01            fan3            fan tray 2, fan 1                   ok                                             4d:20h:11m:54s
    exit01            fan4            fan tray 2, fan 2                   ok                                             4d:20h:11m:54s
    exit01            fan5            fan tray 3, fan 1                   ok                                             4d:20h:11m:54s
    exit01            fan6            fan tray 3, fan 2                   ok                                             4d:20h:11m:54s
    exit01            psu1fan1        psu1 fan                            ok                                             4d:20h:11m:54s
    exit01            psu2fan1        psu2 fan                            ok                                             4d:20h:11m:54s
    exit01            temp1           board sensor near cpu               ok                                             4d:20h:11m:54s
    exit01            temp2           board sensor near virtual switch    ok                                             4d:20h:11m:54s
    exit01            temp3           board sensor at front left corner   ok                                             4d:20h:11m:54s
    exit01            temp5           board sensor near fan               ok                                             4d:20h:11m:54s
    exit02            fan1            fan tray 1, fan 1                   ok                                             4d:20h:11m:30s
    exit02            fan2            fan tray 1, fan 2                   ok                                             4d:20h:11m:30s
    exit02            fan3            fan tray 2, fan 1                   ok                                             4d:20h:11m:30s
    exit02            fan4            fan tray 2, fan 2                   ok                                             4d:20h:11m:30s
    exit02            fan5            fan tray 3, fan 1                   ok                                             4d:20h:11m:30s
    exit02            fan6            fan tray 3, fan 2                   ok                                             4d:20h:11m:30s
    exit02            psu1fan1        psu1 fan                            ok                                             4d:20h:11m:30s
    exit02            psu2fan1        psu2 fan                            ok                                             4d:20h:11m:30s
    exit02            temp4           board sensor at front right corner  ok                                             4d:20h:11m:30s
    internet          fan1            fan tray 1, fan 1                   ok                                             5d:1h:13m:12s
    internet          fan2            fan tray 1, fan 2                   ok                                             5d:1h:13m:12s
    internet          fan3            fan tray 2, fan 1                   ok                                             5d:1h:13m:12s
    ...
